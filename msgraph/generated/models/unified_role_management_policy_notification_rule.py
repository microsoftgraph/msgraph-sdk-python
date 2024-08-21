from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

@dataclass
class UnifiedRoleManagementPolicyNotificationRule(UnifiedRoleManagementPolicyRule):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule"
    # Indicates whether a default recipient will receive the notification email.
    is_default_recipients_enabled: Optional[bool] = None
    # The level of notification. The possible values are None, Critical, All.
    notification_level: Optional[str] = None
    # The list of recipients of the email notifications.
    notification_recipients: Optional[List[str]] = None
    # The type of notification. Only Email is supported.
    notification_type: Optional[str] = None
    # The type of recipient of the notification. The possible values are Requestor, Approver, Admin.
    recipient_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementPolicyNotificationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyNotificationRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementPolicyNotificationRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        fields: Dict[str, Callable[[Any], None]] = {
            "isDefaultRecipientsEnabled": lambda n : setattr(self, 'is_default_recipients_enabled', n.get_bool_value()),
            "notificationLevel": lambda n : setattr(self, 'notification_level', n.get_str_value()),
            "notificationRecipients": lambda n : setattr(self, 'notification_recipients', n.get_collection_of_primitive_values(str)),
            "notificationType": lambda n : setattr(self, 'notification_type', n.get_str_value()),
            "recipientType": lambda n : setattr(self, 'recipient_type', n.get_str_value()),
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
        writer.write_bool_value("isDefaultRecipientsEnabled", self.is_default_recipients_enabled)
        writer.write_str_value("notificationLevel", self.notification_level)
        writer.write_collection_of_primitive_values("notificationRecipients", self.notification_recipients)
        writer.write_str_value("notificationType", self.notification_type)
        writer.write_str_value("recipientType", self.recipient_type)
    

