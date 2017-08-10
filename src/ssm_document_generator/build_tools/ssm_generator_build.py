from pathlib import Path

from setuptools.command import build_py


class SSMGeneratorBuild(build_py.build_py):
    """
    Defines override of build_py step that has ssm_generator step as prerequisite.
    Use this to build CloudFormation template from your generated SSM documents.
    """

    def run(self):
        Path('build/cloudFormation').mkdir(parents=True, exist_ok=True)
        self.run_command('ssm_generator')
        super().run()
