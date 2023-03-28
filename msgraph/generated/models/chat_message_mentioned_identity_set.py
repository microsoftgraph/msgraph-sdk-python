from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity_set, teamwork_conversation_identity

from . import identity_set

class ChatMessageMentionedIdentitySet(identity_set.IdentitySet):
    def __init__(self,) -> None:
        """
        Instantiates a new ChatMessageMentionedIdentitySet and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.chatMessageMentionedIdentitySet"
        # If present, represents a conversation (for example, team or channel) @mentioned in a message.
        self._conversation: Optional[teamwork_conversation_identity.TeamworkConversationIdentity] = None
    
    @property
    def conversation(self,) -> Optional[teamwork_conversation_identity.TeamworkConversationIdentity]:
        """
        Gets the conversation property value. If present, represents a conversation (for example, team or channel) @mentioned in a message.
        Returns: Optional[teamwork_conversation_identity.TeamworkConversationIdentity]
        """
        return self._conversation
    
    @conversation.setter
    def conversation(self,value: Optional[teamwork_conversation_identity.TeamworkConversationIdentity] = None) -> None:
        """
        Sets the conversation property value. If present, represents a conversation (for example, team or channel) @mentioned in a message.
        Args:
            value: Value to set for the conversation property.
        """
        self._conversation = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageMentionedIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageMentionedIdentitySet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessageMentionedIdentitySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity_set, teamwork_conversation_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "conversation": lambda n : setattr(self, 'conversation', n.get_object_value(teamwork_conversation_identity.TeamworkConversationIdentity)),
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
        writer.write_object_value("conversation", self.conversation)
    

