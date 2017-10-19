import pytest

from ssm_document_generator.definition.parameters.common import ENTITIES_LIMIT
from ssm_document_generator.definition.parameters.dict_parameters_mixin import DictParametersMixin
from test.ssm_document_generator_test.definition.filled_definition import FilledDefinition


class Mixed(DictParametersMixin, FilledDefinition):
    pass


@pytest.mark.parametrize('test_input, expected', [
    ([], ['parameters = {}']),
    ([ENTITIES_LIMIT], ["parameters = {\"" + ENTITIES_LIMIT.name + "\": \"{{" + ENTITIES_LIMIT.name + "}}\"}"])
])
def test_generate_parameters_code(test_input, expected):
    tobject = Mixed()
    tobject.parameters = test_input
    assert tobject.generate_parameters_code() == expected
