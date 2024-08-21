from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .importance import Importance
    from .message_action_flag import MessageActionFlag
    from .recipient import Recipient
    from .sensitivity import Sensitivity
    from .size_range import SizeRange

@dataclass
class MessageRulePredicates(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Represents the strings that should appear in the body of an incoming message in order for the condition or exception to apply.
    body_contains: Optional[List[str]] = None
    # Represents the strings that should appear in the body or subject of an incoming message in order for the condition or exception to apply.
    body_or_subject_contains: Optional[List[str]] = None
    # Represents the categories that an incoming message should be labeled with in order for the condition or exception to apply.
    categories: Optional[List[str]] = None
    # Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply.
    from_addresses: Optional[List[Recipient]] = None
    # Indicates whether an incoming message must have attachments in order for the condition or exception to apply.
    has_attachments: Optional[bool] = None
    # Represents the strings that appear in the headers of an incoming message in order for the condition or exception to apply.
    header_contains: Optional[List[str]] = None
    # The importance that is stamped on an incoming message in order for the condition or exception to apply: low, normal, high.
    importance: Optional[Importance] = None
    # Indicates whether an incoming message must be an approval request in order for the condition or exception to apply.
    is_approval_request: Optional[bool] = None
    # Indicates whether an incoming message must be automatically forwarded in order for the condition or exception to apply.
    is_automatic_forward: Optional[bool] = None
    # Indicates whether an incoming message must be an auto reply in order for the condition or exception to apply.
    is_automatic_reply: Optional[bool] = None
    # Indicates whether an incoming message must be encrypted in order for the condition or exception to apply.
    is_encrypted: Optional[bool] = None
    # Indicates whether an incoming message must be a meeting request in order for the condition or exception to apply.
    is_meeting_request: Optional[bool] = None
    # Indicates whether an incoming message must be a meeting response in order for the condition or exception to apply.
    is_meeting_response: Optional[bool] = None
    # Indicates whether an incoming message must be a non-delivery report in order for the condition or exception to apply.
    is_non_delivery_report: Optional[bool] = None
    # Indicates whether an incoming message must be permission controlled (RMS-protected) in order for the condition or exception to apply.
    is_permission_controlled: Optional[bool] = None
    # Indicates whether an incoming message must be a read receipt in order for the condition or exception to apply.
    is_read_receipt: Optional[bool] = None
    # Indicates whether an incoming message must be S/MIME-signed in order for the condition or exception to apply.
    is_signed: Optional[bool] = None
    # Indicates whether an incoming message must be a voice mail in order for the condition or exception to apply.
    is_voicemail: Optional[bool] = None
    # Represents the flag-for-action value that appears on an incoming message in order for the condition or exception to apply. The possible values are: any, call, doNotForward, followUp, fyi, forward, noResponseNecessary, read, reply, replyToAll, review.
    message_action_flag: Optional[MessageActionFlag] = None
    # Indicates whether the owner of the mailbox must not be a recipient of an incoming message in order for the condition or exception to apply.
    not_sent_to_me: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the strings that appear in either the toRecipients or ccRecipients properties of an incoming message in order for the condition or exception to apply.
    recipient_contains: Optional[List[str]] = None
    # Represents the strings that appear in the from property of an incoming message in order for the condition or exception to apply.
    sender_contains: Optional[List[str]] = None
    # Represents the sensitivity level that must be stamped on an incoming message in order for the condition or exception to apply. The possible values are: normal, personal, private, confidential.
    sensitivity: Optional[Sensitivity] = None
    # Indicates whether the owner of the mailbox must be in the ccRecipients property of an incoming message in order for the condition or exception to apply.
    sent_cc_me: Optional[bool] = None
    # Indicates whether the owner of the mailbox must be the only recipient in an incoming message in order for the condition or exception to apply.
    sent_only_to_me: Optional[bool] = None
    # Represents the email addresses that an incoming message must have been sent to in order for the condition or exception to apply.
    sent_to_addresses: Optional[List[Recipient]] = None
    # Indicates whether the owner of the mailbox must be in the toRecipients property of an incoming message in order for the condition or exception to apply.
    sent_to_me: Optional[bool] = None
    # Indicates whether the owner of the mailbox must be in either a toRecipients or ccRecipients property of an incoming message in order for the condition or exception to apply.
    sent_to_or_cc_me: Optional[bool] = None
    # Represents the strings that appear in the subject of an incoming message in order for the condition or exception to apply.
    subject_contains: Optional[List[str]] = None
    # Represents the minimum and maximum sizes (in kilobytes) that an incoming message must fall in between in order for the condition or exception to apply.
    within_size_range: Optional[SizeRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MessageRulePredicates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageRulePredicates
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MessageRulePredicates()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .importance import Importance
        from .message_action_flag import MessageActionFlag
        from .recipient import Recipient
        from .sensitivity import Sensitivity
        from .size_range import SizeRange

        from .importance import Importance
        from .message_action_flag import MessageActionFlag
        from .recipient import Recipient
        from .sensitivity import Sensitivity
        from .size_range import SizeRange

        fields: Dict[str, Callable[[Any], None]] = {
            "bodyContains": lambda n : setattr(self, 'body_contains', n.get_collection_of_primitive_values(str)),
            "bodyOrSubjectContains": lambda n : setattr(self, 'body_or_subject_contains', n.get_collection_of_primitive_values(str)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "fromAddresses": lambda n : setattr(self, 'from_addresses', n.get_collection_of_object_values(Recipient)),
            "hasAttachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "headerContains": lambda n : setattr(self, 'header_contains', n.get_collection_of_primitive_values(str)),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(Importance)),
            "isApprovalRequest": lambda n : setattr(self, 'is_approval_request', n.get_bool_value()),
            "isAutomaticForward": lambda n : setattr(self, 'is_automatic_forward', n.get_bool_value()),
            "isAutomaticReply": lambda n : setattr(self, 'is_automatic_reply', n.get_bool_value()),
            "isEncrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "isMeetingRequest": lambda n : setattr(self, 'is_meeting_request', n.get_bool_value()),
            "isMeetingResponse": lambda n : setattr(self, 'is_meeting_response', n.get_bool_value()),
            "isNonDeliveryReport": lambda n : setattr(self, 'is_non_delivery_report', n.get_bool_value()),
            "isPermissionControlled": lambda n : setattr(self, 'is_permission_controlled', n.get_bool_value()),
            "isReadReceipt": lambda n : setattr(self, 'is_read_receipt', n.get_bool_value()),
            "isSigned": lambda n : setattr(self, 'is_signed', n.get_bool_value()),
            "isVoicemail": lambda n : setattr(self, 'is_voicemail', n.get_bool_value()),
            "messageActionFlag": lambda n : setattr(self, 'message_action_flag', n.get_enum_value(MessageActionFlag)),
            "notSentToMe": lambda n : setattr(self, 'not_sent_to_me', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recipientContains": lambda n : setattr(self, 'recipient_contains', n.get_collection_of_primitive_values(str)),
            "senderContains": lambda n : setattr(self, 'sender_contains', n.get_collection_of_primitive_values(str)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_enum_value(Sensitivity)),
            "sentCcMe": lambda n : setattr(self, 'sent_cc_me', n.get_bool_value()),
            "sentOnlyToMe": lambda n : setattr(self, 'sent_only_to_me', n.get_bool_value()),
            "sentToAddresses": lambda n : setattr(self, 'sent_to_addresses', n.get_collection_of_object_values(Recipient)),
            "sentToMe": lambda n : setattr(self, 'sent_to_me', n.get_bool_value()),
            "sentToOrCcMe": lambda n : setattr(self, 'sent_to_or_cc_me', n.get_bool_value()),
            "subjectContains": lambda n : setattr(self, 'subject_contains', n.get_collection_of_primitive_values(str)),
            "withinSizeRange": lambda n : setattr(self, 'within_size_range', n.get_object_value(SizeRange)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("bodyContains", self.body_contains)
        writer.write_collection_of_primitive_values("bodyOrSubjectContains", self.body_or_subject_contains)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_object_values("fromAddresses", self.from_addresses)
        writer.write_bool_value("hasAttachments", self.has_attachments)
        writer.write_collection_of_primitive_values("headerContains", self.header_contains)
        writer.write_enum_value("importance", self.importance)
        writer.write_bool_value("isApprovalRequest", self.is_approval_request)
        writer.write_bool_value("isAutomaticForward", self.is_automatic_forward)
        writer.write_bool_value("isAutomaticReply", self.is_automatic_reply)
        writer.write_bool_value("isEncrypted", self.is_encrypted)
        writer.write_bool_value("isMeetingRequest", self.is_meeting_request)
        writer.write_bool_value("isMeetingResponse", self.is_meeting_response)
        writer.write_bool_value("isNonDeliveryReport", self.is_non_delivery_report)
        writer.write_bool_value("isPermissionControlled", self.is_permission_controlled)
        writer.write_bool_value("isReadReceipt", self.is_read_receipt)
        writer.write_bool_value("isSigned", self.is_signed)
        writer.write_bool_value("isVoicemail", self.is_voicemail)
        writer.write_enum_value("messageActionFlag", self.message_action_flag)
        writer.write_bool_value("notSentToMe", self.not_sent_to_me)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("recipientContains", self.recipient_contains)
        writer.write_collection_of_primitive_values("senderContains", self.sender_contains)
        writer.write_enum_value("sensitivity", self.sensitivity)
        writer.write_bool_value("sentCcMe", self.sent_cc_me)
        writer.write_bool_value("sentOnlyToMe", self.sent_only_to_me)
        writer.write_collection_of_object_values("sentToAddresses", self.sent_to_addresses)
        writer.write_bool_value("sentToMe", self.sent_to_me)
        writer.write_bool_value("sentToOrCcMe", self.sent_to_or_cc_me)
        writer.write_collection_of_primitive_values("subjectContains", self.subject_contains)
        writer.write_object_value("withinSizeRange", self.within_size_range)
        writer.write_additional_data_value(self.additional_data)
    

