from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
    from .entity import Entity
    from .role_assignment import RoleAssignment
    from .role_permission import RolePermission

from .entity import Entity

@dataclass
class RoleDefinition(Entity, Parsable):
    """
    The Role Definition resource. The role definition is the foundation of role based access in Intune. The role combines an Intune resource such as a Mobile App and associated role permissions such as Create or Read for the resource. There are two types of roles, built-in and custom. Built-in roles cannot be modified. Both built-in roles and custom roles must have assignments to be enforced. Create custom roles if you want to define a role that allows any of the available resources and role permissions to be combined into a single role.
    """
    # Description of the Role definition.
    description: Optional[str] = None
    # Display Name of the Role definition.
    display_name: Optional[str] = None
    # Type of Role. Set to True if it is built-in, or set to False if it is a custom role definition.
    is_built_in: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Role assignments for this role definition.
    role_assignments: Optional[list[RoleAssignment]] = None
    # List of Role Permissions this role is allowed to perform. These must match the actionName that is defined as part of the rolePermission.
    role_permissions: Optional[list[RolePermission]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoleDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleDefinition".casefold():
            from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition

            return DeviceAndAppManagementRoleDefinition()
        return RoleDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
        from .entity import Entity
        from .role_assignment import RoleAssignment
        from .role_permission import RolePermission

        from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
        from .entity import Entity
        from .role_assignment import RoleAssignment
        from .role_permission import RolePermission

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(RoleAssignment)),
            "rolePermissions": lambda n : setattr(self, 'role_permissions', n.get_collection_of_object_values(RolePermission)),
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
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("rolePermissions", self.role_permissions)
    

