from ssm_document_generator.definition.parameters.parameter import Parameter


# A set of commonly used parameters

def entities_limit(default_value=0):
    return Parameter(name='entitiesLimit',
                     description='Maximum number of things (lines, objects, etc) to return.\n'
                                 'Only last {{entitiesLimit}} things would be returned.\n'
                                 'Please specify 0 for no limit.',
                     default=str(default_value))


def regex_filter_expression(expression=''):
    return Parameter(name='filterExpression',
                     description='Filter regexp. It would be applied to the output of command.\n'
                                 'Only lines that match would go into result.',
                     default=expression)


def file_path(default=None):
    return Parameter('filePath', 'Path to file', default=default)


def process_id(default=None):
    return Parameter('processId', 'The PID of interest', allowed_pattern='^\d+$', default=default)
