from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_role_management_policy_approval_rule, unified_role_management_policy_authentication_context_rule, unified_role_management_policy_enablement_rule, unified_role_management_policy_expiration_rule, unified_role_management_policy_notification_rule, unified_role_management_policy_rule_target

from . import entity

class UnifiedRoleManagementPolicyRule(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleManagementPolicyRule and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Defines details of scope that's targeted by role management policy rule. The details can include the principal type, the role assignment type, and actions affecting a role. Supports $filter (eq, ne).
        self._target: Optional[unified_role_management_policy_rule_target.UnifiedRoleManagementPolicyRuleTarget] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule":
                from . import unified_role_management_policy_approval_rule

                return unified_role_management_policy_approval_rule.UnifiedRoleManagementPolicyApprovalRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule":
                from . import unified_role_management_policy_authentication_context_rule

                return unified_role_management_policy_authentication_context_rule.UnifiedRoleManagementPolicyAuthenticationContextRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule":
                from . import unified_role_management_policy_enablement_rule

                return unified_role_management_policy_enablement_rule.UnifiedRoleManagementPolicyEnablementRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule":
                from . import unified_role_management_policy_expiration_rule

                return unified_role_management_policy_expiration_rule.UnifiedRoleManagementPolicyExpirationRule()
            if mapping_value == "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule":
                from . import unified_role_management_policy_notification_rule

                return unified_role_management_policy_notification_rule.UnifiedRoleManagementPolicyNotificationRule()
        return UnifiedRoleManagementPolicyRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, unified_role_management_policy_approval_rule, unified_role_management_policy_authentication_context_rule, unified_role_management_policy_enablement_rule, unified_role_management_policy_expiration_rule, unified_role_management_policy_notification_rule, unified_role_management_policy_rule_target

        fields: Dict[str, Callable[[Any], None]] = {
            "target": lambda n : setattr(self, 'target', n.get_object_value(unified_role_management_policy_rule_target.UnifiedRoleManagementPolicyRuleTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("target", self.target)
    
    @property
    def target(self,) -> Optional[unified_role_management_policy_rule_target.UnifiedRoleManagementPolicyRuleTarget]:
        """
        Gets the target property value. Defines details of scope that's targeted by role management policy rule. The details can include the principal type, the role assignment type, and actions affecting a role. Supports $filter (eq, ne).
        Returns: Optional[unified_role_management_policy_rule_target.UnifiedRoleManagementPolicyRuleTarget]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[unified_role_management_policy_rule_target.UnifiedRoleManagementPolicyRuleTarget] = None) -> None:
        """
        Sets the target property value. Defines details of scope that's targeted by role management policy rule. The details can include the principal type, the role assignment type, and actions affecting a role. Supports $filter (eq, ne).
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

