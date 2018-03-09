from ssm_document_generator.definition.metadata.tag import Tag


def category(category_name):
    return Tag('category', category_name)


def access_level(level):
    return Tag('accessLevel', level)
