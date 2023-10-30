from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.attendee_base import AttendeeBase
    from ....models.location_constraint import LocationConstraint
    from ....models.time_constraint import TimeConstraint

@dataclass
class FindMeetingTimesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The attendees property
    attendees: Optional[List[AttendeeBase]] = None
    # The isOrganizerOptional property
    is_organizer_optional: Optional[bool] = None
    # The locationConstraint property
    location_constraint: Optional[LocationConstraint] = None
    # The maxCandidates property
    max_candidates: Optional[int] = None
    # The meetingDuration property
    meeting_duration: Optional[datetime.timedelta] = None
    # The minimumAttendeePercentage property
    minimum_attendee_percentage: Optional[float] = None
    # The returnSuggestionReasons property
    return_suggestion_reasons: Optional[bool] = None
    # The timeConstraint property
    time_constraint: Optional[TimeConstraint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FindMeetingTimesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FindMeetingTimesPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FindMeetingTimesPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models.attendee_base import AttendeeBase
        from ....models.location_constraint import LocationConstraint
        from ....models.time_constraint import TimeConstraint

        from ....models.attendee_base import AttendeeBase
        from ....models.location_constraint import LocationConstraint
        from ....models.time_constraint import TimeConstraint

        fields: Dict[str, Callable[[Any], None]] = {
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(AttendeeBase)),
            "is_organizer_optional": lambda n : setattr(self, 'is_organizer_optional', n.get_bool_value()),
            "location_constraint": lambda n : setattr(self, 'location_constraint', n.get_object_value(LocationConstraint)),
            "max_candidates": lambda n : setattr(self, 'max_candidates', n.get_int_value()),
            "meeting_duration": lambda n : setattr(self, 'meeting_duration', n.get_timedelta_value()),
            "minimum_attendee_percentage": lambda n : setattr(self, 'minimum_attendee_percentage', n.get_float_value()),
            "return_suggestion_reasons": lambda n : setattr(self, 'return_suggestion_reasons', n.get_bool_value()),
            "time_constraint": lambda n : setattr(self, 'time_constraint', n.get_object_value(TimeConstraint)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_bool_value("is_organizer_optional", self.is_organizer_optional)
        writer.write_object_value("location_constraint", self.location_constraint)
        writer.write_int_value("max_candidates", self.max_candidates)
        writer.write_timedelta_value("meeting_duration", self.meeting_duration)
        writer.write_float_value("minimum_attendee_percentage", self.minimum_attendee_percentage)
        writer.write_bool_value("return_suggestion_reasons", self.return_suggestion_reasons)
        writer.write_object_value("time_constraint", self.time_constraint)
        writer.write_additional_data_value(self.additional_data)
    

