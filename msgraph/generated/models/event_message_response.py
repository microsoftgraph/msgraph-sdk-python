from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .event_message import EventMessage
    from .response_type import ResponseType
    from .time_slot import TimeSlot

from .event_message import EventMessage

@dataclass
class EventMessageResponse(EventMessage, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.eventMessageResponse"
    # An alternate date/time proposed by an invitee for a meeting request to start and end. Read-only. Not filterable.
    proposed_new_time: Optional[TimeSlot] = None
    # Specifies the type of response to a meeting request. The possible values are: tentativelyAccepted, accepted, declined. For the eventMessageResponse type, none, organizer, and notResponded are not supported. Read-only. Not filterable.
    response_type: Optional[ResponseType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EventMessageResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EventMessageResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EventMessageResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .event_message import EventMessage
        from .response_type import ResponseType
        from .time_slot import TimeSlot

        from .event_message import EventMessage
        from .response_type import ResponseType
        from .time_slot import TimeSlot

        fields: dict[str, Callable[[Any], None]] = {
            "proposedNewTime": lambda n : setattr(self, 'proposed_new_time', n.get_object_value(TimeSlot)),
            "responseType": lambda n : setattr(self, 'response_type', n.get_enum_value(ResponseType)),
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
        writer.write_object_value("proposedNewTime", self.proposed_new_time)
        writer.write_enum_value("responseType", self.response_type)
    

