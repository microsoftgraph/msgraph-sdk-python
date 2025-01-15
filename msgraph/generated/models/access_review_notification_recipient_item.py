from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_notification_recipient_scope import AccessReviewNotificationRecipientScope

@dataclass
class AccessReviewNotificationRecipientItem(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Determines the recipient of the notification email.
    notification_recipient_scope: Optional[AccessReviewNotificationRecipientScope] = None
    # Indicates the type of access review email to be sent. Supported template type is CompletedAdditionalRecipients, which sends review completion notifications to the recipients.
    notification_template_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewNotificationRecipientItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewNotificationRecipientItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewNotificationRecipientItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_notification_recipient_scope import AccessReviewNotificationRecipientScope

        from .access_review_notification_recipient_scope import AccessReviewNotificationRecipientScope

        fields: dict[str, Callable[[Any], None]] = {
            "notificationRecipientScope": lambda n : setattr(self, 'notification_recipient_scope', n.get_object_value(AccessReviewNotificationRecipientScope)),
            "notificationTemplateType": lambda n : setattr(self, 'notification_template_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("notificationRecipientScope", self.notification_recipient_scope)
        writer.write_str_value("notificationTemplateType", self.notification_template_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

