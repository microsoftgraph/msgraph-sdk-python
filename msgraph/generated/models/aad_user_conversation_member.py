from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conversation_member = lazy_import('msgraph.generated.models.conversation_member')
user = lazy_import('msgraph.generated.models.user')

class AadUserConversationMember(conversation_member.ConversationMember):
    def __init__(self,) -> None:
        """
        Instantiates a new AadUserConversationMember and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.aadUserConversationMember"
        # The email address of the user.
        self._email: Optional[str] = None
        # TenantId which the Azure AD user belongs to.
        self._tenant_id: Optional[str] = None
        # The user property
        self._user: Optional[user.User] = None
        # The guid of the user.
        self._user_id: Optional[str] = None
    
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
    
    @property
    def email(self,) -> Optional[str]:
        """
        Gets the email property value. The email address of the user.
        Returns: Optional[str]
        """
        return self._email
    
    @email.setter
    def email(self,value: Optional[str] = None) -> None:
        """
        Sets the email property value. The email address of the user.
        Args:
            value: Value to set for the email property.
        """
        self._email = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(user.User)),
            "user_id": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
    
    @property
    def tenant_id(self,) -> Optional[str]:
        """
        Gets the tenantId property value. TenantId which the Azure AD user belongs to.
        Returns: Optional[str]
        """
        return self._tenant_id
    
    @tenant_id.setter
    def tenant_id(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantId property value. TenantId which the Azure AD user belongs to.
        Args:
            value: Value to set for the tenantId property.
        """
        self._tenant_id = value
    
    @property
    def user(self,) -> Optional[user.User]:
        """
        Gets the user property value. The user property
        Returns: Optional[user.User]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[user.User] = None) -> None:
        """
        Sets the user property value. The user property
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. The guid of the user.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. The guid of the user.
        Args:
            value: Value to set for the userId property.
        """
        self._user_id = value
    

