import pytest

from ssm_document_generator.command.result_status import ResultStatus
from ssm_document_generator.command.result import Result


@pytest.mark.parametrize('test_input', [
    [],
    [1, 2],
    {'foo': 'bar'}
])
def test_success(test_input):
    assert Result.success(test_input) == {'status': ResultStatus.Success.value, 'result': test_input}


@pytest.mark.parametrize('error, message, expected', [
    (RuntimeError('tm1'), None,
     {'status': ResultStatus.Failure.value, 'status_details': 'RuntimeError', 'message': 'tm1'}),
    (RuntimeError('tm1'), 'tm2',
     {'status': ResultStatus.Failure.value, 'status_details': 'RuntimeError', 'message': 'tm2'}),
])
def test_failure(error, message, expected):
    assert Result.failure(error, message) == expected


def raiser(exception):
    """
    Need this to work around limitation of the fact that I can't have just a statement in lambda
    """
    raise exception


@pytest.mark.parametrize('runnable, expected', [
    (lambda: [], Result.success([], metadata={'result_type': 'JSON'})),
    (lambda: raiser(RuntimeError('t1')), Result.failure(RuntimeError('t1'), metadata={'result_type': 'JSON'}))
])
def test_run(runnable, expected):
    result = Result.run(runnable)
    result.pop('message', None)
    expected.pop('message', None)
    # Don't compare messages, as in run its traceback.
    assert result == expected
