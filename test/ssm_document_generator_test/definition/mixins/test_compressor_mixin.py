import textwrap

from ssm_document_generator.definition.mixins.compressor_mixin import CompressorMixin
from test.ssm_document_generator_test.definition.dummy_definition import DummyDefinition


class Mixed(CompressorMixin, DummyDefinition):
    pass


def test_compression():
    test_object = lambda: None
    test_code = '''
    test_object.test_var = 'success'
    '''
    assert getattr(test_object, 'test_var', None) is None

    tdefinition = Mixed(commands=textwrap.dedent(test_code).splitlines())

    exec('\n'.join(tdefinition.ssm_document()['mainSteps'][0]['inputs']['runCommand']))

    assert getattr(test_object, 'test_var', None) == 'success'
