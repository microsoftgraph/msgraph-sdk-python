from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .unified_role_management_policy import UnifiedRoleManagementPolicy

from .entity import Entity

@dataclass
class UnifiedRoleManagementPolicyAssignment(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The policy that's associated with a policy assignment. Supports $expand and a nested $expand of the rules and effectiveRules relationships for the policy.
    policy: Optional[UnifiedRoleManagementPolicy] = None
    # The id of the policy. Inherited from entity.
    policy_id: Optional[str] = None
    # For Microsoft Entra roles policy, it's the identifier of the role definition object where the policy applies. For PIM for Groups membership and ownership, it's either member or owner. Supports $filter (eq).
    role_definition_id: Optional[str] = None
    # The identifier of the scope where the policy is assigned. Can be / for the tenant or a group ID. Required.
    scope_id: Optional[str] = None
    # The type of the scope where the policy is assigned. One of Directory, DirectoryRole, Group. Required.
    scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementPolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementPolicyAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .unified_role_management_policy import UnifiedRoleManagementPolicy

        from .entity import Entity
        from .unified_role_management_policy import UnifiedRoleManagementPolicy

        fields: dict[str, Callable[[Any], None]] = {
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(UnifiedRoleManagementPolicy)),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "scopeId": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
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
        writer.write_object_value("policy", self.policy)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

