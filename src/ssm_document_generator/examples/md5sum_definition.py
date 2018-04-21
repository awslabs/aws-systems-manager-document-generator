from ssm_document_generator.definition.bash_formatted_definition import BashFormattedDefinition
from ssm_document_generator.definition.metadata.common import access_level, category
from ssm_document_generator.definition.parameters import common

definition = BashFormattedDefinition(
    name='md5sum',
    description='Retrieves md5sum for file at filePath.',
    user='root',
    commands=['md5sum ${filePath}'],
    metadata=[category('OS'), access_level(1)],
    parameters=[common.file_path()]
)
