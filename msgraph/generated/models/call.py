from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audio_routing_group, call_direction, call_media_state, call_options, call_route, call_state, call_transcription_info, chat_info, comms_operation, content_sharing_session, entity, incoming_context, invitation_participant_info, media_config, meeting_info, modality, participant, participant_info, result_info, tone_info

from . import entity

@dataclass
class Call(entity.Entity):
    # The audioRoutingGroups property
    audio_routing_groups: Optional[List[audio_routing_group.AudioRoutingGroup]] = None
    # A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.
    call_chain_id: Optional[str] = None
    # Contains the optional features for the call.
    call_options: Optional[call_options.CallOptions] = None
    # The routing information on how the call was retargeted. Read-only.
    call_routes: Optional[List[call_route.CallRoute]] = None
    # The callback URL on which callbacks will be delivered. Must be https.
    callback_uri: Optional[str] = None
    # The chat information. Required information for joining a meeting.
    chat_info: Optional[chat_info.ChatInfo] = None
    # The contentSharingSessions property
    content_sharing_sessions: Optional[List[content_sharing_session.ContentSharingSession]] = None
    # The direction of the call. The possible value are incoming or outgoing. Read-only.
    direction: Optional[call_direction.CallDirection] = None
    # Call context associated with an incoming call.
    incoming_context: Optional[incoming_context.IncomingContext] = None
    # The media configuration. Required.
    media_config: Optional[media_config.MediaConfig] = None
    # Read-only. The call media state.
    media_state: Optional[call_media_state.CallMediaState] = None
    # The meeting information. Required information for meeting scenarios.
    meeting_info: Optional[meeting_info.MeetingInfo] = None
    # The myParticipantId property
    my_participant_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operations property
    operations: Optional[List[comms_operation.CommsOperation]] = None
    # The participants property
    participants: Optional[List[participant.Participant]] = None
    # The list of requested modalities. Possible values are: unknown, audio, video, videoBasedScreenSharing, data.
    requested_modalities: Optional[List[modality.Modality]] = None
    # The result information. For example can hold termination reason. Read-only.
    result_info: Optional[result_info.ResultInfo] = None
    # The originator of the call.
    source: Optional[participant_info.ParticipantInfo] = None
    # The call state. Possible values are: incoming, establishing, ringing, established, hold, transferring, transferAccepted, redirecting, terminating, terminated. Read-only.
    state: Optional[call_state.CallState] = None
    # The subject of the conversation.
    subject: Optional[str] = None
    # The targets of the call. Required information for creating peer to peer call.
    targets: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None
    # The tenantId property
    tenant_id: Optional[str] = None
    # The toneInfo property
    tone_info: Optional[tone_info.ToneInfo] = None
    # The transcription information for the call. Read-only.
    transcription: Optional[call_transcription_info.CallTranscriptionInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Call:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Call
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Call()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audio_routing_group, call_direction, call_media_state, call_options, call_route, call_state, call_transcription_info, chat_info, comms_operation, content_sharing_session, entity, incoming_context, invitation_participant_info, media_config, meeting_info, modality, participant, participant_info, result_info, tone_info

        fields: Dict[str, Callable[[Any], None]] = {
            "audioRoutingGroups": lambda n : setattr(self, 'audio_routing_groups', n.get_collection_of_object_values(audio_routing_group.AudioRoutingGroup)),
            "callbackUri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "callChainId": lambda n : setattr(self, 'call_chain_id', n.get_str_value()),
            "callOptions": lambda n : setattr(self, 'call_options', n.get_object_value(call_options.CallOptions)),
            "callRoutes": lambda n : setattr(self, 'call_routes', n.get_collection_of_object_values(call_route.CallRoute)),
            "chatInfo": lambda n : setattr(self, 'chat_info', n.get_object_value(chat_info.ChatInfo)),
            "contentSharingSessions": lambda n : setattr(self, 'content_sharing_sessions', n.get_collection_of_object_values(content_sharing_session.ContentSharingSession)),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(call_direction.CallDirection)),
            "incomingContext": lambda n : setattr(self, 'incoming_context', n.get_object_value(incoming_context.IncomingContext)),
            "mediaConfig": lambda n : setattr(self, 'media_config', n.get_object_value(media_config.MediaConfig)),
            "mediaState": lambda n : setattr(self, 'media_state', n.get_object_value(call_media_state.CallMediaState)),
            "meetingInfo": lambda n : setattr(self, 'meeting_info', n.get_object_value(meeting_info.MeetingInfo)),
            "myParticipantId": lambda n : setattr(self, 'my_participant_id', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(comms_operation.CommsOperation)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(participant.Participant)),
            "requestedModalities": lambda n : setattr(self, 'requested_modalities', n.get_collection_of_enum_values(modality.Modality)),
            "resultInfo": lambda n : setattr(self, 'result_info', n.get_object_value(result_info.ResultInfo)),
            "source": lambda n : setattr(self, 'source', n.get_object_value(participant_info.ParticipantInfo)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(call_state.CallState)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(invitation_participant_info.InvitationParticipantInfo)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "toneInfo": lambda n : setattr(self, 'tone_info', n.get_object_value(tone_info.ToneInfo)),
            "transcription": lambda n : setattr(self, 'transcription', n.get_object_value(call_transcription_info.CallTranscriptionInfo)),
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
        writer.write_collection_of_object_values("audioRoutingGroups", self.audio_routing_groups)
        writer.write_str_value("callbackUri", self.callback_uri)
        writer.write_str_value("callChainId", self.call_chain_id)
        writer.write_object_value("callOptions", self.call_options)
        writer.write_collection_of_object_values("callRoutes", self.call_routes)
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
        writer.write_enum_value("requestedModalities", self.requested_modalities)
        writer.write_object_value("resultInfo", self.result_info)
        writer.write_object_value("source", self.source)
        writer.write_enum_value("state", self.state)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("toneInfo", self.tone_info)
        writer.write_object_value("transcription", self.transcription)
    

