from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aad_user_conversation_member, anonymous_guest_conversation_member, azure_communication_services_user_conversation_member, entity, microsoft_account_user_conversation_member, skype_for_business_user_conversation_member, skype_user_conversation_member

from . import entity

class ConversationMember(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new conversationMember and sets the default values.
        """
        super().__init__()
        # The display name of the user.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The roles for that user. This property only contains additional qualifiers when relevant - for example, if the member has owner privileges, the roles property contains owner as one of the values. Similarly, if the member is a guest, the roles property contains guest as one of the values. A basic member should not have any values specified in the roles property.
        self._roles: Optional[List[str]] = None
        # The timestamp denoting how far back a conversation's history is shared with the conversation member. This property is settable only for members of a chat.
        self._visible_history_start_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConversationMember
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.aadUserConversationMember":
                from . import aad_user_conversation_member

                return aad_user_conversation_member.AadUserConversationMember()
            if mapping_value == "#microsoft.graph.anonymousGuestConversationMember":
                from . import anonymous_guest_conversation_member

                return anonymous_guest_conversation_member.AnonymousGuestConversationMember()
            if mapping_value == "#microsoft.graph.azureCommunicationServicesUserConversationMember":
                from . import azure_communication_services_user_conversation_member

                return azure_communication_services_user_conversation_member.AzureCommunicationServicesUserConversationMember()
            if mapping_value == "#microsoft.graph.microsoftAccountUserConversationMember":
                from . import microsoft_account_user_conversation_member

                return microsoft_account_user_conversation_member.MicrosoftAccountUserConversationMember()
            if mapping_value == "#microsoft.graph.skypeForBusinessUserConversationMember":
                from . import skype_for_business_user_conversation_member

                return skype_for_business_user_conversation_member.SkypeForBusinessUserConversationMember()
            if mapping_value == "#microsoft.graph.skypeUserConversationMember":
                from . import skype_user_conversation_member

                return skype_user_conversation_member.SkypeUserConversationMember()
        return ConversationMember()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name of the user.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name of the user.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aad_user_conversation_member, anonymous_guest_conversation_member, azure_communication_services_user_conversation_member, entity, microsoft_account_user_conversation_member, skype_for_business_user_conversation_member, skype_user_conversation_member

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "visibleHistoryStartDateTime": lambda n : setattr(self, 'visible_history_start_date_time', n.get_datetime_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def roles(self,) -> Optional[List[str]]:
        """
        Gets the roles property value. The roles for that user. This property only contains additional qualifiers when relevant - for example, if the member has owner privileges, the roles property contains owner as one of the values. Similarly, if the member is a guest, the roles property contains guest as one of the values. A basic member should not have any values specified in the roles property.
        Returns: Optional[List[str]]
        """
        return self._roles
    
    @roles.setter
    def roles(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the roles property value. The roles for that user. This property only contains additional qualifiers when relevant - for example, if the member has owner privileges, the roles property contains owner as one of the values. Similarly, if the member is a guest, the roles property contains guest as one of the values. A basic member should not have any values specified in the roles property.
        Args:
            value: Value to set for the roles property.
        """
        self._roles = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_datetime_value("visibleHistoryStartDateTime", self.visible_history_start_date_time)
    
    @property
    def visible_history_start_date_time(self,) -> Optional[datetime]:
        """
        Gets the visibleHistoryStartDateTime property value. The timestamp denoting how far back a conversation's history is shared with the conversation member. This property is settable only for members of a chat.
        Returns: Optional[datetime]
        """
        return self._visible_history_start_date_time
    
    @visible_history_start_date_time.setter
    def visible_history_start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the visibleHistoryStartDateTime property value. The timestamp denoting how far back a conversation's history is shared with the conversation member. This property is settable only for members of a chat.
        Args:
            value: Value to set for the visible_history_start_date_time property.
        """
        self._visible_history_start_date_time = value
    

