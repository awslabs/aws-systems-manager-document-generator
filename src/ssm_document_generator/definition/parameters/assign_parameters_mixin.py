class AssignParametersMixin:
    def generate_parameters_code(self):
        return super().generate_parameters_code() + \
               ['{}='.format(parameter.name) + "{{" + parameter.name + "}}"
                for parameter in self.parameters]
