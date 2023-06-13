from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_notification_recipient_scope

@dataclass
class AccessReviewNotificationRecipientItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Determines the recipient of the notification email.
    notification_recipient_scope: Optional[access_review_notification_recipient_scope.AccessReviewNotificationRecipientScope] = None
    # Indicates the type of access review email to be sent. Supported template type is CompletedAdditionalRecipients, which sends review completion notifications to the recipients.
    notification_template_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewNotificationRecipientItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewNotificationRecipientItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewNotificationRecipientItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_notification_recipient_scope

        fields: Dict[str, Callable[[Any], None]] = {
            "notificationRecipientScope": lambda n : setattr(self, 'notification_recipient_scope', n.get_object_value(access_review_notification_recipient_scope.AccessReviewNotificationRecipientScope)),
            "notificationTemplateType": lambda n : setattr(self, 'notification_template_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("notificationRecipientScope", self.notification_recipient_scope)
        writer.write_str_value("notificationTemplateType", self.notification_template_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

