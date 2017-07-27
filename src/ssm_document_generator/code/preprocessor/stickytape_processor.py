import tempfile
from pathlib import Path

import stickytape

from ssm_document_generator.code.preprocessor.file_processor import FileProcessor


class StickytapeProcessor(FileProcessor):
    """
    Preprocessor that takes in python file that represents entry point for program and returns one-file python program.
    """

    def _process(self, input_data):
        stickytape.script(input_data)
        pass