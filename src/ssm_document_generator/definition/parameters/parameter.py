class Parameter:
    # todo consider Parameters as separate class
    # would allow me to have group conversion
    def __init__(self, name, description='', parameter_type='String', default=None, allowed_pattern=None):
        # todo allowed param for filtering at later stage
        self.name = name
        self.parameter_type = parameter_type
        self.description = description
        self.default = default
        self.allowed_pattern = allowed_pattern

    def get_dict(self):
        return {'name': self.name,
                'type': self.parameter_type,
                'description': self.description,
                'allowedPattern': self.allowed_pattern}

    def add_to_dict(self, params_dict):
        params_dict[self.name] = self.get_dict()
