from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

chat_message_from_identity_set = lazy_import('msgraph.generated.models.chat_message_from_identity_set')
chat_message_type = lazy_import('msgraph.generated.models.chat_message_type')
entity = lazy_import('msgraph.generated.models.entity')
event_message_detail = lazy_import('msgraph.generated.models.event_message_detail')
item_body = lazy_import('msgraph.generated.models.item_body')

class ChatMessageInfo(entity.Entity):
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. Body of the chatMessage. This will still contain markers for @mentions and attachments even though the object does not return @mentions and attachments.
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. Body of the chatMessage. This will still contain markers for @mentions and attachments even though the object does not return @mentions and attachments.
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new chatMessageInfo and sets the default values.
        """
        super().__init__()
        # Body of the chatMessage. This will still contain markers for @mentions and attachments even though the object does not return @mentions and attachments.
        self._body: Optional[item_body.ItemBody] = None
        # Date time object representing the time at which message was created.
        self._created_date_time: Optional[datetime] = None
        # Read-only.  If present, represents details of an event that happened in a chat, a channel, or a team, for example, members were added, and so on. For event messages, the messageType property will be set to systemEventMessage.
        self._event_detail: Optional[event_message_detail.EventMessageDetail] = None
        # Information about the sender of the message.
        self._from_escaped: Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet] = None
        # If set to true, the original message has been deleted.
        self._is_deleted: Optional[bool] = None
        # The messageType property
        self._message_type: Optional[chat_message_type.ChatMessageType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date time object representing the time at which message was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date time object representing the time at which message was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessageInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessageInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessageInfo()
    
    @property
    def event_detail(self,) -> Optional[event_message_detail.EventMessageDetail]:
        """
        Gets the eventDetail property value. Read-only.  If present, represents details of an event that happened in a chat, a channel, or a team, for example, members were added, and so on. For event messages, the messageType property will be set to systemEventMessage.
        Returns: Optional[event_message_detail.EventMessageDetail]
        """
        return self._event_detail
    
    @event_detail.setter
    def event_detail(self,value: Optional[event_message_detail.EventMessageDetail] = None) -> None:
        """
        Sets the eventDetail property value. Read-only.  If present, represents details of an event that happened in a chat, a channel, or a team, for example, members were added, and so on. For event messages, the messageType property will be set to systemEventMessage.
        Args:
            value: Value to set for the eventDetail property.
        """
        self._event_detail = value
    
    @property
    def from_escaped(self,) -> Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet]:
        """
        Gets the from property value. Information about the sender of the message.
        Returns: Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet]
        """
        return self._from_escaped
    
    @from_escaped.setter
    def from_escaped(self,value: Optional[chat_message_from_identity_set.ChatMessageFromIdentitySet] = None) -> None:
        """
        Sets the from property value. Information about the sender of the message.
        Args:
            value: Value to set for the from_escaped property.
        """
        self._from_escaped = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "event_detail": lambda n : setattr(self, 'event_detail', n.get_object_value(event_message_detail.EventMessageDetail)),
            "from": lambda n : setattr(self, 'from_escaped', n.get_object_value(chat_message_from_identity_set.ChatMessageFromIdentitySet)),
            "is_deleted": lambda n : setattr(self, 'is_deleted', n.get_bool_value()),
            "message_type": lambda n : setattr(self, 'message_type', n.get_enum_value(chat_message_type.ChatMessageType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_deleted(self,) -> Optional[bool]:
        """
        Gets the isDeleted property value. If set to true, the original message has been deleted.
        Returns: Optional[bool]
        """
        return self._is_deleted
    
    @is_deleted.setter
    def is_deleted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeleted property value. If set to true, the original message has been deleted.
        Args:
            value: Value to set for the isDeleted property.
        """
        self._is_deleted = value
    
    @property
    def message_type(self,) -> Optional[chat_message_type.ChatMessageType]:
        """
        Gets the messageType property value. The messageType property
        Returns: Optional[chat_message_type.ChatMessageType]
        """
        return self._message_type
    
    @message_type.setter
    def message_type(self,value: Optional[chat_message_type.ChatMessageType] = None) -> None:
        """
        Sets the messageType property value. The messageType property
        Args:
            value: Value to set for the messageType property.
        """
        self._message_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("body", self.body)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("eventDetail", self.event_detail)
        writer.write_object_value("from", self.from_escaped)
        writer.write_bool_value("isDeleted", self.is_deleted)
        writer.write_enum_value("messageType", self.message_type)
    

