from ssm_document_generator.definition.definition import Definition
from ssm_document_generator.definition.metadata.document_tags_metadata_mixin import DocumentTagsMetadataMixin
from ssm_document_generator.definition.mixins.compressor_mixin import CompressorMixin
from ssm_document_generator.definition.mixins.python_entry_point_mixin import PythonEntryPointMixin
from ssm_document_generator.definition.mixins.read_from_file_mixin import ReadFromFileMixin
from ssm_document_generator.definition.mixins.run_as_user_mixin import RunAsUserMixin
from ssm_document_generator.definition.mixins.stickytape_mixin import StickyTapeMixin
from ssm_document_generator.definition.parameters.dict_parameters_mixin import DictParametersMixin


class PythonDefinition(CompressorMixin,
                       StickyTapeMixin,
                       ReadFromFileMixin,
                       DictParametersMixin,
                       PythonEntryPointMixin,
                       RunAsUserMixin,
                       DocumentTagsMetadataMixin,
                       Definition):
    """
    Default definition for python commands
    """
