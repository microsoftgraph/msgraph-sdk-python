from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .exchange_message_trace import ExchangeMessageTrace

from .entity import Entity

@dataclass
class MessageTracingRoot(Entity, Parsable):
    # Represents the trace information of messages that pass through Exchange Online organizations.
    message_traces: Optional[list[ExchangeMessageTrace]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MessageTracingRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageTracingRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MessageTracingRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .exchange_message_trace import ExchangeMessageTrace

        from .entity import Entity
        from .exchange_message_trace import ExchangeMessageTrace

        fields: dict[str, Callable[[Any], None]] = {
            "messageTraces": lambda n : setattr(self, 'message_traces', n.get_collection_of_object_values(ExchangeMessageTrace)),
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
        writer.write_collection_of_object_values("messageTraces", self.message_traces)
    

