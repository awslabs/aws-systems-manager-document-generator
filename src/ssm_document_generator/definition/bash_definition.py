from ssm_document_generator.definition.metadata.ssm_parameter_store_metadata_mixin import SSMParameterStoreMetadataMixin
from ssm_document_generator.definition.mixins.run_as_user_mixin import RunAsUserMixin
from ssm_document_generator.definition.mixins.read_from_file_mixin import ReadFromFileMixin

from ssm_document_generator.definition.parameters.assign_parameters_mixin import AssignParametersMixin
from ssm_document_generator.definition.definition import Definition


class BashDefinition(ReadFromFileMixin,
                     RunAsUserMixin,
                     AssignParametersMixin,
                     SSMParameterStoreMetadataMixin,
                     Definition):
    """
    Default definition for bash commands
    """
