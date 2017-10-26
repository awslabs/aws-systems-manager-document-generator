from ssm_document_generator.definition.parameters import common
from ssm_document_generator.definition.parameters.parameter import Parameter
from ssm_document_generator.definition.python_definition import PythonDefinition

definition = PythonDefinition(
    name='getFile',
    description='Retrieves a specified file content',
    command_file_name='get_file.py',
    user='root',
    parameters=[common.entities_limit(), Parameter('filePath', 'Path to file to retrieve')]
)
