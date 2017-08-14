from lines_filter import include_filter, exclude_filter


def run_command(parameters):
    """
    The interface for Python commands is as demonstrated here - you need to provide a run_command function,
    that would accept dictionary with parameters and would return dictionary with results, specifying execution
    status and passing result content.

    **Don't write anything to stdout** that could interfere with proper result interpretation.
    """

    try:
        with open(parameters['filePath']) as to_retrieve:
            lines = to_retrieve.readlines()
    except IOError as e:
        return {'result': 'failure', 'error': str(e)}

    # include_filter = parameters['includeFilter'] # todo
    include_filter_list = []
    filtered = include_filter(lines, include_filter_list)

    # exclude_filter_list = parameters['excludeFilter'] #todo
    exclude_filter_list = ['dhclient']
    filtered = list(exclude_filter(filtered, exclude_filter_list))

    return {'result': 'success', 'file_content': filtered[-int(parameters['lineLimit']):-1]}
