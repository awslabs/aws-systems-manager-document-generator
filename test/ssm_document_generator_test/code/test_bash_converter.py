import pytest

from ssm_document_generator.code.bash_converter import BashConverter


@pytest.mark.parametrize('test_input, expected', [
    ({}, []),
    ({'testParameter': {'type': 'String'}}, ['testParameter={{testParameter}}'])
])
def test_generate_parameters_code(test_input, expected):
    assert BashConverter().generate_parameters_code(test_input) == expected
