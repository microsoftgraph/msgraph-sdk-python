from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import approval_settings, unified_role_management_policy_rule

from . import unified_role_management_policy_rule

@dataclass
class UnifiedRoleManagementPolicyApprovalRule(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule):
    odata_type = "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule"
    # The settings for approval of the role assignment.
    setting: Optional[approval_settings.ApprovalSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyApprovalRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyApprovalRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyApprovalRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import approval_settings, unified_role_management_policy_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "setting": lambda n : setattr(self, 'setting', n.get_object_value(approval_settings.ApprovalSettings)),
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
        writer.write_object_value("setting", self.setting)
    

