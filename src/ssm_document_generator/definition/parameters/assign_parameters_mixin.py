class AssignParametersMixin:
    """
    Adds the functionality to generate the code for passing the parameters in the following form:
    parameterName={{parameterName}}
    """

    def generate_parameters_code(self):
        return super().generate_parameters_code() + \
               ['{}='.format(parameter.name) + "{{" + parameter.name + "}}"
                for parameter in self.parameters]
