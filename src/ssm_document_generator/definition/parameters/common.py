from ssm_document_generator.definition.parameters.parameter import Parameter


# A set of commonly used parameters

def entities_limit(default_value=0):
    return Parameter(name='entitiesLimit',
                     description='Maximum number of things (lines, objects, etc) to return.\n'
                                 'Only last {{entitiesLimit}} things would be returned.\n'
                                 'Please specify 0 for no limit.',
                     default=str(default_value))
