from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, outlook_geo_coordinates, physical_address, room, room_list

from . import entity

@dataclass
class Place(entity.Entity):
    # The street address of the place.
    address: Optional[physical_address.PhysicalAddress] = None
    # The name associated with the place.
    display_name: Optional[str] = None
    # Specifies the place location in latitude, longitude and (optionally) altitude coordinates.
    geo_coordinates: Optional[outlook_geo_coordinates.OutlookGeoCoordinates] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The phone number of the place.
    phone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Place:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Place
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.room":
                from . import room

                return room.Room()
            if mapping_value == "#microsoft.graph.roomList":
                from . import room_list

                return room_list.RoomList()
        return Place()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, outlook_geo_coordinates, physical_address, room, room_list

        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(physical_address.PhysicalAddress)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "geoCoordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(outlook_geo_coordinates.OutlookGeoCoordinates)),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
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
        writer.write_object_value("address", self.address)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
        writer.write_str_value("phone", self.phone)
    

