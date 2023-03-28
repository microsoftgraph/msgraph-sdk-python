from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_role_management_policy

from . import entity

class UnifiedRoleManagementPolicyAssignment(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleManagementPolicyAssignment and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policy that's associated with a policy assignment. Supports $expand and a nested $expand of the rules and effectiveRules relationships for the policy.
        self._policy: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy] = None
        # The id of the policy. Inherited from entity.
        self._policy_id: Optional[str] = None
        # The identifier of the role definition object where the policy applies. If not specified, the policy applies to all roles. Supports $filter (eq).
        self._role_definition_id: Optional[str] = None
        # The identifier of the scope where the policy is assigned.  Can be / for the tenant or a group ID. Required.
        self._scope_id: Optional[str] = None
        # The type of the scope where the policy is assigned. One of Directory, DirectoryRole. Required.
        self._scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicyAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicyAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicyAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, unified_role_management_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "policy": lambda n : setattr(self, 'policy', n.get_object_value(unified_role_management_policy.UnifiedRoleManagementPolicy)),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "scopeId": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scopeType": lambda n : setattr(self, 'scope_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def policy(self,) -> Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]:
        """
        Gets the policy property value. The policy that's associated with a policy assignment. Supports $expand and a nested $expand of the rules and effectiveRules relationships for the policy.
        Returns: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy]
        """
        return self._policy
    
    @policy.setter
    def policy(self,value: Optional[unified_role_management_policy.UnifiedRoleManagementPolicy] = None) -> None:
        """
        Sets the policy property value. The policy that's associated with a policy assignment. Supports $expand and a nested $expand of the rules and effectiveRules relationships for the policy.
        Args:
            value: Value to set for the policy property.
        """
        self._policy = value
    
    @property
    def policy_id(self,) -> Optional[str]:
        """
        Gets the policyId property value. The id of the policy. Inherited from entity.
        Returns: Optional[str]
        """
        return self._policy_id
    
    @policy_id.setter
    def policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the policyId property value. The id of the policy. Inherited from entity.
        Args:
            value: Value to set for the policy_id property.
        """
        self._policy_id = value
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. The identifier of the role definition object where the policy applies. If not specified, the policy applies to all roles. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. The identifier of the role definition object where the policy applies. If not specified, the policy applies to all roles. Supports $filter (eq).
        Args:
            value: Value to set for the role_definition_id property.
        """
        self._role_definition_id = value
    
    @property
    def scope_id(self,) -> Optional[str]:
        """
        Gets the scopeId property value. The identifier of the scope where the policy is assigned.  Can be / for the tenant or a group ID. Required.
        Returns: Optional[str]
        """
        return self._scope_id
    
    @scope_id.setter
    def scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeId property value. The identifier of the scope where the policy is assigned.  Can be / for the tenant or a group ID. Required.
        Args:
            value: Value to set for the scope_id property.
        """
        self._scope_id = value
    
    @property
    def scope_type(self,) -> Optional[str]:
        """
        Gets the scopeType property value. The type of the scope where the policy is assigned. One of Directory, DirectoryRole. Required.
        Returns: Optional[str]
        """
        return self._scope_type
    
    @scope_type.setter
    def scope_type(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeType property value. The type of the scope where the policy is assigned. One of Directory, DirectoryRole. Required.
        Args:
            value: Value to set for the scope_type property.
        """
        self._scope_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("policy", self.policy)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

