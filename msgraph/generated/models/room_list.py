from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .place import Place
    from .room import Room

from .place import Place

@dataclass
class RoomList(Place, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.roomList"
    # The email address of the room list.
    email_address: Optional[str] = None
    # The rooms property
    rooms: Optional[List[Room]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoomList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoomList
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoomList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .place import Place
        from .room import Room

        from .place import Place
        from .room import Room

        fields: Dict[str, Callable[[Any], None]] = {
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "rooms": lambda n : setattr(self, 'rooms', n.get_collection_of_object_values(Room)),
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
        from .place import Place
        from .room import Room

        writer.write_str_value("emailAddress", self.email_address)
        writer.write_collection_of_object_values("rooms", self.rooms)
    

