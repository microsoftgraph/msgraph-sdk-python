from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

chat_message_mentioned_identity_set = lazy_import('msgraph.generated.models.chat_message_mentioned_identity_set')

class ChatMessageMention(AdditionalDataHolder, Parsable):
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
        Instantiates a new chatMessageMention and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Index of an entity being mentioned in the specified chatMessage. Matches the {index} value in the corresponding <at id='{index}'> tag in the message body.
        self._id: Optional[int] = None
        # The entity (user, application, team, or channel) that was @mentioned.
        self._mentioned: Optional[chat_message_mentioned_identity_set.ChatMessageMentionedIdentitySet] = None
        # String used to represent the mention. For example, a user's display name, a team name.
        self._mention_text: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageMention:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageMention
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessageMention()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "mentioned": lambda n : setattr(self, 'mentioned', n.get_object_value(chat_message_mentioned_identity_set.ChatMessageMentionedIdentitySet)),
            "mention_text": lambda n : setattr(self, 'mention_text', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[int]:
        """
        Gets the id property value. Index of an entity being mentioned in the specified chatMessage. Matches the {index} value in the corresponding <at id='{index}'> tag in the message body.
        Returns: Optional[int]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[int] = None) -> None:
        """
        Sets the id property value. Index of an entity being mentioned in the specified chatMessage. Matches the {index} value in the corresponding <at id='{index}'> tag in the message body.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def mentioned(self,) -> Optional[chat_message_mentioned_identity_set.ChatMessageMentionedIdentitySet]:
        """
        Gets the mentioned property value. The entity (user, application, team, or channel) that was @mentioned.
        Returns: Optional[chat_message_mentioned_identity_set.ChatMessageMentionedIdentitySet]
        """
        return self._mentioned
    
    @mentioned.setter
    def mentioned(self,value: Optional[chat_message_mentioned_identity_set.ChatMessageMentionedIdentitySet] = None) -> None:
        """
        Sets the mentioned property value. The entity (user, application, team, or channel) that was @mentioned.
        Args:
            value: Value to set for the mentioned property.
        """
        self._mentioned = value
    
    @property
    def mention_text(self,) -> Optional[str]:
        """
        Gets the mentionText property value. String used to represent the mention. For example, a user's display name, a team name.
        Returns: Optional[str]
        """
        return self._mention_text
    
    @mention_text.setter
    def mention_text(self,value: Optional[str] = None) -> None:
        """
        Sets the mentionText property value. String used to represent the mention. For example, a user's display name, a team name.
        Args:
            value: Value to set for the mentionText property.
        """
        self._mention_text = value
    
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
        writer.write_int_value("id", self.id)
        writer.write_object_value("mentioned", self.mentioned)
        writer.write_str_value("mentionText", self.mention_text)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

