from unittest import mock
from unittest.mock import MagicMock
import pytest

from troposphere import Template

from ssm_document_generator.converter import Converter


@mock.patch('ssm_document_generator.converter.code_converter_factory')
@mock.patch('ssm_document_generator.converter.yaml')
def test_convert_sanity(yaml_mock, converter_factory_mock):
    definition_path_mock = MagicMock()
    yaml_mock.load.return_value = {'name': 'test', 'description': '', 'command_file': 'test', 'command_type': 'python'}
    converter_factory_mock.get_converter.return_value = MagicMock()

    Converter.convert(definition_path_mock)
    converter_factory_mock.get_converter().convert.assert_called_once()


@pytest.mark.parametrize('test_input, expected', [
    ([], Template().to_dict()),
    ([Converter.ConversionResult({}, {'name': 'tname'})],
     {'Resources': {'tname': {
         'Type': 'AWS::SSM::Document',
         'Properties': {'Content': {}, 'DocumentType': 'Command'}
     }}})
])
def test_to_cloudformation(test_input, expected):
    assert Converter.to_cloudformation(test_input).to_dict() == expected


@pytest.mark.parametrize('discovered, converted, expected', [
    ([], [], []),
    (['mock.def'], 'mock_return', ['mock_return']),
])
@mock.patch('ssm_document_generator.converter.Converter.convert')
@mock.patch('ssm_document_generator.converter.discovery')
def test_convert_directory(discovery_mock, convert_mock, discovered, converted, expected):
    discovery_mock.get_definitions.return_value = discovered
    convert_mock.return_value = converted

    assert Converter.convert_directory(directory_path='dummy_path') == expected
