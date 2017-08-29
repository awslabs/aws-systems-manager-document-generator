import inspect
import itertools
from abc import ABC
from pathlib import Path

from troposphere import ssm

from ssm_document_generator.definition.parameters.parameter import Parameter
from ssm_document_generator.utils import constants


# class Definition(ssm.Document): # todo
class Definition(ABC):
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
                 # command_type,
                 command_file,
                 parameters,
                 interpreter='bash',
                 # todo interpreter - property? will override here value set in mixins otherwise -_-
                 # run_as_user=None,
                 definition_path=None,
                 schemaVersion='2.2',
                 template_path=constants.DEFAULT_TEMPLATE_PATH, **kwargs):
        # todo validation
        # todo troposphere integration
        # super().__init__(name, DocumentType='Command')
        # todo override Content property for CFN

        # self.name = name
        self.description = description
        # self.command_type = command_type
        # type defined by definition class?
        self.command_file = command_file
        self.parameters = self.DEFAULT_PARAMETERS + parameters
        self.interpreter = interpreter
        # self.run_as_user = run_as_user
        self.schemaVersion = schemaVersion
        self.template_path = template_path

        ##
        self.definition_path = definition_path if definition_path is not None \
            else Path(inspect.stack()[1].filename).parent

        # todo accept kwargrs or just dict as override for template?

    def ssm_document(self):
        document = self.DOCUMENT_TEMPLATE  # todo consider not having template
        # document['name'] = self.name
        # document['description'] = self.description
        self.copy_fields(document)
        self.add_parameters(document)
        self.add_code(document)
        return document

    def add_parameters(self, document):
        document['parameters'] = {}  # todo
        for parameter in self.parameters:
            parameter.add_to_dict(document['parameters'])

    def shebang(self):
        # if self.run_as_user():
        #     return CodeConverter.SHEBANG

        return constants.SHEBANG_ENV + ' ' + self.interpreter

    def generate_parameters_code(self):
        return []

    def generate_commands(self):
        return self.get_file_lines(self.get_command_file_path())

    def get_command_file_path(self):
        return self.definition_path / self.command_file

    def get_file_lines(self, file_path):
        with Path(file_path).open() as code_stream:
            return code_stream.readlines()

    def prefix_code(self):
        """
        Returns code that should be added at the beginning of the generated script before the main body of code.
        :return:
        """
        # return [self.shebang()] + self.get_run_as_user_prefix()
        return [self.shebang()]

    def add_code(self, document):
        document['mainSteps'][0]['inputs']['runCommand'] = \
            list(itertools.chain(self.prefix_code(),
                                 self.generate_parameters_code(),
                                 self.generate_commands(),
                                 self.postfix_code()))

    def postfix_code(self):
        # return [str(self.uuid)] if self.run_as_user() else []
        return []

    def copy_fields(self, document):
        for field in self.FIELDS_TO_COPY:
            document[field] = getattr(self, field)
