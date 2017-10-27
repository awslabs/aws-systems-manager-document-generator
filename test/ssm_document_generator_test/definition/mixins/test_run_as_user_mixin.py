from copy import deepcopy

from ssm_document_generator.definition.mixins.run_as_user_mixin import RunAsUserMixin
from ssm_document_generator.utils import constants
from test.ssm_document_generator_test.definition.dummy_definition import DummyDefinition


class Mixed(RunAsUserMixin, DummyDefinition):
    pass


def test_empty_run_as_user():
    user = 'tuser'
    tobject = Mixed(user=user)
    tdoc = deepcopy(tobject.DOCUMENT_TEMPLATE)
    tobject.parameters = []
    tobject.add_code(tdoc)

    assert tdoc['mainSteps'][0]['inputs']['runCommand'] == \
           [constants.SHEBANG_ENV + ' bash',
            "su - {} -c '{} -' <<'{}'".format(user, 'bash', str(tobject.uuid)),
            str(tobject.uuid)]
