from copy import deepcopy
from unittest import mock
from unittest.mock import MagicMock

import pytest
from io import StringIO

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


def test_convert_sanity():
    code_converter = CodeConverter()

    barebones_template = {'mainSteps': [{'inputs': {'runCommand': []}}], 'parameters': {}}

    code_converter.process_code = MagicMock(return_value=[])
    code_converter.read_template = MagicMock(return_value=deepcopy(barebones_template))

    result = deepcopy(barebones_template)
    result['mainSteps'][0]['inputs']['runCommand'].append(CodeConverter.SHEBANG)

    assert result == code_converter.convert({}, 'dummy_path')


@mock.patch('ssm_document_generator.code.code_converter.Path')
def test_process_code(mocked_path):
    mocked_path.return_value.open.return_value.__enter__.return_value = StringIO('test\nline')
    code_converter = CodeConverter()
    assert code_converter.process_code('some_path') == ['test\n', 'line']
