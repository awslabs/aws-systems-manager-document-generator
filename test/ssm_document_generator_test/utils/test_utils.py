import pytest

from ssm_document_generator import utils


@pytest.mark.parametrize('test_input, expected', [
    ({}, {}),
    ({'test': 'test'}, {'test': 'test'}),
    ({'test': 'test', 'tnone': None}, {'test': 'test'}),
])
def test_dict_without_none_entries(test_input, expected):
    assert utils.dict_without_none_entries(test_input) == expected
