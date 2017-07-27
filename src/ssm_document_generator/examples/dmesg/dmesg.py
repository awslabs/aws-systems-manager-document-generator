# from ssm_document_generator.examples.dmesg.dmesg_base import DmesgReaderBase
# from ssm_document_generator.examples.dmesg.dmesg_base import DmesgReaderBase
# import Dmes
from dmesg_base import DmesgReaderBase


class DmesgReader(DmesgReaderBase):
    def read_dmesg(self, parameters):
        return {'result': 'success', 'content': open('/var/log/messages').readlines(), 'parameters': parameters}


def run_command(parameters):
    """
    This is overcomplicated for demonstration purposes
    """
    # print(parameters)
    line_limit = parameters['lineLimit']

    # open(encoding='utf-8')
    # return {'result': 'success', 'content': open('/var/log/messages').readlines(), 'parameters': parameters}
    return DmesgReader().read_dmesg(parameters)
