from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment = lazy_import('msgraph.generated.models.attachment')
extension = lazy_import('msgraph.generated.models.extension')
item_body = lazy_import('msgraph.generated.models.item_body')
multi_value_legacy_extended_property = lazy_import('msgraph.generated.models.multi_value_legacy_extended_property')
outlook_item = lazy_import('msgraph.generated.models.outlook_item')
recipient = lazy_import('msgraph.generated.models.recipient')
single_value_legacy_extended_property = lazy_import('msgraph.generated.models.single_value_legacy_extended_property')

class Post(outlook_item.OutlookItem):
    @property
    def attachments(self,) -> Optional[List[attachment.Attachment]]:
        """
        Gets the attachments property value. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[attachment.Attachment]]
        """
        return self._attachments
    
    @attachments.setter
    def attachments(self,value: Optional[List[attachment.Attachment]] = None) -> None:
        """
        Sets the attachments property value. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the attachments property.
        """
        self._attachments = value
    
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. The contents of the post. This is a default property. This property can be null.
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. The contents of the post. This is a default property. This property can be null.
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Post and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.post"
        # Read-only. Nullable. Supports $expand.
        self._attachments: Optional[List[attachment.Attachment]] = None
        # The contents of the post. This is a default property. This property can be null.
        self._body: Optional[item_body.ItemBody] = None
        # Unique ID of the conversation. Read-only.
        self._conversation_id: Optional[str] = None
        # Unique ID of the conversation thread. Read-only.
        self._conversation_thread_id: Optional[str] = None
        # The collection of open extensions defined for the post. Read-only. Nullable. Supports $expand.
        self._extensions: Optional[List[extension.Extension]] = None
        # The from property
        self._from_escaped: Optional[recipient.Recipient] = None
        # Indicates whether the post has at least one attachment. This is a default property.
        self._has_attachments: Optional[bool] = None
        # Read-only. Supports $expand.
        self._in_reply_to: Optional[post.Post] = None
        # The collection of multi-value extended properties defined for the post. Read-only. Nullable.
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        # Conversation participants that were added to the thread as part of this post.
        self._new_participants: Optional[List[recipient.Recipient]] = None
        # Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._received_date_time: Optional[datetime] = None
        # Contains the address of the sender. The value of Sender is assumed to be the address of the authenticated user in the case when Sender is not specified. This is a default property.
        self._sender: Optional[recipient.Recipient] = None
        # The collection of single-value extended properties defined for the post. Read-only. Nullable.
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
    
    @property
    def conversation_id(self,) -> Optional[str]:
        """
        Gets the conversationId property value. Unique ID of the conversation. Read-only.
        Returns: Optional[str]
        """
        return self._conversation_id
    
    @conversation_id.setter
    def conversation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the conversationId property value. Unique ID of the conversation. Read-only.
        Args:
            value: Value to set for the conversationId property.
        """
        self._conversation_id = value
    
    @property
    def conversation_thread_id(self,) -> Optional[str]:
        """
        Gets the conversationThreadId property value. Unique ID of the conversation thread. Read-only.
        Returns: Optional[str]
        """
        return self._conversation_thread_id
    
    @conversation_thread_id.setter
    def conversation_thread_id(self,value: Optional[str] = None) -> None:
        """
        Sets the conversationThreadId property value. Unique ID of the conversation thread. Read-only.
        Args:
            value: Value to set for the conversationThreadId property.
        """
        self._conversation_thread_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Post:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Post
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Post()
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the post. Read-only. Nullable. Supports $expand.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the post. Read-only. Nullable. Supports $expand.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    @property
    def from_escaped(self,) -> Optional[recipient.Recipient]:
        """
        Gets the from property value. The from property
        Returns: Optional[recipient.Recipient]
        """
        return self._from_escaped
    
    @from_escaped.setter
    def from_escaped(self,value: Optional[recipient.Recipient] = None) -> None:
        """
        Sets the from property value. The from property
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
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(attachment.Attachment)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "conversation_id": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "conversation_thread_id": lambda n : setattr(self, 'conversation_thread_id', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "from": lambda n : setattr(self, 'from_escaped', n.get_object_value(recipient.Recipient)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "in_reply_to": lambda n : setattr(self, 'in_reply_to', n.get_object_value(post.Post)),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "new_participants": lambda n : setattr(self, 'new_participants', n.get_collection_of_object_values(recipient.Recipient)),
            "received_date_time": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "sender": lambda n : setattr(self, 'sender', n.get_object_value(recipient.Recipient)),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. Indicates whether the post has at least one attachment. This is a default property.
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. Indicates whether the post has at least one attachment. This is a default property.
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def in_reply_to(self,) -> Optional[post.Post]:
        """
        Gets the inReplyTo property value. Read-only. Supports $expand.
        Returns: Optional[post.Post]
        """
        return self._in_reply_to
    
    @in_reply_to.setter
    def in_reply_to(self,value: Optional[post.Post] = None) -> None:
        """
        Sets the inReplyTo property value. Read-only. Supports $expand.
        Args:
            value: Value to set for the inReplyTo property.
        """
        self._in_reply_to = value
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the post. Read-only. Nullable.
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the post. Read-only. Nullable.
        Args:
            value: Value to set for the multiValueExtendedProperties property.
        """
        self._multi_value_extended_properties = value
    
    @property
    def new_participants(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the newParticipants property value. Conversation participants that were added to the thread as part of this post.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._new_participants
    
    @new_participants.setter
    def new_participants(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the newParticipants property value. Conversation participants that were added to the thread as part of this post.
        Args:
            value: Value to set for the newParticipants property.
        """
        self._new_participants = value
    
    @property
    def received_date_time(self,) -> Optional[datetime]:
        """
        Gets the receivedDateTime property value. Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._received_date_time
    
    @received_date_time.setter
    def received_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the receivedDateTime property value. Specifies when the post was received. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the receivedDateTime property.
        """
        self._received_date_time = value
    
    @property
    def sender(self,) -> Optional[recipient.Recipient]:
        """
        Gets the sender property value. Contains the address of the sender. The value of Sender is assumed to be the address of the authenticated user in the case when Sender is not specified. This is a default property.
        Returns: Optional[recipient.Recipient]
        """
        return self._sender
    
    @sender.setter
    def sender(self,value: Optional[recipient.Recipient] = None) -> None:
        """
        Sets the sender property value. Contains the address of the sender. The value of Sender is assumed to be the address of the authenticated user in the case when Sender is not specified. This is a default property.
        Args:
            value: Value to set for the sender property.
        """
        self._sender = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_object_value("body", self.body)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_str_value("conversationThreadId", self.conversation_thread_id)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_object_value("from", self.from_escaped)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_object_value("inReplyTo", self.in_reply_to)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_collection_of_object_values("newParticipants", self.new_participants)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_object_value("sender", self.sender)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the post. Read-only. Nullable.
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the post. Read-only. Nullable.
        Args:
            value: Value to set for the singleValueExtendedProperties property.
        """
        self._single_value_extended_properties = value
    

