from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity import Identity
    from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

from .entity import Entity

@dataclass
class UnifiedRoleManagementPolicy(Entity, Parsable):
    # Description for the policy.
    description: Optional[str] = None
    # Display name for the policy.
    display_name: Optional[str] = None
    # The list of effective rules like approval rules and expiration rules evaluated based on inherited referenced rules. For example, if there is a tenant-wide policy to enforce enabling an approval rule, the effective rule will be to enable approval even if the policy has a rule to disable approval. Supports $expand.
    effective_rules: Optional[list[UnifiedRoleManagementPolicyRule]] = None
    # This can only be set to true for a single tenant-wide policy which will apply to all scopes and roles. Set the scopeId to / and scopeType to Directory. Supports $filter (eq, ne).
    is_organization_default: Optional[bool] = None
    # The identity who last modified the role setting.
    last_modified_by: Optional[Identity] = None
    # The time when the role setting was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The collection of rules like approval rules and expiration rules. Supports $expand.
    rules: Optional[list[UnifiedRoleManagementPolicyRule]] = None
    # The identifier of the scope where the policy is created. Can be / for the tenant or a group ID. Required.
    scope_id: Optional[str] = None
    # The type of the scope where the policy is created. One of Directory, DirectoryRole, Group. Required.
    scope_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleManagementPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleManagementPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleManagementPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity import Identity
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        from .entity import Entity
        from .identity import Identity
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "effectiveRules": lambda n : setattr(self, 'effective_rules', n.get_collection_of_object_values(UnifiedRoleManagementPolicyRule)),
            "isOrganizationDefault": lambda n : setattr(self, 'is_organization_default', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(Identity)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "rules": lambda n : setattr(self, 'rules', n.get_collection_of_object_values(UnifiedRoleManagementPolicyRule)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("effectiveRules", self.effective_rules)
        writer.write_bool_value("isOrganizationDefault", self.is_organization_default)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("rules", self.rules)
        writer.write_str_value("scopeId", self.scope_id)
        writer.write_str_value("scopeType", self.scope_type)
    

