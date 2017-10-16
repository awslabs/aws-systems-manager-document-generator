import pytest
from copy import deepcopy

from ssm_document_generator.definition.mixins.python_entry_point_mixin import PythonEntryPointMixin
from ssm_document_generator.utils import constants
from test.ssm_document_generator_test.definition.filled_definition import FilledDefinition


class Mixed(PythonEntryPointMixin, FilledDefinition):
    pass


def test_python_entry_point():
    tobject = Mixed()
    tdoc = deepcopy(tobject.DOCUMENT_TEMPLATE)
    tobject.parameters = []
    tobject.add_code(tdoc)

    assert tdoc['mainSteps'][0]['inputs']['runCommand'] == \
           [constants.SHEBANG_ENV + ' python3',
            'import json',
            tobject.postfix_code()[0]]
