from troposphere import ssm


class DefinitionTroposphereAdapter(ssm.Document):
    DocumentType = 'Command'

    def __init__(self, definition, **kwargs):
        super().__init__(definition.name, **kwargs)
        self.Content = definition.ssm_document()
