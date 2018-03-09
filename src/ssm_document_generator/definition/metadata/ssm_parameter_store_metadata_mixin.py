class SSMParameterStoreMetadataMixin:
    """
    Adds metadata support in form of things stored to SSM parameter store to definition.
    """

    def __init__(self, metadata=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = metadata or []

    def get_complimentary_cfn_resources(self):
        return [tag.as_ssm_parameter(self.name) for tag in self.tags] + super().get_complimentary_cfn_resources()
