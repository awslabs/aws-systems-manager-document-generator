import pytest

from ssm_document_generator.definition.definition import Definition


def test_copy_fields():
    tdef = Definition('tdef', 'tdef')
    tresult = {}
    tdef.copy_fields(tresult)
    assert tresult == {'description': 'tdef', 'schemaVersion': '2.2'}


def test_add_parameters():
    tdef = Definition('tdef', 'tdef')
    tresult = {}
    tdef.add_parameters(tresult)
    expected = {'parameters': {parameter.name: parameter.get_dict() for parameter in tdef.DEFAULT_PARAMETERS}}
    assert tresult == expected
