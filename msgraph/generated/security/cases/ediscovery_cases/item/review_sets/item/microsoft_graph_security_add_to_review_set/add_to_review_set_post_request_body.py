from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.security.additional_data_options import AdditionalDataOptions
    from ........models.security.cloud_attachment_version import CloudAttachmentVersion
    from ........models.security.document_version import DocumentVersion
    from ........models.security.ediscovery_search import EdiscoverySearch
    from ........models.security.items_to_include import ItemsToInclude

@dataclass
class AddToReviewSetPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The additionalDataOptions property
    additional_data_options: Optional[AdditionalDataOptions] = None
    # The cloudAttachmentVersion property
    cloud_attachment_version: Optional[CloudAttachmentVersion] = None
    # The documentVersion property
    document_version: Optional[DocumentVersion] = None
    # The itemsToInclude property
    items_to_include: Optional[ItemsToInclude] = None
    # The search property
    search: Optional[EdiscoverySearch] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AddToReviewSetPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AddToReviewSetPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AddToReviewSetPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ........models.security.additional_data_options import AdditionalDataOptions
        from ........models.security.cloud_attachment_version import CloudAttachmentVersion
        from ........models.security.document_version import DocumentVersion
        from ........models.security.ediscovery_search import EdiscoverySearch
        from ........models.security.items_to_include import ItemsToInclude

        from ........models.security.additional_data_options import AdditionalDataOptions
        from ........models.security.cloud_attachment_version import CloudAttachmentVersion
        from ........models.security.document_version import DocumentVersion
        from ........models.security.ediscovery_search import EdiscoverySearch
        from ........models.security.items_to_include import ItemsToInclude

        fields: dict[str, Callable[[Any], None]] = {
            "additionalDataOptions": lambda n : setattr(self, 'additional_data_options', n.get_collection_of_enum_values(AdditionalDataOptions)),
            "cloudAttachmentVersion": lambda n : setattr(self, 'cloud_attachment_version', n.get_enum_value(CloudAttachmentVersion)),
            "documentVersion": lambda n : setattr(self, 'document_version', n.get_enum_value(DocumentVersion)),
            "itemsToInclude": lambda n : setattr(self, 'items_to_include', n.get_collection_of_enum_values(ItemsToInclude)),
            "search": lambda n : setattr(self, 'search', n.get_object_value(EdiscoverySearch)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("additionalDataOptions", self.additional_data_options)
        writer.write_enum_value("cloudAttachmentVersion", self.cloud_attachment_version)
        writer.write_enum_value("documentVersion", self.document_version)
        writer.write_enum_value("itemsToInclude", self.items_to_include)
        writer.write_object_value("search", self.search)
        writer.write_additional_data_value(self.additional_data)
    

