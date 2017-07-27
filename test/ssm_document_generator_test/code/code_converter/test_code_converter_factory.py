import pytest

from ssm_document_generator.code.code_converter_factory import get_converter
from ssm_document_generator.code.python_converter import PythonConverter


def test_python():
    assert get_converter('python').__class__ == PythonConverter


def test_not_found():
    with pytest.raises(KeyError):
        get_converter('imaginary')