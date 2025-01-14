from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attendee_availability import AttendeeAvailability
    from .free_busy_status import FreeBusyStatus
    from .location import Location
    from .time_slot import TimeSlot

@dataclass
class MeetingTimeSuggestion(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # An array that shows the availability status of each attendee for this meeting suggestion.
    attendee_availability: Optional[list[AttendeeAvailability]] = None
    # A percentage that represents the likelhood of all the attendees attending.
    confidence: Optional[float] = None
    # An array that specifies the name and geographic location of each meeting location for this meeting suggestion.
    locations: Optional[list[Location]] = None
    # A time period suggested for the meeting.
    meeting_time_slot: Optional[TimeSlot] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Order of meeting time suggestions sorted by their computed confidence value from high to low, then by chronology if there are suggestions with the same confidence.
    order: Optional[int] = None
    # Availability of the meeting organizer for this meeting suggestion. The possible values are: free, tentative, busy, oof, workingElsewhere, unknown.
    organizer_availability: Optional[FreeBusyStatus] = None
    # Reason for suggesting the meeting time.
    suggestion_reason: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingTimeSuggestion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingTimeSuggestion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingTimeSuggestion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attendee_availability import AttendeeAvailability
        from .free_busy_status import FreeBusyStatus
        from .location import Location
        from .time_slot import TimeSlot

        from .attendee_availability import AttendeeAvailability
        from .free_busy_status import FreeBusyStatus
        from .location import Location
        from .time_slot import TimeSlot

        fields: dict[str, Callable[[Any], None]] = {
            "attendeeAvailability": lambda n : setattr(self, 'attendee_availability', n.get_collection_of_object_values(AttendeeAvailability)),
            "confidence": lambda n : setattr(self, 'confidence', n.get_float_value()),
            "locations": lambda n : setattr(self, 'locations', n.get_collection_of_object_values(Location)),
            "meetingTimeSlot": lambda n : setattr(self, 'meeting_time_slot', n.get_object_value(TimeSlot)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "order": lambda n : setattr(self, 'order', n.get_int_value()),
            "organizerAvailability": lambda n : setattr(self, 'organizer_availability', n.get_enum_value(FreeBusyStatus)),
            "suggestionReason": lambda n : setattr(self, 'suggestion_reason', n.get_str_value()),
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
        writer.write_collection_of_object_values("attendeeAvailability", self.attendee_availability)
        writer.write_float_value("confidence", self.confidence)
        writer.write_collection_of_object_values("locations", self.locations)
        writer.write_object_value("meetingTimeSlot", self.meeting_time_slot)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("order", self.order)
        writer.write_enum_value("organizerAvailability", self.organizer_availability)
        writer.write_str_value("suggestionReason", self.suggestion_reason)
        writer.write_additional_data_value(self.additional_data)
    

