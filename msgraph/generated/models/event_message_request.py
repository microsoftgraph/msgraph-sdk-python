from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .event_message import EventMessage
    from .location import Location
    from .meeting_request_type import MeetingRequestType

from .event_message import EventMessage

@dataclass
class EventMessageRequest(EventMessage, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.eventMessageRequest"
    # True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.
    allow_new_time_proposals: Optional[bool] = None
    # The meetingRequestType property
    meeting_request_type: Optional[MeetingRequestType] = None
    # If the meeting update changes the meeting end time, this property specifies the previous meeting end time.
    previous_end_date_time: Optional[DateTimeTimeZone] = None
    # If the meeting update changes the meeting location, this property specifies the previous meeting location.
    previous_location: Optional[Location] = None
    # If the meeting update changes the meeting start time, this property specifies the previous meeting start time.
    previous_start_date_time: Optional[DateTimeTimeZone] = None
    # Set to true if the sender would like the invitee to send a response to the requested meeting.
    response_requested: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EventMessageRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EventMessageRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EventMessageRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .event_message import EventMessage
        from .location import Location
        from .meeting_request_type import MeetingRequestType

        from .date_time_time_zone import DateTimeTimeZone
        from .event_message import EventMessage
        from .location import Location
        from .meeting_request_type import MeetingRequestType

        fields: dict[str, Callable[[Any], None]] = {
            "allowNewTimeProposals": lambda n : setattr(self, 'allow_new_time_proposals', n.get_bool_value()),
            "meetingRequestType": lambda n : setattr(self, 'meeting_request_type', n.get_enum_value(MeetingRequestType)),
            "previousEndDateTime": lambda n : setattr(self, 'previous_end_date_time', n.get_object_value(DateTimeTimeZone)),
            "previousLocation": lambda n : setattr(self, 'previous_location', n.get_object_value(Location)),
            "previousStartDateTime": lambda n : setattr(self, 'previous_start_date_time', n.get_object_value(DateTimeTimeZone)),
            "responseRequested": lambda n : setattr(self, 'response_requested', n.get_bool_value()),
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
        writer.write_bool_value("allowNewTimeProposals", self.allow_new_time_proposals)
        writer.write_enum_value("meetingRequestType", self.meeting_request_type)
        writer.write_object_value("previousEndDateTime", self.previous_end_date_time)
        writer.write_object_value("previousLocation", self.previous_location)
        writer.write_object_value("previousStartDateTime", self.previous_start_date_time)
        writer.write_bool_value("responseRequested", self.response_requested)
    

