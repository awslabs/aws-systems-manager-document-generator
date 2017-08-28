from ssm_document_generator.utils.result import Result
from messages_getter_base import MessagesGetterBase


class MessagesGetter(MessagesGetterBase):
    def read_messages(self, parameters):
        line_limit = int(parameters['lineLimit'])

        return open('/var/log/messages').readlines()[-line_limit:]


def run_command(parameters):
    """
    This is overcomplicated for demonstration purposes
    """
    return Result.run(lambda: MessagesGetter().read_messages(parameters))
