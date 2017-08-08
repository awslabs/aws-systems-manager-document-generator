from collections import namedtuple

import yaml
from voluptuous import Schema, Required, All, Length, ALLOW_EXTRA, In
from troposphere import Template
import troposphere.ssm as ssm

from ssm_document_generator.code import code_converter_factory
from ssm_document_generator.discovery import discovery


class Converter(object):
    DEFINITION_SCHEMA = Schema({
        Required('name'): All(str, Length(min=4)),  # todo name camelcase validation
        Required('description'): str,
        Required('command_file'): All(str, Length(min=1)),
        Required('command_type'): In(code_converter_factory.COMMAND_TYPE_MAP.keys(),
                                     msg='The supported command types are: {}'.format(
                                         ', '.join(code_converter_factory.COMMAND_TYPE_MAP.keys())))
    }, extra=ALLOW_EXTRA)

    ConversionResult = namedtuple('ConversionResult', ['ssm_document', 'document_definition'])

    @classmethod
    def convert(cls, definition_path):
        """
        Takes in path to the command definition and returns generated SSM document and validated definition.
        """
        definition = cls.load_definition(definition_path)

        command_path = definition_path.parent / definition['command_file']
        if not command_path.exists():
            raise RuntimeError('The command file {} does not exist'.format(command_path))

        code_converter = code_converter_factory.get_converter(definition['command_type'])
        return cls.ConversionResult(code_converter.convert(definition, str(command_path.resolve())), definition)

    @classmethod
    def load_definition(cls, definition_path):
        """
        Reads and validates definition from the given definition_path
        """
        with definition_path.open() as stream:
            definition = yaml.load(stream)
        cls.DEFINITION_SCHEMA(definition)
        return definition

    @classmethod
    def convert_directory(cls, directory_path):
        """
        Takes in the directory_path and returns ssm_documents and definitions for the .definition files in the
        directory tree that starts at given directory.
        """
        definitions = discovery.get_definitions(directory_path)

        return [cls.convert(definition_path) for definition_path in definitions]

    @staticmethod
    def to_cloudformation(conversion_result_list):
        """
        Takes in the conversion result list that contains ssm document and document definitions
        and returns CloudFormation template that would contain all the documents.
        """
        template = Template()
        for document, definition in conversion_result_list:
            cf_document = ssm.Document(definition['name'])
            cf_document.DocumentType = 'Command'
            cf_document.Content = document
            template.add_resource(cf_document)

        return template
