from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import aad_user_notification_recipient, channel_members_notification_recipient, chat_members_notification_recipient, team_members_notification_recipient

@dataclass
class TeamworkNotificationRecipient(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkNotificationRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkNotificationRecipient
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aadUserNotificationRecipient".casefold():
            from . import aad_user_notification_recipient

            return aad_user_notification_recipient.AadUserNotificationRecipient()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channelMembersNotificationRecipient".casefold():
            from . import channel_members_notification_recipient

            return channel_members_notification_recipient.ChannelMembersNotificationRecipient()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMembersNotificationRecipient".casefold():
            from . import chat_members_notification_recipient

            return chat_members_notification_recipient.ChatMembersNotificationRecipient()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamMembersNotificationRecipient".casefold():
            from . import team_members_notification_recipient

            return team_members_notification_recipient.TeamMembersNotificationRecipient()
        return TeamworkNotificationRecipient()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import aad_user_notification_recipient, channel_members_notification_recipient, chat_members_notification_recipient, team_members_notification_recipient

        from . import aad_user_notification_recipient, channel_members_notification_recipient, chat_members_notification_recipient, team_members_notification_recipient

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

