from pathlib import Path
from setuptools import Command

from ssm_document_generator.converter import Converter


class SSMGenerator(Command):
    """
    A custom command to generate CloudFormation template with your SSM documents from your command definitions.
    """

    description = 'generate SSM documents from your command definitions'
    user_options = [
        ('source-directory=', None, 'path to the directory to scan for command definitions'),
        ('destination-path=', None, 'where to put resulting template'),
    ]

    def initialize_options(self):
        self.source_directory = 'src'
        self.destination_path = 'build/cloudFormation/ssm_commands.template'

    def finalize_options(self):
        source_path = Path(self.source_directory)
        assert source_path.exists() and source_path.is_dir(), \
            "Specified source directory {} does not exist".format(self.source_directory)

    def run(self):
        template = Converter.to_cloudformation(Converter.convert_directory(self.source_directory))
        Path(self.destination_path).write_text(template.to_json())
