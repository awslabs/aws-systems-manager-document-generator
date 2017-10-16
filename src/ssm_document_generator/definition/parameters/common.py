from ssm_document_generator.definition.parameters.parameter import Parameter

# A set of commonly used parameters

ENTITIES_LIMIT = Parameter(name='entitiesLimit',
                           description='Maximum number of things (lines, objects, etc) to return.\n'
                                       'Only last {{lineLimit}} lines would be returned.\n'
                                       'Please specify 0 for no limit.',
                           default='0')
