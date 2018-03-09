class DocumentTagsMetadataMixin:
    """
    Adds metadata support in form of tags on SSM document.
    """

    def __init__(self, metadata=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = metadata or []

    def get_metadata(self):
        return {**{tag.name: tag.value for tag in self.tags}, **super().get_metadata()}
