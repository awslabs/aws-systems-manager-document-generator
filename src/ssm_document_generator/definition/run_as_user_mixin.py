import uuid

from ssm_document_generator.utils import constants


class RunAsUserMixin:
    def __init__(self, user='root', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.uuid = uuid.uuid4()

    def prefix_code(self):
        return super().prefix_code() + ["su - {} -c '{} -' <<'{}'".format(self.user, self.interpreter, str(self.uuid))]

    def postfix_code(self):
        return [str(self.uuid)] + super().postfix_code()

    def shebang(self):
        return constants.SHEBANG_ENV + ' bash'
