import inspect
from pathlib import Path


class ReadFromFileMixin:
    """
    Adds the functionality of reading commands to be run from the specified file.
    """

    def __init__(self, command_file_name, command_file_directory=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.command_file_name = command_file_name

        self.command_file_directory = Path(command_file_directory) if command_file_directory else \
            self.infer_command_directory(command_file_name)

    @classmethod
    def infer_command_directory(cls, command_file_name):
        for frame in inspect.stack():
            considered_directory = Path(frame.filename).parent
            if considered_directory.joinpath(command_file_name).exists():
                return considered_directory

        raise RuntimeError("Can't infer the command directory. "
                           "Please check that the command_file you've specified is present in the directory."
                           "You can also pass the command directory explicitly.")

    def generate_commands(self):
        return super().generate_commands() + \
               self.command_file_directory.joinpath(self.command_file_name).read_text().splitlines()
