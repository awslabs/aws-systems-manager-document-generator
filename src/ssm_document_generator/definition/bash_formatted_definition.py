from ssm_document_generator.definition.bash_definition import BashDefinition
from ssm_document_generator.definition.mixins.bash_simple_result_format_mixin import BashSimpleResultFormatMixin


class BashFormattedDefinition(BashSimpleResultFormatMixin, BashDefinition):
    """
    A definition for bash commands with formatted output template
    """
