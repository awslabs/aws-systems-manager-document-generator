import json

from ssm_document_generator.code.code_converter import CodeConverter


class PythonConverter(CodeConverter):
    COMMAND_TYPE = 'python'
    SHEBANG = '#!/usr/bin/env python'
    # !/rds/bin/opt/redshift/bin/python

    def generate_parameters_code(self, parameter_definition):
        parameters_dict = {parameter_name: "{{" + parameter_name + "}}"
                           for parameter_name in parameter_definition.keys()}
        return ['parameters = ' + json.dumps(parameters_dict)]

    def get_postfix_code(self): # todo consider reading this from file
        return super().get_postfix_code() + ['print(run_command(parameters))']


