from ssm_document_generator.definition.metadata.document_tags_metadata_mixin import DocumentTagsMetadataMixin
from ssm_document_generator.definition.mixins.run_as_user_mixin import RunAsUserMixin
from ssm_document_generator.definition.mixins.read_from_file_mixin import ReadFromFileMixin

from ssm_document_generator.definition.parameters.assign_parameters_mixin import AssignParametersMixin
from ssm_document_generator.definition.definition import Definition


class BashDefinition(ReadFromFileMixin,
                     RunAsUserMixin,
                     AssignParametersMixin,
                     DocumentTagsMetadataMixin,
                     Definition):
    """
    Default definition for bash commands
    """
