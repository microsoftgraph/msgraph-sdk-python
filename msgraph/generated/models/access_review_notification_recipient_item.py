from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_notification_recipient_scope = lazy_import('msgraph.generated.models.access_review_notification_recipient_scope')

class AccessReviewNotificationRecipientItem(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new accessReviewNotificationRecipientItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Determines the recipient of the notification email.
        self._notification_recipient_scope: Optional[access_review_notification_recipient_scope.AccessReviewNotificationRecipientScope] = None
        # Indicates the type of access review email to be sent. Supported template type is CompletedAdditionalRecipients, which sends review completion notifications to the recipients.
        self._notification_template_type: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
        fields = {
            "notification_recipient_scope": lambda n : setattr(self, 'notification_recipient_scope', n.get_object_value(access_review_notification_recipient_scope.AccessReviewNotificationRecipientScope)),
            "notification_template_type": lambda n : setattr(self, 'notification_template_type', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def notification_recipient_scope(self,) -> Optional[access_review_notification_recipient_scope.AccessReviewNotificationRecipientScope]:
        """
        Gets the notificationRecipientScope property value. Determines the recipient of the notification email.
        Returns: Optional[access_review_notification_recipient_scope.AccessReviewNotificationRecipientScope]
        """
        return self._notification_recipient_scope
    
    @notification_recipient_scope.setter
    def notification_recipient_scope(self,value: Optional[access_review_notification_recipient_scope.AccessReviewNotificationRecipientScope] = None) -> None:
        """
        Sets the notificationRecipientScope property value. Determines the recipient of the notification email.
        Args:
            value: Value to set for the notificationRecipientScope property.
        """
        self._notification_recipient_scope = value
    
    @property
    def notification_template_type(self,) -> Optional[str]:
        """
        Gets the notificationTemplateType property value. Indicates the type of access review email to be sent. Supported template type is CompletedAdditionalRecipients, which sends review completion notifications to the recipients.
        Returns: Optional[str]
        """
        return self._notification_template_type
    
    @notification_template_type.setter
    def notification_template_type(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationTemplateType property value. Indicates the type of access review email to be sent. Supported template type is CompletedAdditionalRecipients, which sends review completion notifications to the recipients.
        Args:
            value: Value to set for the notificationTemplateType property.
        """
        self._notification_template_type = value
    
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
    

