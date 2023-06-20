from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conversation_member

from . import conversation_member

@dataclass
class AnonymousGuestConversationMember(conversation_member.ConversationMember):
    odata_type = "#microsoft.graph.anonymousGuestConversationMember"
    # Unique ID that represents the user. Note: This ID can change if the user leaves and rejoins the meeting, or joins from a different device.
    anonymous_guest_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AnonymousGuestConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AnonymousGuestConversationMember
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AnonymousGuestConversationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conversation_member

        from . import conversation_member

        fields: Dict[str, Callable[[Any], None]] = {
            "anonymousGuestId": lambda n : setattr(self, 'anonymous_guest_id', n.get_str_value()),
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
        writer.write_str_value("anonymousGuestId", self.anonymous_guest_id)
    

