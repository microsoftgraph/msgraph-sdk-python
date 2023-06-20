from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message, response_type, time_slot

from . import event_message

@dataclass
class EventMessageResponse(event_message.EventMessage):
    odata_type = "#microsoft.graph.eventMessageResponse"
    # The proposedNewTime property
    proposed_new_time: Optional[time_slot.TimeSlot] = None
    # The responseType property
    response_type: Optional[response_type.ResponseType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EventMessageResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EventMessageResponse
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EventMessageResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message, response_type, time_slot

        from . import event_message, response_type, time_slot

        fields: Dict[str, Callable[[Any], None]] = {
            "proposedNewTime": lambda n : setattr(self, 'proposed_new_time', n.get_object_value(time_slot.TimeSlot)),
            "responseType": lambda n : setattr(self, 'response_type', n.get_enum_value(response_type.ResponseType)),
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
        writer.write_object_value("proposedNewTime", self.proposed_new_time)
        writer.write_enum_value("responseType", self.response_type)
    

