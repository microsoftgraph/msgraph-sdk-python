from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
post = lazy_import('msgraph.generated.models.post')
recipient = lazy_import('msgraph.generated.models.recipient')

class ConversationThread(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def cc_recipients(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the ccRecipients property value. The Cc: recipients for the thread. Returned only on $select.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._cc_recipients
    
    @cc_recipients.setter
    def cc_recipients(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the ccRecipients property value. The Cc: recipients for the thread. Returned only on $select.
        Args:
            value: Value to set for the ccRecipients property.
        """
        self._cc_recipients = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new conversationThread and sets the default values.
        """
        super().__init__()
        # The Cc: recipients for the thread. Returned only on $select.
        self._cc_recipients: Optional[List[recipient.Recipient]] = None
        # Indicates whether any of the posts within this thread has at least one attachment. Returned by default.
        self._has_attachments: Optional[bool] = None
        # Indicates if the thread is locked. Returned by default.
        self._is_locked: Optional[bool] = None
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.Returned by default.
        self._last_delivered_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The posts property
        self._posts: Optional[List[post.Post]] = None
        # A short summary from the body of the latest post in this conversation. Returned by default.
        self._preview: Optional[str] = None
        # The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated. Returned by default.
        self._topic: Optional[str] = None
        # The To: recipients for the thread. Returned only on $select.
        self._to_recipients: Optional[List[recipient.Recipient]] = None
        # All the users that sent a message to this thread. Returned by default.
        self._unique_senders: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConversationThread:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConversationThread
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConversationThread()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "cc_recipients": lambda n : setattr(self, 'cc_recipients', n.get_collection_of_object_values(recipient.Recipient)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "is_locked": lambda n : setattr(self, 'is_locked', n.get_bool_value()),
            "last_delivered_date_time": lambda n : setattr(self, 'last_delivered_date_time', n.get_datetime_value()),
            "posts": lambda n : setattr(self, 'posts', n.get_collection_of_object_values(post.Post)),
            "preview": lambda n : setattr(self, 'preview', n.get_str_value()),
            "topic": lambda n : setattr(self, 'topic', n.get_str_value()),
            "to_recipients": lambda n : setattr(self, 'to_recipients', n.get_collection_of_object_values(recipient.Recipient)),
            "unique_senders": lambda n : setattr(self, 'unique_senders', n.get_collection_of_primitive_values(str)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. Indicates whether any of the posts within this thread has at least one attachment. Returned by default.
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. Indicates whether any of the posts within this thread has at least one attachment. Returned by default.
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def is_locked(self,) -> Optional[bool]:
        """
        Gets the isLocked property value. Indicates if the thread is locked. Returned by default.
        Returns: Optional[bool]
        """
        return self._is_locked
    
    @is_locked.setter
    def is_locked(self,value: Optional[bool] = None) -> None:
        """
        Sets the isLocked property value. Indicates if the thread is locked. Returned by default.
        Args:
            value: Value to set for the isLocked property.
        """
        self._is_locked = value
    
    @property
    def last_delivered_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastDeliveredDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.Returned by default.
        Returns: Optional[datetime]
        """
        return self._last_delivered_date_time
    
    @last_delivered_date_time.setter
    def last_delivered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastDeliveredDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.Returned by default.
        Args:
            value: Value to set for the lastDeliveredDateTime property.
        """
        self._last_delivered_date_time = value
    
    @property
    def posts(self,) -> Optional[List[post.Post]]:
        """
        Gets the posts property value. The posts property
        Returns: Optional[List[post.Post]]
        """
        return self._posts
    
    @posts.setter
    def posts(self,value: Optional[List[post.Post]] = None) -> None:
        """
        Sets the posts property value. The posts property
        Args:
            value: Value to set for the posts property.
        """
        self._posts = value
    
    @property
    def preview(self,) -> Optional[str]:
        """
        Gets the preview property value. A short summary from the body of the latest post in this conversation. Returned by default.
        Returns: Optional[str]
        """
        return self._preview
    
    @preview.setter
    def preview(self,value: Optional[str] = None) -> None:
        """
        Sets the preview property value. A short summary from the body of the latest post in this conversation. Returned by default.
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
        writer.write_collection_of_object_values("ccRecipients", self.cc_recipients)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_bool_value("isLocked", self.is_locked)
        writer.write_datetime_value("lastDeliveredDateTime", self.last_delivered_date_time)
        writer.write_collection_of_object_values("posts", self.posts)
        writer.write_str_value("preview", self.preview)
        writer.write_str_value("topic", self.topic)
        writer.write_collection_of_object_values("toRecipients", self.to_recipients)
        writer.write_collection_of_primitive_values("uniqueSenders", self.unique_senders)
    
    @property
    def topic(self,) -> Optional[str]:
        """
        Gets the topic property value. The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated. Returned by default.
        Returns: Optional[str]
        """
        return self._topic
    
    @topic.setter
    def topic(self,value: Optional[str] = None) -> None:
        """
        Sets the topic property value. The topic of the conversation. This property can be set when the conversation is created, but it cannot be updated. Returned by default.
        Args:
            value: Value to set for the topic property.
        """
        self._topic = value
    
    @property
    def to_recipients(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the toRecipients property value. The To: recipients for the thread. Returned only on $select.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._to_recipients
    
    @to_recipients.setter
    def to_recipients(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the toRecipients property value. The To: recipients for the thread. Returned only on $select.
        Args:
            value: Value to set for the toRecipients property.
        """
        self._to_recipients = value
    
    @property
    def unique_senders(self,) -> Optional[List[str]]:
        """
        Gets the uniqueSenders property value. All the users that sent a message to this thread. Returned by default.
        Returns: Optional[List[str]]
        """
        return self._unique_senders
    
    @unique_senders.setter
    def unique_senders(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the uniqueSenders property value. All the users that sent a message to this thread. Returned by default.
        Args:
            value: Value to set for the uniqueSenders property.
        """
        self._unique_senders = value
    

