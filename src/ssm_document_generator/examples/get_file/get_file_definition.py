from ssm_document_generator.definition.metadata.common import category, access_level
from ssm_document_generator.definition.parameters import common
from ssm_document_generator.definition.python_definition import PythonDefinition

definition = PythonDefinition(
    name='getFile',
    description='Retrieves a specified file content',
    command_file_name='get_file.py',
    user='root',
    metadata=[category('OS'), access_level(2)],
    parameters=[common.entities_limit(), common.file_path()]
)
