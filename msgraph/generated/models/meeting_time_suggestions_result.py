from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

meeting_time_suggestion = lazy_import('msgraph.generated.models.meeting_time_suggestion')

class MeetingTimeSuggestionsResult(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new meetingTimeSuggestionsResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A reason for not returning any meeting suggestions. The possible values are: attendeesUnavailable, attendeesUnavailableOrUnknown, locationsUnavailable, organizerUnavailable, or unknown. This property is an empty string if the meetingTimeSuggestions property does include any meeting suggestions.
        self._empty_suggestions_reason: Optional[str] = None
        # An array of meeting suggestions.
        self._meeting_time_suggestions: Optional[List[meeting_time_suggestion.MeetingTimeSuggestion]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingTimeSuggestionsResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingTimeSuggestionsResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingTimeSuggestionsResult()
    
    @property
    def empty_suggestions_reason(self,) -> Optional[str]:
        """
        Gets the emptySuggestionsReason property value. A reason for not returning any meeting suggestions. The possible values are: attendeesUnavailable, attendeesUnavailableOrUnknown, locationsUnavailable, organizerUnavailable, or unknown. This property is an empty string if the meetingTimeSuggestions property does include any meeting suggestions.
        Returns: Optional[str]
        """
        return self._empty_suggestions_reason
    
    @empty_suggestions_reason.setter
    def empty_suggestions_reason(self,value: Optional[str] = None) -> None:
        """
        Sets the emptySuggestionsReason property value. A reason for not returning any meeting suggestions. The possible values are: attendeesUnavailable, attendeesUnavailableOrUnknown, locationsUnavailable, organizerUnavailable, or unknown. This property is an empty string if the meetingTimeSuggestions property does include any meeting suggestions.
        Args:
            value: Value to set for the emptySuggestionsReason property.
        """
        self._empty_suggestions_reason = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "empty_suggestions_reason": lambda n : setattr(self, 'empty_suggestions_reason', n.get_str_value()),
            "meeting_time_suggestions": lambda n : setattr(self, 'meeting_time_suggestions', n.get_collection_of_object_values(meeting_time_suggestion.MeetingTimeSuggestion)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def meeting_time_suggestions(self,) -> Optional[List[meeting_time_suggestion.MeetingTimeSuggestion]]:
        """
        Gets the meetingTimeSuggestions property value. An array of meeting suggestions.
        Returns: Optional[List[meeting_time_suggestion.MeetingTimeSuggestion]]
        """
        return self._meeting_time_suggestions
    
    @meeting_time_suggestions.setter
    def meeting_time_suggestions(self,value: Optional[List[meeting_time_suggestion.MeetingTimeSuggestion]] = None) -> None:
        """
        Sets the meetingTimeSuggestions property value. An array of meeting suggestions.
        Args:
            value: Value to set for the meetingTimeSuggestions property.
        """
        self._meeting_time_suggestions = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("emptySuggestionsReason", self.empty_suggestions_reason)
        writer.write_collection_of_object_values("meetingTimeSuggestions", self.meeting_time_suggestions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

