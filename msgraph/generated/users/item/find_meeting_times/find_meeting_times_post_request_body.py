from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.attendee_base import AttendeeBase
    from ....models.location_constraint import LocationConstraint
    from ....models.time_constraint import TimeConstraint

@dataclass
class FindMeetingTimesPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The attendees property
    attendees: Optional[list[AttendeeBase]] = None
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
    def create_from_discriminator_value(parse_node: ParseNode) -> FindMeetingTimesPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FindMeetingTimesPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FindMeetingTimesPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....models.attendee_base import AttendeeBase
        from ....models.location_constraint import LocationConstraint
        from ....models.time_constraint import TimeConstraint

        from ....models.attendee_base import AttendeeBase
        from ....models.location_constraint import LocationConstraint
        from ....models.time_constraint import TimeConstraint

        fields: dict[str, Callable[[Any], None]] = {
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(AttendeeBase)),
            "isOrganizerOptional": lambda n : setattr(self, 'is_organizer_optional', n.get_bool_value()),
            "locationConstraint": lambda n : setattr(self, 'location_constraint', n.get_object_value(LocationConstraint)),
            "maxCandidates": lambda n : setattr(self, 'max_candidates', n.get_int_value()),
            "meetingDuration": lambda n : setattr(self, 'meeting_duration', n.get_timedelta_value()),
            "minimumAttendeePercentage": lambda n : setattr(self, 'minimum_attendee_percentage', n.get_float_value()),
            "returnSuggestionReasons": lambda n : setattr(self, 'return_suggestion_reasons', n.get_bool_value()),
            "timeConstraint": lambda n : setattr(self, 'time_constraint', n.get_object_value(TimeConstraint)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_bool_value("isOrganizerOptional", self.is_organizer_optional)
        writer.write_object_value("locationConstraint", self.location_constraint)
        writer.write_int_value("maxCandidates", self.max_candidates)
        writer.write_timedelta_value("meetingDuration", self.meeting_duration)
        writer.write_float_value("minimumAttendeePercentage", self.minimum_attendee_percentage)
        writer.write_bool_value("returnSuggestionReasons", self.return_suggestion_reasons)
        writer.write_object_value("timeConstraint", self.time_constraint)
        writer.write_additional_data_value(self.additional_data)
    

