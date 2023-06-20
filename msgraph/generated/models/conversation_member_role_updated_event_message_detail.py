from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import event_message_detail, identity_set, teamwork_user_identity

from . import event_message_detail

@dataclass
class ConversationMemberRoleUpdatedEventMessageDetail(event_message_detail.EventMessageDetail):
    odata_type = "#microsoft.graph.conversationMemberRoleUpdatedEventMessageDetail"
    # Roles for the coversation member user.
    conversation_member_roles: Optional[List[str]] = None
    # Identity of the conversation member user.
    conversation_member_user: Optional[teamwork_user_identity.TeamworkUserIdentity] = None
    # Initiator of the event.
    initiator: Optional[identity_set.IdentitySet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConversationMemberRoleUpdatedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConversationMemberRoleUpdatedEventMessageDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ConversationMemberRoleUpdatedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import event_message_detail, identity_set, teamwork_user_identity

        from . import event_message_detail, identity_set, teamwork_user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "conversationMemberRoles": lambda n : setattr(self, 'conversation_member_roles', n.get_collection_of_primitive_values(str)),
            "conversationMemberUser": lambda n : setattr(self, 'conversation_member_user', n.get_object_value(teamwork_user_identity.TeamworkUserIdentity)),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
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
        writer.write_collection_of_primitive_values("conversationMemberRoles", self.conversation_member_roles)
        writer.write_object_value("conversationMemberUser", self.conversation_member_user)
        writer.write_object_value("initiator", self.initiator)
    

