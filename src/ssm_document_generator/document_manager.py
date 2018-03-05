from troposphere import Template

from ssm_document_generator.definition.utils.definition_troposphere_adapter import DefinitionTroposphereAdapter
from ssm_document_generator import utils
from ssm_document_generator.discovery import discovery


class DocumentManager(object):
    @classmethod
    def load(cls, definition_path):
        """
        Load the definition from the given path.
        """
        return utils.load_module(definition_path).definition

    @classmethod
    def load_from_directory(cls, directory_path):
        """
        Takes in the directory_path and loads document definitions from the directory tree that starts at
        given directory.
        """
        return [cls.load(definition_path) for definition_path in
                discovery.get_definitions(directory_path)]

    @staticmethod
    def cloudformation_template(definitions):
        """
        Takes in the list of document definitions and combines them into the troposphere CloudFormation template
        that would contain all the documents.
        """
        template = Template()
        for document in definitions:
            template.add_resource(DefinitionTroposphereAdapter(document))
            for tag in document.get_metadata():
                template.add_resource(tag)

        return template
