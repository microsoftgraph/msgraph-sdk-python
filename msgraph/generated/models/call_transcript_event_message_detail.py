from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message_detail, identity_set

from . import event_message_detail

@dataclass
class CallTranscriptEventMessageDetail(event_message_detail.EventMessageDetail):
    odata_type = "#microsoft.graph.callTranscriptEventMessageDetail"
    # Unique identifier of the call.
    call_id: Optional[str] = None
    # Unique identifier for a call transcript.
    call_transcript_i_cal_uid: Optional[str] = None
    # The organizer of the meeting.
    meeting_organizer: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallTranscriptEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallTranscriptEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallTranscriptEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message_detail, identity_set

        fields: Dict[str, Callable[[Any], None]] = {
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "callTranscriptICalUid": lambda n : setattr(self, 'call_transcript_i_cal_uid', n.get_str_value()),
            "meetingOrganizer": lambda n : setattr(self, 'meeting_organizer', n.get_object_value(identity_set.IdentitySet)),
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
        writer.write_str_value("callId", self.call_id)
        writer.write_str_value("callTranscriptICalUid", self.call_transcript_i_cal_uid)
        writer.write_object_value("meetingOrganizer", self.meeting_organizer)
    

