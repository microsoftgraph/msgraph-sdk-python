from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .unified_role_permission import UnifiedRolePermission

from .entity import Entity

@dataclass
class UnifiedRoleDefinition(Entity, Parsable):
    # The description for the unifiedRoleDefinition. Read-only when isBuiltIn is true.
    description: Optional[str] = None
    # The display name for the unifiedRoleDefinition. Read-only when isBuiltIn is true. Required.  Supports $filter (eq, in).
    display_name: Optional[str] = None
    # Read-only collection of role definitions that the given role definition inherits from. Only Microsoft Entra built-in roles (isBuiltIn is true) support this attribute. Supports $expand.
    inherits_permissions_from: Optional[list[UnifiedRoleDefinition]] = None
    # Flag indicating whether the role definition is part of the default set included in Microsoft Entra or a custom definition. Read-only. Supports $filter (eq, in).
    is_built_in: Optional[bool] = None
    # Flag indicating whether the role is enabled for assignment. If false the role is not available for assignment. Read-only when isBuiltIn is true.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # List of the scopes or permissions the role definition applies to. Currently only / is supported. Read-only when isBuiltIn is true. DO NOT USE. This will be deprecated soon. Attach scope to role assignment.
    resource_scopes: Optional[list[str]] = None
    # List of permissions included in the role. Read-only when isBuiltIn is true. Required.
    role_permissions: Optional[list[UnifiedRolePermission]] = None
    # Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories.
    template_id: Optional[str] = None
    # Indicates version of the role definition. Read-only when isBuiltIn is true.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .unified_role_permission import UnifiedRolePermission

        from .entity import Entity
        from .unified_role_permission import UnifiedRolePermission

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "inheritsPermissionsFrom": lambda n : setattr(self, 'inherits_permissions_from', n.get_collection_of_object_values(UnifiedRoleDefinition)),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "resourceScopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_primitive_values(str)),
            "rolePermissions": lambda n : setattr(self, 'role_permissions', n.get_collection_of_object_values(UnifiedRolePermission)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_collection_of_object_values("inheritsPermissionsFrom", self.inherits_permissions_from)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_primitive_values("resourceScopes", self.resource_scopes)
        writer.write_collection_of_object_values("rolePermissions", self.role_permissions)
        writer.write_str_value("templateId", self.template_id)
        writer.write_str_value("version", self.version)
    

