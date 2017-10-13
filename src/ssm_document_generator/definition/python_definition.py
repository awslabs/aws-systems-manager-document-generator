from ssm_document_generator.definition.definition import Definition
from ssm_document_generator.definition.parameters.dict_parameters_mixin import DictParametersMixin
from ssm_document_generator.definition.python_entry_point_mixin import PythonEntryPointMixin
from ssm_document_generator.definition.read_from_file_mixin import ReadFromFileMixin
from ssm_document_generator.definition.run_as_user_mixin import RunAsUserMixin


class PythonDefinition(ReadFromFileMixin, DictParametersMixin, PythonEntryPointMixin, RunAsUserMixin, Definition):
    """
    Definition for bash commands
    """
