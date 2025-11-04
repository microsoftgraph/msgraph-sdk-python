from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

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
class Message(OutlookItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.message"
    # The fileAttachment and itemAttachment attachments for the message.
    attachments: Optional[list[Attachment]] = None
    # The Bcc: recipients for the message.
    bcc_recipients: Optional[list[Recipient]] = None
    # The body of the message. It can be in HTML or text format. Find out about safe HTML in a message body.
    body: Optional[ItemBody] = None
    # The first 255 characters of the message body. It is in text format.
    body_preview: Optional[str] = None
    # The Cc: recipients for the message.
    cc_recipients: Optional[list[Recipient]] = None
    # The ID of the conversation the email belongs to.
    conversation_id: Optional[str] = None
    # Indicates the position of the message within the conversation.
    conversation_index: Optional[bytes] = None
    # The collection of open extensions defined for the message. Nullable.
    extensions: Optional[list[Extension]] = None
    # Indicates the status, start date, due date, or completion date for the message.
    flag: Optional[FollowupFlag] = None
    # The owner of the mailbox from which the message is sent. In most cases, this value is the same as the sender property, except for sharing or delegation scenarios. The value must correspond to the actual mailbox used. Find out more about setting the from and sender properties of a message.
    from_: Optional[Recipient] = None
    # Indicates whether the message has attachments. This property doesn't include inline attachments, so if a message contains only inline attachments, this property is false. To verify the existence of inline attachments, parse the body property to look for a src attribute, such as <IMG src='cid:image001.jpg@01D26CD8.6C05F070'>.
    has_attachments: Optional[bool] = None
    # The importance of the message. The possible values are: low, normal, and high.
    importance: Optional[Importance] = None
    # The classification of the message for the user, based on inferred relevance or importance, or on an explicit override. The possible values are: focused or other.
    inference_classification: Optional[InferenceClassificationType] = None
    # A collection of message headers defined by RFC5322. The set includes message headers indicating the network path taken by a message from the sender to the recipient. It can also contain custom message headers that hold app data for the message.  Returned only on applying a $select query option. Read-only.
    internet_message_headers: Optional[list[InternetMessageHeader]] = None
    # The message ID in the format specified by RFC2822.
    internet_message_id: Optional[str] = None
    # Indicates whether a read receipt is requested for the message.
    is_delivery_receipt_requested: Optional[bool] = None
    # Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet.
    is_draft: Optional[bool] = None
    # Indicates whether the message has been read.
    is_read: Optional[bool] = None
    # Indicates whether a read receipt is requested for the message.
    is_read_receipt_requested: Optional[bool] = None
    # The collection of multi-value extended properties defined for the message. Nullable.
    multi_value_extended_properties: Optional[list[MultiValueLegacyExtendedProperty]] = None
    # The unique identifier for the message's parent mailFolder.
    parent_folder_id: Optional[str] = None
    # The date and time the message was received.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    received_date_time: Optional[datetime.datetime] = None
    # The email addresses to use when replying.
    reply_to: Optional[list[Recipient]] = None
    # The account that is used to generate the message. In most cases, this value is the same as the from property. You can set this property to a different value when sending a message from a shared mailbox, for a shared calendar, or as a delegate. In any case, the value must correspond to the actual mailbox used. Find out more about setting the from and sender properties of a message.
    sender: Optional[Recipient] = None
    # The date and time the message was sent.  The date and time information uses ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    sent_date_time: Optional[datetime.datetime] = None
    # The collection of single-value extended properties defined for the message. Nullable.
    single_value_extended_properties: Optional[list[SingleValueLegacyExtendedProperty]] = None
    # The subject of the message.
    subject: Optional[str] = None
    # The To: recipients for the message.
    to_recipients: Optional[list[Recipient]] = None
    # The part of the body of the message that is unique to the current message. uniqueBody is not returned by default but can be retrieved for a given message by use of the ?$select=uniqueBody query. It can be in HTML or text format.
    unique_body: Optional[ItemBody] = None
    # The URL to open the message in Outlook on the web.You can append an ispopout argument to the end of the URL to change how the message is displayed. If ispopout is not present or if it is set to 1, then the message is shown in a popout window. If ispopout is set to 0, the browser shows the message in the Outlook on the web review pane.The message opens in the browser if you are signed in to your mailbox via Outlook on the web. You are prompted to sign in if you are not already signed in with the browser.This URL cannot be accessed from within an iFrame.NOTE: When using this URL to access a message from a mailbox with delegate permissions, both the signed-in user and the target mailbox must be in the same database region. For example, an error is returned when a user with a mailbox in the EUR (Europe) region attempts to access messages from a mailbox in the NAM (North America) region.
    web_link: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Message:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Message
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
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
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
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

        fields: dict[str, Callable[[Any], None]] = {
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
        if writer is None:
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
    

