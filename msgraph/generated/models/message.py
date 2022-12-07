from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

attachment = lazy_import('msgraph.generated.models.attachment')
extension = lazy_import('msgraph.generated.models.extension')
followup_flag = lazy_import('msgraph.generated.models.followup_flag')
importance = lazy_import('msgraph.generated.models.importance')
inference_classification_type = lazy_import('msgraph.generated.models.inference_classification_type')
internet_message_header = lazy_import('msgraph.generated.models.internet_message_header')
item_body = lazy_import('msgraph.generated.models.item_body')
multi_value_legacy_extended_property = lazy_import('msgraph.generated.models.multi_value_legacy_extended_property')
outlook_item = lazy_import('msgraph.generated.models.outlook_item')
recipient = lazy_import('msgraph.generated.models.recipient')
single_value_legacy_extended_property = lazy_import('msgraph.generated.models.single_value_legacy_extended_property')

class Message(outlook_item.OutlookItem):
    @property
    def attachments(self,) -> Optional[List[attachment.Attachment]]:
        """
        Gets the attachments property value. The fileAttachment and itemAttachment attachments for the message.
        Returns: Optional[List[attachment.Attachment]]
        """
        return self._attachments
    
    @attachments.setter
    def attachments(self,value: Optional[List[attachment.Attachment]] = None) -> None:
        """
        Sets the attachments property value. The fileAttachment and itemAttachment attachments for the message.
        Args:
            value: Value to set for the attachments property.
        """
        self._attachments = value
    
    @property
    def bcc_recipients(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the bccRecipients property value. The Bcc: recipients for the message.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._bcc_recipients
    
    @bcc_recipients.setter
    def bcc_recipients(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the bccRecipients property value. The Bcc: recipients for the message.
        Args:
            value: Value to set for the bccRecipients property.
        """
        self._bcc_recipients = value
    
    @property
    def body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the body property value. The body of the message. It can be in HTML or text format. Find out about safe HTML in a message body.
        Returns: Optional[item_body.ItemBody]
        """
        return self._body
    
    @body.setter
    def body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the body property value. The body of the message. It can be in HTML or text format. Find out about safe HTML in a message body.
        Args:
            value: Value to set for the body property.
        """
        self._body = value
    
    @property
    def body_preview(self,) -> Optional[str]:
        """
        Gets the bodyPreview property value. The first 255 characters of the message body. It is in text format.
        Returns: Optional[str]
        """
        return self._body_preview
    
    @body_preview.setter
    def body_preview(self,value: Optional[str] = None) -> None:
        """
        Sets the bodyPreview property value. The first 255 characters of the message body. It is in text format.
        Args:
            value: Value to set for the bodyPreview property.
        """
        self._body_preview = value
    
    @property
    def cc_recipients(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the ccRecipients property value. The Cc: recipients for the message.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._cc_recipients
    
    @cc_recipients.setter
    def cc_recipients(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the ccRecipients property value. The Cc: recipients for the message.
        Args:
            value: Value to set for the ccRecipients property.
        """
        self._cc_recipients = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Message and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.message"
        # The fileAttachment and itemAttachment attachments for the message.
        self._attachments: Optional[List[attachment.Attachment]] = None
        # The Bcc: recipients for the message.
        self._bcc_recipients: Optional[List[recipient.Recipient]] = None
        # The body of the message. It can be in HTML or text format. Find out about safe HTML in a message body.
        self._body: Optional[item_body.ItemBody] = None
        # The first 255 characters of the message body. It is in text format.
        self._body_preview: Optional[str] = None
        # The Cc: recipients for the message.
        self._cc_recipients: Optional[List[recipient.Recipient]] = None
        # The ID of the conversation the email belongs to.
        self._conversation_id: Optional[str] = None
        # Indicates the position of the message within the conversation.
        self._conversation_index: Optional[bytes] = None
        # The collection of open extensions defined for the message. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # The flag value that indicates the status, start date, due date, or completion date for the message.
        self._flag: Optional[followup_flag.FollowupFlag] = None
        # The owner of the mailbox from which the message is sent. In most cases, this value is the same as the sender property, except for sharing or delegation scenarios. The value must correspond to the actual mailbox used. Find out more about setting the from and sender properties of a message.
        self._from_escaped: Optional[recipient.Recipient] = None
        # Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
        self._has_attachments: Optional[bool] = None
        # The importance property
        self._importance: Optional[importance.Importance] = None
        # The inferenceClassification property
        self._inference_classification: Optional[inference_classification_type.InferenceClassificationType] = None
        # The internetMessageHeaders property
        self._internet_message_headers: Optional[List[internet_message_header.InternetMessageHeader]] = None
        # The internetMessageId property
        self._internet_message_id: Optional[str] = None
        # The isDeliveryReceiptRequested property
        self._is_delivery_receipt_requested: Optional[bool] = None
        # The isDraft property
        self._is_draft: Optional[bool] = None
        # The isRead property
        self._is_read: Optional[bool] = None
        # The isReadReceiptRequested property
        self._is_read_receipt_requested: Optional[bool] = None
        # The collection of multi-value extended properties defined for the message. Nullable.
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        # The parentFolderId property
        self._parent_folder_id: Optional[str] = None
        # The receivedDateTime property
        self._received_date_time: Optional[datetime] = None
        # The replyTo property
        self._reply_to: Optional[List[recipient.Recipient]] = None
        # The sender property
        self._sender: Optional[recipient.Recipient] = None
        # The sentDateTime property
        self._sent_date_time: Optional[datetime] = None
        # The collection of single-value extended properties defined for the message. Nullable.
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
        # The subject property
        self._subject: Optional[str] = None
        # The toRecipients property
        self._to_recipients: Optional[List[recipient.Recipient]] = None
        # The uniqueBody property
        self._unique_body: Optional[item_body.ItemBody] = None
        # The webLink property
        self._web_link: Optional[str] = None
    
    @property
    def conversation_id(self,) -> Optional[str]:
        """
        Gets the conversationId property value. The ID of the conversation the email belongs to.
        Returns: Optional[str]
        """
        return self._conversation_id
    
    @conversation_id.setter
    def conversation_id(self,value: Optional[str] = None) -> None:
        """
        Sets the conversationId property value. The ID of the conversation the email belongs to.
        Args:
            value: Value to set for the conversationId property.
        """
        self._conversation_id = value
    
    @property
    def conversation_index(self,) -> Optional[bytes]:
        """
        Gets the conversationIndex property value. Indicates the position of the message within the conversation.
        Returns: Optional[bytes]
        """
        return self._conversation_index
    
    @conversation_index.setter
    def conversation_index(self,value: Optional[bytes] = None) -> None:
        """
        Sets the conversationIndex property value. Indicates the position of the message within the conversation.
        Args:
            value: Value to set for the conversationIndex property.
        """
        self._conversation_index = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Message:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Message
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Message()
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the message. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the message. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    @property
    def flag(self,) -> Optional[followup_flag.FollowupFlag]:
        """
        Gets the flag property value. The flag value that indicates the status, start date, due date, or completion date for the message.
        Returns: Optional[followup_flag.FollowupFlag]
        """
        return self._flag
    
    @flag.setter
    def flag(self,value: Optional[followup_flag.FollowupFlag] = None) -> None:
        """
        Sets the flag property value. The flag value that indicates the status, start date, due date, or completion date for the message.
        Args:
            value: Value to set for the flag property.
        """
        self._flag = value
    
    @property
    def from_escaped(self,) -> Optional[recipient.Recipient]:
        """
        Gets the from property value. The owner of the mailbox from which the message is sent. In most cases, this value is the same as the sender property, except for sharing or delegation scenarios. The value must correspond to the actual mailbox used. Find out more about setting the from and sender properties of a message.
        Returns: Optional[recipient.Recipient]
        """
        return self._from_escaped
    
    @from_escaped.setter
    def from_escaped(self,value: Optional[recipient.Recipient] = None) -> None:
        """
        Sets the from property value. The owner of the mailbox from which the message is sent. In most cases, this value is the same as the sender property, except for sharing or delegation scenarios. The value must correspond to the actual mailbox used. Find out more about setting the from and sender properties of a message.
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
            "bcc_recipients": lambda n : setattr(self, 'bcc_recipients', n.get_collection_of_object_values(recipient.Recipient)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(item_body.ItemBody)),
            "body_preview": lambda n : setattr(self, 'body_preview', n.get_str_value()),
            "cc_recipients": lambda n : setattr(self, 'cc_recipients', n.get_collection_of_object_values(recipient.Recipient)),
            "conversation_id": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "conversation_index": lambda n : setattr(self, 'conversation_index', n.get_bytes_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "flag": lambda n : setattr(self, 'flag', n.get_object_value(followup_flag.FollowupFlag)),
            "from": lambda n : setattr(self, 'from_escaped', n.get_object_value(recipient.Recipient)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(importance.Importance)),
            "inference_classification": lambda n : setattr(self, 'inference_classification', n.get_enum_value(inference_classification_type.InferenceClassificationType)),
            "internet_message_headers": lambda n : setattr(self, 'internet_message_headers', n.get_collection_of_object_values(internet_message_header.InternetMessageHeader)),
            "internet_message_id": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "is_delivery_receipt_requested": lambda n : setattr(self, 'is_delivery_receipt_requested', n.get_bool_value()),
            "is_draft": lambda n : setattr(self, 'is_draft', n.get_bool_value()),
            "is_read": lambda n : setattr(self, 'is_read', n.get_bool_value()),
            "is_read_receipt_requested": lambda n : setattr(self, 'is_read_receipt_requested', n.get_bool_value()),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "parent_folder_id": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "received_date_time": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "reply_to": lambda n : setattr(self, 'reply_to', n.get_collection_of_object_values(recipient.Recipient)),
            "sender": lambda n : setattr(self, 'sender', n.get_object_value(recipient.Recipient)),
            "sent_date_time": lambda n : setattr(self, 'sent_date_time', n.get_datetime_value()),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "to_recipients": lambda n : setattr(self, 'to_recipients', n.get_collection_of_object_values(recipient.Recipient)),
            "unique_body": lambda n : setattr(self, 'unique_body', n.get_object_value(item_body.ItemBody)),
            "web_link": lambda n : setattr(self, 'web_link', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def importance(self,) -> Optional[importance.Importance]:
        """
        Gets the importance property value. The importance property
        Returns: Optional[importance.Importance]
        """
        return self._importance
    
    @importance.setter
    def importance(self,value: Optional[importance.Importance] = None) -> None:
        """
        Sets the importance property value. The importance property
        Args:
            value: Value to set for the importance property.
        """
        self._importance = value
    
    @property
    def inference_classification(self,) -> Optional[inference_classification_type.InferenceClassificationType]:
        """
        Gets the inferenceClassification property value. The inferenceClassification property
        Returns: Optional[inference_classification_type.InferenceClassificationType]
        """
        return self._inference_classification
    
    @inference_classification.setter
    def inference_classification(self,value: Optional[inference_classification_type.InferenceClassificationType] = None) -> None:
        """
        Sets the inferenceClassification property value. The inferenceClassification property
        Args:
            value: Value to set for the inferenceClassification property.
        """
        self._inference_classification = value
    
    @property
    def internet_message_headers(self,) -> Optional[List[internet_message_header.InternetMessageHeader]]:
        """
        Gets the internetMessageHeaders property value. The internetMessageHeaders property
        Returns: Optional[List[internet_message_header.InternetMessageHeader]]
        """
        return self._internet_message_headers
    
    @internet_message_headers.setter
    def internet_message_headers(self,value: Optional[List[internet_message_header.InternetMessageHeader]] = None) -> None:
        """
        Sets the internetMessageHeaders property value. The internetMessageHeaders property
        Args:
            value: Value to set for the internetMessageHeaders property.
        """
        self._internet_message_headers = value
    
    @property
    def internet_message_id(self,) -> Optional[str]:
        """
        Gets the internetMessageId property value. The internetMessageId property
        Returns: Optional[str]
        """
        return self._internet_message_id
    
    @internet_message_id.setter
    def internet_message_id(self,value: Optional[str] = None) -> None:
        """
        Sets the internetMessageId property value. The internetMessageId property
        Args:
            value: Value to set for the internetMessageId property.
        """
        self._internet_message_id = value
    
    @property
    def is_delivery_receipt_requested(self,) -> Optional[bool]:
        """
        Gets the isDeliveryReceiptRequested property value. The isDeliveryReceiptRequested property
        Returns: Optional[bool]
        """
        return self._is_delivery_receipt_requested
    
    @is_delivery_receipt_requested.setter
    def is_delivery_receipt_requested(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDeliveryReceiptRequested property value. The isDeliveryReceiptRequested property
        Args:
            value: Value to set for the isDeliveryReceiptRequested property.
        """
        self._is_delivery_receipt_requested = value
    
    @property
    def is_draft(self,) -> Optional[bool]:
        """
        Gets the isDraft property value. The isDraft property
        Returns: Optional[bool]
        """
        return self._is_draft
    
    @is_draft.setter
    def is_draft(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDraft property value. The isDraft property
        Args:
            value: Value to set for the isDraft property.
        """
        self._is_draft = value
    
    @property
    def is_read(self,) -> Optional[bool]:
        """
        Gets the isRead property value. The isRead property
        Returns: Optional[bool]
        """
        return self._is_read
    
    @is_read.setter
    def is_read(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRead property value. The isRead property
        Args:
            value: Value to set for the isRead property.
        """
        self._is_read = value
    
    @property
    def is_read_receipt_requested(self,) -> Optional[bool]:
        """
        Gets the isReadReceiptRequested property value. The isReadReceiptRequested property
        Returns: Optional[bool]
        """
        return self._is_read_receipt_requested
    
    @is_read_receipt_requested.setter
    def is_read_receipt_requested(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReadReceiptRequested property value. The isReadReceiptRequested property
        Args:
            value: Value to set for the isReadReceiptRequested property.
        """
        self._is_read_receipt_requested = value
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the message. Nullable.
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the message. Nullable.
        Args:
            value: Value to set for the multiValueExtendedProperties property.
        """
        self._multi_value_extended_properties = value
    
    @property
    def parent_folder_id(self,) -> Optional[str]:
        """
        Gets the parentFolderId property value. The parentFolderId property
        Returns: Optional[str]
        """
        return self._parent_folder_id
    
    @parent_folder_id.setter
    def parent_folder_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentFolderId property value. The parentFolderId property
        Args:
            value: Value to set for the parentFolderId property.
        """
        self._parent_folder_id = value
    
    @property
    def received_date_time(self,) -> Optional[datetime]:
        """
        Gets the receivedDateTime property value. The receivedDateTime property
        Returns: Optional[datetime]
        """
        return self._received_date_time
    
    @received_date_time.setter
    def received_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the receivedDateTime property value. The receivedDateTime property
        Args:
            value: Value to set for the receivedDateTime property.
        """
        self._received_date_time = value
    
    @property
    def reply_to(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the replyTo property value. The replyTo property
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._reply_to
    
    @reply_to.setter
    def reply_to(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the replyTo property value. The replyTo property
        Args:
            value: Value to set for the replyTo property.
        """
        self._reply_to = value
    
    @property
    def sender(self,) -> Optional[recipient.Recipient]:
        """
        Gets the sender property value. The sender property
        Returns: Optional[recipient.Recipient]
        """
        return self._sender
    
    @sender.setter
    def sender(self,value: Optional[recipient.Recipient] = None) -> None:
        """
        Sets the sender property value. The sender property
        Args:
            value: Value to set for the sender property.
        """
        self._sender = value
    
    @property
    def sent_date_time(self,) -> Optional[datetime]:
        """
        Gets the sentDateTime property value. The sentDateTime property
        Returns: Optional[datetime]
        """
        return self._sent_date_time
    
    @sent_date_time.setter
    def sent_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the sentDateTime property value. The sentDateTime property
        Args:
            value: Value to set for the sentDateTime property.
        """
        self._sent_date_time = value
    
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
        writer.write_collection_of_object_values("bccRecipients", self.bcc_recipients)
        writer.write_object_value("body", self.body)
        writer.write_str_value("bodyPreview", self.body_preview)
        writer.write_collection_of_object_values("ccRecipients", self.cc_recipients)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_object_value("conversationIndex", self.conversation_index)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_object_value("flag", self.flag)
        writer.write_object_value("from", self.from_escaped)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_enum_value("importance", self.importance)
        writer.write_enum_value("inferenceClassification", self.inference_classification)
        writer.write_collection_of_object_values("internetMessageHeaders", self.internet_message_headers)
        writer.write_str_value("internetMessageId", self.internet_message_id)
        writer.write_bool_value("isDeliveryReceiptRequested", self.is_delivery_receipt_requested)
        writer.write_bool_value("isDraft", self.is_draft)
        writer.write_bool_value("isRead", self.is_read)
        writer.write_bool_value("isReadReceiptRequested", self.is_read_receipt_requested)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("parentFolderId", self.parent_folder_id)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_collection_of_object_values("replyTo", self.reply_to)
        writer.write_object_value("sender", self.sender)
        writer.write_datetime_value("sentDateTime", self.sent_date_time)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_str_value("subject", self.subject)
        writer.write_collection_of_object_values("toRecipients", self.to_recipients)
        writer.write_object_value("uniqueBody", self.unique_body)
        writer.write_str_value("webLink", self.web_link)
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the message. Nullable.
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the message. Nullable.
        Args:
            value: Value to set for the singleValueExtendedProperties property.
        """
        self._single_value_extended_properties = value
    
    @property
    def subject(self,) -> Optional[str]:
        """
        Gets the subject property value. The subject property
        Returns: Optional[str]
        """
        return self._subject
    
    @subject.setter
    def subject(self,value: Optional[str] = None) -> None:
        """
        Sets the subject property value. The subject property
        Args:
            value: Value to set for the subject property.
        """
        self._subject = value
    
    @property
    def to_recipients(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the toRecipients property value. The toRecipients property
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._to_recipients
    
    @to_recipients.setter
    def to_recipients(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the toRecipients property value. The toRecipients property
        Args:
            value: Value to set for the toRecipients property.
        """
        self._to_recipients = value
    
    @property
    def unique_body(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the uniqueBody property value. The uniqueBody property
        Returns: Optional[item_body.ItemBody]
        """
        return self._unique_body
    
    @unique_body.setter
    def unique_body(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the uniqueBody property value. The uniqueBody property
        Args:
            value: Value to set for the uniqueBody property.
        """
        self._unique_body = value
    
    @property
    def web_link(self,) -> Optional[str]:
        """
        Gets the webLink property value. The webLink property
        Returns: Optional[str]
        """
        return self._web_link
    
    @web_link.setter
    def web_link(self,value: Optional[str] = None) -> None:
        """
        Sets the webLink property value. The webLink property
        Args:
            value: Value to set for the webLink property.
        """
        self._web_link = value
    

