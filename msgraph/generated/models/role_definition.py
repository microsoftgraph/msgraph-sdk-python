from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_role_definition, entity, role_assignment, role_permission

from . import entity

@dataclass
class RoleDefinition(entity.Entity):
    # Description of the Role definition.
    description: Optional[str] = None
    # Display Name of the Role definition.
    display_name: Optional[str] = None
    # Type of Role. Set to True if it is built-in, or set to False if it is a custom role definition.
    is_built_in: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of Role assignments for this role definition.
    role_assignments: Optional[List[role_assignment.RoleAssignment]] = None
    # List of Role Permissions this role is allowed to perform. These must match the actionName that is defined as part of the rolePermission.
    role_permissions: Optional[List[role_permission.RolePermission]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleDefinition".casefold():
            from . import device_and_app_management_role_definition

            return device_and_app_management_role_definition.DeviceAndAppManagementRoleDefinition()
        return RoleDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_role_definition, entity, role_assignment, role_permission

        from . import device_and_app_management_role_definition, entity, role_assignment, role_permission

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(role_assignment.RoleAssignment)),
            "rolePermissions": lambda n : setattr(self, 'role_permissions', n.get_collection_of_object_values(role_permission.RolePermission)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("rolePermissions", self.role_permissions)
    

