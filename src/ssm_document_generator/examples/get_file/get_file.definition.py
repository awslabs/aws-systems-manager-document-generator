# name: getFile
# description: Retrieves a specified file content.
# parameters:
#   lineLimit:
#     type: String
#     default: "0"
#     description: >
#       Maximum number of lines to return. Only last {{lineLimit}} lines would be returned.
#       Please specify 0 for no limit.
#   filePath:
#     # Todo consider limiting this to some pre-defined list.
#     type: String
#     description: Path to file to retrieve.
#     #Todo consider passing regexes instead
# #Commented out for now as I'm contacting SSM team to investigate expected behaviour of StringList type parameters.
# #  includeFilter:
# #    type: StringList
# #    default: []
# #    description: Include only lines that contain words in the given list. If list is empty - include everything.
# #  excludeFilter:
# #    type: StringList
# #    default: []
# #    description: >
# #      Include only lines that don't contain words in the given list.
# #      If list is empty - include everything. Applied after includeFilter
# command_type: python
# command_file: get_file.py




# 'filePath': {
#         'type': 'String',
#         'description': 'bla'
#     }
# parameters = {
#     'lineLimit': {
#         'type': 'String',
#         'default': '0',
#         'description': 'blah'
#     },
#     'filePath': Parameter('test', 'test')
# }

# class Parameters(object):
#     def __init__(self, *args):
#         pass


# name = 'getFile'
# description = 'blah'
# nparameters = Parameters(
#     Parameter('test', 'test', 'test'),
#     Parameter('test', 'test', 'test'),
#     Parameter('test', 'test', 'test'),
#     Parameter('test', 'test', 'test')
# )
from ssm_document_generator.definition.definition import Definition
from ssm_document_generator.definition.parameter import Parameter

definition = Definition(
    name='getFile',
    description='Retrieves a specified file content',
    command_file='get_file.py',
    interpreter='python',  # won't be here
    parameters=[
        Parameter(name='lineLimit',
                  description='Maximum number of lines to return. Only last {{lineLimit}} lines would be returned'
                              'Please specify 0 for no limit.',
                  default='0'),
        Parameter('filePath', 'Path to file to retrieve')
    ]
)
