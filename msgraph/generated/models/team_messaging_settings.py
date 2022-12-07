from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamMessagingSettings(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def allow_channel_mentions(self,) -> Optional[bool]:
        """
        Gets the allowChannelMentions property value. If set to true, @channel mentions are allowed.
        Returns: Optional[bool]
        """
        return self._allow_channel_mentions
    
    @allow_channel_mentions.setter
    def allow_channel_mentions(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowChannelMentions property value. If set to true, @channel mentions are allowed.
        Args:
            value: Value to set for the allowChannelMentions property.
        """
        self._allow_channel_mentions = value
    
    @property
    def allow_owner_delete_messages(self,) -> Optional[bool]:
        """
        Gets the allowOwnerDeleteMessages property value. If set to true, owners can delete any message.
        Returns: Optional[bool]
        """
        return self._allow_owner_delete_messages
    
    @allow_owner_delete_messages.setter
    def allow_owner_delete_messages(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowOwnerDeleteMessages property value. If set to true, owners can delete any message.
        Args:
            value: Value to set for the allowOwnerDeleteMessages property.
        """
        self._allow_owner_delete_messages = value
    
    @property
    def allow_team_mentions(self,) -> Optional[bool]:
        """
        Gets the allowTeamMentions property value. If set to true, @team mentions are allowed.
        Returns: Optional[bool]
        """
        return self._allow_team_mentions
    
    @allow_team_mentions.setter
    def allow_team_mentions(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowTeamMentions property value. If set to true, @team mentions are allowed.
        Args:
            value: Value to set for the allowTeamMentions property.
        """
        self._allow_team_mentions = value
    
    @property
    def allow_user_delete_messages(self,) -> Optional[bool]:
        """
        Gets the allowUserDeleteMessages property value. If set to true, users can delete their messages.
        Returns: Optional[bool]
        """
        return self._allow_user_delete_messages
    
    @allow_user_delete_messages.setter
    def allow_user_delete_messages(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowUserDeleteMessages property value. If set to true, users can delete their messages.
        Args:
            value: Value to set for the allowUserDeleteMessages property.
        """
        self._allow_user_delete_messages = value
    
    @property
    def allow_user_edit_messages(self,) -> Optional[bool]:
        """
        Gets the allowUserEditMessages property value. If set to true, users can edit their messages.
        Returns: Optional[bool]
        """
        return self._allow_user_edit_messages
    
    @allow_user_edit_messages.setter
    def allow_user_edit_messages(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowUserEditMessages property value. If set to true, users can edit their messages.
        Args:
            value: Value to set for the allowUserEditMessages property.
        """
        self._allow_user_edit_messages = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamMessagingSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If set to true, @channel mentions are allowed.
        self._allow_channel_mentions: Optional[bool] = None
        # If set to true, owners can delete any message.
        self._allow_owner_delete_messages: Optional[bool] = None
        # If set to true, @team mentions are allowed.
        self._allow_team_mentions: Optional[bool] = None
        # If set to true, users can delete their messages.
        self._allow_user_delete_messages: Optional[bool] = None
        # If set to true, users can edit their messages.
        self._allow_user_edit_messages: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamMessagingSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamMessagingSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamMessagingSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_channel_mentions": lambda n : setattr(self, 'allow_channel_mentions', n.get_bool_value()),
            "allow_owner_delete_messages": lambda n : setattr(self, 'allow_owner_delete_messages', n.get_bool_value()),
            "allow_team_mentions": lambda n : setattr(self, 'allow_team_mentions', n.get_bool_value()),
            "allow_user_delete_messages": lambda n : setattr(self, 'allow_user_delete_messages', n.get_bool_value()),
            "allow_user_edit_messages": lambda n : setattr(self, 'allow_user_edit_messages', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowChannelMentions", self.allow_channel_mentions)
        writer.write_bool_value("allowOwnerDeleteMessages", self.allow_owner_delete_messages)
        writer.write_bool_value("allowTeamMentions", self.allow_team_mentions)
        writer.write_bool_value("allowUserDeleteMessages", self.allow_user_delete_messages)
        writer.write_bool_value("allowUserEditMessages", self.allow_user_edit_messages)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

