import json
from pathlib import Path


class CodeConverter(object):
    DEFAULT_TEMPLATE_PATH = str(Path(__file__).parent.resolve()) + "/../templates/run_command_template.json"
    SHEBANG = '#!/usr/bin/bash'
    DEFINITION_KEYS_TO_FILTER = ('command_type', 'command_file', 'name', 'parameters')

    def __init__(self):
        pass

    def convert(self, definition, code_filepath):
        ssm_document = self.read_template()
        self.merge_definition_into_template(ssm_document, definition)

        command_list = ssm_document['mainSteps'][0]['inputs']['runCommand']
        command_list.extend(self.get_prefix_code())
        command_list.extend(self.generate_parameters_code(ssm_document['parameters']))
        command_list.extend(self.process_code(code_filepath))
        command_list.extend(self.get_postfix_code())

        return ssm_document

    def generate_parameters_code(self, parameter_definition):
        return []

    def process_code(self, code_filepath):
        # todo consider having processors hierarchy (see OmniFocus for detail)
        with Path(code_filepath).open() as code_stream:
            return code_stream.readlines()

    def get_prefix_code(self):
        return [self.shebang()]

    def get_postfix_code(self):
        # todo consider reading this from file
        return []

    @staticmethod
    def merge_definition_into_template(template, definition, keys_to_filter=DEFINITION_KEYS_TO_FILTER):
        """
        Application specific dict merge - merge definition into document template, overriding parameters that
        are not filtered out.
        :param template:
        :param definition:
        :param keys_to_filter: List of keys to ignore during the merge.
        """
        template.update({k: v for k, v in definition.items() if k not in keys_to_filter})
        # consider doing deep merge if there would be more special cases then params.
        if 'parameters' in definition:
            template['parameters'].update(definition['parameters'])

        return template

    @classmethod
    def shebang(cls):
        return cls.SHEBANG

    @staticmethod
    def read_template(template_path=DEFAULT_TEMPLATE_PATH):
        return json.loads(Path(template_path).read_text())
