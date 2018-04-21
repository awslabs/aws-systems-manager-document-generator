from ssm_document_generator.definition.bash_formatted_definition import BashFormattedDefinition
from ssm_document_generator.definition.metadata.common import access_level, category
from ssm_document_generator.definition.parameters import common

definition = BashFormattedDefinition(
    name='pstack',
    description='Retrieves stack for given processId',
    user='root',
    commands=['pstack ${processId}'],
    metadata=[category('OS'), access_level(2)],
    parameters=[common.process_id(),
                common.regex_filter_expression(),
                common.entities_limit()]
)
