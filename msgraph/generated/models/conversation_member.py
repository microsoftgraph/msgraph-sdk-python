from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aad_user_conversation_member import AadUserConversationMember
    from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
    from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
    from .entity import Entity
    from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
    from .phone_user_conversation_member import PhoneUserConversationMember
    from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
    from .skype_user_conversation_member import SkypeUserConversationMember

from .entity import Entity

@dataclass
class ConversationMember(Entity, Parsable):
    # The display name of the user.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The roles for that user. This property contains more qualifiers only when relevant - for example, if the member has owner privileges, the roles property contains owner as one of the values. Similarly, if the member is an in-tenant guest, the roles property contains guest as one of the values. A basic member shouldn't have any values specified in the roles property. An Out-of-tenant external member is assigned the owner role.
    roles: Optional[list[str]] = None
    # The timestamp denoting how far back a conversation's history is shared with the conversation member. This property is settable only for members of a chat.
    visible_history_start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConversationMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConversationMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aadUserConversationMember".casefold():
            from .aad_user_conversation_member import AadUserConversationMember

            return AadUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.anonymousGuestConversationMember".casefold():
            from .anonymous_guest_conversation_member import AnonymousGuestConversationMember

            return AnonymousGuestConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureCommunicationServicesUserConversationMember".casefold():
            from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember

            return AzureCommunicationServicesUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAccountUserConversationMember".casefold():
            from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember

            return MicrosoftAccountUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.phoneUserConversationMember".casefold():
            from .phone_user_conversation_member import PhoneUserConversationMember

            return PhoneUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeForBusinessUserConversationMember".casefold():
            from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember

            return SkypeForBusinessUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeUserConversationMember".casefold():
            from .skype_user_conversation_member import SkypeUserConversationMember

            return SkypeUserConversationMember()
        return ConversationMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aad_user_conversation_member import AadUserConversationMember
        from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
        from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
        from .entity import Entity
        from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
        from .phone_user_conversation_member import PhoneUserConversationMember
        from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
        from .skype_user_conversation_member import SkypeUserConversationMember

        from .aad_user_conversation_member import AadUserConversationMember
        from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
        from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
        from .entity import Entity
        from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
        from .phone_user_conversation_member import PhoneUserConversationMember
        from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
        from .skype_user_conversation_member import SkypeUserConversationMember

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "roles": lambda n : setattr(self, 'roles', n.get_collection_of_primitive_values(str)),
            "visibleHistoryStartDateTime": lambda n : setattr(self, 'visible_history_start_date_time', n.get_datetime_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("roles", self.roles)
        writer.write_datetime_value("visibleHistoryStartDateTime", self.visible_history_start_date_time)
    

