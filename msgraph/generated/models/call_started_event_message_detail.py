from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_message_detail import EventMessageDetail
    from .identity_set import IdentitySet
    from .teamwork_call_event_type import TeamworkCallEventType

from .event_message_detail import EventMessageDetail

@dataclass
class CallStartedEventMessageDetail(EventMessageDetail, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.callStartedEventMessageDetail"
    # Represents the call event type. The possible values are: call, meeting, screenShare, unknownFutureValue.
    call_event_type: Optional[TeamworkCallEventType] = None
    # Unique identifier of the call.
    call_id: Optional[str] = None
    # Initiator of the event.
    initiator: Optional[IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CallStartedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CallStartedEventMessageDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CallStartedEventMessageDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet
        from .teamwork_call_event_type import TeamworkCallEventType

        from .event_message_detail import EventMessageDetail
        from .identity_set import IdentitySet
        from .teamwork_call_event_type import TeamworkCallEventType

        fields: dict[str, Callable[[Any], None]] = {
            "callEventType": lambda n : setattr(self, 'call_event_type', n.get_enum_value(TeamworkCallEventType)),
            "callId": lambda n : setattr(self, 'call_id', n.get_str_value()),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(IdentitySet)),
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
        writer.write_enum_value("callEventType", self.call_event_type)
        writer.write_str_value("callId", self.call_id)
        writer.write_object_value("initiator", self.initiator)
    

