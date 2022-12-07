from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

date_time_time_zone = lazy_import('msgraph.generated.models.date_time_time_zone')
event_message = lazy_import('msgraph.generated.models.event_message')
location = lazy_import('msgraph.generated.models.location')
meeting_request_type = lazy_import('msgraph.generated.models.meeting_request_type')

class EventMessageRequest(event_message.EventMessage):
    @property
    def allow_new_time_proposals(self,) -> Optional[bool]:
        """
        Gets the allowNewTimeProposals property value. True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.
        Returns: Optional[bool]
        """
        return self._allow_new_time_proposals
    
    @allow_new_time_proposals.setter
    def allow_new_time_proposals(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowNewTimeProposals property value. True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.
        Args:
            value: Value to set for the allowNewTimeProposals property.
        """
        self._allow_new_time_proposals = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EventMessageRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.eventMessageRequest"
        # True if the meeting organizer allows invitees to propose a new time when responding, false otherwise. Optional. Default is true.
        self._allow_new_time_proposals: Optional[bool] = None
        # The meetingRequestType property
        self._meeting_request_type: Optional[meeting_request_type.MeetingRequestType] = None
        # If the meeting update changes the meeting end time, this property specifies the previous meeting end time.
        self._previous_end_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # If the meeting update changes the meeting location, this property specifies the previous meeting location.
        self._previous_location: Optional[location.Location] = None
        # If the meeting update changes the meeting start time, this property specifies the previous meeting start time.
        self._previous_start_date_time: Optional[date_time_time_zone.DateTimeTimeZone] = None
        # Set to true if the sender would like the invitee to send a response to the requested meeting.
        self._response_requested: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventMessageRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventMessageRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EventMessageRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_new_time_proposals": lambda n : setattr(self, 'allow_new_time_proposals', n.get_bool_value()),
            "meeting_request_type": lambda n : setattr(self, 'meeting_request_type', n.get_enum_value(meeting_request_type.MeetingRequestType)),
            "previous_end_date_time": lambda n : setattr(self, 'previous_end_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "previous_location": lambda n : setattr(self, 'previous_location', n.get_object_value(location.Location)),
            "previous_start_date_time": lambda n : setattr(self, 'previous_start_date_time', n.get_object_value(date_time_time_zone.DateTimeTimeZone)),
            "response_requested": lambda n : setattr(self, 'response_requested', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def meeting_request_type(self,) -> Optional[meeting_request_type.MeetingRequestType]:
        """
        Gets the meetingRequestType property value. The meetingRequestType property
        Returns: Optional[meeting_request_type.MeetingRequestType]
        """
        return self._meeting_request_type
    
    @meeting_request_type.setter
    def meeting_request_type(self,value: Optional[meeting_request_type.MeetingRequestType] = None) -> None:
        """
        Sets the meetingRequestType property value. The meetingRequestType property
        Args:
            value: Value to set for the meetingRequestType property.
        """
        self._meeting_request_type = value
    
    @property
    def previous_end_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the previousEndDateTime property value. If the meeting update changes the meeting end time, this property specifies the previous meeting end time.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._previous_end_date_time
    
    @previous_end_date_time.setter
    def previous_end_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the previousEndDateTime property value. If the meeting update changes the meeting end time, this property specifies the previous meeting end time.
        Args:
            value: Value to set for the previousEndDateTime property.
        """
        self._previous_end_date_time = value
    
    @property
    def previous_location(self,) -> Optional[location.Location]:
        """
        Gets the previousLocation property value. If the meeting update changes the meeting location, this property specifies the previous meeting location.
        Returns: Optional[location.Location]
        """
        return self._previous_location
    
    @previous_location.setter
    def previous_location(self,value: Optional[location.Location] = None) -> None:
        """
        Sets the previousLocation property value. If the meeting update changes the meeting location, this property specifies the previous meeting location.
        Args:
            value: Value to set for the previousLocation property.
        """
        self._previous_location = value
    
    @property
    def previous_start_date_time(self,) -> Optional[date_time_time_zone.DateTimeTimeZone]:
        """
        Gets the previousStartDateTime property value. If the meeting update changes the meeting start time, this property specifies the previous meeting start time.
        Returns: Optional[date_time_time_zone.DateTimeTimeZone]
        """
        return self._previous_start_date_time
    
    @previous_start_date_time.setter
    def previous_start_date_time(self,value: Optional[date_time_time_zone.DateTimeTimeZone] = None) -> None:
        """
        Sets the previousStartDateTime property value. If the meeting update changes the meeting start time, this property specifies the previous meeting start time.
        Args:
            value: Value to set for the previousStartDateTime property.
        """
        self._previous_start_date_time = value
    
    @property
    def response_requested(self,) -> Optional[bool]:
        """
        Gets the responseRequested property value. Set to true if the sender would like the invitee to send a response to the requested meeting.
        Returns: Optional[bool]
        """
        return self._response_requested
    
    @response_requested.setter
    def response_requested(self,value: Optional[bool] = None) -> None:
        """
        Sets the responseRequested property value. Set to true if the sender would like the invitee to send a response to the requested meeting.
        Args:
            value: Value to set for the responseRequested property.
        """
        self._response_requested = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("allowNewTimeProposals", self.allow_new_time_proposals)
        writer.write_enum_value("meetingRequestType", self.meeting_request_type)
        writer.write_object_value("previousEndDateTime", self.previous_end_date_time)
        writer.write_object_value("previousLocation", self.previous_location)
        writer.write_object_value("previousStartDateTime", self.previous_start_date_time)
        writer.write_bool_value("responseRequested", self.response_requested)
    

