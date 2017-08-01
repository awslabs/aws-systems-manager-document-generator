from io import StringIO
from unittest import mock
from unittest.mock import MagicMock

import pytest

from ssm_document_generator.converter import Converter


@mock.patch('ssm_document_generator.converter.code_converter_factory')
@mock.patch('ssm_document_generator.converter.yaml')
def test_convert_sanity(yaml_mock, converter_factory_mock):
    definition_path_mock = MagicMock()

    yaml_mock.load.return_value = {'name': 'test', 'description': '', 'command_file': 'test', 'command_type': 'python'}

    converter_factory_mock.get_converter.return_value = MagicMock()

    Converter.convert(definition_path_mock)

    converter_factory_mock.get_converter().convert.assert_called_once()
