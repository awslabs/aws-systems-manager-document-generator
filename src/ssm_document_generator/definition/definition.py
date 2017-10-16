import itertools

from copy import deepcopy

from ssm_document_generator.definition.parameters.parameter import Parameter
from ssm_document_generator.utils import constants


class Definition:
    """
    The base Definition class that serves as a foundation for any document definition. You can introduce additional
    functionality by inheriting from this class and using one of the provided mixins, one of your own mixins
    or by just overriding the functions of this class.
    """

    DEFAULT_PARAMETERS = [
        Parameter('executionTimeout',
                  '(Optional) The time in seconds for a command to complete '
                  'before it is considered to have failed. Default is 120.'
                  ' Maximum is 28800 (8 hours).',
                  default='120',
                  allowed_pattern='([1-9][0-9]{0,3})|(1[0-9]{1,4})|(2[0-7][0-9]{1,3})|(28[0-7][0-9]{1,2})|(28800)')
    ]

    DOCUMENT_TEMPLATE = {
        "mainSteps": [
            {
                "action": "aws:runShellScript",
                "name": "runShellScript",
                "inputs": {
                    "id": "0.runShellScript",
                    "runCommand": [],
                    "timeoutSeconds": "{{ executionTimeout }}"
                }
            }
        ]
    }

    FIELDS_TO_COPY = ['description', 'schemaVersion']

    def __init__(self, name,
                 description,
                 parameters=None,
                 interpreter='bash',
                 schema_version='2.2'):
        self.name = name
        self.description = description
        self.parameters = self.DEFAULT_PARAMETERS + (parameters if parameters is not None else [])
        self.interpreter = interpreter
        self.schemaVersion = schema_version

    def ssm_document(self):
        """
        Return the ssm document in the form of the dictionary, based on the definition.
        :return:
        """
        document = deepcopy(self.DOCUMENT_TEMPLATE)
        self.copy_fields(document)
        self.add_parameters(document)
        self.add_code(document)
        return document

    def copy_fields(self, document):
        """
        Copy the defined set of fields from the definition to the provided document dictionary.
        """
        for field in self.FIELDS_TO_COPY:
            document[field] = getattr(self, field)

    def add_parameters(self, document):
        """
        Add the parameters description to the given document dictionary.
        """
        document.setdefault('parameters', {})
        for parameter in self.parameters:
            parameter.add_to_dict(document['parameters'])

    def add_code(self, document):
        """
        Add the commands to be executed to the given document dictionary.
        """
        document['mainSteps'][0]['inputs']['runCommand'] = \
            list(itertools.chain(self.prefix_code(),
                                 self.generate_parameters_code(),
                                 self.generate_commands(),
                                 self.postfix_code()))

    def shebang(self):
        return constants.SHEBANG_ENV + ' ' + self.interpreter

    def generate_commands(self):
        return []

    def generate_parameters_code(self):
        """
        From given parameter definition - generate code to pass the parameters to the command implementation
        """
        return []

    def prefix_code(self):
        """
        Returns code that should be added at the beginning of the generated script before the main body of code.
        :return:
        """
        return [self.shebang()]

    def postfix_code(self):
        """
        Returns code that should be added at the end of the generated script after the main body of code.
        """
        return []
