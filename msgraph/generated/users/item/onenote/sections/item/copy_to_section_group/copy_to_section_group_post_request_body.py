from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CopyToSectionGroupPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The groupId property
    group_id: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The renameAs property
    rename_as: Optional[str] = None
    # The siteCollectionId property
    site_collection_id: Optional[str] = None
    # The siteId property
    site_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopyToSectionGroupPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopyToSectionGroupPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopyToSectionGroupPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "renameAs": lambda n : setattr(self, 'rename_as', n.get_str_value()),
            "siteCollectionId": lambda n : setattr(self, 'site_collection_id', n.get_str_value()),
            "siteId": lambda n : setattr(self, 'site_id', n.get_str_value()),
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
        writer.write_str_value("groupId", self.group_id)
        writer.write_str_value("id", self.id)
        writer.write_str_value("renameAs", self.rename_as)
        writer.write_str_value("siteCollectionId", self.site_collection_id)
        writer.write_str_value("siteId", self.site_id)
        writer.write_additional_data_value(self.additional_data)
    

