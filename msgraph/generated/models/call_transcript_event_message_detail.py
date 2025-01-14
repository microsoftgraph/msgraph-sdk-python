from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_message_detail import EventMessageDetail
    from .identity_set import IdentitySet

from .event_message_detail import EventMessageDetail

@dataclass
class CallTranscriptEventMessageDetail(EventMessageDetail, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.callTranscriptEventMessageDetail"
    # Unique identifier of the call.
    call_id: Optional[str] = None
    # Unique identifier for a call transcript.
    call_transcript_i_cal_uid: Optional[str] = None
    # The organizer of the meeting.
    meeting_organizer: Optional[IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallTranscriptEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallTranscriptEventMessageDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CallTranscriptEventMessageDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "callTranscriptICalUid": lambda n : setattr(self, 'call_transcript_i_cal_uid', n.get_str_value()),
            "meetingOrganizer": lambda n : setattr(self, 'meeting_organizer', n.get_object_value(IdentitySet)),
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
        writer.write_str_value("callId", self.call_id)
        writer.write_str_value("callTranscriptICalUid", self.call_transcript_i_cal_uid)
        writer.write_object_value("meetingOrganizer", self.meeting_organizer)
    

