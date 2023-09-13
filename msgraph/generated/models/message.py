from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attachment import Attachment
    from .calendar_sharing_message import CalendarSharingMessage
    from .event_message import EventMessage
    from .event_message_request import EventMessageRequest
    from .event_message_response import EventMessageResponse
    from .extension import Extension
    from .followup_flag import FollowupFlag
    from .importance import Importance
    from .inference_classification_type import InferenceClassificationType
    from .internet_message_header import InternetMessageHeader
    from .item_body import ItemBody
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .outlook_item import OutlookItem
    from .recipient import Recipient
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .outlook_item import OutlookItem

@dataclass
class Message(OutlookItem):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.message"
    # The fileAttachment and itemAttachment attachments for the message.
    attachments: Optional[List[Attachment]] = None
    # The Bcc: recipients for the message.
    bcc_recipients: Optional[List[Recipient]] = None
    # The body of the message. It can be in HTML or text format. Find out about safe HTML in a message body.
    body: Optional[ItemBody] = None
    # The first 255 characters of the message body. It is in text format.
    body_preview: Optional[str] = None
    # The Cc: recipients for the message.
    cc_recipients: Optional[List[Recipient]] = None
    # The ID of the conversation the email belongs to.
    conversation_id: Optional[str] = None
    # Indicates the position of the message within the conversation.
    conversation_index: Optional[bytes] = None
    # The collection of open extensions defined for the message. Nullable.
    extensions: Optional[List[Extension]] = None
    # The flag value that indicates the status, start date, due date, or completion date for the message.
    flag: Optional[FollowupFlag] = None
    # The owner of the mailbox from which the message is sent. In most cases, this value is the same as the sender property, except for sharing or delegation scenarios. The value must correspond to the actual mailbox used. Find out more about setting the from and sender properties of a message.
    from_: Optional[Recipient] = None
    # Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
    has_attachments: Optional[bool] = None
    # The importance property
    importance: Optional[Importance] = None
    # The inferenceClassification property
    inference_classification: Optional[InferenceClassificationType] = None
    # The internetMessageHeaders property
    internet_message_headers: Optional[List[InternetMessageHeader]] = None
    # The internetMessageId property
    internet_message_id: Optional[str] = None
    # The isDeliveryReceiptRequested property
    is_delivery_receipt_requested: Optional[bool] = None
    # The isDraft property
    is_draft: Optional[bool] = None
    # The isRead property
    is_read: Optional[bool] = None
    # The isReadReceiptRequested property
    is_read_receipt_requested: Optional[bool] = None
    # The collection of multi-value extended properties defined for the message. Nullable.
    multi_value_extended_properties: Optional[List[MultiValueLegacyExtendedProperty]] = None
    # The parentFolderId property
    parent_folder_id: Optional[str] = None
    # The receivedDateTime property
    received_date_time: Optional[datetime.datetime] = None
    # The replyTo property
    reply_to: Optional[List[Recipient]] = None
    # The sender property
    sender: Optional[Recipient] = None
    # The sentDateTime property
    sent_date_time: Optional[datetime.datetime] = None
    # The collection of single-value extended properties defined for the message. Nullable.
    single_value_extended_properties: Optional[List[SingleValueLegacyExtendedProperty]] = None
    # The subject property
    subject: Optional[str] = None
    # The toRecipients property
    to_recipients: Optional[List[Recipient]] = None
    # The uniqueBody property
    unique_body: Optional[ItemBody] = None
    # The webLink property
    web_link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Message:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Message
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarSharingMessage".casefold():
            from .calendar_sharing_message import CalendarSharingMessage

            return CalendarSharingMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessage".casefold():
            from .event_message import EventMessage

            return EventMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageRequest".casefold():
            from .event_message_request import EventMessageRequest

            return EventMessageRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageResponse".casefold():
            from .event_message_response import EventMessageResponse

            return EventMessageResponse()
        return Message()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attachment import Attachment
        from .calendar_sharing_message import CalendarSharingMessage
        from .event_message import EventMessage
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .extension import Extension
        from .followup_flag import FollowupFlag
        from .importance import Importance
        from .inference_classification_type import InferenceClassificationType
        from .internet_message_header import InternetMessageHeader
        from .item_body import ItemBody
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .recipient import Recipient
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .attachment import Attachment
        from .calendar_sharing_message import CalendarSharingMessage
        from .event_message import EventMessage
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .extension import Extension
        from .followup_flag import FollowupFlag
        from .importance import Importance
        from .inference_classification_type import InferenceClassificationType
        from .internet_message_header import InternetMessageHeader
        from .item_body import ItemBody
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .outlook_item import OutlookItem
        from .recipient import Recipient
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: Dict[str, Callable[[Any], None]] = {
            "attachments": lambda n : setattr(self, 'attachments', n.get_collection_of_object_values(Attachment)),
            "bccRecipients": lambda n : setattr(self, 'bcc_recipients', n.get_collection_of_object_values(Recipient)),
            "body": lambda n : setattr(self, 'body', n.get_object_value(ItemBody)),
            "bodyPreview": lambda n : setattr(self, 'body_preview', n.get_str_value()),
            "ccRecipients": lambda n : setattr(self, 'cc_recipients', n.get_collection_of_object_values(Recipient)),
            "conversationId": lambda n : setattr(self, 'conversation_id', n.get_str_value()),
            "conversationIndex": lambda n : setattr(self, 'conversation_index', n.get_bytes_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "flag": lambda n : setattr(self, 'flag', n.get_object_value(FollowupFlag)),
            "from": lambda n : setattr(self, 'from_', n.get_object_value(Recipient)),
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(Importance)),
            "inferenceClassification": lambda n : setattr(self, 'inference_classification', n.get_enum_value(InferenceClassificationType)),
            "internetMessageHeaders": lambda n : setattr(self, 'internet_message_headers', n.get_collection_of_object_values(InternetMessageHeader)),
            "internetMessageId": lambda n : setattr(self, 'internet_message_id', n.get_str_value()),
            "isDeliveryReceiptRequested": lambda n : setattr(self, 'is_delivery_receipt_requested', n.get_bool_value()),
            "isDraft": lambda n : setattr(self, 'is_draft', n.get_bool_value()),
            "isRead": lambda n : setattr(self, 'is_read', n.get_bool_value()),
            "isReadReceiptRequested": lambda n : setattr(self, 'is_read_receipt_requested', n.get_bool_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "parentFolderId": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "receivedDateTime": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "replyTo": lambda n : setattr(self, 'reply_to', n.get_collection_of_object_values(Recipient)),
            "sender": lambda n : setattr(self, 'sender', n.get_object_value(Recipient)),
            "sentDateTime": lambda n : setattr(self, 'sent_date_time', n.get_datetime_value()),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "toRecipients": lambda n : setattr(self, 'to_recipients', n.get_collection_of_object_values(Recipient)),
            "uniqueBody": lambda n : setattr(self, 'unique_body', n.get_object_value(ItemBody)),
            "webLink": lambda n : setattr(self, 'web_link', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("attachments", self.attachments)
        writer.write_collection_of_object_values("bccRecipients", self.bcc_recipients)
        writer.write_object_value("body", self.body)
        writer.write_str_value("bodyPreview", self.body_preview)
        writer.write_collection_of_object_values("ccRecipients", self.cc_recipients)
        writer.write_str_value("conversationId", self.conversation_id)
        writer.write_bytes_value("conversationIndex", self.conversation_index)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_object_value("flag", self.flag)
        writer.write_object_value("from", self.from_)
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
    

