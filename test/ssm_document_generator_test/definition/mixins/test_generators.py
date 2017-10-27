from ssm_document_generator.definition.mixins.generators import add_params_mixin


def test_add_params_mixin():
    class TestBase:
        parameters = []

    class TestMix(add_params_mixin(['test']), TestBase):
        pass

    assert TestMix().parameters == ['test']


def test_add_params_mixin_init():
    class TestBase:
        def __init__(self, tparam):
            self.tparam = tparam
            self.parameters = []

    class TestMix(add_params_mixin(tparam='tparam'), TestBase):
        pass

    assert TestMix().tparam == 'tparam'
    assert TestMix().parameters == []
