from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message import ChatMessage
    from .identity import Identity

from .chat_message import ChatMessage

@dataclass
class TargetedChatMessage(ChatMessage, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.targetedChatMessage"
    # The recipient property
    recipient: Optional[Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TargetedChatMessage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TargetedChatMessage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TargetedChatMessage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message import ChatMessage
        from .identity import Identity

        from .chat_message import ChatMessage
        from .identity import Identity

        fields: dict[str, Callable[[Any], None]] = {
            "recipient": lambda n : setattr(self, 'recipient', n.get_object_value(Identity)),
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
        writer.write_object_value("recipient", self.recipient)
    

