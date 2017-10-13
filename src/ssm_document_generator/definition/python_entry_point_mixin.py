class PythonEntryPointMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(interpreter='python', *args, **kwargs)

    def prefix_code(self):
        return super().prefix_code() + ['import json']

    def postfix_code(self):
        # Todo consider having custom Json encoder
        return ['print(json.dumps(run_command(parameters), sort_keys=True, default=str))'] + super().postfix_code()
