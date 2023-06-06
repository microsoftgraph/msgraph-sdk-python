from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TeamMemberSettings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamMemberSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamMemberSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamMemberSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowAddRemoveApps", self.allow_add_remove_apps)
        writer.write_bool_value("allowCreatePrivateChannels", self.allow_create_private_channels)
        writer.write_bool_value("allowCreateUpdateChannels", self.allow_create_update_channels)
        writer.write_bool_value("allowCreateUpdateRemoveConnectors", self.allow_create_update_remove_connectors)
        writer.write_bool_value("allowCreateUpdateRemoveTabs", self.allow_create_update_remove_tabs)
        writer.write_bool_value("allowDeleteChannels", self.allow_delete_channels)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

