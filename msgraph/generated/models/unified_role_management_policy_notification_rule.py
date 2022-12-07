from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

unified_role_management_policy_rule = lazy_import('msgraph.generated.models.unified_role_management_policy_rule')

class UnifiedRoleManagementPolicyNotificationRule(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule):
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRoleManagementPolicyNotificationRule and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule"
        # Indicates whether a default recipient will receive the notification email.
        self._is_default_recipients_enabled: Optional[bool] = None
        # The level of notification. The possible values are None, Critical, All.
        self._notification_level: Optional[str] = None
        # The list of recipients of the email notifications.
        self._notification_recipients: Optional[List[str]] = None
        # The type of notification. Only Email is supported.
        self._notification_type: Optional[str] = None
        # The type of recipient of the notification. The possible values are Requestor, Approver, Admin.
        self._recipient_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyNotificationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyNotificationRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyNotificationRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "is_default_recipients_enabled": lambda n : setattr(self, 'is_default_recipients_enabled', n.get_bool_value()),
            "notification_level": lambda n : setattr(self, 'notification_level', n.get_str_value()),
            "notification_recipients": lambda n : setattr(self, 'notification_recipients', n.get_collection_of_primitive_values(str)),
            "notification_type": lambda n : setattr(self, 'notification_type', n.get_str_value()),
            "recipient_type": lambda n : setattr(self, 'recipient_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_default_recipients_enabled(self,) -> Optional[bool]:
        """
        Gets the isDefaultRecipientsEnabled property value. Indicates whether a default recipient will receive the notification email.
        Returns: Optional[bool]
        """
        return self._is_default_recipients_enabled
    
    @is_default_recipients_enabled.setter
    def is_default_recipients_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isDefaultRecipientsEnabled property value. Indicates whether a default recipient will receive the notification email.
        Args:
            value: Value to set for the isDefaultRecipientsEnabled property.
        """
        self._is_default_recipients_enabled = value
    
    @property
    def notification_level(self,) -> Optional[str]:
        """
        Gets the notificationLevel property value. The level of notification. The possible values are None, Critical, All.
        Returns: Optional[str]
        """
        return self._notification_level
    
    @notification_level.setter
    def notification_level(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationLevel property value. The level of notification. The possible values are None, Critical, All.
        Args:
            value: Value to set for the notificationLevel property.
        """
        self._notification_level = value
    
    @property
    def notification_recipients(self,) -> Optional[List[str]]:
        """
        Gets the notificationRecipients property value. The list of recipients of the email notifications.
        Returns: Optional[List[str]]
        """
        return self._notification_recipients
    
    @notification_recipients.setter
    def notification_recipients(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the notificationRecipients property value. The list of recipients of the email notifications.
        Args:
            value: Value to set for the notificationRecipients property.
        """
        self._notification_recipients = value
    
    @property
    def notification_type(self,) -> Optional[str]:
        """
        Gets the notificationType property value. The type of notification. Only Email is supported.
        Returns: Optional[str]
        """
        return self._notification_type
    
    @notification_type.setter
    def notification_type(self,value: Optional[str] = None) -> None:
        """
        Sets the notificationType property value. The type of notification. Only Email is supported.
        Args:
            value: Value to set for the notificationType property.
        """
        self._notification_type = value
    
    @property
    def recipient_type(self,) -> Optional[str]:
        """
        Gets the recipientType property value. The type of recipient of the notification. The possible values are Requestor, Approver, Admin.
        Returns: Optional[str]
        """
        return self._recipient_type
    
    @recipient_type.setter
    def recipient_type(self,value: Optional[str] = None) -> None:
        """
        Sets the recipientType property value. The type of recipient of the notification. The possible values are Requestor, Approver, Admin.
        Args:
            value: Value to set for the recipientType property.
        """
        self._recipient_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("isDefaultRecipientsEnabled", self.is_default_recipients_enabled)
        writer.write_str_value("notificationLevel", self.notification_level)
        writer.write_collection_of_primitive_values("notificationRecipients", self.notification_recipients)
        writer.write_str_value("notificationType", self.notification_type)
        writer.write_str_value("recipientType", self.recipient_type)
    

