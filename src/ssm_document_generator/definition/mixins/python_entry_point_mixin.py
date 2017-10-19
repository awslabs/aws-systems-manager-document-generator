class PythonEntryPointMixin:
    """
    Adds python entry point for the commands. The function run_command would be executed and the parameters would be
    passed to it.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(interpreter='python3', *args, **kwargs)

    def postfix_code(self):
        return ['run_command(parameters)'] + super().postfix_code()
