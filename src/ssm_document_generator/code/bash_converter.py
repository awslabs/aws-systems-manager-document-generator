from ssm_document_generator.code.code_converter import CodeConverter


class BashConverter(CodeConverter):
    COMMAND_TYPE = 'bash'
    SHEBANG = '#!/usr/bin/bash'

    def generate_parameters_code(self, parameter_definition):
        return ['{}='.format(parameter_name) + "{{" + parameter_name + "}}"
                for parameter_name in parameter_definition.keys()]
