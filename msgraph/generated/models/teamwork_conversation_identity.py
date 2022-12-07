from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')
teamwork_conversation_identity_type = lazy_import('msgraph.generated.models.teamwork_conversation_identity_type')

class TeamworkConversationIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new TeamworkConversationIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teamworkConversationIdentity"
        # Type of conversation. Possible values are: team, channel, chat, and unknownFutureValue.
        self._conversation_identity_type: Optional[teamwork_conversation_identity_type.TeamworkConversationIdentityType] = None
    
    @property
    def conversation_identity_type(self,) -> Optional[teamwork_conversation_identity_type.TeamworkConversationIdentityType]:
        """
        Gets the conversationIdentityType property value. Type of conversation. Possible values are: team, channel, chat, and unknownFutureValue.
        Returns: Optional[teamwork_conversation_identity_type.TeamworkConversationIdentityType]
        """
        return self._conversation_identity_type
    
    @conversation_identity_type.setter
    def conversation_identity_type(self,value: Optional[teamwork_conversation_identity_type.TeamworkConversationIdentityType] = None) -> None:
        """
        Sets the conversationIdentityType property value. Type of conversation. Possible values are: team, channel, chat, and unknownFutureValue.
        Args:
            value: Value to set for the conversationIdentityType property.
        """
        self._conversation_identity_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkConversationIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkConversationIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkConversationIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conversation_identity_type": lambda n : setattr(self, 'conversation_identity_type', n.get_enum_value(teamwork_conversation_identity_type.TeamworkConversationIdentityType)),
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
        writer.write_enum_value("conversationIdentityType", self.conversation_identity_type)
    

