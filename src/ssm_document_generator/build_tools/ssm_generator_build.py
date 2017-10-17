import sys

from pathlib import Path
from setuptools.command.install_scripts import install_scripts


class SSMGeneratorBuild(install_scripts):
    """
    Defines override of build_py step that has ssm_generator step as prerequisite.
    Use this to build CloudFormation template from your generated SSM documents.
    """

    def run(self):
        super().run()
        Path('build/cloudFormation').mkdir(parents=True, exist_ok=True)

        # This is needed if we want to use the modules defined in the same package as definition, as the
        # directory for the module does not exist initially - the path_importer stored in cache is None
        # And so we need to clean cache to recreate the importers.
        sys.path_importer_cache.clear()
        self.run_command('ssm_generator')
