from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest

from ssm_document_generator.definition.mixins.read_from_file_mixin import ReadFromFileMixin
from test.ssm_document_generator_test.definition.dummy_definition import DummyDefinition


class Mixed(ReadFromFileMixin, DummyDefinition):
    pass


def test_read_from_file():
    temp_commands = ['wh', 'eee']
    with NamedTemporaryFile(mode='w') as temp_file:
        temp_file.write('\n'.join(temp_commands))
        temp_file.flush()

        tobject = Mixed(command_file_name=temp_file.name)
        assert tobject.generate_commands() == temp_commands


def test_infer_command_directory():
    assert ReadFromFileMixin.infer_command_directory('test_read_from_file_mixin.py') == Path(__file__).parent


def test_infer_command_directory_not_found():
    with pytest.raises(RuntimeError):
        ReadFromFileMixin.infer_command_directory('6246c60c-87d7-4b6c-ad89-78a2bdc63962')  # random uuid
