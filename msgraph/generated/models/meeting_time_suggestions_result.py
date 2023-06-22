from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import meeting_time_suggestion

@dataclass
class MeetingTimeSuggestionsResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A reason for not returning any meeting suggestions. The possible values are: attendeesUnavailable, attendeesUnavailableOrUnknown, locationsUnavailable, organizerUnavailable, or unknown. This property is an empty string if the meetingTimeSuggestions property does include any meeting suggestions.
    empty_suggestions_reason: Optional[str] = None
    # An array of meeting suggestions.
    meeting_time_suggestions: Optional[List[meeting_time_suggestion.MeetingTimeSuggestion]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingTimeSuggestionsResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingTimeSuggestionsResult
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return MeetingTimeSuggestionsResult()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import meeting_time_suggestion

        from . import meeting_time_suggestion

        fields: Dict[str, Callable[[Any], None]] = {
            "emptySuggestionsReason": lambda n : setattr(self, 'empty_suggestions_reason', n.get_str_value()),
            "meetingTimeSuggestions": lambda n : setattr(self, 'meeting_time_suggestions', n.get_collection_of_object_values(meeting_time_suggestion.MeetingTimeSuggestion)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("emptySuggestionsReason", self.empty_suggestions_reason)
        writer.write_collection_of_object_values("meetingTimeSuggestions", self.meeting_time_suggestions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

