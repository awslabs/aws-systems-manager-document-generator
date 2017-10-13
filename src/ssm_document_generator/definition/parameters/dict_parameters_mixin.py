import json


class DictParametersMixin:
    def generate_parameters_code(self):
        parameters_dict = {parameter.name: "{{" + parameter.name + "}}"
                           for parameter in self.parameters}

        return super().generate_parameters_code() + \
               ['parameters = ' + json.dumps(parameters_dict, sort_keys=True)]
