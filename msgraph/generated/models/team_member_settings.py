from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class TeamMemberSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # If set to true, members can add and remove apps.
    allow_add_remove_apps: Optional[bool] = None
    # If set to true, members can add and update private channels.
    allow_create_private_channels: Optional[bool] = None
    # If set to true, members can add and update channels.
    allow_create_update_channels: Optional[bool] = None
    # If set to true, members can add, update, and remove connectors.
    allow_create_update_remove_connectors: Optional[bool] = None
    # If set to true, members can add, update, and remove tabs.
    allow_create_update_remove_tabs: Optional[bool] = None
    # If set to true, members can delete channels.
    allow_delete_channels: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamMemberSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamMemberSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamMemberSettings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowAddRemoveApps": lambda n : setattr(self, 'allow_add_remove_apps', n.get_bool_value()),
            "allowCreatePrivateChannels": lambda n : setattr(self, 'allow_create_private_channels', n.get_bool_value()),
            "allowCreateUpdateChannels": lambda n : setattr(self, 'allow_create_update_channels', n.get_bool_value()),
            "allowCreateUpdateRemoveConnectors": lambda n : setattr(self, 'allow_create_update_remove_connectors', n.get_bool_value()),
            "allowCreateUpdateRemoveTabs": lambda n : setattr(self, 'allow_create_update_remove_tabs', n.get_bool_value()),
            "allowDeleteChannels": lambda n : setattr(self, 'allow_delete_channels', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_bool_value("allowAddRemoveApps", self.allow_add_remove_apps)
        writer.write_bool_value("allowCreatePrivateChannels", self.allow_create_private_channels)
        writer.write_bool_value("allowCreateUpdateChannels", self.allow_create_update_channels)
        writer.write_bool_value("allowCreateUpdateRemoveConnectors", self.allow_create_update_remove_connectors)
        writer.write_bool_value("allowCreateUpdateRemoveTabs", self.allow_create_update_remove_tabs)
        writer.write_bool_value("allowDeleteChannels", self.allow_delete_channels)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

