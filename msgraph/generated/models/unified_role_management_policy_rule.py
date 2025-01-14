from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
    from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
    from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
    from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
    from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
    from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

from .entity import Entity

@dataclass
class UnifiedRoleManagementPolicyRule(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines details of scope that's targeted by role management policy rule. The details can include the principal type, the role assignment type, and actions affecting a role. Supports $filter (eq, ne).
    target: Optional[UnifiedRoleManagementPolicyRuleTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementPolicyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule".casefold():
            from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule

            return UnifiedRoleManagementPolicyApprovalRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule".casefold():
            from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule

            return UnifiedRoleManagementPolicyAuthenticationContextRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule".casefold():
            from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule

            return UnifiedRoleManagementPolicyEnablementRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule".casefold():
            from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule

            return UnifiedRoleManagementPolicyExpirationRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule".casefold():
            from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule

            return UnifiedRoleManagementPolicyNotificationRule()
        return UnifiedRoleManagementPolicyRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
        from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
        from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
        from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
        from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
        from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

        from .entity import Entity
        from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
        from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
        from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
        from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
        from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
        from .unified_role_management_policy_rule_target import UnifiedRoleManagementPolicyRuleTarget

        fields: dict[str, Callable[[Any], None]] = {
            "target": lambda n : setattr(self, 'target', n.get_object_value(UnifiedRoleManagementPolicyRuleTarget)),
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
        writer.write_object_value("target", self.target)
    

