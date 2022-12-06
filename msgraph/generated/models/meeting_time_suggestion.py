from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attendee_availability = lazy_import('msgraph.generated.models.attendee_availability')
free_busy_status = lazy_import('msgraph.generated.models.free_busy_status')
location = lazy_import('msgraph.generated.models.location')
time_slot = lazy_import('msgraph.generated.models.time_slot')

class MeetingTimeSuggestion(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def attendee_availability(self,) -> Optional[List[attendee_availability.AttendeeAvailability]]:
        """
        Gets the attendeeAvailability property value. An array that shows the availability status of each attendee for this meeting suggestion.
        Returns: Optional[List[attendee_availability.AttendeeAvailability]]
        """
        return self._attendee_availability
    
    @attendee_availability.setter
    def attendee_availability(self,value: Optional[List[attendee_availability.AttendeeAvailability]] = None) -> None:
        """
        Sets the attendeeAvailability property value. An array that shows the availability status of each attendee for this meeting suggestion.
        Args:
            value: Value to set for the attendeeAvailability property.
        """
        self._attendee_availability = value
    
    @property
    def confidence(self,) -> Optional[float]:
        """
        Gets the confidence property value. A percentage that represents the likelhood of all the attendees attending.
        Returns: Optional[float]
        """
        return self._confidence
    
    @confidence.setter
    def confidence(self,value: Optional[float] = None) -> None:
        """
        Sets the confidence property value. A percentage that represents the likelhood of all the attendees attending.
        Args:
            value: Value to set for the confidence property.
        """
        self._confidence = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new meetingTimeSuggestion and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # An array that shows the availability status of each attendee for this meeting suggestion.
        self._attendee_availability: Optional[List[attendee_availability.AttendeeAvailability]] = None
        # A percentage that represents the likelhood of all the attendees attending.
        self._confidence: Optional[float] = None
        # An array that specifies the name and geographic location of each meeting location for this meeting suggestion.
        self._locations: Optional[List[location.Location]] = None
        # A time period suggested for the meeting.
        self._meeting_time_slot: Optional[time_slot.TimeSlot] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Order of meeting time suggestions sorted by their computed confidence value from high to low, then by chronology if there are suggestions with the same confidence.
        self._order: Optional[int] = None
        # Availability of the meeting organizer for this meeting suggestion. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        self._organizer_availability: Optional[free_busy_status.FreeBusyStatus] = None
        # Reason for suggesting the meeting time.
        self._suggestion_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingTimeSuggestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingTimeSuggestion
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingTimeSuggestion()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attendee_availability": lambda n : setattr(self, 'attendee_availability', n.get_collection_of_object_values(attendee_availability.AttendeeAvailability)),
            "confidence": lambda n : setattr(self, 'confidence', n.get_float_value()),
            "locations": lambda n : setattr(self, 'locations', n.get_collection_of_object_values(location.Location)),
            "meeting_time_slot": lambda n : setattr(self, 'meeting_time_slot', n.get_object_value(time_slot.TimeSlot)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "organizer_availability": lambda n : setattr(self, 'organizer_availability', n.get_enum_value(free_busy_status.FreeBusyStatus)),
            "suggestion_reason": lambda n : setattr(self, 'suggestion_reason', n.get_str_value()),
        }
        return fields
    
    @property
    def locations(self,) -> Optional[List[location.Location]]:
        """
        Gets the locations property value. An array that specifies the name and geographic location of each meeting location for this meeting suggestion.
        Returns: Optional[List[location.Location]]
        """
        return self._locations
    
    @locations.setter
    def locations(self,value: Optional[List[location.Location]] = None) -> None:
        """
        Sets the locations property value. An array that specifies the name and geographic location of each meeting location for this meeting suggestion.
        Args:
            value: Value to set for the locations property.
        """
        self._locations = value
    
    @property
    def meeting_time_slot(self,) -> Optional[time_slot.TimeSlot]:
        """
        Gets the meetingTimeSlot property value. A time period suggested for the meeting.
        Returns: Optional[time_slot.TimeSlot]
        """
        return self._meeting_time_slot
    
    @meeting_time_slot.setter
    def meeting_time_slot(self,value: Optional[time_slot.TimeSlot] = None) -> None:
        """
        Sets the meetingTimeSlot property value. A time period suggested for the meeting.
        Args:
            value: Value to set for the meetingTimeSlot property.
        """
        self._meeting_time_slot = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def order(self,) -> Optional[int]:
        """
        Gets the order property value. Order of meeting time suggestions sorted by their computed confidence value from high to low, then by chronology if there are suggestions with the same confidence.
        Returns: Optional[int]
        """
        return self._order
    
    @order.setter
    def order(self,value: Optional[int] = None) -> None:
        """
        Sets the order property value. Order of meeting time suggestions sorted by their computed confidence value from high to low, then by chronology if there are suggestions with the same confidence.
        Args:
            value: Value to set for the order property.
        """
        self._order = value
    
    @property
    def organizer_availability(self,) -> Optional[free_busy_status.FreeBusyStatus]:
        """
        Gets the organizerAvailability property value. Availability of the meeting organizer for this meeting suggestion. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        Returns: Optional[free_busy_status.FreeBusyStatus]
        """
        return self._organizer_availability
    
    @organizer_availability.setter
    def organizer_availability(self,value: Optional[free_busy_status.FreeBusyStatus] = None) -> None:
        """
        Sets the organizerAvailability property value. Availability of the meeting organizer for this meeting suggestion. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
        Args:
            value: Value to set for the organizerAvailability property.
        """
        self._organizer_availability = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("attendeeAvailability", self.attendee_availability)
        writer.write_float_value("confidence", self.confidence)
        writer.write_collection_of_object_values("locations", self.locations)
        writer.write_object_value("meetingTimeSlot", self.meeting_time_slot)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("order", self.order)
        writer.write_enum_value("organizerAvailability", self.organizer_availability)
        writer.write_str_value("suggestionReason", self.suggestion_reason)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def suggestion_reason(self,) -> Optional[str]:
        """
        Gets the suggestionReason property value. Reason for suggesting the meeting time.
        Returns: Optional[str]
        """
        return self._suggestion_reason
    
    @suggestion_reason.setter
    def suggestion_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the suggestionReason property value. Reason for suggesting the meeting time.
        Args:
            value: Value to set for the suggestionReason property.
        """
        self._suggestion_reason = value
    

