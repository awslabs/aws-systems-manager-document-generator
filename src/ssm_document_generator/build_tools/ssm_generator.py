from setuptools import Command

from pathlib import Path
from ssm_document_generator.converter import Converter
from troposphere import Template
import troposphere.ssm as ssm


class SSMGenerator(Command):
    """

    """

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # todo iterdir to do discovery
        definition_path = Path("src/owls/get_file/get_file.definition")

        document = Converter.convert(definition_path)

        template = Template()
        cf_document = ssm.Document('getFile')  # todo name camelcase
        cf_document.DocumentType = 'Command'
        cf_document.Content = document
        template.add_resource(cf_document)
        print(template.to_json())

        Path('configuration/cloudFormation/getFile.template').write_text(template.to_json())
        print(Path('build_tools/cloudFormation/getFile.template').resolve())
