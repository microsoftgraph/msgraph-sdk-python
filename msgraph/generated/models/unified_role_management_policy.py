from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity = lazy_import('msgraph.generated.models.identity')
unified_role_management_policy_rule = lazy_import('msgraph.generated.models.unified_role_management_policy_rule')

class UnifiedRoleManagementPolicy(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleManagementPolicy and sets the default values.
        """
        super().__init__()
        # Description for the policy.
        self._description: Optional[str] = None
        # Display name for the policy.
        self._display_name: Optional[str] = None
        # The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.
        self._effective_rules: Optional[List[unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule]] = None
        # This can only be set to true for a single tenant-wide policy which will apply to all scopes and roles. Set the scopeId to / and scopeType to Directory. Supports $filter (eq, ne).
        self._is_organization_default: Optional[bool] = None
        # The identity who last modified the role setting.
        self._last_modified_by: Optional[identity.Identity] = None
        # The time when the role setting was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The collection of rules like approval rules and expiration rules. Supports $expand.
        self._rules: Optional[List[unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule]] = None
        # The identifier of the scope where the policy is created. Can be / for the tenant or a group ID. Required.
        self._scope_id: Optional[str] = None
        # The type of the scope where the policy is created. One of Directory, DirectoryRole. Required.
        self._scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleManagementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleManagementPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Description for the policy.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Description for the policy.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name for the policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name for the policy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def effective_rules(self,) -> Optional[List[unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule]]:
        """
        Gets the effectiveRules property value. The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.
        Returns: Optional[List[unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule]]
        """
        return self._effective_rules
    
    @effective_rules.setter
    def effective_rules(self,value: Optional[List[unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule]] = None) -> None:
        """
        Sets the effectiveRules property value. The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.
        Args:
            value: Value to set for the effectiveRules property.
        """
        self._effective_rules = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "effective_rules": lambda n : setattr(self, 'effective_rules', n.get_collection_of_object_values(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule)),
            "is_organization_default": lambda n : setattr(self, 'is_organization_default', n.get_bool_value()),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity.Identity)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule)),
            "scope_id": lambda n : setattr(self, 'scope_id', n.get_str_value()),
            "scope_type": lambda n : setattr(self, 'scope_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_organization_default(self,) -> Optional[bool]:
        """
        Gets the isOrganizationDefault property value. This can only be set to true for a single tenant-wide policy which will apply to all scopes and roles. Set the scopeId to / and scopeType to Directory. Supports $filter (eq, ne).
        Returns: Optional[bool]
        """
        return self._is_organization_default
    
    @is_organization_default.setter
    def is_organization_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOrganizationDefault property value. This can only be set to true for a single tenant-wide policy which will apply to all scopes and roles. Set the scopeId to / and scopeType to Directory. Supports $filter (eq, ne).
        Args:
            value: Value to set for the isOrganizationDefault property.
        """
        self._is_organization_default = value
    
    @property
    def last_modified_by(self,) -> Optional[identity.Identity]:
        """
        Gets the lastModifiedBy property value. The identity who last modified the role setting.
        Returns: Optional[identity.Identity]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the lastModifiedBy property value. The identity who last modified the role setting.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The time when the role setting was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The time when the role setting was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def rules(self,) -> Optional[List[unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule]]:
        """
        Gets the rules property value. The collection of rules like approval rules and expiration rules. Supports $expand.
        Returns: Optional[List[unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule]]
        """
        return self._rules
    
    @rules.setter
    def rules(self,value: Optional[List[unified_role_management_policy_rule.UnifiedRoleManagementPolicyRule]] = None) -> None:
        """
        Sets the rules property value. The collection of rules like approval rules and expiration rules. Supports $expand.
        Args:
            value: Value to set for the rules property.
        """
        self._rules = value
    
    @property
    def scope_id(self,) -> Optional[str]:
        """
        Gets the scopeId property value. The identifier of the scope where the policy is created. Can be / for the tenant or a group ID. Required.
        Returns: Optional[str]
        """
        return self._scope_id
    
    @scope_id.setter
    def scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeId property value. The identifier of the scope where the policy is created. Can be / for the tenant or a group ID. Required.
        Args:
            value: Value to set for the scopeId property.
        """
        self._scope_id = value
    
    @property
    def scope_type(self,) -> Optional[str]:
        """
        Gets the scopeType property value. The type of the scope where the policy is created. One of Directory, DirectoryRole. Required.
        Returns: Optional[str]
        """
        return self._scope_type
    
    @scope_type.setter
    def scope_type(self,value: Optional[str] = None) -> None:
        """
        Sets the scopeType property value. The type of the scope where the policy is created. One of Directory, DirectoryRole. Required.
        Args:
            value: Value to set for the scopeType property.
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("effectiveRules", self.effective_rules)
        writer.write_bool_value("isOrganizationDefault", self.is_organization_default)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

