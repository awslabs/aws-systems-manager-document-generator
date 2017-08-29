from ssm_document_generator.code.code_converter import CodeConverter


class BashConverter(CodeConverter):
    """
    CodeConverter specification for Bash
    """
    COMMAND_TYPE = 'bash'

    def generate_parameters_code(self, parameter_definition):
        return ['{}='.format(parameter_name) + "{{" + parameter_name + "}}"
                for parameter_name in parameter_definition.keys()]

    def get_prefix_code(self):
        return super().get_prefix_code() + (['su - ' + self.run_as_user()] if self.run_as_user() else [])
