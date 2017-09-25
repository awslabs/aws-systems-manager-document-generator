import pytest

from ssm_document_generator.utils.result import Result


@pytest.mark.parametrize('test_input', [
    [],
    [1, 2],
    {'foo': 'bar'}
])
def test_success(test_input):
    assert Result.success(test_input) == {'status': 'Success', 'result': test_input}


@pytest.mark.parametrize('error, message, expected', [
    (RuntimeError('tm1'), None, {'status': 'Failed', 'status_details': 'RuntimeError', 'message': 'tm1'}),
    (RuntimeError('tm1'), 'tm2', {'status': 'Failed', 'status_details': 'RuntimeError', 'message': 'tm2'}),
])
def test_failure(error, message, expected):
    assert Result.failure(error, message) == expected


def raiser(exception):
    """
    Need this to work around limitation of the fact that I can't have just a statement in lambda
    """
    raise exception


@pytest.mark.parametrize('runnable, expected', [
    (lambda: [], Result.success([])),
    (lambda: raiser(RuntimeError('t1')), Result.failure(RuntimeError('t1')))
])
def test_run(runnable, expected):
    assert Result.run(runnable) == expected
