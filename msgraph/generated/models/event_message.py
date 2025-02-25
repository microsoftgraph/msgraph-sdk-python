from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .event import Event
    from .event_message_request import EventMessageRequest
    from .event_message_response import EventMessageResponse
    from .event_type import EventType
    from .location import Location
    from .meeting_message_type import MeetingMessageType
    from .message import Message
    from .patterned_recurrence import PatternedRecurrence

from .message import Message

@dataclass
class EventMessage(Message, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.eventMessage"
    # The endDateTime property
    end_date_time: Optional[DateTimeTimeZone] = None
    # The event associated with the event message. The assumption for attendees or room resources is that the Calendar Attendant is set to automatically update the calendar with an event when meeting request event messages arrive. Navigation property. Read-only.
    event: Optional[Event] = None
    # The isAllDay property
    is_all_day: Optional[bool] = None
    # True if this meeting request is accessible to a delegate, false otherwise. The default is false.
    is_delegated: Optional[bool] = None
    # The isOutOfDate property
    is_out_of_date: Optional[bool] = None
    # The location property
    location: Optional[Location] = None
    # The type of event message: none, meetingRequest, meetingCancelled, meetingAccepted, meetingTenativelyAccepted, meetingDeclined.
    meeting_message_type: Optional[MeetingMessageType] = None
    # The recurrence property
    recurrence: Optional[PatternedRecurrence] = None
    # The startDateTime property
    start_date_time: Optional[DateTimeTimeZone] = None
    # The type property
    type: Optional[EventType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EventMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EventMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageRequest".casefold():
            from .event_message_request import EventMessageRequest

            return EventMessageRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageResponse".casefold():
            from .event_message_response import EventMessageResponse

            return EventMessageResponse()
        return EventMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .event import Event
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .event_type import EventType
        from .location import Location
        from .meeting_message_type import MeetingMessageType
        from .message import Message
        from .patterned_recurrence import PatternedRecurrence

        from .date_time_time_zone import DateTimeTimeZone
        from .event import Event
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .event_type import EventType
        from .location import Location
        from .meeting_message_type import MeetingMessageType
        from .message import Message
        from .patterned_recurrence import PatternedRecurrence

        fields: dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(DateTimeTimeZone)),
            "event": lambda n : setattr(self, 'event', n.get_object_value(Event)),
            "isAllDay": lambda n : setattr(self, 'is_all_day', n.get_bool_value()),
            "isDelegated": lambda n : setattr(self, 'is_delegated', n.get_bool_value()),
            "isOutOfDate": lambda n : setattr(self, 'is_out_of_date', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(Location)),
            "meetingMessageType": lambda n : setattr(self, 'meeting_message_type', n.get_enum_value(MeetingMessageType)),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(PatternedRecurrence)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(DateTimeTimeZone)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(EventType)),
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
        writer.write_object_value("endDateTime", self.end_date_time)
        writer.write_object_value("event", self.event)
        writer.write_bool_value("isAllDay", self.is_all_day)
        writer.write_bool_value("isDelegated", self.is_delegated)
        writer.write_bool_value("isOutOfDate", self.is_out_of_date)
        writer.write_object_value("location", self.location)
        writer.write_enum_value("meetingMessageType", self.meeting_message_type)
        writer.write_object_value("recurrence", self.recurrence)
        writer.write_object_value("startDateTime", self.start_date_time)
        writer.write_enum_value("type", self.type)
    

