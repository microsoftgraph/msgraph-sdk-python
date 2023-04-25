from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, sharepoint_settings

from . import entity

class Sharepoint(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Sharepoint and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The settings property
        self._settings: Optional[sharepoint_settings.SharepointSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Sharepoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Sharepoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Sharepoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, sharepoint_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(sharepoint_settings.SharepointSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("settings", self.settings)
    
    @property
    def settings(self,) -> Optional[sharepoint_settings.SharepointSettings]:
        """
        Gets the settings property value. The settings property
        Returns: Optional[sharepoint_settings.SharepointSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[sharepoint_settings.SharepointSettings] = None) -> None:
        """
        Sets the settings property value. The settings property
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    

