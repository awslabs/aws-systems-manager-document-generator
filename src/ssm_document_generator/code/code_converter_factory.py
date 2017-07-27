from ssm_document_generator.code.python_converter import PythonConverter

COMMAND_TYPE_MAP = {PythonConverter.COMMAND_TYPE: PythonConverter}


def get_converter(command_type):
    return COMMAND_TYPE_MAP[command_type]()
