from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conversation_member, user

from . import conversation_member

@dataclass
class AadUserConversationMember(conversation_member.ConversationMember):
    odata_type = "#microsoft.graph.aadUserConversationMember"
    # The email address of the user.
    email: Optional[str] = None
    # TenantId which the Azure AD user belongs to.
    tenant_id: Optional[str] = None
    # The user property
    user: Optional[user.User] = None
    # The guid of the user.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AadUserConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AadUserConversationMember
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AadUserConversationMember()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conversation_member, user

        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(user.User)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userId", self.user_id)
    

