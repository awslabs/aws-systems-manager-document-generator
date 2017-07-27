from ssm_document_generator.code.python_converter import PythonConverter

COMMAND_TYPE_MAP = {'python': PythonConverter}


def get_converter(command_type):
    return COMMAND_TYPE_MAP.get(command_type)()
