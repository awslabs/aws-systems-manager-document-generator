import json
from pathlib import Path


class CodeConverter(object):
    DEFAULT_TEMPLATE_PATH = str(Path(__file__).parent.resolve()) + "/../templates/run_command_template.json"

    def __init__(self):
        pass

    def convert(self, definition, code_filepath):
        ssm_document = self.read_template()
        command_list = ssm_document['mainSteps'][0]['inputs']['runCommand']

        command_list.extend(self.get_prefix_code())

        ssm_document['parameters'].update(definition['parameters'])
        command_list.extend(self.generate_parameters_code(ssm_document['parameters']))

        command_list.extend(self.process_code(code_filepath))

        command_list.extend(self.get_postfix_code())

        # print('\n'.join(command_list))

        return ssm_document

    def preprocess(self):
        pass
        # add shaebang
        # do minification/compression

    def generate_parameters_code(self, parameter_definition):
        return []

    def process_code(self, code_filepath):
        # todo consider having processors hierarchy (see OmniFocus for detail)
        with Path(code_filepath).open() as code_stream:
            return code_stream.readlines()

    def get_prefix_code(self):
        return [self.shebang()]

    def get_postfix_code(self):
        return []

    @classmethod
    def shebang(cls):
        return cls.SHEBANG


    @staticmethod
    def read_template(template_path=DEFAULT_TEMPLATE_PATH):
        return json.loads(Path(template_path).read_text())
