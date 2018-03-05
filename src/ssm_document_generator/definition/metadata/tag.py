from troposphere import ssm, Sub


class Tag:
    """
    The tag for SSD document command. The current implementation is based on the SSM parameter store.
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def as_ssm_parameter(self, command_name):
        """
        Return representation of key-value tag for command in a form of SSM ParameterStore parameter.
        :param command_name:
        :return:
        """
        return ssm.Parameter("{}{}Tag".format(command_name, self.name.title()),
                             Name=Sub('/owls/${{AWS::StackName}}/{}/{}'.format(command_name, self.name)),
                             Type=self.get_type(self.value),
                             Value=str(self.value))

    @staticmethod
    def get_type(value):
        if type(value) is list:
            return 'StringList'

        return 'String'
