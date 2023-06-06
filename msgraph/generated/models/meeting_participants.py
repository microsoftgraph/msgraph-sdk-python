from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import meeting_participant_info

@dataclass
class MeetingParticipants(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The attendees property
    attendees: Optional[List[meeting_participant_info.MeetingParticipantInfo]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organizer property
    organizer: Optional[meeting_participant_info.MeetingParticipantInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MeetingParticipants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MeetingParticipants
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MeetingParticipants()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import meeting_participant_info

        fields: Dict[str, Callable[[Any], None]] = {
            "attendees": lambda n : setattr(self, 'attendees', n.get_collection_of_object_values(meeting_participant_info.MeetingParticipantInfo)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizer": lambda n : setattr(self, 'organizer', n.get_object_value(meeting_participant_info.MeetingParticipantInfo)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("attendees", self.attendees)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("organizer", self.organizer)
        writer.write_additional_data_value(self.additional_data)
    

