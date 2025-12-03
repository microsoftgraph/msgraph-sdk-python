from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .place import Place
    from .place_mode import PlaceMode

from .place import Place

@dataclass
class Workspace(Place, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.workspace"
    # The capacity property
    capacity: Optional[int] = None
    # The displayDeviceName property
    display_device_name: Optional[str] = None
    # The emailAddress property
    email_address: Optional[str] = None
    # The mode property
    mode: Optional[PlaceMode] = None
    # The nickname property
    nickname: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Workspace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Workspace
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Workspace()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .place import Place
        from .place_mode import PlaceMode

        from .place import Place
        from .place_mode import PlaceMode

        fields: dict[str, Callable[[Any], None]] = {
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "displayDeviceName": lambda n : setattr(self, 'display_device_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_object_value(PlaceMode)),
            "nickname": lambda n : setattr(self, 'nickname', n.get_str_value()),
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
        writer.write_int_value("capacity", self.capacity)
        writer.write_str_value("displayDeviceName", self.display_device_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_object_value("mode", self.mode)
        writer.write_str_value("nickname", self.nickname)
    

