from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, media_stream, online_meeting_restricted, participant_info, recording_info

from . import entity

@dataclass
class Participant(entity.Entity):
    # The info property
    info: Optional[participant_info.ParticipantInfo] = None
    # true if the participant is in lobby.
    is_in_lobby: Optional[bool] = None
    # true if the participant is muted (client or server muted).
    is_muted: Optional[bool] = None
    # The list of media streams.
    media_streams: Optional[List[media_stream.MediaStream]] = None
    # A blob of data provided by the participant in the roster.
    metadata: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about whether the participant has recording capability.
    recording_info: Optional[recording_info.RecordingInfo] = None
    # Indicates the reason or reasons media content from this participant is restricted.
    restricted_experience: Optional[online_meeting_restricted.OnlineMeetingRestricted] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Participant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Participant
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Participant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, media_stream, online_meeting_restricted, participant_info, recording_info

        fields: Dict[str, Callable[[Any], None]] = {
            "info": lambda n : setattr(self, 'info', n.get_object_value(participant_info.ParticipantInfo)),
            "isInLobby": lambda n : setattr(self, 'is_in_lobby', n.get_bool_value()),
            "isMuted": lambda n : setattr(self, 'is_muted', n.get_bool_value()),
            "mediaStreams": lambda n : setattr(self, 'media_streams', n.get_collection_of_object_values(media_stream.MediaStream)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_str_value()),
            "recordingInfo": lambda n : setattr(self, 'recording_info', n.get_object_value(recording_info.RecordingInfo)),
            "restrictedExperience": lambda n : setattr(self, 'restricted_experience', n.get_object_value(online_meeting_restricted.OnlineMeetingRestricted)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("info", self.info)
        writer.write_bool_value("isInLobby", self.is_in_lobby)
        writer.write_bool_value("isMuted", self.is_muted)
        writer.write_collection_of_object_values("mediaStreams", self.media_streams)
        writer.write_str_value("metadata", self.metadata)
        writer.write_object_value("recordingInfo", self.recording_info)
        writer.write_object_value("restrictedExperience", self.restricted_experience)
    

