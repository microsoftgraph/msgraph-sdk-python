from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .booking_type import BookingType
    from .place import Place
    from .place_feature_enablement import PlaceFeatureEnablement

from .place import Place

@dataclass
class Room(Place, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.room"
    # Specifies the name of the audio device in the room.
    audio_device_name: Optional[str] = None
    # Type of room. Possible values are: unknown, standard, reserved.
    booking_type: Optional[BookingType] = None
    # Specifies the building name or building number that the room is in.
    building: Optional[str] = None
    # Specifies the capacity of the room.
    capacity: Optional[int] = None
    # Specifies the name of the display device in the room.
    display_device_name: Optional[str] = None
    # Email address of the room.
    email_address: Optional[str] = None
    # Specifies a descriptive label for the floor, for example, P.
    floor_label: Optional[str] = None
    # Specifies the floor number that the room is on.
    floor_number: Optional[int] = None
    # Specifies a nickname for the room, for example, 'conf room'.
    nickname: Optional[str] = None
    # An alternative immutable unique identifier of the room. Read-only.
    place_id: Optional[str] = None
    # The teamsEnabledState property
    teams_enabled_state: Optional[PlaceFeatureEnablement] = None
    # Specifies the name of the video device in the room.
    video_device_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Room:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Room
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Room()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .booking_type import BookingType
        from .place import Place
        from .place_feature_enablement import PlaceFeatureEnablement

        from .booking_type import BookingType
        from .place import Place
        from .place_feature_enablement import PlaceFeatureEnablement

        fields: dict[str, Callable[[Any], None]] = {
            "audioDeviceName": lambda n : setattr(self, 'audio_device_name', n.get_str_value()),
            "bookingType": lambda n : setattr(self, 'booking_type', n.get_enum_value(BookingType)),
            "building": lambda n : setattr(self, 'building', n.get_str_value()),
            "capacity": lambda n : setattr(self, 'capacity', n.get_int_value()),
            "displayDeviceName": lambda n : setattr(self, 'display_device_name', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "floorLabel": lambda n : setattr(self, 'floor_label', n.get_str_value()),
            "floorNumber": lambda n : setattr(self, 'floor_number', n.get_int_value()),
            "nickname": lambda n : setattr(self, 'nickname', n.get_str_value()),
            "placeId": lambda n : setattr(self, 'place_id', n.get_str_value()),
            "teamsEnabledState": lambda n : setattr(self, 'teams_enabled_state', n.get_enum_value(PlaceFeatureEnablement)),
            "videoDeviceName": lambda n : setattr(self, 'video_device_name', n.get_str_value()),
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
        writer.write_str_value("audioDeviceName", self.audio_device_name)
        writer.write_enum_value("bookingType", self.booking_type)
        writer.write_str_value("building", self.building)
        writer.write_int_value("capacity", self.capacity)
        writer.write_str_value("displayDeviceName", self.display_device_name)
        writer.write_str_value("emailAddress", self.email_address)
        writer.write_str_value("floorLabel", self.floor_label)
        writer.write_int_value("floorNumber", self.floor_number)
        writer.write_str_value("nickname", self.nickname)
        writer.write_str_value("placeId", self.place_id)
        writer.write_enum_value("teamsEnabledState", self.teams_enabled_state)
        writer.write_str_value("videoDeviceName", self.video_device_name)
    

