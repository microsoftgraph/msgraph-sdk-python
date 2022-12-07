from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

chat_message_reaction_identity_set = lazy_import('msgraph.generated.models.chat_message_reaction_identity_set')

class ChatMessageReaction(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new chatMessageReaction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._created_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Supported values are like, angry, sad, laugh, heart, surprised.
        self._reaction_type: Optional[str] = None
        # The user property
        self._user: Optional[chat_message_reaction_identity_set.ChatMessageReactionIdentitySet] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageReaction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageReaction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessageReaction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reaction_type": lambda n : setattr(self, 'reaction_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(chat_message_reaction_identity_set.ChatMessageReactionIdentitySet)),
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
    
    @property
    def reaction_type(self,) -> Optional[str]:
        """
        Gets the reactionType property value. Supported values are like, angry, sad, laugh, heart, surprised.
        Returns: Optional[str]
        """
        return self._reaction_type
    
    @reaction_type.setter
    def reaction_type(self,value: Optional[str] = None) -> None:
        """
        Sets the reactionType property value. Supported values are like, angry, sad, laugh, heart, surprised.
        Args:
            value: Value to set for the reactionType property.
        """
        self._reaction_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("reactionType", self.reaction_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user(self,) -> Optional[chat_message_reaction_identity_set.ChatMessageReactionIdentitySet]:
        """
        Gets the user property value. The user property
        Returns: Optional[chat_message_reaction_identity_set.ChatMessageReactionIdentitySet]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[chat_message_reaction_identity_set.ChatMessageReactionIdentitySet] = None) -> None:
        """
        Sets the user property value. The user property
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    

