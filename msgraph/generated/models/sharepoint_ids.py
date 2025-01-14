from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SharepointIds(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The unique identifier (guid) for the item's list in SharePoint.
    list_id: Optional[str] = None
    # An integer identifier for the item within the containing list.
    list_item_id: Optional[str] = None
    # The unique identifier (guid) for the item within OneDrive for Business or a SharePoint site.
    list_item_unique_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier (guid) for the item's site collection (SPSite).
    site_id: Optional[str] = None
    # The SharePoint URL for the site that contains the item.
    site_url: Optional[str] = None
    # The unique identifier (guid) for the tenancy.
    tenant_id: Optional[str] = None
    # The unique identifier (guid) for the item's site (SPWeb).
    web_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharepointIds:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharepointIds
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharepointIds()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "listId": lambda n : setattr(self, 'list_id', n.get_str_value()),
            "listItemId": lambda n : setattr(self, 'list_item_id', n.get_str_value()),
            "listItemUniqueId": lambda n : setattr(self, 'list_item_unique_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "siteId": lambda n : setattr(self, 'site_id', n.get_str_value()),
            "siteUrl": lambda n : setattr(self, 'site_url', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "webId": lambda n : setattr(self, 'web_id', n.get_str_value()),
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
        writer.write_str_value("listId", self.list_id)
        writer.write_str_value("listItemId", self.list_item_id)
        writer.write_str_value("listItemUniqueId", self.list_item_unique_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("siteId", self.site_id)
        writer.write_str_value("siteUrl", self.site_url)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_str_value("webId", self.web_id)
        writer.write_additional_data_value(self.additional_data)
    

