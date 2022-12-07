from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

call_participant_info = lazy_import('msgraph.generated.models.call_participant_info')
event_message_detail = lazy_import('msgraph.generated.models.event_message_detail')
identity_set = lazy_import('msgraph.generated.models.identity_set')
teamwork_call_event_type = lazy_import('msgraph.generated.models.teamwork_call_event_type')

class CallEndedEventMessageDetail(event_message_detail.EventMessageDetail):
    @property
    def call_duration(self,) -> Optional[Timedelta]:
        """
        Gets the callDuration property value. Duration of the call.
        Returns: Optional[Timedelta]
        """
        return self._call_duration
    
    @call_duration.setter
    def call_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the callDuration property value. Duration of the call.
        Args:
            value: Value to set for the callDuration property.
        """
        self._call_duration = value
    
    @property
    def call_event_type(self,) -> Optional[teamwork_call_event_type.TeamworkCallEventType]:
        """
        Gets the callEventType property value. Represents the call event type. Possible values are: call, meeting, screenShare, unknownFutureValue.
        Returns: Optional[teamwork_call_event_type.TeamworkCallEventType]
        """
        return self._call_event_type
    
    @call_event_type.setter
    def call_event_type(self,value: Optional[teamwork_call_event_type.TeamworkCallEventType] = None) -> None:
        """
        Sets the callEventType property value. Represents the call event type. Possible values are: call, meeting, screenShare, unknownFutureValue.
        Args:
            value: Value to set for the callEventType property.
        """
        self._call_event_type = value
    
    @property
    def call_id(self,) -> Optional[str]:
        """
        Gets the callId property value. Unique identifier of the call.
        Returns: Optional[str]
        """
        return self._call_id
    
    @call_id.setter
    def call_id(self,value: Optional[str] = None) -> None:
        """
        Sets the callId property value. Unique identifier of the call.
        Args:
            value: Value to set for the callId property.
        """
        self._call_id = value
    
    @property
    def call_participants(self,) -> Optional[List[call_participant_info.CallParticipantInfo]]:
        """
        Gets the callParticipants property value. List of call participants.
        Returns: Optional[List[call_participant_info.CallParticipantInfo]]
        """
        return self._call_participants
    
    @call_participants.setter
    def call_participants(self,value: Optional[List[call_participant_info.CallParticipantInfo]] = None) -> None:
        """
        Sets the callParticipants property value. List of call participants.
        Args:
            value: Value to set for the callParticipants property.
        """
        self._call_participants = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new CallEndedEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.callEndedEventMessageDetail"
        # Duration of the call.
        self._call_duration: Optional[Timedelta] = None
        # Represents the call event type. Possible values are: call, meeting, screenShare, unknownFutureValue.
        self._call_event_type: Optional[teamwork_call_event_type.TeamworkCallEventType] = None
        # Unique identifier of the call.
        self._call_id: Optional[str] = None
        # List of call participants.
        self._call_participants: Optional[List[call_participant_info.CallParticipantInfo]] = None
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallEndedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallEndedEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallEndedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "call_duration": lambda n : setattr(self, 'call_duration', n.get_object_value(Timedelta)),
            "call_event_type": lambda n : setattr(self, 'call_event_type', n.get_enum_value(teamwork_call_event_type.TeamworkCallEventType)),
            "call_id": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "call_participants": lambda n : setattr(self, 'call_participants', n.get_collection_of_object_values(call_participant_info.CallParticipantInfo)),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiator(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the initiator property value. Initiator of the event.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._initiator
    
    @initiator.setter
    def initiator(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the initiator property value. Initiator of the event.
        Args:
            value: Value to set for the initiator property.
        """
        self._initiator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("callDuration", self.call_duration)
        writer.write_enum_value("callEventType", self.call_event_type)
        writer.write_str_value("callId", self.call_id)
        writer.write_collection_of_object_values("callParticipants", self.call_participants)
        writer.write_object_value("initiator", self.initiator)
    

