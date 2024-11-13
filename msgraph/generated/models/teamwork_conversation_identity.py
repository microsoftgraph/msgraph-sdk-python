from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity import Identity
    from .teamwork_conversation_identity_type import TeamworkConversationIdentityType

from .identity import Identity

@dataclass
class TeamworkConversationIdentity(Identity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.teamworkConversationIdentity"
    # Type of conversation. Possible values are: team, channel, chat, and unknownFutureValue.
    conversation_identity_type: Optional[TeamworkConversationIdentityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeamworkConversationIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkConversationIdentity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TeamworkConversationIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .identity import Identity
        from .teamwork_conversation_identity_type import TeamworkConversationIdentityType

        from .identity import Identity
        from .teamwork_conversation_identity_type import TeamworkConversationIdentityType

        fields: Dict[str, Callable[[Any], None]] = {
            "conversationIdentityType": lambda n : setattr(self, 'conversation_identity_type', n.get_enum_value(TeamworkConversationIdentityType)),
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
        from .identity import Identity
        from .teamwork_conversation_identity_type import TeamworkConversationIdentityType

        writer.write_enum_value("conversationIdentityType", self.conversation_identity_type)
    

