from ssm_document_generator.code.python_converter import PythonConverter
from ssm_document_generator.code.bash_converter import BashConverter

CONVERTOR_LIST = [PythonConverter, BashConverter]
COMMAND_TYPE_MAP = {converter.COMMAND_TYPE: converter for converter in CONVERTOR_LIST}


def get_converter(command_type):
    """
    Returns a proper converter object for given command type.
    :param command_type:
    :return:
    """
    return COMMAND_TYPE_MAP[command_type]()
