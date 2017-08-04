import yaml
from voluptuous import Schema, Required, All, Length, ALLOW_EXTRA, In

from ssm_document_generator.code import code_converter_factory


class Converter(object):
    DEFINITION_SCHEMA = Schema({
        Required('name'): All(str, Length(min=4)),  # todo name camelcase validation
        Required('description'): str,
        Required('command_file'): All(str, Length(min=1)),
        Required('command_type'): In(code_converter_factory.COMMAND_TYPE_MAP.keys(),
                                     msg='The supported command types are: {}'.format(
                                         ', '.join(code_converter_factory.COMMAND_TYPE_MAP.keys())))
    }, extra=ALLOW_EXTRA)

    @staticmethod
    def convert(definition_path):
        """
        Takes in path to the command definition and returns generated SSM document.
        """

        with definition_path.open() as stream:
            definition = yaml.load(stream)

        Converter.DEFINITION_SCHEMA(definition)

        command_path = definition_path.parent / definition['command_file']
        if not command_path.exists():
            raise RuntimeError('The command file {} does not exist'.format(command_path))

        code_converter = code_converter_factory.get_converter(definition['command_type'])
        return code_converter.convert(definition, str(command_path.resolve()))

