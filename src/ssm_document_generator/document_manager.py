from troposphere import Template

from ssm_document_generator.definition.utils.definition_troposphere_adapter import DefinitionTroposphereAdapter
from ssm_document_generator import utils
from ssm_document_generator.discovery import discovery


class DocumentManager(object):
    @classmethod
    def load(cls, definition_path):
        return utils.load_module(definition_path).definition

    @classmethod
    def load_from_directory(cls, directory_path):
        """
        Takes in the directory_path and returns ssm_documents and definitions for the .definition files in the
        directory tree that starts at given directory.
        """
        return [cls.load(definition_path) for definition_path in
                discovery.get_definitions(directory_path)]

    @staticmethod
    def cloudformation_template(definitions):
        """
        Takes in the conversion result list that contains ssm document and document definitions
        and returns CloudFormation template that would contain all the documents.
        """
        template = Template()
        for document in definitions:
            template.add_resource(DefinitionTroposphereAdapter(document))

        return template
