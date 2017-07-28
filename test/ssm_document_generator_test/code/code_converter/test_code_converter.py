import pytest

from ssm_document_generator.code.code_converter import CodeConverter


@pytest.mark.parametrize('template, definition, expected', [
    ({'parameters': {}},
     {'name': 'name'},
     {'parameters': {}}),
    ({'parameters': {'whee': 'param'}},
     {'notname': 'notname'},
     {'notname': 'notname', 'parameters': {'whee': 'param'}}),
    ({'parameters': {'whee': 'foo'}},
     {'notname': 'notname', 'parameters': {'whee': 'bar'}},
     {'notname': 'notname', 'parameters': {'whee': 'bar'}}),
    ({'parameters': {'whee': 'foo'}},
     {'notname': 'notname', 'parameters': {'param2': 'bar'}},
     {'notname': 'notname', 'parameters': {'whee': 'foo', 'param2': 'bar'}}),
])
def test_merge_definition_into_template(template, definition, expected):
    assert CodeConverter.merge_definition_into_template(template, definition) == expected
