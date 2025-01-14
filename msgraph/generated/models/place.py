from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .outlook_geo_coordinates import OutlookGeoCoordinates
    from .physical_address import PhysicalAddress
    from .room import Room
    from .room_list import RoomList

from .entity import Entity

@dataclass
class Place(Entity, Parsable):
    # The street address of the place.
    address: Optional[PhysicalAddress] = None
    # The name associated with the place.
    display_name: Optional[str] = None
    # Specifies the place location in latitude, longitude, and (optionally) altitude coordinates.
    geo_coordinates: Optional[OutlookGeoCoordinates] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phone number of the place.
    phone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Place:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Place
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.room".casefold():
            from .room import Room

            return Room()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roomList".casefold():
            from .room_list import RoomList

            return RoomList()
        return Place()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .outlook_geo_coordinates import OutlookGeoCoordinates
        from .physical_address import PhysicalAddress
        from .room import Room
        from .room_list import RoomList

        from .entity import Entity
        from .outlook_geo_coordinates import OutlookGeoCoordinates
        from .physical_address import PhysicalAddress
        from .room import Room
        from .room_list import RoomList

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalAddress)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "geoCoordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(OutlookGeoCoordinates)),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
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
        writer.write_object_value("address", self.address)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
        writer.write_str_value("phone", self.phone)
    

