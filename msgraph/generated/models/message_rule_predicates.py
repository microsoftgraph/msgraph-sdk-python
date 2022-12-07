from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

importance = lazy_import('msgraph.generated.models.importance')
message_action_flag = lazy_import('msgraph.generated.models.message_action_flag')
recipient = lazy_import('msgraph.generated.models.recipient')
sensitivity = lazy_import('msgraph.generated.models.sensitivity')
size_range = lazy_import('msgraph.generated.models.size_range')

class MessageRulePredicates(AdditionalDataHolder, Parsable):
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
    
    @property
    def body_contains(self,) -> Optional[List[str]]:
        """
        Gets the bodyContains property value. Represents the strings that should appear in the body of an incoming message in order for the condition or exception to apply.
        Returns: Optional[List[str]]
        """
        return self._body_contains
    
    @body_contains.setter
    def body_contains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the bodyContains property value. Represents the strings that should appear in the body of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the bodyContains property.
        """
        self._body_contains = value
    
    @property
    def body_or_subject_contains(self,) -> Optional[List[str]]:
        """
        Gets the bodyOrSubjectContains property value. Represents the strings that should appear in the body or subject of an incoming message in order for the condition or exception to apply.
        Returns: Optional[List[str]]
        """
        return self._body_or_subject_contains
    
    @body_or_subject_contains.setter
    def body_or_subject_contains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the bodyOrSubjectContains property value. Represents the strings that should appear in the body or subject of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the bodyOrSubjectContains property.
        """
        self._body_or_subject_contains = value
    
    @property
    def categories(self,) -> Optional[List[str]]:
        """
        Gets the categories property value. Represents the categories that an incoming message should be labeled with in order for the condition or exception to apply.
        Returns: Optional[List[str]]
        """
        return self._categories
    
    @categories.setter
    def categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the categories property value. Represents the categories that an incoming message should be labeled with in order for the condition or exception to apply.
        Args:
            value: Value to set for the categories property.
        """
        self._categories = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new messageRulePredicates and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Represents the strings that should appear in the body of an incoming message in order for the condition or exception to apply.
        self._body_contains: Optional[List[str]] = None
        # Represents the strings that should appear in the body or subject of an incoming message in order for the condition or exception to apply.
        self._body_or_subject_contains: Optional[List[str]] = None
        # Represents the categories that an incoming message should be labeled with in order for the condition or exception to apply.
        self._categories: Optional[List[str]] = None
        # Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply.
        self._from_addresses: Optional[List[recipient.Recipient]] = None
        # Indicates whether an incoming message must have attachments in order for the condition or exception to apply.
        self._has_attachments: Optional[bool] = None
        # Represents the strings that appear in the headers of an incoming message in order for the condition or exception to apply.
        self._header_contains: Optional[List[str]] = None
        # The importance that is stamped on an incoming message in order for the condition or exception to apply: low, normal, high.
        self._importance: Optional[importance.Importance] = None
        # Indicates whether an incoming message must be an approval request in order for the condition or exception to apply.
        self._is_approval_request: Optional[bool] = None
        # Indicates whether an incoming message must be automatically forwarded in order for the condition or exception to apply.
        self._is_automatic_forward: Optional[bool] = None
        # Indicates whether an incoming message must be an auto reply in order for the condition or exception to apply.
        self._is_automatic_reply: Optional[bool] = None
        # Indicates whether an incoming message must be encrypted in order for the condition or exception to apply.
        self._is_encrypted: Optional[bool] = None
        # Indicates whether an incoming message must be a meeting request in order for the condition or exception to apply.
        self._is_meeting_request: Optional[bool] = None
        # Indicates whether an incoming message must be a meeting response in order for the condition or exception to apply.
        self._is_meeting_response: Optional[bool] = None
        # Indicates whether an incoming message must be a non-delivery report in order for the condition or exception to apply.
        self._is_non_delivery_report: Optional[bool] = None
        # Indicates whether an incoming message must be permission controlled (RMS-protected) in order for the condition or exception to apply.
        self._is_permission_controlled: Optional[bool] = None
        # Indicates whether an incoming message must be a read receipt in order for the condition or exception to apply.
        self._is_read_receipt: Optional[bool] = None
        # Indicates whether an incoming message must be S/MIME-signed in order for the condition or exception to apply.
        self._is_signed: Optional[bool] = None
        # Indicates whether an incoming message must be a voice mail in order for the condition or exception to apply.
        self._is_voicemail: Optional[bool] = None
        # Represents the flag-for-action value that appears on an incoming message in order for the condition or exception to apply. The possible values are: any, call, doNotForward, followUp, fyi, forward, noResponseNecessary, read, reply, replyToAll, review.
        self._message_action_flag: Optional[message_action_flag.MessageActionFlag] = None
        # Indicates whether the owner of the mailbox must not be a recipient of an incoming message in order for the condition or exception to apply.
        self._not_sent_to_me: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Represents the strings that appear in either the toRecipients or ccRecipients properties of an incoming message in order for the condition or exception to apply.
        self._recipient_contains: Optional[List[str]] = None
        # Represents the strings that appear in the from property of an incoming message in order for the condition or exception to apply.
        self._sender_contains: Optional[List[str]] = None
        # Represents the sensitivity level that must be stamped on an incoming message in order for the condition or exception to apply. The possible values are: normal, personal, private, confidential.
        self._sensitivity: Optional[sensitivity.Sensitivity] = None
        # Indicates whether the owner of the mailbox must be in the ccRecipients property of an incoming message in order for the condition or exception to apply.
        self._sent_cc_me: Optional[bool] = None
        # Indicates whether the owner of the mailbox must be the only recipient in an incoming message in order for the condition or exception to apply.
        self._sent_only_to_me: Optional[bool] = None
        # Represents the email addresses that an incoming message must have been sent to in order for the condition or exception to apply.
        self._sent_to_addresses: Optional[List[recipient.Recipient]] = None
        # Indicates whether the owner of the mailbox must be in the toRecipients property of an incoming message in order for the condition or exception to apply.
        self._sent_to_me: Optional[bool] = None
        # Indicates whether the owner of the mailbox must be in either a toRecipients or ccRecipients property of an incoming message in order for the condition or exception to apply.
        self._sent_to_or_cc_me: Optional[bool] = None
        # Represents the strings that appear in the subject of an incoming message in order for the condition or exception to apply.
        self._subject_contains: Optional[List[str]] = None
        # Represents the minimum and maximum sizes (in kilobytes) that an incoming message must fall in between in order for the condition or exception to apply.
        self._within_size_range: Optional[size_range.SizeRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageRulePredicates:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MessageRulePredicates
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MessageRulePredicates()
    
    @property
    def from_addresses(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the fromAddresses property value. Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._from_addresses
    
    @from_addresses.setter
    def from_addresses(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the fromAddresses property value. Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the fromAddresses property.
        """
        self._from_addresses = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "body_contains": lambda n : setattr(self, 'body_contains', n.get_collection_of_primitive_values(str)),
            "body_or_subject_contains": lambda n : setattr(self, 'body_or_subject_contains', n.get_collection_of_primitive_values(str)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "from_addresses": lambda n : setattr(self, 'from_addresses', n.get_collection_of_object_values(recipient.Recipient)),
            "has_attachments": lambda n : setattr(self, 'has_attachments', n.get_bool_value()),
            "header_contains": lambda n : setattr(self, 'header_contains', n.get_collection_of_primitive_values(str)),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(importance.Importance)),
            "is_approval_request": lambda n : setattr(self, 'is_approval_request', n.get_bool_value()),
            "is_automatic_forward": lambda n : setattr(self, 'is_automatic_forward', n.get_bool_value()),
            "is_automatic_reply": lambda n : setattr(self, 'is_automatic_reply', n.get_bool_value()),
            "is_encrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "is_meeting_request": lambda n : setattr(self, 'is_meeting_request', n.get_bool_value()),
            "is_meeting_response": lambda n : setattr(self, 'is_meeting_response', n.get_bool_value()),
            "is_non_delivery_report": lambda n : setattr(self, 'is_non_delivery_report', n.get_bool_value()),
            "is_permission_controlled": lambda n : setattr(self, 'is_permission_controlled', n.get_bool_value()),
            "is_read_receipt": lambda n : setattr(self, 'is_read_receipt', n.get_bool_value()),
            "is_signed": lambda n : setattr(self, 'is_signed', n.get_bool_value()),
            "is_voicemail": lambda n : setattr(self, 'is_voicemail', n.get_bool_value()),
            "message_action_flag": lambda n : setattr(self, 'message_action_flag', n.get_enum_value(message_action_flag.MessageActionFlag)),
            "not_sent_to_me": lambda n : setattr(self, 'not_sent_to_me', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recipient_contains": lambda n : setattr(self, 'recipient_contains', n.get_collection_of_primitive_values(str)),
            "sender_contains": lambda n : setattr(self, 'sender_contains', n.get_collection_of_primitive_values(str)),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_enum_value(sensitivity.Sensitivity)),
            "sent_cc_me": lambda n : setattr(self, 'sent_cc_me', n.get_bool_value()),
            "sent_only_to_me": lambda n : setattr(self, 'sent_only_to_me', n.get_bool_value()),
            "sent_to_addresses": lambda n : setattr(self, 'sent_to_addresses', n.get_collection_of_object_values(recipient.Recipient)),
            "sent_to_me": lambda n : setattr(self, 'sent_to_me', n.get_bool_value()),
            "sent_to_or_cc_me": lambda n : setattr(self, 'sent_to_or_cc_me', n.get_bool_value()),
            "subject_contains": lambda n : setattr(self, 'subject_contains', n.get_collection_of_primitive_values(str)),
            "within_size_range": lambda n : setattr(self, 'within_size_range', n.get_object_value(size_range.SizeRange)),
        }
        return fields
    
    @property
    def has_attachments(self,) -> Optional[bool]:
        """
        Gets the hasAttachments property value. Indicates whether an incoming message must have attachments in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._has_attachments
    
    @has_attachments.setter
    def has_attachments(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasAttachments property value. Indicates whether an incoming message must have attachments in order for the condition or exception to apply.
        Args:
            value: Value to set for the hasAttachments property.
        """
        self._has_attachments = value
    
    @property
    def header_contains(self,) -> Optional[List[str]]:
        """
        Gets the headerContains property value. Represents the strings that appear in the headers of an incoming message in order for the condition or exception to apply.
        Returns: Optional[List[str]]
        """
        return self._header_contains
    
    @header_contains.setter
    def header_contains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the headerContains property value. Represents the strings that appear in the headers of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the headerContains property.
        """
        self._header_contains = value
    
    @property
    def importance(self,) -> Optional[importance.Importance]:
        """
        Gets the importance property value. The importance that is stamped on an incoming message in order for the condition or exception to apply: low, normal, high.
        Returns: Optional[importance.Importance]
        """
        return self._importance
    
    @importance.setter
    def importance(self,value: Optional[importance.Importance] = None) -> None:
        """
        Sets the importance property value. The importance that is stamped on an incoming message in order for the condition or exception to apply: low, normal, high.
        Args:
            value: Value to set for the importance property.
        """
        self._importance = value
    
    @property
    def is_approval_request(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequest property value. Indicates whether an incoming message must be an approval request in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_approval_request
    
    @is_approval_request.setter
    def is_approval_request(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequest property value. Indicates whether an incoming message must be an approval request in order for the condition or exception to apply.
        Args:
            value: Value to set for the isApprovalRequest property.
        """
        self._is_approval_request = value
    
    @property
    def is_automatic_forward(self,) -> Optional[bool]:
        """
        Gets the isAutomaticForward property value. Indicates whether an incoming message must be automatically forwarded in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_automatic_forward
    
    @is_automatic_forward.setter
    def is_automatic_forward(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAutomaticForward property value. Indicates whether an incoming message must be automatically forwarded in order for the condition or exception to apply.
        Args:
            value: Value to set for the isAutomaticForward property.
        """
        self._is_automatic_forward = value
    
    @property
    def is_automatic_reply(self,) -> Optional[bool]:
        """
        Gets the isAutomaticReply property value. Indicates whether an incoming message must be an auto reply in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_automatic_reply
    
    @is_automatic_reply.setter
    def is_automatic_reply(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAutomaticReply property value. Indicates whether an incoming message must be an auto reply in order for the condition or exception to apply.
        Args:
            value: Value to set for the isAutomaticReply property.
        """
        self._is_automatic_reply = value
    
    @property
    def is_encrypted(self,) -> Optional[bool]:
        """
        Gets the isEncrypted property value. Indicates whether an incoming message must be encrypted in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_encrypted
    
    @is_encrypted.setter
    def is_encrypted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEncrypted property value. Indicates whether an incoming message must be encrypted in order for the condition or exception to apply.
        Args:
            value: Value to set for the isEncrypted property.
        """
        self._is_encrypted = value
    
    @property
    def is_meeting_request(self,) -> Optional[bool]:
        """
        Gets the isMeetingRequest property value. Indicates whether an incoming message must be a meeting request in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_meeting_request
    
    @is_meeting_request.setter
    def is_meeting_request(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMeetingRequest property value. Indicates whether an incoming message must be a meeting request in order for the condition or exception to apply.
        Args:
            value: Value to set for the isMeetingRequest property.
        """
        self._is_meeting_request = value
    
    @property
    def is_meeting_response(self,) -> Optional[bool]:
        """
        Gets the isMeetingResponse property value. Indicates whether an incoming message must be a meeting response in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_meeting_response
    
    @is_meeting_response.setter
    def is_meeting_response(self,value: Optional[bool] = None) -> None:
        """
        Sets the isMeetingResponse property value. Indicates whether an incoming message must be a meeting response in order for the condition or exception to apply.
        Args:
            value: Value to set for the isMeetingResponse property.
        """
        self._is_meeting_response = value
    
    @property
    def is_non_delivery_report(self,) -> Optional[bool]:
        """
        Gets the isNonDeliveryReport property value. Indicates whether an incoming message must be a non-delivery report in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_non_delivery_report
    
    @is_non_delivery_report.setter
    def is_non_delivery_report(self,value: Optional[bool] = None) -> None:
        """
        Sets the isNonDeliveryReport property value. Indicates whether an incoming message must be a non-delivery report in order for the condition or exception to apply.
        Args:
            value: Value to set for the isNonDeliveryReport property.
        """
        self._is_non_delivery_report = value
    
    @property
    def is_permission_controlled(self,) -> Optional[bool]:
        """
        Gets the isPermissionControlled property value. Indicates whether an incoming message must be permission controlled (RMS-protected) in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_permission_controlled
    
    @is_permission_controlled.setter
    def is_permission_controlled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isPermissionControlled property value. Indicates whether an incoming message must be permission controlled (RMS-protected) in order for the condition or exception to apply.
        Args:
            value: Value to set for the isPermissionControlled property.
        """
        self._is_permission_controlled = value
    
    @property
    def is_read_receipt(self,) -> Optional[bool]:
        """
        Gets the isReadReceipt property value. Indicates whether an incoming message must be a read receipt in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_read_receipt
    
    @is_read_receipt.setter
    def is_read_receipt(self,value: Optional[bool] = None) -> None:
        """
        Sets the isReadReceipt property value. Indicates whether an incoming message must be a read receipt in order for the condition or exception to apply.
        Args:
            value: Value to set for the isReadReceipt property.
        """
        self._is_read_receipt = value
    
    @property
    def is_signed(self,) -> Optional[bool]:
        """
        Gets the isSigned property value. Indicates whether an incoming message must be S/MIME-signed in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_signed
    
    @is_signed.setter
    def is_signed(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSigned property value. Indicates whether an incoming message must be S/MIME-signed in order for the condition or exception to apply.
        Args:
            value: Value to set for the isSigned property.
        """
        self._is_signed = value
    
    @property
    def is_voicemail(self,) -> Optional[bool]:
        """
        Gets the isVoicemail property value. Indicates whether an incoming message must be a voice mail in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._is_voicemail
    
    @is_voicemail.setter
    def is_voicemail(self,value: Optional[bool] = None) -> None:
        """
        Sets the isVoicemail property value. Indicates whether an incoming message must be a voice mail in order for the condition or exception to apply.
        Args:
            value: Value to set for the isVoicemail property.
        """
        self._is_voicemail = value
    
    @property
    def message_action_flag(self,) -> Optional[message_action_flag.MessageActionFlag]:
        """
        Gets the messageActionFlag property value. Represents the flag-for-action value that appears on an incoming message in order for the condition or exception to apply. The possible values are: any, call, doNotForward, followUp, fyi, forward, noResponseNecessary, read, reply, replyToAll, review.
        Returns: Optional[message_action_flag.MessageActionFlag]
        """
        return self._message_action_flag
    
    @message_action_flag.setter
    def message_action_flag(self,value: Optional[message_action_flag.MessageActionFlag] = None) -> None:
        """
        Sets the messageActionFlag property value. Represents the flag-for-action value that appears on an incoming message in order for the condition or exception to apply. The possible values are: any, call, doNotForward, followUp, fyi, forward, noResponseNecessary, read, reply, replyToAll, review.
        Args:
            value: Value to set for the messageActionFlag property.
        """
        self._message_action_flag = value
    
    @property
    def not_sent_to_me(self,) -> Optional[bool]:
        """
        Gets the notSentToMe property value. Indicates whether the owner of the mailbox must not be a recipient of an incoming message in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._not_sent_to_me
    
    @not_sent_to_me.setter
    def not_sent_to_me(self,value: Optional[bool] = None) -> None:
        """
        Sets the notSentToMe property value. Indicates whether the owner of the mailbox must not be a recipient of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the notSentToMe property.
        """
        self._not_sent_to_me = value
    
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
    
    @property
    def recipient_contains(self,) -> Optional[List[str]]:
        """
        Gets the recipientContains property value. Represents the strings that appear in either the toRecipients or ccRecipients properties of an incoming message in order for the condition or exception to apply.
        Returns: Optional[List[str]]
        """
        return self._recipient_contains
    
    @recipient_contains.setter
    def recipient_contains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the recipientContains property value. Represents the strings that appear in either the toRecipients or ccRecipients properties of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the recipientContains property.
        """
        self._recipient_contains = value
    
    @property
    def sender_contains(self,) -> Optional[List[str]]:
        """
        Gets the senderContains property value. Represents the strings that appear in the from property of an incoming message in order for the condition or exception to apply.
        Returns: Optional[List[str]]
        """
        return self._sender_contains
    
    @sender_contains.setter
    def sender_contains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the senderContains property value. Represents the strings that appear in the from property of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the senderContains property.
        """
        self._sender_contains = value
    
    @property
    def sensitivity(self,) -> Optional[sensitivity.Sensitivity]:
        """
        Gets the sensitivity property value. Represents the sensitivity level that must be stamped on an incoming message in order for the condition or exception to apply. The possible values are: normal, personal, private, confidential.
        Returns: Optional[sensitivity.Sensitivity]
        """
        return self._sensitivity
    
    @sensitivity.setter
    def sensitivity(self,value: Optional[sensitivity.Sensitivity] = None) -> None:
        """
        Sets the sensitivity property value. Represents the sensitivity level that must be stamped on an incoming message in order for the condition or exception to apply. The possible values are: normal, personal, private, confidential.
        Args:
            value: Value to set for the sensitivity property.
        """
        self._sensitivity = value
    
    @property
    def sent_cc_me(self,) -> Optional[bool]:
        """
        Gets the sentCcMe property value. Indicates whether the owner of the mailbox must be in the ccRecipients property of an incoming message in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._sent_cc_me
    
    @sent_cc_me.setter
    def sent_cc_me(self,value: Optional[bool] = None) -> None:
        """
        Sets the sentCcMe property value. Indicates whether the owner of the mailbox must be in the ccRecipients property of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the sentCcMe property.
        """
        self._sent_cc_me = value
    
    @property
    def sent_only_to_me(self,) -> Optional[bool]:
        """
        Gets the sentOnlyToMe property value. Indicates whether the owner of the mailbox must be the only recipient in an incoming message in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._sent_only_to_me
    
    @sent_only_to_me.setter
    def sent_only_to_me(self,value: Optional[bool] = None) -> None:
        """
        Sets the sentOnlyToMe property value. Indicates whether the owner of the mailbox must be the only recipient in an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the sentOnlyToMe property.
        """
        self._sent_only_to_me = value
    
    @property
    def sent_to_addresses(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the sentToAddresses property value. Represents the email addresses that an incoming message must have been sent to in order for the condition or exception to apply.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._sent_to_addresses
    
    @sent_to_addresses.setter
    def sent_to_addresses(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the sentToAddresses property value. Represents the email addresses that an incoming message must have been sent to in order for the condition or exception to apply.
        Args:
            value: Value to set for the sentToAddresses property.
        """
        self._sent_to_addresses = value
    
    @property
    def sent_to_me(self,) -> Optional[bool]:
        """
        Gets the sentToMe property value. Indicates whether the owner of the mailbox must be in the toRecipients property of an incoming message in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._sent_to_me
    
    @sent_to_me.setter
    def sent_to_me(self,value: Optional[bool] = None) -> None:
        """
        Sets the sentToMe property value. Indicates whether the owner of the mailbox must be in the toRecipients property of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the sentToMe property.
        """
        self._sent_to_me = value
    
    @property
    def sent_to_or_cc_me(self,) -> Optional[bool]:
        """
        Gets the sentToOrCcMe property value. Indicates whether the owner of the mailbox must be in either a toRecipients or ccRecipients property of an incoming message in order for the condition or exception to apply.
        Returns: Optional[bool]
        """
        return self._sent_to_or_cc_me
    
    @sent_to_or_cc_me.setter
    def sent_to_or_cc_me(self,value: Optional[bool] = None) -> None:
        """
        Sets the sentToOrCcMe property value. Indicates whether the owner of the mailbox must be in either a toRecipients or ccRecipients property of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the sentToOrCcMe property.
        """
        self._sent_to_or_cc_me = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def subject_contains(self,) -> Optional[List[str]]:
        """
        Gets the subjectContains property value. Represents the strings that appear in the subject of an incoming message in order for the condition or exception to apply.
        Returns: Optional[List[str]]
        """
        return self._subject_contains
    
    @subject_contains.setter
    def subject_contains(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the subjectContains property value. Represents the strings that appear in the subject of an incoming message in order for the condition or exception to apply.
        Args:
            value: Value to set for the subjectContains property.
        """
        self._subject_contains = value
    
    @property
    def within_size_range(self,) -> Optional[size_range.SizeRange]:
        """
        Gets the withinSizeRange property value. Represents the minimum and maximum sizes (in kilobytes) that an incoming message must fall in between in order for the condition or exception to apply.
        Returns: Optional[size_range.SizeRange]
        """
        return self._within_size_range
    
    @within_size_range.setter
    def within_size_range(self,value: Optional[size_range.SizeRange] = None) -> None:
        """
        Sets the withinSizeRange property value. Represents the minimum and maximum sizes (in kilobytes) that an incoming message must fall in between in order for the condition or exception to apply.
        Args:
            value: Value to set for the withinSizeRange property.
        """
        self._within_size_range = value
    

