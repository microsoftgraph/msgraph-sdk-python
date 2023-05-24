from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import chat_message_actions, chat_message_reaction

class ChatMessageHistoryItem(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new chatMessageHistoryItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The actions property
        self._actions: Optional[chat_message_actions.ChatMessageActions] = None
        # The date and time when the message was modified.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The reaction in the modified message.
        self._reaction: Optional[chat_message_reaction.ChatMessageReaction] = None
    
    @property
    def actions(self,) -> Optional[chat_message_actions.ChatMessageActions]:
        """
        Gets the actions property value. The actions property
        Returns: Optional[chat_message_actions.ChatMessageActions]
        """
        return self._actions
    
    @actions.setter
    def actions(self,value: Optional[chat_message_actions.ChatMessageActions] = None) -> None:
        """
        Sets the actions property value. The actions property
        Args:
            value: Value to set for the actions property.
        """
        self._actions = value
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageHistoryItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageHistoryItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessageHistoryItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import chat_message_actions, chat_message_reaction

        fields: Dict[str, Callable[[Any], None]] = {
            "actions": lambda n : setattr(self, 'actions', n.get_enum_value(chat_message_actions.ChatMessageActions)),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "reaction": lambda n : setattr(self, 'reaction', n.get_object_value(chat_message_reaction.ChatMessageReaction)),
        }
        return fields
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The date and time when the message was modified.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The date and time when the message was modified.
        Args:
            value: Value to set for the modified_date_time property.
        """
        self._modified_date_time = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def reaction(self,) -> Optional[chat_message_reaction.ChatMessageReaction]:
        """
        Gets the reaction property value. The reaction in the modified message.
        Returns: Optional[chat_message_reaction.ChatMessageReaction]
        """
        return self._reaction
    
    @reaction.setter
    def reaction(self,value: Optional[chat_message_reaction.ChatMessageReaction] = None) -> None:
        """
        Sets the reaction property value. The reaction in the modified message.
        Args:
            value: Value to set for the reaction property.
        """
        self._reaction = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("actions", self.actions)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("reaction", self.reaction)
        writer.write_additional_data_value(self.additional_data)
    

