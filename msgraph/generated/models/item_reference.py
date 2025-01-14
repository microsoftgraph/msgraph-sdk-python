from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sharepoint_ids import SharepointIds

@dataclass
class ItemReference(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Unique identifier of the drive instance that contains the driveItem. Only returned if the item is located in a drive. Read-only.
    drive_id: Optional[str] = None
    # Identifies the type of drive. Only returned if the item is located in a drive. See drive resource for values.
    drive_type: Optional[str] = None
    # Unique identifier of the driveItem in the drive or a listItem in a list. Read-only.
    id: Optional[str] = None
    # The name of the item being referenced. Read-only.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Percent-encoded path that can be used to navigate to the item. Read-only.
    path: Optional[str] = None
    # A unique identifier for a shared resource that can be accessed via the Shares API.
    share_id: Optional[str] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[SharepointIds] = None
    # For OneDrive for Business and SharePoint, this property represents the ID of the site that contains the parent document library of the driveItem resource or the parent list of the listItem resource. The value is the same as the id property of that site resource. It is an opaque string that consists of three identifiers of the site. For OneDrive, this property is not populated.
    site_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItemReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItemReference
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItemReference()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sharepoint_ids import SharepointIds

        from .sharepoint_ids import SharepointIds

        fields: dict[str, Callable[[Any], None]] = {
            "driveId": lambda n : setattr(self, 'drive_id', n.get_str_value()),
            "driveType": lambda n : setattr(self, 'drive_type', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "shareId": lambda n : setattr(self, 'share_id', n.get_str_value()),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(SharepointIds)),
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
        writer.write_str_value("driveId", self.drive_id)
        writer.write_str_value("driveType", self.drive_type)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("path", self.path)
        writer.write_str_value("shareId", self.share_id)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_str_value("siteId", self.site_id)
        writer.write_additional_data_value(self.additional_data)
    

