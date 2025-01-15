from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
    from .entity import Entity
    from .role_definition import RoleDefinition

from .entity import Entity

@dataclass
class RoleAssignment(Entity, Parsable):
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
    resource_scopes: Optional[list[str]] = None
    # Role definition this assignment is part of.
    role_definition: Optional[RoleDefinition] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoleAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleAssignment".casefold():
            from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment

            return DeviceAndAppManagementRoleAssignment()
        return RoleAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from .entity import Entity
        from .role_definition import RoleDefinition

        from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from .entity import Entity
        from .role_definition import RoleDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "resourceScopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_primitive_values(str)),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(RoleDefinition)),
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
        writer.write_collection_of_primitive_values("resourceScopes", self.resource_scopes)
        writer.write_object_value("roleDefinition", self.role_definition)
    

