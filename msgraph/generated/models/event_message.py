from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import date_time_time_zone, event, event_message_request, event_message_response, event_type, location, meeting_message_type, message, patterned_recurrence

from . import message

@dataclass
class EventMessage(message.Message):
    odata_type = "#microsoft.graph.eventMessage"
    # The endDateTime property
    end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    # The event associated with the event message. The assumption for attendees or room resources is that the Calendar Attendant is set to automatically update the calendar with an event when meeting request event messages arrive. Navigation property.  Read-only.
    event: Optional[event.Event] = None
    # The isAllDay property
    is_all_day: Optional[bool] = None
    # The isDelegated property
    is_delegated: Optional[bool] = None
    # The isOutOfDate property
    is_out_of_date: Optional[bool] = None
    # The location property
    location: Optional[location.Location] = None
    # The meetingMessageType property
    meeting_message_type: Optional[meeting_message_type.MeetingMessageType] = None
    # The recurrence property
    recurrence: Optional[patterned_recurrence.PatternedRecurrence] = None
    # The startDateTime property
    start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
    # The type property
    type: Optional[event_type.EventType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventMessage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.eventMessageRequest":
                from . import event_message_request

                return event_message_request.EventMessageRequest()
            if mapping_value == "#microsoft.graph.eventMessageResponse":
                from . import event_message_response

                return event_message_response.EventMessageResponse()
        return EventMessage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import date_time_time_zone, event, event_message_request, event_message_response, event_type, location, meeting_message_type, message, patterned_recurrence

        fields: Dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "event": lambda n : setattr(self, 'event', n.get_object_value(event.Event)),
            "isAllDay": lambda n : setattr(self, 'is_all_day', n.get_bool_value()),
            "isDelegated": lambda n : setattr(self, 'is_delegated', n.get_bool_value()),
            "isOutOfDate": lambda n : setattr(self, 'is_out_of_date', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_object_value(location.Location)),
            "meetingMessageType": lambda n : setattr(self, 'meeting_message_type', n.get_enum_value(meeting_message_type.MeetingMessageType)),
            "recurrence": lambda n : setattr(self, 'recurrence', n.get_object_value(patterned_recurrence.PatternedRecurrence)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(event_type.EventType)),
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
    

