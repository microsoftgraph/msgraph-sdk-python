from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .additional_data_options import AdditionalDataOptions
    from .case_operation import CaseOperation
    from .cloud_attachment_version import CloudAttachmentVersion
    from .document_version import DocumentVersion
    from .ediscovery_review_set import EdiscoveryReviewSet
    from .ediscovery_search import EdiscoverySearch
    from .items_to_include import ItemsToInclude

from .case_operation import CaseOperation

@dataclass
class EdiscoveryAddToReviewSetOperation(CaseOperation, Parsable):
    # The additionalDataOptions property
    additional_data_options: Optional[AdditionalDataOptions] = None
    # The cloudAttachmentVersion property
    cloud_attachment_version: Optional[CloudAttachmentVersion] = None
    # The documentVersion property
    document_version: Optional[DocumentVersion] = None
    # The itemsToInclude property
    items_to_include: Optional[ItemsToInclude] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # eDiscovery review set to which items matching source collection query gets added.
    review_set: Optional[EdiscoveryReviewSet] = None
    # eDiscovery search that gets added to review set.
    search: Optional[EdiscoverySearch] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryAddToReviewSetOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryAddToReviewSetOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryAddToReviewSetOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .additional_data_options import AdditionalDataOptions
        from .case_operation import CaseOperation
        from .cloud_attachment_version import CloudAttachmentVersion
        from .document_version import DocumentVersion
        from .ediscovery_review_set import EdiscoveryReviewSet
        from .ediscovery_search import EdiscoverySearch
        from .items_to_include import ItemsToInclude

        from .additional_data_options import AdditionalDataOptions
        from .case_operation import CaseOperation
        from .cloud_attachment_version import CloudAttachmentVersion
        from .document_version import DocumentVersion
        from .ediscovery_review_set import EdiscoveryReviewSet
        from .ediscovery_search import EdiscoverySearch
        from .items_to_include import ItemsToInclude

        fields: dict[str, Callable[[Any], None]] = {
            "additionalDataOptions": lambda n : setattr(self, 'additional_data_options', n.get_collection_of_enum_values(AdditionalDataOptions)),
            "cloudAttachmentVersion": lambda n : setattr(self, 'cloud_attachment_version', n.get_enum_value(CloudAttachmentVersion)),
            "documentVersion": lambda n : setattr(self, 'document_version', n.get_enum_value(DocumentVersion)),
            "itemsToInclude": lambda n : setattr(self, 'items_to_include', n.get_collection_of_enum_values(ItemsToInclude)),
            "reviewSet": lambda n : setattr(self, 'review_set', n.get_object_value(EdiscoveryReviewSet)),
            "search": lambda n : setattr(self, 'search', n.get_object_value(EdiscoverySearch)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("additionalDataOptions", self.additional_data_options)
        writer.write_enum_value("cloudAttachmentVersion", self.cloud_attachment_version)
        writer.write_enum_value("documentVersion", self.document_version)
        writer.write_enum_value("itemsToInclude", self.items_to_include)
        writer.write_object_value("reviewSet", self.review_set)
        writer.write_object_value("search", self.search)
    

