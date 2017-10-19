import pytest

from ssm_document_generator.definition.parameters.common import entities_limit
from ssm_document_generator.definition.parameters.dict_parameters_mixin import DictParametersMixin
from test.ssm_document_generator_test.definition.dummy_definition import DummyDefinition


class Mixed(DictParametersMixin, DummyDefinition):
    pass


@pytest.mark.parametrize('test_input, expected', [
    ([], ['parameters = {}']),
    ([entities_limit()], ["parameters = {\"" + entities_limit().name + "\": \"{{" + entities_limit().name + "}}\"}"])
])
def test_generate_parameters_code(test_input, expected):
    tobject = Mixed()
    tobject.parameters = test_input
    assert tobject.generate_parameters_code() == expected
