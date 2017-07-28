import pytest

from ssm_document_generator.code.python_converter import PythonConverter


@pytest.mark.parametrize('test_input, expected', [
    ({}, ['parameters = {}']),
    ({'testParameter': {'type': 'String'}}, ['parameters = {\"testParameter\": \"{{testParameter}}\"}'])
])
def test_generate_parameters_code(test_input, expected):
    print(PythonConverter().generate_parameters_code(test_input))
    assert PythonConverter().generate_parameters_code(test_input) == expected
