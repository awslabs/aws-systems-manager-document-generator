from ssm_document_generator.utils.result_status import ResultStatus


class Result:
    """
    Util for simplifying providing unified interface to generated commands
    """

    @classmethod
    def success(cls, result_data):
        return {'status': ResultStatus.Success.value, 'result': result_data}

    @classmethod
    def failure(cls, error, message=None):
        return {'status': ResultStatus.Failure.value, 'status_details': type(error).__name__,
                'message': message if message else str(error)}

    @classmethod
    def run(cls, runnable):
        """
        Try running passed runnable, if run is successful return Result.success if run threw some exception
        catch it and return Result.failure.
        If functions has parameters - you should pass a lambda with the function call. It's done like that
        so that if any exceptions arise at the parameter evaluation time - they would be caught.
        """
        try:
            return Result.success(runnable())
        except Exception as error:
            return Result.failure(error)
