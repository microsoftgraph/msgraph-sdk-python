from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
media_stream = lazy_import('msgraph.generated.models.media_stream')
participant_info = lazy_import('msgraph.generated.models.participant_info')
recording_info = lazy_import('msgraph.generated.models.recording_info')

class Participant(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new participant and sets the default values.
        """
        super().__init__()
        # The info property
        self._info: Optional[participant_info.ParticipantInfo] = None
        # true if the participant is in lobby.
        self._is_in_lobby: Optional[bool] = None
        # true if the participant is muted (client or server muted).
        self._is_muted: Optional[bool] = None
        # The list of media streams.
        self._media_streams: Optional[List[media_stream.MediaStream]] = None
        # A blob of data provided by the participant in the roster.
        self._metadata: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Information about whether the participant has recording capability.
        self._recording_info: Optional[recording_info.RecordingInfo] = None
    
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
        fields = {
            "info": lambda n : setattr(self, 'info', n.get_object_value(participant_info.ParticipantInfo)),
            "is_in_lobby": lambda n : setattr(self, 'is_in_lobby', n.get_bool_value()),
            "is_muted": lambda n : setattr(self, 'is_muted', n.get_bool_value()),
            "media_streams": lambda n : setattr(self, 'media_streams', n.get_collection_of_object_values(media_stream.MediaStream)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_str_value()),
            "recording_info": lambda n : setattr(self, 'recording_info', n.get_object_value(recording_info.RecordingInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def info(self,) -> Optional[participant_info.ParticipantInfo]:
        """
        Gets the info property value. The info property
        Returns: Optional[participant_info.ParticipantInfo]
        """
        return self._info
    
    @info.setter
    def info(self,value: Optional[participant_info.ParticipantInfo] = None) -> None:
        """
        Sets the info property value. The info property
        Args:
            value: Value to set for the info property.
        """
        self._info = value
    
    @property
    def is_in_lobby(self,) -> Optional[bool]:
        """
        Gets the isInLobby property value. true if the participant is in lobby.
        Returns: Optional[bool]
        """
        return self._is_in_lobby
    
    @is_in_lobby.setter
    def is_in_lobby(self,value: Optional[bool] = None) -> None:
        """
        Sets the isInLobby property value. true if the participant is in lobby.
        Args:
            value: Value to set for the isInLobby property.
        """
        self._is_in_lobby = value
    
    @property
    def is_muted(self,) -> Optional[bool]:
        """
        Gets the isMuted property value. true if the participant is muted (client or server muted).
        Returns: Optional[bool]
        """
        return self._is_muted
    
    @is_muted.setter
    def is_muted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMuted property value. true if the participant is muted (client or server muted).
        Args:
            value: Value to set for the isMuted property.
        """
        self._is_muted = value
    
    @property
    def media_streams(self,) -> Optional[List[media_stream.MediaStream]]:
        """
        Gets the mediaStreams property value. The list of media streams.
        Returns: Optional[List[media_stream.MediaStream]]
        """
        return self._media_streams
    
    @media_streams.setter
    def media_streams(self,value: Optional[List[media_stream.MediaStream]] = None) -> None:
        """
        Sets the mediaStreams property value. The list of media streams.
        Args:
            value: Value to set for the mediaStreams property.
        """
        self._media_streams = value
    
    @property
    def metadata(self,) -> Optional[str]:
        """
        Gets the metadata property value. A blob of data provided by the participant in the roster.
        Returns: Optional[str]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[str] = None) -> None:
        """
        Sets the metadata property value. A blob of data provided by the participant in the roster.
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
    @property
    def recording_info(self,) -> Optional[recording_info.RecordingInfo]:
        """
        Gets the recordingInfo property value. Information about whether the participant has recording capability.
        Returns: Optional[recording_info.RecordingInfo]
        """
        return self._recording_info
    
    @recording_info.setter
    def recording_info(self,value: Optional[recording_info.RecordingInfo] = None) -> None:
        """
        Sets the recordingInfo property value. Information about whether the participant has recording capability.
        Args:
            value: Value to set for the recordingInfo property.
        """
        self._recording_info = value
    
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
    

