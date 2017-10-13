from ssm_document_generator.definition.definition import Definition
from ssm_document_generator.definition.parameters.assign_parameters_mixin import AssignParametersMixin
from ssm_document_generator.definition.read_from_file_mixin import ReadFromFileMixin
from ssm_document_generator.definition.run_as_user_mixin import RunAsUserMixin


class BashDefinition(ReadFromFileMixin, RunAsUserMixin, AssignParametersMixin, Definition):
    """
    Definition for bash commands
    """
