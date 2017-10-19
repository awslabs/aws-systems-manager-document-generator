from ssm_document_generator.definition.bash_definition import BashDefinition
from ssm_document_generator.definition.parameters import common

definition = BashDefinition(
    name='dmesg',
    description='Retrieves filtered dmesg content.',
    command_file_name='dmesg.sh',
    parameters=[common.ENTITIES_LIMIT]
)
