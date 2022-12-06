from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

event_message_detail = lazy_import('msgraph.generated.models.event_message_detail')
identity_set = lazy_import('msgraph.generated.models.identity_set')
teamwork_user_identity = lazy_import('msgraph.generated.models.teamwork_user_identity')

class ConversationMemberRoleUpdatedEventMessageDetail(event_message_detail.EventMessageDetail):
    def __init__(self,) -> None:
        """
        Instantiates a new ConversationMemberRoleUpdatedEventMessageDetail and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.conversationMemberRoleUpdatedEventMessageDetail"
        # Roles for the coversation member user.
        self._conversation_member_roles: Optional[List[str]] = None
        # Identity of the conversation member user.
        self._conversation_member_user: Optional[teamwork_user_identity.TeamworkUserIdentity] = None
        # Initiator of the event.
        self._initiator: Optional[identity_set.IdentitySet] = None
    
    @property
    def conversation_member_roles(self,) -> Optional[List[str]]:
        """
        Gets the conversationMemberRoles property value. Roles for the coversation member user.
        Returns: Optional[List[str]]
        """
        return self._conversation_member_roles
    
    @conversation_member_roles.setter
    def conversation_member_roles(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the conversationMemberRoles property value. Roles for the coversation member user.
        Args:
            value: Value to set for the conversationMemberRoles property.
        """
        self._conversation_member_roles = value
    
    @property
    def conversation_member_user(self,) -> Optional[teamwork_user_identity.TeamworkUserIdentity]:
        """
        Gets the conversationMemberUser property value. Identity of the conversation member user.
        Returns: Optional[teamwork_user_identity.TeamworkUserIdentity]
        """
        return self._conversation_member_user
    
    @conversation_member_user.setter
    def conversation_member_user(self,value: Optional[teamwork_user_identity.TeamworkUserIdentity] = None) -> None:
        """
        Sets the conversationMemberUser property value. Identity of the conversation member user.
        Args:
            value: Value to set for the conversationMemberUser property.
        """
        self._conversation_member_user = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConversationMemberRoleUpdatedEventMessageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConversationMemberRoleUpdatedEventMessageDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConversationMemberRoleUpdatedEventMessageDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "conversation_member_roles": lambda n : setattr(self, 'conversation_member_roles', n.get_collection_of_primitive_values(str)),
            "conversation_member_user": lambda n : setattr(self, 'conversation_member_user', n.get_object_value(teamwork_user_identity.TeamworkUserIdentity)),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(identity_set.IdentitySet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def initiator(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the initiator property value. Initiator of the event.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._initiator
    
    @initiator.setter
    def initiator(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the initiator property value. Initiator of the event.
        Args:
            value: Value to set for the initiator property.
        """
        self._initiator = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_primitive_values("conversationMemberRoles", self.conversation_member_roles)
        writer.write_object_value("conversationMemberUser", self.conversation_member_user)
        writer.write_object_value("initiator", self.initiator)
    

