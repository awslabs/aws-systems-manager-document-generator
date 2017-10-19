from troposphere import ssm


class DefinitionTroposphereAdapter(ssm.Document):
    """
    An adapter to integrate the Definition of the SSM document with Troposphere.
    """

    DocumentType = 'Command'

    def __init__(self, definition, **kwargs):
        super().__init__(definition.name, **kwargs)
        self.Content = definition.ssm_document()
