from troposphere import Sub

from ssm_document_generator.definition.metadata.tag import Tag


def test_type_str():
    assert 'String' == Tag.get_type('a')


def test_type_list():
    assert 'StringList' == Tag.get_type(['a'])


def test_as_ssm_parameter():
    ttag = Tag('tname', 'tvalue')
    t_parameter = ttag.as_ssm_parameter('tcommand')

    assert t_parameter.title == 'tcommandTnameTag'
    assert t_parameter.Name.to_dict() == Sub('/owls/${AWS::StackName}/tcommand/tname').to_dict()
    assert t_parameter.Type == 'String'
    assert t_parameter.Value == 'tvalue'
