from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conversation_member import ConversationMember
    from .user import User

from .conversation_member import ConversationMember

@dataclass
class AadUserConversationMember(ConversationMember, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.aadUserConversationMember"
    # The email address of the user.
    email: Optional[str] = None
    # The tenant ID of the Microsoft Entra user.
    tenant_id: Optional[str] = None
    # The user property
    user: Optional[User] = None
    # The user ID of the Microsoft Entra user.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AadUserConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AadUserConversationMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AadUserConversationMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conversation_member import ConversationMember
        from .user import User

        from .conversation_member import ConversationMember
        from .user import User

        fields: dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(User)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_object_value("user", self.user)
        writer.write_str_value("userId", self.user_id)
    

