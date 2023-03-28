from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import date_time_time_zone, event, event_message_request, event_message_response, event_type, location, meeting_message_type, message, patterned_recurrence

from . import message

class EventMessage(message.Message):
    def __init__(self,) -> None:
        """
        Instantiates a new EventMessage and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.eventMessage"
        # The endDateTime property
        self._end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The event associated with the event message. The assumption for attendees or room resources is that the Calendar Attendant is set to automatically update the calendar with an event when meeting request event messages arrive. Navigation property.  Read-only.
        self._event: Optional[event.Event] = None
        # The isAllDay property
        self._is_all_day: Optional[bool] = None
        # The isDelegated property
        self._is_delegated: Optional[bool] = None
        # The isOutOfDate property
        self._is_out_of_date: Optional[bool] = None
        # The location property
        self._location: Optional[location.Location] = None
        # The meetingMessageType property
        self._meeting_message_type: Optional[meeting_message_type.MeetingMessageType] = None
        # The recurrence property
        self._recurrence: Optional[patterned_recurrence.PatternedRecurrence] = None
        # The startDateTime property
        self._start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # The type property
        self._type: Optional[event_type.EventType] = None
    
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
    
    @property
    def end_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the endDateTime property value. The endDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the endDateTime property value. The endDateTime property
        Args:
            value: Value to set for the end_date_time property.
        """
        self._end_date_time = value
    
    @property
    def event(self,) -> Optional[event.Event]:
        """
        Gets the event property value. The event associated with the event message. The assumption for attendees or room resources is that the Calendar Attendant is set to automatically update the calendar with an event when meeting request event messages arrive. Navigation property.  Read-only.
        Returns: Optional[event.Event]
        """
        return self._event
    
    @event.setter
    def event(self,value: Optional[event.Event] = None) -> None:
        """
        Sets the event property value. The event associated with the event message. The assumption for attendees or room resources is that the Calendar Attendant is set to automatically update the calendar with an event when meeting request event messages arrive. Navigation property.  Read-only.
        Args:
            value: Value to set for the event property.
        """
        self._event = value
    
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
    
    @property
    def is_all_day(self,) -> Optional[bool]:
        """
        Gets the isAllDay property value. The isAllDay property
        Returns: Optional[bool]
        """
        return self._is_all_day
    
    @is_all_day.setter
    def is_all_day(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAllDay property value. The isAllDay property
        Args:
            value: Value to set for the is_all_day property.
        """
        self._is_all_day = value
    
    @property
    def is_delegated(self,) -> Optional[bool]:
        """
        Gets the isDelegated property value. The isDelegated property
        Returns: Optional[bool]
        """
        return self._is_delegated
    
    @is_delegated.setter
    def is_delegated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDelegated property value. The isDelegated property
        Args:
            value: Value to set for the is_delegated property.
        """
        self._is_delegated = value
    
    @property
    def is_out_of_date(self,) -> Optional[bool]:
        """
        Gets the isOutOfDate property value. The isOutOfDate property
        Returns: Optional[bool]
        """
        return self._is_out_of_date
    
    @is_out_of_date.setter
    def is_out_of_date(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOutOfDate property value. The isOutOfDate property
        Args:
            value: Value to set for the is_out_of_date property.
        """
        self._is_out_of_date = value
    
    @property
    def location(self,) -> Optional[location.Location]:
        """
        Gets the location property value. The location property
        Returns: Optional[location.Location]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the location property value. The location property
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def meeting_message_type(self,) -> Optional[meeting_message_type.MeetingMessageType]:
        """
        Gets the meetingMessageType property value. The meetingMessageType property
        Returns: Optional[meeting_message_type.MeetingMessageType]
        """
        return self._meeting_message_type
    
    @meeting_message_type.setter
    def meeting_message_type(self,value: Optional[meeting_message_type.MeetingMessageType] = None) -> None:
        """
        Sets the meetingMessageType property value. The meetingMessageType property
        Args:
            value: Value to set for the meeting_message_type property.
        """
        self._meeting_message_type = value
    
    @property
    def recurrence(self,) -> Optional[patterned_recurrence.PatternedRecurrence]:
        """
        Gets the recurrence property value. The recurrence property
        Returns: Optional[patterned_recurrence.PatternedRecurrence]
        """
        return self._recurrence
    
    @recurrence.setter
    def recurrence(self,value: Optional[patterned_recurrence.PatternedRecurrence] = None) -> None:
        """
        Sets the recurrence property value. The recurrence property
        Args:
            value: Value to set for the recurrence property.
        """
        self._recurrence = value
    
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
    
    @property
    def start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the startDateTime property value. The startDateTime property
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the startDateTime property value. The startDateTime property
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def type(self,) -> Optional[event_type.EventType]:
        """
        Gets the type property value. The type property
        Returns: Optional[event_type.EventType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[event_type.EventType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

