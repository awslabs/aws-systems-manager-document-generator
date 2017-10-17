import json

from ssm_document_generator.command.result_status import ResultStatus
from ssm_document_generator.command.result_type import ResultType


class Result:
    """
    Util for simplifying providing unified interface to generated commands
    """

    @classmethod
    def success(cls, result_data, metadata=None):
        if metadata is None:
            metadata = {}

        return {**{'status': ResultStatus.Success.value, 'result': result_data}, **metadata}

    @classmethod
    def failure(cls, error, message=None, metadata=None):
        if metadata is None:
            metadata = {}

        return {**{'status': ResultStatus.Failure.value, 'status_details': type(error).__name__,
                   'message': message if message else str(error)},
                **metadata}

    @classmethod
    def run(cls, runnable, result_type=ResultType.JSON):
        """
        Try running passed runnable, if run is successful return Result.success if run threw some exception
        catch it and return Result.failure.
        If functions has parameters - you should pass a lambda with the function call. It's done like that
        so that if any exceptions arise at the parameter evaluation time - they would be caught.
        """
        metadata = {'result_type': result_type.value}

        try:
            result = Result.success(runnable(), metadata)
        except Exception as error:
            result = Result.failure(error, metadata=metadata)
        finally:
            print(json.dumps(result, sort_keys=True, default=str))
            return result
