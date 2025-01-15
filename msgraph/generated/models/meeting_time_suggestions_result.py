from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .meeting_time_suggestion import MeetingTimeSuggestion

@dataclass
class MeetingTimeSuggestionsResult(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A reason for not returning any meeting suggestions. The possible values are: attendeesUnavailable, attendeesUnavailableOrUnknown, locationsUnavailable, organizerUnavailable, or unknown. This property is an empty string if the meetingTimeSuggestions property does include any meeting suggestions.
    empty_suggestions_reason: Optional[str] = None
    # An array of meeting suggestions.
    meeting_time_suggestions: Optional[list[MeetingTimeSuggestion]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MeetingTimeSuggestionsResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MeetingTimeSuggestionsResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MeetingTimeSuggestionsResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .meeting_time_suggestion import MeetingTimeSuggestion

        from .meeting_time_suggestion import MeetingTimeSuggestion

        fields: dict[str, Callable[[Any], None]] = {
            "emptySuggestionsReason": lambda n : setattr(self, 'empty_suggestions_reason', n.get_str_value()),
            "meetingTimeSuggestions": lambda n : setattr(self, 'meeting_time_suggestions', n.get_collection_of_object_values(MeetingTimeSuggestion)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_str_value("emptySuggestionsReason", self.empty_suggestions_reason)
        writer.write_collection_of_object_values("meetingTimeSuggestions", self.meeting_time_suggestions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

