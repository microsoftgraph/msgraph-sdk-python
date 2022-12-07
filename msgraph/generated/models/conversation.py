from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conversation_thread = lazy_import('msgraph.generated.models.conversation_thread')
entity = lazy_import('msgraph.generated.models.entity')

class Conversation(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new conversation and sets the default values.
        """
        super().__init__()
        # Indicates whether any of the posts within this Conversation has at least one attachment. Supports $filter (eq, ne) and $search.
        self._has_attachments: Optional[bool] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._last_delivered_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A short summary from the body of the latest post in this conversation. Supports $filter (eq, ne, le, ge).
        self._preview: Optional[str] = None
        # A collection of all the conversation threads in the conversation. A navigation property. Read-only. Nullable.
        self._threads: Optional[List[conversation_thread.ConversationThread]] = None
        # The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.
        self._topic: Optional[str] = None
        # All the users that sent a message to this Conversation.
        self._unique_senders: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Conversation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Conversation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Conversation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "last_delivered_date_time": lambda n : setattr(self, 'last_delivered_date_time', n.get_datetime_value()),
            "preview": lambda n : setattr(self, 'preview', n.get_str_value()),
            "threads": lambda n : setattr(self, 'threads', n.get_collection_of_object_values(conversation_thread.ConversationThread)),
            "topic": lambda n : setattr(self, 'topic', n.get_str_value()),
            "unique_senders": lambda n : setattr(self, 'unique_senders', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. Indicates whether any of the posts within this Conversation has at least one attachment. Supports $filter (eq, ne) and $search.
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. Indicates whether any of the posts within this Conversation has at least one attachment. Supports $filter (eq, ne) and $search.
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def last_delivered_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastDeliveredDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._last_delivered_date_time
    
    @last_delivered_date_time.setter
    def last_delivered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastDeliveredDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the lastDeliveredDateTime property.
        """
        self._last_delivered_date_time = value
    
    @property
    def preview(self,) -> Optional[str]:
        """
        Gets the preview property value. A short summary from the body of the latest post in this conversation. Supports $filter (eq, ne, le, ge).
        Returns: Optional[str]
        """
        return self._preview
    
    @preview.setter
    def preview(self,value: Optional[str] = None) -> None:
        """
        Sets the preview property value. A short summary from the body of the latest post in this conversation. Supports $filter (eq, ne, le, ge).
        Args:
            value: Value to set for the preview property.
        """
        self._preview = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_datetime_value("lastDeliveredDateTime", self.last_delivered_date_time)
        writer.write_str_value("preview", self.preview)
        writer.write_collection_of_object_values("threads", self.threads)
        writer.write_str_value("topic", self.topic)
        writer.write_collection_of_primitive_values("uniqueSenders", self.unique_senders)
    
    @property
    def threads(self,) -> Optional[List[conversation_thread.ConversationThread]]:
        """
        Gets the threads property value. A collection of all the conversation threads in the conversation. A navigation property. Read-only. Nullable.
        Returns: Optional[List[conversation_thread.ConversationThread]]
        """
        return self._threads
    
    @threads.setter
    def threads(self,value: Optional[List[conversation_thread.ConversationThread]] = None) -> None:
        """
        Sets the threads property value. A collection of all the conversation threads in the conversation. A navigation property. Read-only. Nullable.
        Args:
            value: Value to set for the threads property.
        """
        self._threads = value
    
    @property
    def topic(self,) -> Optional[str]:
        """
        Gets the topic property value. The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.
        Returns: Optional[str]
        """
        return self._topic
    
    @topic.setter
    def topic(self,value: Optional[str] = None) -> None:
        """
        Sets the topic property value. The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated.
        Args:
            value: Value to set for the topic property.
        """
        self._topic = value
    
    @property
    def unique_senders(self,) -> Optional[List[str]]:
        """
        Gets the uniqueSenders property value. All the users that sent a message to this Conversation.
        Returns: Optional[List[str]]
        """
        return self._unique_senders
    
    @unique_senders.setter
    def unique_senders(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the uniqueSenders property value. All the users that sent a message to this Conversation.
        Args:
            value: Value to set for the uniqueSenders property.
        """
        self._unique_senders = value
    

