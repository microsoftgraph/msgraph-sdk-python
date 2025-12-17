from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .building import Building
    from .check_in_claim import CheckInClaim
    from .desk import Desk
    from .entity import Entity
    from .floor import Floor
    from .outlook_geo_coordinates import OutlookGeoCoordinates
    from .physical_address import PhysicalAddress
    from .room import Room
    from .room_list import RoomList
    from .section import Section
    from .workspace import Workspace

from .entity import Entity

@dataclass
class Place(Entity, Parsable):
    # The physical address of the place, including the street, city, state, country or region, and postal code.
    address: Optional[PhysicalAddress] = None
    # A subresource of a place object that indicates the check-in status of an Outlook calendar event booked at the place.
    check_ins: Optional[list[CheckInClaim]] = None
    # The name that is associated with the place.
    display_name: Optional[str] = None
    # Specifies the place location in latitude, longitude, and (optionally) altitude coordinates.
    geo_coordinates: Optional[OutlookGeoCoordinates] = None
    # Indicates whether the place is wheelchair accessible.
    is_wheel_chair_accessible: Optional[bool] = None
    # User-defined description of the place.
    label: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of a parent place.
    parent_id: Optional[str] = None
    # The phone number of the place.
    phone: Optional[str] = None
    # Custom tags that are associated with the place for categorization or filtering.
    tags: Optional[list[str]] = None
    
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
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.building".casefold():
            from .building import Building

            return Building()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.desk".casefold():
            from .desk import Desk

            return Desk()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.floor".casefold():
            from .floor import Floor

            return Floor()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.room".casefold():
            from .room import Room

            return Room()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roomList".casefold():
            from .room_list import RoomList

            return RoomList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.section".casefold():
            from .section import Section

            return Section()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workspace".casefold():
            from .workspace import Workspace

            return Workspace()
        return Place()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .building import Building
        from .check_in_claim import CheckInClaim
        from .desk import Desk
        from .entity import Entity
        from .floor import Floor
        from .outlook_geo_coordinates import OutlookGeoCoordinates
        from .physical_address import PhysicalAddress
        from .room import Room
        from .room_list import RoomList
        from .section import Section
        from .workspace import Workspace

        from .building import Building
        from .check_in_claim import CheckInClaim
        from .desk import Desk
        from .entity import Entity
        from .floor import Floor
        from .outlook_geo_coordinates import OutlookGeoCoordinates
        from .physical_address import PhysicalAddress
        from .room import Room
        from .room_list import RoomList
        from .section import Section
        from .workspace import Workspace

        fields: dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_object_value(PhysicalAddress)),
            "checkIns": lambda n : setattr(self, 'check_ins', n.get_collection_of_object_values(CheckInClaim)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "geoCoordinates": lambda n : setattr(self, 'geo_coordinates', n.get_object_value(OutlookGeoCoordinates)),
            "isWheelChairAccessible": lambda n : setattr(self, 'is_wheel_chair_accessible', n.get_bool_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "parentId": lambda n : setattr(self, 'parent_id', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("checkIns", self.check_ins)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("geoCoordinates", self.geo_coordinates)
        writer.write_bool_value("isWheelChairAccessible", self.is_wheel_chair_accessible)
        writer.write_str_value("label", self.label)
        writer.write_str_value("parentId", self.parent_id)
        writer.write_str_value("phone", self.phone)
        writer.write_collection_of_primitive_values("tags", self.tags)
    

