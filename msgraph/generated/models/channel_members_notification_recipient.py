from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

teamwork_notification_recipient = lazy_import('msgraph.generated.models.teamwork_notification_recipient')

class ChannelMembersNotificationRecipient(teamwork_notification_recipient.TeamworkNotificationRecipient):
    @property
    def channel_id(self,) -> Optional[str]:
        """
        Gets the channelId property value. The unique identifier for the channel whose members should receive the notification.
        Returns: Optional[str]
        """
        return self._channel_id
    
    @channel_id.setter
    def channel_id(self,value: Optional[str] = None) -> None:
        """
        Sets the channelId property value. The unique identifier for the channel whose members should receive the notification.
        Args:
            value: Value to set for the channelId property.
        """
        self._channel_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ChannelMembersNotificationRecipient and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.channelMembersNotificationRecipient"
        # The unique identifier for the channel whose members should receive the notification.
        self._channel_id: Optional[str] = None
        # The unique identifier for the team under which the channel resides.
        self._team_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChannelMembersNotificationRecipient:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChannelMembersNotificationRecipient
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChannelMembersNotificationRecipient()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "channel_id": lambda n : setattr(self, 'channel_id', n.get_str_value()),
            "team_id": lambda n : setattr(self, 'team_id', n.get_str_value()),
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
        writer.write_str_value("channelId", self.channel_id)
        writer.write_str_value("teamId", self.team_id)
    
    @property
    def team_id(self,) -> Optional[str]:
        """
        Gets the teamId property value. The unique identifier for the team under which the channel resides.
        Returns: Optional[str]
        """
        return self._team_id
    
    @team_id.setter
    def team_id(self,value: Optional[str] = None) -> None:
        """
        Sets the teamId property value. The unique identifier for the team under which the channel resides.
        Args:
            value: Value to set for the teamId property.
        """
        self._team_id = value
    

