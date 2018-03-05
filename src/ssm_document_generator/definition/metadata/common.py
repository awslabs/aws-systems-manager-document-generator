from ssm_document_generator.definition.metadata.tag import Tag


def category(categories):
    return Tag('category', categories)


def access_level(level):
    return Tag('accessLevel', level)


def nodes_filter_leader():
    return Tag('nodesFilter', 'leader')
