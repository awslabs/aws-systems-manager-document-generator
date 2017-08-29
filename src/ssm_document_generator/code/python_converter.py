import json
import sys

import stickytape

from ssm_document_generator.code.code_converter import CodeConverter


class PythonConverter(CodeConverter):
    """
    CodeConverter specification for Python
    """
    COMMAND_TYPE = 'python'
    SHEBANG = '#!/usr/bin/env python'
    INTERPRETER = '/usr/bin/python3'
    USE_STICKYTAPE = True
    DEFINITION_KEYS_TO_FILTER = CodeConverter.DEFINITION_KEYS_TO_FILTER | {'use_stickytape'}

    def generate_parameters_code(self, parameter_definition):
        parameters_dict = {parameter_name: "{{" + parameter_name + "}}"
                           for parameter_name in parameter_definition.keys()}
        return ['parameters = ' + json.dumps(parameters_dict, sort_keys=True)]

    def get_postfix_code(self):
        # Todo consider having custom Json encoder
        return super().get_postfix_code() + \
               ['print(json.dumps(run_command(parameters), sort_keys=True, default=str))',
                str(self.uuid)]

    def get_prefix_code(self):
        return super().get_prefix_code() + \
               ["su - {} -c '{} -' <<'{}'".format(self.user(), self.INTERPRETER, str(self.uuid)),
                'import json']

    def process_code(self, code_file_path):
        if self.should_use_stickytape():
            return stickytape.script(code_file_path, add_python_paths=sys.path).splitlines()
        else:
            return super().process_code(code_file_path)

    def should_use_stickytape(self):
        return self.document_definition.get('use_stickytape', self.USE_STICKYTAPE)
