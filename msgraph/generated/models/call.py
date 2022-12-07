from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

audio_routing_group = lazy_import('msgraph.generated.models.audio_routing_group')
call_direction = lazy_import('msgraph.generated.models.call_direction')
call_media_state = lazy_import('msgraph.generated.models.call_media_state')
call_options = lazy_import('msgraph.generated.models.call_options')
call_route = lazy_import('msgraph.generated.models.call_route')
call_state = lazy_import('msgraph.generated.models.call_state')
call_transcription_info = lazy_import('msgraph.generated.models.call_transcription_info')
chat_info = lazy_import('msgraph.generated.models.chat_info')
comms_operation = lazy_import('msgraph.generated.models.comms_operation')
content_sharing_session = lazy_import('msgraph.generated.models.content_sharing_session')
entity = lazy_import('msgraph.generated.models.entity')
incoming_context = lazy_import('msgraph.generated.models.incoming_context')
invitation_participant_info = lazy_import('msgraph.generated.models.invitation_participant_info')
media_config = lazy_import('msgraph.generated.models.media_config')
meeting_info = lazy_import('msgraph.generated.models.meeting_info')
modality = lazy_import('msgraph.generated.models.modality')
participant = lazy_import('msgraph.generated.models.participant')
participant_info = lazy_import('msgraph.generated.models.participant_info')
result_info = lazy_import('msgraph.generated.models.result_info')
tone_info = lazy_import('msgraph.generated.models.tone_info')

class Call(entity.Entity):
    """
    Provides operations to manage the cloudCommunications singleton.
    """
    @property
    def audio_routing_groups(self,) -> Optional[List[audio_routing_group.AudioRoutingGroup]]:
        """
        Gets the audioRoutingGroups property value. The audioRoutingGroups property
        Returns: Optional[List[audio_routing_group.AudioRoutingGroup]]
        """
        return self._audio_routing_groups
    
    @audio_routing_groups.setter
    def audio_routing_groups(self,value: Optional[List[audio_routing_group.AudioRoutingGroup]] = None) -> None:
        """
        Sets the audioRoutingGroups property value. The audioRoutingGroups property
        Args:
            value: Value to set for the audioRoutingGroups property.
        """
        self._audio_routing_groups = value
    
    @property
    def callback_uri(self,) -> Optional[str]:
        """
        Gets the callbackUri property value. The callback URL on which callbacks will be delivered. Must be https.
        Returns: Optional[str]
        """
        return self._callback_uri
    
    @callback_uri.setter
    def callback_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the callbackUri property value. The callback URL on which callbacks will be delivered. Must be https.
        Args:
            value: Value to set for the callbackUri property.
        """
        self._callback_uri = value
    
    @property
    def call_chain_id(self,) -> Optional[str]:
        """
        Gets the callChainId property value. A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        Returns: Optional[str]
        """
        return self._call_chain_id
    
    @call_chain_id.setter
    def call_chain_id(self,value: Optional[str] = None) -> None:
        """
        Sets the callChainId property value. A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        Args:
            value: Value to set for the callChainId property.
        """
        self._call_chain_id = value
    
    @property
    def call_options(self,) -> Optional[call_options.CallOptions]:
        """
        Gets the callOptions property value. Contains the optional features for the call.
        Returns: Optional[call_options.CallOptions]
        """
        return self._call_options
    
    @call_options.setter
    def call_options(self,value: Optional[call_options.CallOptions] = None) -> None:
        """
        Sets the callOptions property value. Contains the optional features for the call.
        Args:
            value: Value to set for the callOptions property.
        """
        self._call_options = value
    
    @property
    def call_routes(self,) -> Optional[List[call_route.CallRoute]]:
        """
        Gets the callRoutes property value. The routing information on how the call was retargeted. Read-only.
        Returns: Optional[List[call_route.CallRoute]]
        """
        return self._call_routes
    
    @call_routes.setter
    def call_routes(self,value: Optional[List[call_route.CallRoute]] = None) -> None:
        """
        Sets the callRoutes property value. The routing information on how the call was retargeted. Read-only.
        Args:
            value: Value to set for the callRoutes property.
        """
        self._call_routes = value
    
    @property
    def chat_info(self,) -> Optional[chat_info.ChatInfo]:
        """
        Gets the chatInfo property value. The chat information. Required information for joining a meeting.
        Returns: Optional[chat_info.ChatInfo]
        """
        return self._chat_info
    
    @chat_info.setter
    def chat_info(self,value: Optional[chat_info.ChatInfo] = None) -> None:
        """
        Sets the chatInfo property value. The chat information. Required information for joining a meeting.
        Args:
            value: Value to set for the chatInfo property.
        """
        self._chat_info = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new call and sets the default values.
        """
        super().__init__()
        # The audioRoutingGroups property
        self._audio_routing_groups: Optional[List[audio_routing_group.AudioRoutingGroup]] = None
        # The callback URL on which callbacks will be delivered. Must be https.
        self._callback_uri: Optional[str] = None
        # A unique identifier for all the participant calls in a conference or a unique identifier for two participant calls in a P2P call.  This needs to be copied over from Microsoft.Graph.Call.CallChainId.
        self._call_chain_id: Optional[str] = None
        # Contains the optional features for the call.
        self._call_options: Optional[call_options.CallOptions] = None
        # The routing information on how the call was retargeted. Read-only.
        self._call_routes: Optional[List[call_route.CallRoute]] = None
        # The chat information. Required information for joining a meeting.
        self._chat_info: Optional[chat_info.ChatInfo] = None
        # The contentSharingSessions property
        self._content_sharing_sessions: Optional[List[content_sharing_session.ContentSharingSession]] = None
        # The direction of the call. The possible value are incoming or outgoing. Read-only.
        self._direction: Optional[call_direction.CallDirection] = None
        # Call context associated with an incoming call.
        self._incoming_context: Optional[incoming_context.IncomingContext] = None
        # The media configuration. Required.
        self._media_config: Optional[media_config.MediaConfig] = None
        # Read-only. The call media state.
        self._media_state: Optional[call_media_state.CallMediaState] = None
        # The meeting information that's required for joining a meeting.
        self._meeting_info: Optional[meeting_info.MeetingInfo] = None
        # The myParticipantId property
        self._my_participant_id: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The operations property
        self._operations: Optional[List[comms_operation.CommsOperation]] = None
        # The participants property
        self._participants: Optional[List[participant.Participant]] = None
        # The list of requested modalities. Possible values are: unknown, audio, video, videoBasedScreenSharing, data.
        self._requested_modalities: Optional[List[modality.Modality]] = None
        # The result information. For example can hold termination reason. Read-only.
        self._result_info: Optional[result_info.ResultInfo] = None
        # The originator of the call.
        self._source: Optional[participant_info.ParticipantInfo] = None
        # The call state. Possible values are: incoming, establishing, ringing, established, hold, transferring, transferAccepted, redirecting, terminating, terminated. Read-only.
        self._state: Optional[call_state.CallState] = None
        # The subject of the conversation.
        self._subject: Optional[str] = None
        # The targets of the call. Required information for creating peer to peer call.
        self._targets: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None
        # The tenantId property
        self._tenant_id: Optional[str] = None
        # The toneInfo property
        self._tone_info: Optional[tone_info.ToneInfo] = None
        # The transcription information for the call. Read-only.
        self._transcription: Optional[call_transcription_info.CallTranscriptionInfo] = None
    
    @property
    def content_sharing_sessions(self,) -> Optional[List[content_sharing_session.ContentSharingSession]]:
        """
        Gets the contentSharingSessions property value. The contentSharingSessions property
        Returns: Optional[List[content_sharing_session.ContentSharingSession]]
        """
        return self._content_sharing_sessions
    
    @content_sharing_sessions.setter
    def content_sharing_sessions(self,value: Optional[List[content_sharing_session.ContentSharingSession]] = None) -> None:
        """
        Sets the contentSharingSessions property value. The contentSharingSessions property
        Args:
            value: Value to set for the contentSharingSessions property.
        """
        self._content_sharing_sessions = value
    
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
    
    @property
    def direction(self,) -> Optional[call_direction.CallDirection]:
        """
        Gets the direction property value. The direction of the call. The possible value are incoming or outgoing. Read-only.
        Returns: Optional[call_direction.CallDirection]
        """
        return self._direction
    
    @direction.setter
    def direction(self,value: Optional[call_direction.CallDirection] = None) -> None:
        """
        Sets the direction property value. The direction of the call. The possible value are incoming or outgoing. Read-only.
        Args:
            value: Value to set for the direction property.
        """
        self._direction = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audio_routing_groups": lambda n : setattr(self, 'audio_routing_groups', n.get_collection_of_object_values(audio_routing_group.AudioRoutingGroup)),
            "callback_uri": lambda n : setattr(self, 'callback_uri', n.get_str_value()),
            "call_chain_id": lambda n : setattr(self, 'call_chain_id', n.get_str_value()),
            "call_options": lambda n : setattr(self, 'call_options', n.get_object_value(call_options.CallOptions)),
            "call_routes": lambda n : setattr(self, 'call_routes', n.get_collection_of_object_values(call_route.CallRoute)),
            "chat_info": lambda n : setattr(self, 'chat_info', n.get_object_value(chat_info.ChatInfo)),
            "content_sharing_sessions": lambda n : setattr(self, 'content_sharing_sessions', n.get_collection_of_object_values(content_sharing_session.ContentSharingSession)),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(call_direction.CallDirection)),
            "incoming_context": lambda n : setattr(self, 'incoming_context', n.get_object_value(incoming_context.IncomingContext)),
            "media_config": lambda n : setattr(self, 'media_config', n.get_object_value(media_config.MediaConfig)),
            "media_state": lambda n : setattr(self, 'media_state', n.get_object_value(call_media_state.CallMediaState)),
            "meeting_info": lambda n : setattr(self, 'meeting_info', n.get_object_value(meeting_info.MeetingInfo)),
            "my_participant_id": lambda n : setattr(self, 'my_participant_id', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(comms_operation.CommsOperation)),
            "participants": lambda n : setattr(self, 'participants', n.get_collection_of_object_values(participant.Participant)),
            "requested_modalities": lambda n : setattr(self, 'requested_modalities', n.get_collection_of_enum_values(modality.Modality)),
            "result_info": lambda n : setattr(self, 'result_info', n.get_object_value(result_info.ResultInfo)),
            "source": lambda n : setattr(self, 'source', n.get_object_value(participant_info.ParticipantInfo)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(call_state.CallState)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(invitation_participant_info.InvitationParticipantInfo)),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "tone_info": lambda n : setattr(self, 'tone_info', n.get_object_value(tone_info.ToneInfo)),
            "transcription": lambda n : setattr(self, 'transcription', n.get_object_value(call_transcription_info.CallTranscriptionInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incoming_context(self,) -> Optional[incoming_context.IncomingContext]:
        """
        Gets the incomingContext property value. Call context associated with an incoming call.
        Returns: Optional[incoming_context.IncomingContext]
        """
        return self._incoming_context
    
    @incoming_context.setter
    def incoming_context(self,value: Optional[incoming_context.IncomingContext] = None) -> None:
        """
        Sets the incomingContext property value. Call context associated with an incoming call.
        Args:
            value: Value to set for the incomingContext property.
        """
        self._incoming_context = value
    
    @property
    def media_config(self,) -> Optional[media_config.MediaConfig]:
        """
        Gets the mediaConfig property value. The media configuration. Required.
        Returns: Optional[media_config.MediaConfig]
        """
        return self._media_config
    
    @media_config.setter
    def media_config(self,value: Optional[media_config.MediaConfig] = None) -> None:
        """
        Sets the mediaConfig property value. The media configuration. Required.
        Args:
            value: Value to set for the mediaConfig property.
        """
        self._media_config = value
    
    @property
    def media_state(self,) -> Optional[call_media_state.CallMediaState]:
        """
        Gets the mediaState property value. Read-only. The call media state.
        Returns: Optional[call_media_state.CallMediaState]
        """
        return self._media_state
    
    @media_state.setter
    def media_state(self,value: Optional[call_media_state.CallMediaState] = None) -> None:
        """
        Sets the mediaState property value. Read-only. The call media state.
        Args:
            value: Value to set for the mediaState property.
        """
        self._media_state = value
    
    @property
    def meeting_info(self,) -> Optional[meeting_info.MeetingInfo]:
        """
        Gets the meetingInfo property value. The meeting information that's required for joining a meeting.
        Returns: Optional[meeting_info.MeetingInfo]
        """
        return self._meeting_info
    
    @meeting_info.setter
    def meeting_info(self,value: Optional[meeting_info.MeetingInfo] = None) -> None:
        """
        Sets the meetingInfo property value. The meeting information that's required for joining a meeting.
        Args:
            value: Value to set for the meetingInfo property.
        """
        self._meeting_info = value
    
    @property
    def my_participant_id(self,) -> Optional[str]:
        """
        Gets the myParticipantId property value. The myParticipantId property
        Returns: Optional[str]
        """
        return self._my_participant_id
    
    @my_participant_id.setter
    def my_participant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the myParticipantId property value. The myParticipantId property
        Args:
            value: Value to set for the myParticipantId property.
        """
        self._my_participant_id = value
    
    @property
    def operations(self,) -> Optional[List[comms_operation.CommsOperation]]:
        """
        Gets the operations property value. The operations property
        Returns: Optional[List[comms_operation.CommsOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[comms_operation.CommsOperation]] = None) -> None:
        """
        Sets the operations property value. The operations property
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def participants(self,) -> Optional[List[participant.Participant]]:
        """
        Gets the participants property value. The participants property
        Returns: Optional[List[participant.Participant]]
        """
        return self._participants
    
    @participants.setter
    def participants(self,value: Optional[List[participant.Participant]] = None) -> None:
        """
        Sets the participants property value. The participants property
        Args:
            value: Value to set for the participants property.
        """
        self._participants = value
    
    @property
    def requested_modalities(self,) -> Optional[List[modality.Modality]]:
        """
        Gets the requestedModalities property value. The list of requested modalities. Possible values are: unknown, audio, video, videoBasedScreenSharing, data.
        Returns: Optional[List[modality.Modality]]
        """
        return self._requested_modalities
    
    @requested_modalities.setter
    def requested_modalities(self,value: Optional[List[modality.Modality]] = None) -> None:
        """
        Sets the requestedModalities property value. The list of requested modalities. Possible values are: unknown, audio, video, videoBasedScreenSharing, data.
        Args:
            value: Value to set for the requestedModalities property.
        """
        self._requested_modalities = value
    
    @property
    def result_info(self,) -> Optional[result_info.ResultInfo]:
        """
        Gets the resultInfo property value. The result information. For example can hold termination reason. Read-only.
        Returns: Optional[result_info.ResultInfo]
        """
        return self._result_info
    
    @result_info.setter
    def result_info(self,value: Optional[result_info.ResultInfo] = None) -> None:
        """
        Sets the resultInfo property value. The result information. For example can hold termination reason. Read-only.
        Args:
            value: Value to set for the resultInfo property.
        """
        self._result_info = value
    
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
    
    @property
    def source(self,) -> Optional[participant_info.ParticipantInfo]:
        """
        Gets the source property value. The originator of the call.
        Returns: Optional[participant_info.ParticipantInfo]
        """
        return self._source
    
    @source.setter
    def source(self,value: Optional[participant_info.ParticipantInfo] = None) -> None:
        """
        Sets the source property value. The originator of the call.
        Args:
            value: Value to set for the source property.
        """
        self._source = value
    
    @property
    def state(self,) -> Optional[call_state.CallState]:
        """
        Gets the state property value. The call state. Possible values are: incoming, establishing, ringing, established, hold, transferring, transferAccepted, redirecting, terminating, terminated. Read-only.
        Returns: Optional[call_state.CallState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[call_state.CallState] = None) -> None:
        """
        Sets the state property value. The call state. Possible values are: incoming, establishing, ringing, established, hold, transferring, transferAccepted, redirecting, terminating, terminated. Read-only.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject of the conversation.
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject of the conversation.
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def targets(self,) -> Optional[List[invitation_participant_info.InvitationParticipantInfo]]:
        """
        Gets the targets property value. The targets of the call. Required information for creating peer to peer call.
        Returns: Optional[List[invitation_participant_info.InvitationParticipantInfo]]
        """
        return self._targets
    
    @targets.setter
    def targets(self,value: Optional[List[invitation_participant_info.InvitationParticipantInfo]] = None) -> None:
        """
        Sets the targets property value. The targets of the call. Required information for creating peer to peer call.
        Args:
            value: Value to set for the targets property.
        """
        self._targets = value
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. The tenantId property
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. The tenantId property
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def tone_info(self,) -> Optional[tone_info.ToneInfo]:
        """
        Gets the toneInfo property value. The toneInfo property
        Returns: Optional[tone_info.ToneInfo]
        """
        return self._tone_info
    
    @tone_info.setter
    def tone_info(self,value: Optional[tone_info.ToneInfo] = None) -> None:
        """
        Sets the toneInfo property value. The toneInfo property
        Args:
            value: Value to set for the toneInfo property.
        """
        self._tone_info = value
    
    @property
    def transcription(self,) -> Optional[call_transcription_info.CallTranscriptionInfo]:
        """
        Gets the transcription property value. The transcription information for the call. Read-only.
        Returns: Optional[call_transcription_info.CallTranscriptionInfo]
        """
        return self._transcription
    
    @transcription.setter
    def transcription(self,value: Optional[call_transcription_info.CallTranscriptionInfo] = None) -> None:
        """
        Sets the transcription property value. The transcription information for the call. Read-only.
        Args:
            value: Value to set for the transcription property.
        """
        self._transcription = value
    

