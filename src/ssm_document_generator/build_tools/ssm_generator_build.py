from setuptools.command import build_py


class SSMGeneratorBuild(build_py.build_py):
    def run(self):
        self.run_command('ssm_generator')
        super().run()
