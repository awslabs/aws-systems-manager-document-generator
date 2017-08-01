from messages_getter_base import MessagesGetterBase


class MessagesGetter(MessagesGetterBase):
    def read_messages(self, parameters):
        line_limit = int(parameters['lineLimit'])

        return {'result': 'success', 'content': open('/var/log/messages').readlines()[-line_limit:],
                'parameters': parameters}


def run_command(parameters):
    """
    This is overcomplicated for demonstration purposes
    """
    return MessagesGetter().read_messages(parameters)
