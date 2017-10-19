import base64
import lzma
import textwrap

compressed_code_template = """
import base64, {}
exec(lzma.decompress(base64.decodebytes({})))
"""


class CompressorMixin:
    """
    This Mixin allows to compress the size of the resulting documents to mitigate various size constraints.
    I've observed ~50% compression level for the documents I've tested this upon.
    """

    def __init__(self, compressor=lzma, *args, **kwargs):
        """
        :param compressor: Compressor object that provides the compress/decompress functions (also should be present on
        the target machine).
        Examples lzma, bz2 zlib from standard lib.
        """
        super().__init__(*args, **kwargs)
        self.compressor = compressor

    def generate_commands(self):
        commands_text = '\n'.join(super().generate_commands())
        compressed_commands = base64.encodebytes(self.compressor.compress(commands_text.encode()))
        return textwrap.dedent(compressed_code_template).format(
            self.compressor.__name__, compressed_commands).splitlines()
