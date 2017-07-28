from collections import namedtuple

import yaml
from voluptuous import Schema, Required, All, Length, ALLOW_EXTRA, IsFile, In

from ssm_document_generator.code import code_converter_factory


class Converter(object):
    """
    Takes in definition
    returns ssm doc
    """
    TEMPLATE_SCHEMA = Schema({
        Required('name'): All(str, Length(min=4)),
        Required('description'): str,
        Required('command_file'): str,
        Required('command_type'): In(code_converter_factory.COMMAND_TYPE_MAP.keys(),
                                     msg='The supported command types are: {}'.format(
                                         ', '.join(code_converter_factory.COMMAND_TYPE_MAP.keys())))
    }, extra=ALLOW_EXTRA)

    def __init__(self):
        pass

    def convert(self, definition_path):
        with definition_path.open() as stream:
            definition = yaml.load(stream)

        Converter.TEMPLATE_SCHEMA(definition)

        command_path = definition_path.parent / definition['command_file']
        if not command_path.exists():
            raise RuntimeError('The command file {} does not exist'.format(command_path))

        code_converter = code_converter_factory.get_converter(definition['command_type'])
        return code_converter.convert(definition, str(command_path.resolve()))

    @staticmethod
    def validate_definition(definition):
        # todo consider using https://pypi.python.org/pypi/voluptuous
        Field = namedtuple('Field', ['name', 'message'])
        required = [Field('command_file', 'Command definition does not contain the path to the command file')]

        for field in required:
            if field.name not in definition:
                raise field.message

    def read_definition(self):
        pass
