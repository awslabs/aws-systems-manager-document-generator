def add_params_mixin(params=None, **keyword_args):
    parameters = params or []

    class GeneratedMixin:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **keyword_args, **kwargs)
            self.parameters.extend(parameters)

    return GeneratedMixin
