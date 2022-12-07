from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

automatic_replies_mail_tips = lazy_import('msgraph.generated.models.automatic_replies_mail_tips')
email_address = lazy_import('msgraph.generated.models.email_address')
mail_tips_error = lazy_import('msgraph.generated.models.mail_tips_error')
recipient = lazy_import('msgraph.generated.models.recipient')
recipient_scope_type = lazy_import('msgraph.generated.models.recipient_scope_type')

class MailTips(AdditionalDataHolder, Parsable):
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
    def automatic_replies(self,) -> Optional[automatic_replies_mail_tips.AutomaticRepliesMailTips]:
        """
        Gets the automaticReplies property value. Mail tips for automatic reply if it has been set up by the recipient.
        Returns: Optional[automatic_replies_mail_tips.AutomaticRepliesMailTips]
        """
        return self._automatic_replies
    
    @automatic_replies.setter
    def automatic_replies(self,value: Optional[automatic_replies_mail_tips.AutomaticRepliesMailTips] = None) -> None:
        """
        Sets the automaticReplies property value. Mail tips for automatic reply if it has been set up by the recipient.
        Args:
            value: Value to set for the automaticReplies property.
        """
        self._automatic_replies = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mailTips and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Mail tips for automatic reply if it has been set up by the recipient.
        self._automatic_replies: Optional[automatic_replies_mail_tips.AutomaticRepliesMailTips] = None
        # A custom mail tip that can be set on the recipient's mailbox.
        self._custom_mail_tip: Optional[str] = None
        # Whether the recipient's mailbox is restricted, for example, accepting messages from only a predefined list of senders, rejecting messages from a predefined list of senders, or accepting messages from only authenticated senders.
        self._delivery_restricted: Optional[bool] = None
        # The email address of the recipient to get mailtips for.
        self._email_address: Optional[email_address.EmailAddress] = None
        # Errors that occur during the getMailTips action.
        self._error: Optional[mail_tips_error.MailTipsError] = None
        # The number of external members if the recipient is a distribution list.
        self._external_member_count: Optional[int] = None
        # Whether sending messages to the recipient requires approval. For example, if the recipient is a large distribution list and a moderator has been set up to approve messages sent to that distribution list, or if sending messages to a recipient requires approval of the recipient's manager.
        self._is_moderated: Optional[bool] = None
        # The mailbox full status of the recipient.
        self._mailbox_full: Optional[bool] = None
        # The maximum message size that has been configured for the recipient's organization or mailbox.
        self._max_message_size: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The scope of the recipient. Possible values are: none, internal, external, externalPartner, externalNonParther. For example, an administrator can set another organization to be its 'partner'. The scope is useful if an administrator wants certain mailtips to be accessible to certain scopes. It's also useful to senders to inform them that their message may leave the organization, helping them make the correct decisions about wording, tone and content.
        self._recipient_scope: Optional[recipient_scope_type.RecipientScopeType] = None
        # Recipients suggested based on previous contexts where they appear in the same message.
        self._recipient_suggestions: Optional[List[recipient.Recipient]] = None
        # The number of members if the recipient is a distribution list.
        self._total_member_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MailTips:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MailTips
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MailTips()
    
    @property
    def custom_mail_tip(self,) -> Optional[str]:
        """
        Gets the customMailTip property value. A custom mail tip that can be set on the recipient's mailbox.
        Returns: Optional[str]
        """
        return self._custom_mail_tip
    
    @custom_mail_tip.setter
    def custom_mail_tip(self,value: Optional[str] = None) -> None:
        """
        Sets the customMailTip property value. A custom mail tip that can be set on the recipient's mailbox.
        Args:
            value: Value to set for the customMailTip property.
        """
        self._custom_mail_tip = value
    
    @property
    def delivery_restricted(self,) -> Optional[bool]:
        """
        Gets the deliveryRestricted property value. Whether the recipient's mailbox is restricted, for example, accepting messages from only a predefined list of senders, rejecting messages from a predefined list of senders, or accepting messages from only authenticated senders.
        Returns: Optional[bool]
        """
        return self._delivery_restricted
    
    @delivery_restricted.setter
    def delivery_restricted(self,value: Optional[bool] = None) -> None:
        """
        Sets the deliveryRestricted property value. Whether the recipient's mailbox is restricted, for example, accepting messages from only a predefined list of senders, rejecting messages from a predefined list of senders, or accepting messages from only authenticated senders.
        Args:
            value: Value to set for the deliveryRestricted property.
        """
        self._delivery_restricted = value
    
    @property
    def email_address(self,) -> Optional[email_address.EmailAddress]:
        """
        Gets the emailAddress property value. The email address of the recipient to get mailtips for.
        Returns: Optional[email_address.EmailAddress]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[email_address.EmailAddress] = None) -> None:
        """
        Sets the emailAddress property value. The email address of the recipient to get mailtips for.
        Args:
            value: Value to set for the emailAddress property.
        """
        self._email_address = value
    
    @property
    def error(self,) -> Optional[mail_tips_error.MailTipsError]:
        """
        Gets the error property value. Errors that occur during the getMailTips action.
        Returns: Optional[mail_tips_error.MailTipsError]
        """
        return self._error
    
    @error.setter
    def error(self,value: Optional[mail_tips_error.MailTipsError] = None) -> None:
        """
        Sets the error property value. Errors that occur during the getMailTips action.
        Args:
            value: Value to set for the error property.
        """
        self._error = value
    
    @property
    def external_member_count(self,) -> Optional[int]:
        """
        Gets the externalMemberCount property value. The number of external members if the recipient is a distribution list.
        Returns: Optional[int]
        """
        return self._external_member_count
    
    @external_member_count.setter
    def external_member_count(self,value: Optional[int] = None) -> None:
        """
        Sets the externalMemberCount property value. The number of external members if the recipient is a distribution list.
        Args:
            value: Value to set for the externalMemberCount property.
        """
        self._external_member_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "automatic_replies": lambda n : setattr(self, 'automatic_replies', n.get_object_value(automatic_replies_mail_tips.AutomaticRepliesMailTips)),
            "custom_mail_tip": lambda n : setattr(self, 'custom_mail_tip', n.get_str_value()),
            "delivery_restricted": lambda n : setattr(self, 'delivery_restricted', n.get_bool_value()),
            "email_address": lambda n : setattr(self, 'email_address', n.get_object_value(email_address.EmailAddress)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(mail_tips_error.MailTipsError)),
            "external_member_count": lambda n : setattr(self, 'external_member_count', n.get_int_value()),
            "is_moderated": lambda n : setattr(self, 'is_moderated', n.get_bool_value()),
            "mailbox_full": lambda n : setattr(self, 'mailbox_full', n.get_bool_value()),
            "max_message_size": lambda n : setattr(self, 'max_message_size', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recipient_scope": lambda n : setattr(self, 'recipient_scope', n.get_enum_value(recipient_scope_type.RecipientScopeType)),
            "recipient_suggestions": lambda n : setattr(self, 'recipient_suggestions', n.get_collection_of_object_values(recipient.Recipient)),
            "total_member_count": lambda n : setattr(self, 'total_member_count', n.get_int_value()),
        }
        return fields
    
    @property
    def is_moderated(self,) -> Optional[bool]:
        """
        Gets the isModerated property value. Whether sending messages to the recipient requires approval. For example, if the recipient is a large distribution list and a moderator has been set up to approve messages sent to that distribution list, or if sending messages to a recipient requires approval of the recipient's manager.
        Returns: Optional[bool]
        """
        return self._is_moderated
    
    @is_moderated.setter
    def is_moderated(self,value: Optional[bool] = None) -> None:
        """
        Sets the isModerated property value. Whether sending messages to the recipient requires approval. For example, if the recipient is a large distribution list and a moderator has been set up to approve messages sent to that distribution list, or if sending messages to a recipient requires approval of the recipient's manager.
        Args:
            value: Value to set for the isModerated property.
        """
        self._is_moderated = value
    
    @property
    def mailbox_full(self,) -> Optional[bool]:
        """
        Gets the mailboxFull property value. The mailbox full status of the recipient.
        Returns: Optional[bool]
        """
        return self._mailbox_full
    
    @mailbox_full.setter
    def mailbox_full(self,value: Optional[bool] = None) -> None:
        """
        Sets the mailboxFull property value. The mailbox full status of the recipient.
        Args:
            value: Value to set for the mailboxFull property.
        """
        self._mailbox_full = value
    
    @property
    def max_message_size(self,) -> Optional[int]:
        """
        Gets the maxMessageSize property value. The maximum message size that has been configured for the recipient's organization or mailbox.
        Returns: Optional[int]
        """
        return self._max_message_size
    
    @max_message_size.setter
    def max_message_size(self,value: Optional[int] = None) -> None:
        """
        Sets the maxMessageSize property value. The maximum message size that has been configured for the recipient's organization or mailbox.
        Args:
            value: Value to set for the maxMessageSize property.
        """
        self._max_message_size = value
    
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
    def recipient_scope(self,) -> Optional[recipient_scope_type.RecipientScopeType]:
        """
        Gets the recipientScope property value. The scope of the recipient. Possible values are: none, internal, external, externalPartner, externalNonParther. For example, an administrator can set another organization to be its 'partner'. The scope is useful if an administrator wants certain mailtips to be accessible to certain scopes. It's also useful to senders to inform them that their message may leave the organization, helping them make the correct decisions about wording, tone and content.
        Returns: Optional[recipient_scope_type.RecipientScopeType]
        """
        return self._recipient_scope
    
    @recipient_scope.setter
    def recipient_scope(self,value: Optional[recipient_scope_type.RecipientScopeType] = None) -> None:
        """
        Sets the recipientScope property value. The scope of the recipient. Possible values are: none, internal, external, externalPartner, externalNonParther. For example, an administrator can set another organization to be its 'partner'. The scope is useful if an administrator wants certain mailtips to be accessible to certain scopes. It's also useful to senders to inform them that their message may leave the organization, helping them make the correct decisions about wording, tone and content.
        Args:
            value: Value to set for the recipientScope property.
        """
        self._recipient_scope = value
    
    @property
    def recipient_suggestions(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the recipientSuggestions property value. Recipients suggested based on previous contexts where they appear in the same message.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._recipient_suggestions
    
    @recipient_suggestions.setter
    def recipient_suggestions(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the recipientSuggestions property value. Recipients suggested based on previous contexts where they appear in the same message.
        Args:
            value: Value to set for the recipientSuggestions property.
        """
        self._recipient_suggestions = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("automaticReplies", self.automatic_replies)
        writer.write_str_value("customMailTip", self.custom_mail_tip)
        writer.write_bool_value("deliveryRestricted", self.delivery_restricted)
        writer.write_object_value("emailAddress", self.email_address)
        writer.write_object_value("error", self.error)
        writer.write_int_value("externalMemberCount", self.external_member_count)
        writer.write_bool_value("isModerated", self.is_moderated)
        writer.write_bool_value("mailboxFull", self.mailbox_full)
        writer.write_int_value("maxMessageSize", self.max_message_size)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("recipientScope", self.recipient_scope)
        writer.write_collection_of_object_values("recipientSuggestions", self.recipient_suggestions)
        writer.write_int_value("totalMemberCount", self.total_member_count)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def total_member_count(self,) -> Optional[int]:
        """
        Gets the totalMemberCount property value. The number of members if the recipient is a distribution list.
        Returns: Optional[int]
        """
        return self._total_member_count
    
    @total_member_count.setter
    def total_member_count(self,value: Optional[int] = None) -> None:
        """
        Sets the totalMemberCount property value. The number of members if the recipient is a distribution list.
        Args:
            value: Value to set for the totalMemberCount property.
        """
        self._total_member_count = value
    

