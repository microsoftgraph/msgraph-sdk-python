from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audio_routing_group import AudioRoutingGroup
    from .call_direction import CallDirection
    from .call_media_state import CallMediaState
    from .call_options import CallOptions
    from .call_route import CallRoute
    from .call_state import CallState
    from .call_transcription_info import CallTranscriptionInfo
    from .chat_info import ChatInfo
    from .comms_operation import CommsOperation
    from .content_sharing_session import ContentSharingSession
    from .entity import Entity
    from .incoming_context import IncomingContext
    from .invitation_participant_info import InvitationParticipantInfo
    from .media_config import MediaConfig
    from .meeting_info import MeetingInfo
    from .modality import Modality
    from .participant import Participant
    from .participant_info import ParticipantInfo
    from .result_info import ResultInfo
    from .tone_info import ToneInfo

from .entity import Entity

@dataclass
class Call(Entity, Parsable):
    # The audioRoutingGroups property
    audio_routing_groups: Optional[list[AudioRoutingGroup]] = None
    # A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This identifier must be copied over from Microsoft.Graph.Call.CallChainId.
    call_chain_id: Optional[str] = None
    # Contains the optional features for the call.
    call_options: Optional[CallOptions] = None
    # The routing information on how the call was retargeted. Read-only.
    call_routes: Optional[list[CallRoute]] = None
    # The callback URL on which callbacks are delivered. Must be an HTTPS URL.
    callback_uri: Optional[str] = None
    # The chat information. Required information for joining a meeting.
    chat_info: Optional[ChatInfo] = None
    # The contentSharingSessions property
    content_sharing_sessions: Optional[list[ContentSharingSession]] = None
    # The direction of the call. The possible values are incoming or outgoing. Read-only.
    direction: Optional[CallDirection] = None
    # Call context associated with an incoming call.
    incoming_context: Optional[IncomingContext] = None
    # The media configuration. Required.
    media_config: Optional[MediaConfig] = None
    # Read-only. The call media state.
    media_state: Optional[CallMediaState] = None
    # The meeting information. Required information for meeting scenarios.
    meeting_info: Optional[MeetingInfo] = None
    # The myParticipantId property
    my_participant_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[list[CommsOperation]] = None
    # The participants property
    participants: Optional[list[Participant]] = None
    # The list of requested modalities. The possible values are: unknown, audio, video, videoBasedScreenSharing, data.
    requested_modalities: Optional[list[Modality]] = None
    # The result information. For example, the result can hold termination reason. Read-only.
    result_info: Optional[ResultInfo] = None
    # The originator of the call.
    source: Optional[ParticipantInfo] = None
    # The call state. The possible values are: incoming, establishing, ringing, established, hold, transferring, transferAccepted, redirecting, terminating, terminated. Read-only.
    state: Optional[CallState] = None
    # The subject of the conversation.
    subject: Optional[str] = None
    # The targets of the call. Required information for creating peer to peer call.
    targets: Optional[list[InvitationParticipantInfo]] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The toneInfo property
    tone_info: Optional[ToneInfo] = None
    # The transcription information for the call. Read-only.
    transcription: Optional[CallTranscriptionInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Call:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Call
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Call()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .audio_routing_group import AudioRoutingGroup
        from .call_direction import CallDirection
        from .call_media_state import CallMediaState
        from .call_options import CallOptions
        from .call_route import CallRoute
        from .call_state import CallState
        from .call_transcription_info import CallTranscriptionInfo
        from .chat_info import ChatInfo
        from .comms_operation import CommsOperation
        from .content_sharing_session import ContentSharingSession
        from .entity import Entity
        from .incoming_context import IncomingContext
        from .invitation_participant_info import InvitationParticipantInfo
        from .media_config import MediaConfig
        from .meeting_info import MeetingInfo
        from .modality import Modality
        from .participant import Participant
        from .participant_info import ParticipantInfo
        from .result_info import ResultInfo
        from .tone_info import ToneInfo

        from .audio_routing_group import AudioRoutingGroup
        from .call_direction import CallDirection
        from .call_media_state import CallMediaState
        from .call_options import CallOptions
        from .call_route import CallRoute
        from .call_state import CallState
        from .call_transcription_info import CallTranscriptionInfo
        from .chat_info import ChatInfo
        from .comms_operation import CommsOperation
        from .content_sharing_session import ContentSharingSession
        from .entity import Entity
        from .incoming_context import IncomingContext
        from .invitation_participant_info import InvitationParticipantInfo
        from .media_config import MediaConfig
        from .meeting_info import MeetingInfo
        from .modality import Modality
        from .participant import Participant
        from .participant_info import ParticipantInfo
        from .result_info import ResultInfo
        from .tone_info import ToneInfo

        fields: dict[str, Callable[[Any], None]] = {
            "audioRoutingGroups": lambda n : setattr(self, 'audio_routing_groups', n.get_collection_of_object_values(AudioRoutingGroup)),
            "callChainId": lambda n : setattr(self, 'call_chain_id', n.get_str_value()),
            "callOptions": lambda n : setattr(self, 'call_options', n.get_object_value(CallOptions)),
            "callRoutes": lambda n : setattr(self, 'call_routes', n.get_collection_of_object_values(CallRoute)),
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(ChatInfo)),
            "contentSharingSessions": lambda n : setattr(self, 'content_sharing_sessions', n.get_collection_of_object_values(ContentSharingSession)),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(CallDirection)),
            "incomingContext": lambda n : setattr(self, 'incoming_context', n.get_object_value(IncomingContext)),
            "mediaConfig": lambda n : setattr(self, 'media_config', n.get_object_value(MediaConfig)),
            "mediaState": lambda n : setattr(self, 'media_state', n.get_object_value(CallMediaState)),
            "meetingInfo": lambda n : setattr(self, 'meeting_info', n.get_object_value(MeetingInfo)),
            "myParticipantId": lambda n : setattr(self, 'my_participant_id', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(CommsOperation)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(Participant)),
            "requestedModalities": lambda n : setattr(self, 'requested_modalities', n.get_collection_of_enum_values(Modality)),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(ResultInfo)),
            "source": lambda n : setattr(self, 'source', n.get_object_value(ParticipantInfo)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(CallState)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(InvitationParticipantInfo)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "toneInfo": lambda n : setattr(self, 'tone_info', n.get_object_value(ToneInfo)),
            "transcription": lambda n : setattr(self, 'transcription', n.get_object_value(CallTranscriptionInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("audioRoutingGroups", self.audio_routing_groups)
        writer.write_str_value("callChainId", self.call_chain_id)
        writer.write_object_value("callOptions", self.call_options)
        writer.write_collection_of_object_values("callRoutes", self.call_routes)
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_object_value("chatInfo", self.chat_info)
        writer.write_collection_of_object_values("contentSharingSessions", self.content_sharing_sessions)
        writer.write_enum_value("direction", self.direction)
        writer.write_object_value("incomingContext", self.incoming_context)
        writer.write_object_value("mediaConfig", self.media_config)
        writer.write_object_value("mediaState", self.media_state)
        writer.write_object_value("meetingInfo", self.meeting_info)
        writer.write_str_value("myParticipantId", self.my_participant_id)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("participants", self.participants)
        writer.write_collection_of_enum_values("requestedModalities", self.requested_modalities)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_object_value("source", self.source)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("toneInfo", self.tone_info)
        writer.write_object_value("transcription", self.transcription)
    

