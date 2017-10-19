from ssm_document_generator.command.result_type import ResultType
from ssm_document_generator.command.result import Result

from ssm_document_generator.examples.get_file.lines_filter import include_filter, exclude_filter


def get_file(file_path, line_limit):
    with open(file_path) as to_retrieve:
        lines = to_retrieve.readlines()

    # include_filter = parameters['includeFilter'] # todo
    include_filter_list = []
    filtered = include_filter(lines, include_filter_list)

    # exclude_filter_list = parameters['excludeFilter'] #todo
    exclude_filter_list = ['dhclient']
    filtered = list(exclude_filter(filtered, exclude_filter_list))

    return ''.join(filtered[-line_limit:])


def run_command(parameters):
    """
    The interface for Python commands is as demonstrated here - you need to provide a run_command function,
    that would accept dictionary with parameters and would return dictionary with results, specifying execution
    status and passing result content.

    **Don't write anything to stdout** that could interfere with proper result interpretation.
    """

    return Result.run(lambda: get_file(parameters['filePath'], int(parameters['entitiesLimit'])),
                      result_type=ResultType.PlainText)
