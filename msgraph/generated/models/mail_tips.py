from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .automatic_replies_mail_tips import AutomaticRepliesMailTips
    from .email_address import EmailAddress
    from .mail_tips_error import MailTipsError
    from .recipient import Recipient
    from .recipient_scope_type import RecipientScopeType

@dataclass
class MailTips(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Mail tips for automatic reply if it has been set up by the recipient.
    automatic_replies: Optional[AutomaticRepliesMailTips] = None
    # A custom mail tip that can be set on the recipient's mailbox.
    custom_mail_tip: Optional[str] = None
    # Whether the recipient's mailbox is restricted, for example, accepting messages from only a predefined list of senders, rejecting messages from a predefined list of senders, or accepting messages from only authenticated senders.
    delivery_restricted: Optional[bool] = None
    # The email address of the recipient to get mailtips for.
    email_address: Optional[EmailAddress] = None
    # Errors that occur during the getMailTips action.
    error: Optional[MailTipsError] = None
    # The number of external members if the recipient is a distribution list.
    external_member_count: Optional[int] = None
    # Whether sending messages to the recipient requires approval. For example, if the recipient is a large distribution list and a moderator has been set up to approve messages sent to that distribution list, or if sending messages to a recipient requires approval of the recipient's manager.
    is_moderated: Optional[bool] = None
    # The mailbox full status of the recipient.
    mailbox_full: Optional[bool] = None
    # The maximum message size that has been configured for the recipient's organization or mailbox.
    max_message_size: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scope of the recipient. Possible values are: none, internal, external, externalPartner, externalNonParther. For example, an administrator can set another organization to be its 'partner'. The scope is useful if an administrator wants certain mailtips to be accessible to certain scopes. It's also useful to senders to inform them that their message may leave the organization, helping them make the correct decisions about wording, tone and content.
    recipient_scope: Optional[RecipientScopeType] = None
    # Recipients suggested based on previous contexts where they appear in the same message.
    recipient_suggestions: Optional[List[Recipient]] = None
    # The number of members if the recipient is a distribution list.
    total_member_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailTips:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailTips
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailTips()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .automatic_replies_mail_tips import AutomaticRepliesMailTips
        from .email_address import EmailAddress
        from .mail_tips_error import MailTipsError
        from .recipient import Recipient
        from .recipient_scope_type import RecipientScopeType

        from .automatic_replies_mail_tips import AutomaticRepliesMailTips
        from .email_address import EmailAddress
        from .mail_tips_error import MailTipsError
        from .recipient import Recipient
        from .recipient_scope_type import RecipientScopeType

        fields: Dict[str, Callable[[Any], None]] = {
            "automaticReplies": lambda n : setattr(self, 'automatic_replies', n.get_object_value(AutomaticRepliesMailTips)),
            "customMailTip": lambda n : setattr(self, 'custom_mail_tip', n.get_str_value()),
            "deliveryRestricted": lambda n : setattr(self, 'delivery_restricted', n.get_bool_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_object_value(EmailAddress)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(MailTipsError)),
            "externalMemberCount": lambda n : setattr(self, 'external_member_count', n.get_int_value()),
            "isModerated": lambda n : setattr(self, 'is_moderated', n.get_bool_value()),
            "mailboxFull": lambda n : setattr(self, 'mailbox_full', n.get_bool_value()),
            "maxMessageSize": lambda n : setattr(self, 'max_message_size', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recipientScope": lambda n : setattr(self, 'recipient_scope', n.get_collection_of_enum_values(RecipientScopeType)),
            "recipientSuggestions": lambda n : setattr(self, 'recipient_suggestions', n.get_collection_of_object_values(Recipient)),
            "totalMemberCount": lambda n : setattr(self, 'total_member_count', n.get_int_value()),
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
    

