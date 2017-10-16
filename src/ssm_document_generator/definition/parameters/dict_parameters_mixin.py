import json


class DictParametersMixin:
    """
    Adds the functionality to generate the code for passing the parameters as a dictionary
    (the original intended syntax is Python, but given that it's fairly generic - should be compatible with
     other languages e.g. JS or Ruby)
    """

    def generate_parameters_code(self):
        parameters_dict = {parameter.name: "{{" + parameter.name + "}}"
                           for parameter in self.parameters}

        return super().generate_parameters_code() + \
               ['parameters = ' + json.dumps(parameters_dict, sort_keys=True)]
