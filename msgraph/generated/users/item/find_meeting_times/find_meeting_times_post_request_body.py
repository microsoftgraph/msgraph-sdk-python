from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attendee_base = lazy_import('msgraph.generated.models.attendee_base')
location_constraint = lazy_import('msgraph.generated.models.location_constraint')
time_constraint = lazy_import('msgraph.generated.models.time_constraint')

class FindMeetingTimesPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the findMeetingTimes method.
    """
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
    def attendees(self,) -> Optional[List[attendee_base.AttendeeBase]]:
        """
        Gets the attendees property value. The attendees property
        Returns: Optional[List[attendee_base.AttendeeBase]]
        """
        return self._attendees
    
    @attendees.setter
    def attendees(self,value: Optional[List[attendee_base.AttendeeBase]] = None) -> None:
        """
        Sets the attendees property value. The attendees property
        Args:
            value: Value to set for the attendees property.
        """
        self._attendees = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new findMeetingTimesPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The attendees property
        self._attendees: Optional[List[attendee_base.AttendeeBase]] = None
        # The isOrganizerOptional property
        self._is_organizer_optional: Optional[bool] = None
        # The locationConstraint property
        self._location_constraint: Optional[location_constraint.LocationConstraint] = None
        # The maxCandidates property
        self._max_candidates: Optional[int] = None
        # The meetingDuration property
        self._meeting_duration: Optional[Timedelta] = None
        # The minimumAttendeePercentage property
        self._minimum_attendee_percentage: Optional[float] = None
        # The returnSuggestionReasons property
        self._return_suggestion_reasons: Optional[bool] = None
        # The timeConstraint property
        self._time_constraint: Optional[time_constraint.TimeConstraint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FindMeetingTimesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FindMeetingTimesPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FindMeetingTimesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(attendee_base.AttendeeBase)),
            "is_organizer_optional": lambda n : setattr(self, 'is_organizer_optional', n.get_bool_value()),
            "location_constraint": lambda n : setattr(self, 'location_constraint', n.get_object_value(location_constraint.LocationConstraint)),
            "max_candidates": lambda n : setattr(self, 'max_candidates', n.get_int_value()),
            "meeting_duration": lambda n : setattr(self, 'meeting_duration', n.get_object_value(Timedelta)),
            "minimum_attendee_percentage": lambda n : setattr(self, 'minimum_attendee_percentage', n.get_float_value()),
            "return_suggestion_reasons": lambda n : setattr(self, 'return_suggestion_reasons', n.get_bool_value()),
            "time_constraint": lambda n : setattr(self, 'time_constraint', n.get_object_value(time_constraint.TimeConstraint)),
        }
        return fields
    
    @property
    def is_organizer_optional(self,) -> Optional[bool]:
        """
        Gets the isOrganizerOptional property value. The isOrganizerOptional property
        Returns: Optional[bool]
        """
        return self._is_organizer_optional
    
    @is_organizer_optional.setter
    def is_organizer_optional(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOrganizerOptional property value. The isOrganizerOptional property
        Args:
            value: Value to set for the isOrganizerOptional property.
        """
        self._is_organizer_optional = value
    
    @property
    def location_constraint(self,) -> Optional[location_constraint.LocationConstraint]:
        """
        Gets the locationConstraint property value. The locationConstraint property
        Returns: Optional[location_constraint.LocationConstraint]
        """
        return self._location_constraint
    
    @location_constraint.setter
    def location_constraint(self,value: Optional[location_constraint.LocationConstraint] = None) -> None:
        """
        Sets the locationConstraint property value. The locationConstraint property
        Args:
            value: Value to set for the locationConstraint property.
        """
        self._location_constraint = value
    
    @property
    def max_candidates(self,) -> Optional[int]:
        """
        Gets the maxCandidates property value. The maxCandidates property
        Returns: Optional[int]
        """
        return self._max_candidates
    
    @max_candidates.setter
    def max_candidates(self,value: Optional[int] = None) -> None:
        """
        Sets the maxCandidates property value. The maxCandidates property
        Args:
            value: Value to set for the maxCandidates property.
        """
        self._max_candidates = value
    
    @property
    def meeting_duration(self,) -> Optional[Timedelta]:
        """
        Gets the meetingDuration property value. The meetingDuration property
        Returns: Optional[Timedelta]
        """
        return self._meeting_duration
    
    @meeting_duration.setter
    def meeting_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the meetingDuration property value. The meetingDuration property
        Args:
            value: Value to set for the meetingDuration property.
        """
        self._meeting_duration = value
    
    @property
    def minimum_attendee_percentage(self,) -> Optional[float]:
        """
        Gets the minimumAttendeePercentage property value. The minimumAttendeePercentage property
        Returns: Optional[float]
        """
        return self._minimum_attendee_percentage
    
    @minimum_attendee_percentage.setter
    def minimum_attendee_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the minimumAttendeePercentage property value. The minimumAttendeePercentage property
        Args:
            value: Value to set for the minimumAttendeePercentage property.
        """
        self._minimum_attendee_percentage = value
    
    @property
    def return_suggestion_reasons(self,) -> Optional[bool]:
        """
        Gets the returnSuggestionReasons property value. The returnSuggestionReasons property
        Returns: Optional[bool]
        """
        return self._return_suggestion_reasons
    
    @return_suggestion_reasons.setter
    def return_suggestion_reasons(self,value: Optional[bool] = None) -> None:
        """
        Sets the returnSuggestionReasons property value. The returnSuggestionReasons property
        Args:
            value: Value to set for the returnSuggestionReasons property.
        """
        self._return_suggestion_reasons = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_bool_value("isOrganizerOptional", self.is_organizer_optional)
        writer.write_object_value("locationConstraint", self.location_constraint)
        writer.write_int_value("maxCandidates", self.max_candidates)
        writer.write_object_value("meetingDuration", self.meeting_duration)
        writer.write_float_value("minimumAttendeePercentage", self.minimum_attendee_percentage)
        writer.write_bool_value("returnSuggestionReasons", self.return_suggestion_reasons)
        writer.write_object_value("timeConstraint", self.time_constraint)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def time_constraint(self,) -> Optional[time_constraint.TimeConstraint]:
        """
        Gets the timeConstraint property value. The timeConstraint property
        Returns: Optional[time_constraint.TimeConstraint]
        """
        return self._time_constraint
    
    @time_constraint.setter
    def time_constraint(self,value: Optional[time_constraint.TimeConstraint] = None) -> None:
        """
        Sets the timeConstraint property value. The timeConstraint property
        Args:
            value: Value to set for the timeConstraint property.
        """
        self._time_constraint = value
    

