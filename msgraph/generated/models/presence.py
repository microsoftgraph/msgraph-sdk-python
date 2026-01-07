from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .out_of_office_settings import OutOfOfficeSettings
    from .presence_status_message import PresenceStatusMessage
    from .user_work_location import UserWorkLocation

from .entity import Entity

@dataclass
class Presence(Entity, Parsable):
    # The supplemental information to a user's availability. Possible values are available, away, beRightBack, busy, doNotDisturb, offline, outOfOffice, presenceUnknown.
    activity: Optional[str] = None
    # The base presence information for a user. Possible values are available, away, beRightBack, busy, doNotDisturb, focusing, inACall, inAMeeting, offline, presenting, presenceUnknown.
    availability: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The out of office settings for a user.
    out_of_office_settings: Optional[OutOfOfficeSettings] = None
    # The lexicographically sortable String stamp that represents the version of a presence object.
    sequence_number: Optional[str] = None
    # The presence status message of a user.
    status_message: Optional[PresenceStatusMessage] = None
    # Represents the user’s aggregated work location state.
    work_location: Optional[UserWorkLocation] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Presence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Presence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Presence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .out_of_office_settings import OutOfOfficeSettings
        from .presence_status_message import PresenceStatusMessage
        from .user_work_location import UserWorkLocation

        from .entity import Entity
        from .out_of_office_settings import OutOfOfficeSettings
        from .presence_status_message import PresenceStatusMessage
        from .user_work_location import UserWorkLocation

        fields: dict[str, Callable[[Any], None]] = {
            "activity": lambda n : setattr(self, 'activity', n.get_str_value()),
            "availability": lambda n : setattr(self, 'availability', n.get_str_value()),
            "outOfOfficeSettings": lambda n : setattr(self, 'out_of_office_settings', n.get_object_value(OutOfOfficeSettings)),
            "sequenceNumber": lambda n : setattr(self, 'sequence_number', n.get_str_value()),
            "statusMessage": lambda n : setattr(self, 'status_message', n.get_object_value(PresenceStatusMessage)),
            "workLocation": lambda n : setattr(self, 'work_location', n.get_object_value(UserWorkLocation)),
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
        writer.write_str_value("activity", self.activity)
        writer.write_str_value("availability", self.availability)
        writer.write_object_value("outOfOfficeSettings", self.out_of_office_settings)
        writer.write_object_value("statusMessage", self.status_message)
        writer.write_object_value("workLocation", self.work_location)
    

