from collections import namedtuple

import yaml
from ssm_document_generator.code.code_converter import CodeConverter
from ssm_document_generator.code import code_converter_factory


class Converter(object):
    """
    Takes in definition
    returns ssm doc
    """
    def __init__(self):
        pass

    def convert(self, definition_path):
        # definition_path.
        with definition_path.open() as stream:
            definition = yaml.load(stream)

        # todo should default to something?
        command_path = definition_path.parent / definition['command_file']
        code_converter = code_converter_factory.get_converter(definition['command_type'])
        if not command_path.exists():
            raise ''

        return code_converter.convert(definition, str(command_path.resolve()))


    @staticmethod
    def validate_definition(definition):
        #todo consider using https://pypi.python.org/pypi/voluptuous
        Field = namedtuple('Field', ['name', 'message'])
        required = [Field('command_file', 'Command definition does not contain the path to the command file')]

        for field in required:
            if field.name not in definition:
                raise field.message

    def read_definition(self):
        pass

