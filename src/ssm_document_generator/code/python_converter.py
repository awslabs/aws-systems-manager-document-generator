import json

import stickytape

from ssm_document_generator.code.code_converter import CodeConverter


class PythonConverter(CodeConverter):
    COMMAND_TYPE = 'python'
    SHEBANG = '#!/usr/bin/env python'
    # !/rds/bin/opt/redshift/bin/python
    USE_STICKYTAPE = True  # todo move to config

    def generate_parameters_code(self, parameter_definition):
        parameters_dict = {parameter_name: "{{" + parameter_name + "}}"
                           for parameter_name in parameter_definition.keys()}
        return ['parameters = ' + json.dumps(parameters_dict, sort_keys=True)]

    def get_postfix_code(self):
        return super().get_postfix_code() + ['print(json.dumps(run_command(parameters)))']

    def get_prefix_code(self):
        return super().get_prefix_code() + ['import json']

    def process_code(self, code_filepath):  # todo proper search path to get modules from brazil build/brazil deps.
        if self.USE_STICKYTAPE:
            return stickytape.script(code_filepath).splitlines()
        else:
            return super().process_code(code_filepath)
