from ssm_document_generator import utils


class Parameter:
    def __init__(self, name, description='', parameter_type='String', default=None, allowed_pattern=None):
        self.name = name
        self.parameter_type = parameter_type
        self.description = description
        self.default = default
        self.allowed_pattern = allowed_pattern

    def get_dict(self):
        return utils.dict_without_none_entries({'type': self.parameter_type,
                                                'description': self.description,
                                                'allowedPattern': self.allowed_pattern,
                                                'default': self.default})

    def add_to_dict(self, params_dict):
        params_dict[self.name] = self.get_dict()
