from ssm_document_generator.definition.definition import Definition
from ssm_document_generator.definition.parameters.assign_parameters_mixin import AssignParametersMixin
from ssm_document_generator.definition.run_as_user_mixin import RunAsUserMixin


class BashDefinition(RunAsUserMixin, AssignParametersMixin, Definition):
    pass
