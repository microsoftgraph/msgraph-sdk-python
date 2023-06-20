from __future__ import annotations
from dataclasses import dataclass, field
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import call_participant_info, event_message_detail, identity_set, teamwork_call_event_type

from . import event_message_detail

@dataclass
class CallEndedEventMessageDetail(event_message_detail.EventMessageDetail):
    odata_type = "#microsoft.graph.callEndedEventMessageDetail"
    # Duration of the call.
    call_duration: Optional[timedelta] = None
    # Represents the call event type. Possible values are: call, meeting, screenShare, unknownFutureValue.
    call_event_type: Optional[teamwork_call_event_type.TeamworkCallEventType] = None
    # Unique identifier of the call.
    call_id: Optional[str] = None
    # List of call participants.
    call_participants: Optional[List[call_participant_info.CallParticipantInfo]] = None
    # Initiator of the event.
    initiator: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallEndedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallEndedEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CallEndedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import call_participant_info, event_message_detail, identity_set, teamwork_call_event_type

        from . import call_participant_info, event_message_detail, identity_set, teamwork_call_event_type

        fields: Dict[str, Callable[[Any], None]] = {
            "callDuration": lambda n : setattr(self, 'call_duration', n.get_timedelta_value()),
            "callEventType": lambda n : setattr(self, 'call_event_type', n.get_enum_value(teamwork_call_event_type.TeamworkCallEventType)),
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "callParticipants": lambda n : setattr(self, 'call_participants', n.get_collection_of_object_values(call_participant_info.CallParticipantInfo)),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_timedelta_value("callDuration", self.call_duration)
        writer.write_enum_value("callEventType", self.call_event_type)
        writer.write_str_value("callId", self.call_id)
        writer.write_collection_of_object_values("callParticipants", self.call_participants)
        writer.write_object_value("initiator", self.initiator)
    

