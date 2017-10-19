import pytest

from ssm_document_generator.definition.parameters.assign_parameters_mixin import AssignParametersMixin
from ssm_document_generator.definition.parameters.common import entities_limit
from test.ssm_document_generator_test.definition.dummy_definition import DummyDefinition


class Mixed(AssignParametersMixin, DummyDefinition):
    pass


@pytest.mark.parametrize('test_input, expected', [
    ([], []),
    ([entities_limit()], [entities_limit().name + '={{' + entities_limit().name + '}}'])
])
def test_generate_parameters_code(test_input, expected):
    tobject = Mixed()
    tobject.parameters = test_input
    assert tobject.generate_parameters_code() == expected
