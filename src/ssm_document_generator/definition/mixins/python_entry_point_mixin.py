class PythonEntryPointMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(interpreter='python3', *args, **kwargs)

    def postfix_code(self):
        return ['run_command(parameters)'] + super().postfix_code()
