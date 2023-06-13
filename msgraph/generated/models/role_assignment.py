from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_and_app_management_role_assignment, entity, role_definition

from . import entity

@dataclass
class RoleAssignment(entity.Entity):
    """
    The Role Assignment resource. Role assignments tie together a role definition with members and scopes. There can be one or more role assignments per role. This applies to custom and built-in roles.
    """
    # Description of the Role Assignment.
    description: Optional[str] = None
    # The display or friendly name of the role Assignment.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of ids of role scope member security groups.  These are IDs from Azure Active Directory.
    resource_scopes: Optional[List[str]] = None
    # Role definition this assignment is part of.
    role_definition: Optional[role_definition.RoleDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RoleAssignment
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.deviceAndAppManagementRoleAssignment":
                from . import device_and_app_management_role_assignment

                return device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment()
        return RoleAssignment()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_and_app_management_role_assignment, entity, role_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resourceScopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_primitive_values(str)),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(role_definition.RoleDefinition)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("resourceScopes", self.resource_scopes)
        writer.write_object_value("roleDefinition", self.role_definition)
    

