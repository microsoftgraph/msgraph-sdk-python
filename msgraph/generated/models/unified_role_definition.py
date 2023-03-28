from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_role_permission

from . import entity

class UnifiedRoleDefinition(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new unifiedRoleDefinition and sets the default values.
        """
        super().__init__()
        # The description for the unifiedRoleDefinition. Read-only when isBuiltIn is true.
        self._description: Optional[str] = None
        # The display name for the unifiedRoleDefinition. Read-only when isBuiltIn is true. Required.  Supports $filter (eq, in).
        self._display_name: Optional[str] = None
        # Read-only collection of role definitions that the given role definition inherits from. Only Azure AD built-in roles (isBuiltIn is true) support this attribute. Supports $expand.
        self._inherits_permissions_from: Optional[List[UnifiedRoleDefinition]] = None
        # Flag indicating whether the role definition is part of the default set included in Azure Active Directory (Azure AD) or a custom definition. Read-only. Supports $filter (eq, in).
        self._is_built_in: Optional[bool] = None
        # Flag indicating whether the role is enabled for assignment. If false the role is not available for assignment. Read-only when isBuiltIn is true.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # List of the scopes or permissions the role definition applies to. Currently only / is supported. Read-only when isBuiltIn is true. DO NOT USE. This will be deprecated soon. Attach scope to role assignment.
        self._resource_scopes: Optional[List[str]] = None
        # List of permissions included in the role. Read-only when isBuiltIn is true. Required.
        self._role_permissions: Optional[List[unified_role_permission.UnifiedRolePermission]] = None
        # Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories.
        self._template_id: Optional[str] = None
        # Indicates version of the role definition. Read-only when isBuiltIn is true.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleDefinition()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description for the unifiedRoleDefinition. Read-only when isBuiltIn is true.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description for the unifiedRoleDefinition. Read-only when isBuiltIn is true.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the unifiedRoleDefinition. Read-only when isBuiltIn is true. Required.  Supports $filter (eq, in).
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the unifiedRoleDefinition. Read-only when isBuiltIn is true. Required.  Supports $filter (eq, in).
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, unified_role_permission

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "inheritsPermissionsFrom": lambda n : setattr(self, 'inherits_permissions_from', n.get_collection_of_object_values(UnifiedRoleDefinition)),
            "isBuiltIn": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "resourceScopes": lambda n : setattr(self, 'resource_scopes', n.get_collection_of_primitive_values(str)),
            "rolePermissions": lambda n : setattr(self, 'role_permissions', n.get_collection_of_object_values(unified_role_permission.UnifiedRolePermission)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def inherits_permissions_from(self,) -> Optional[List[UnifiedRoleDefinition]]:
        """
        Gets the inheritsPermissionsFrom property value. Read-only collection of role definitions that the given role definition inherits from. Only Azure AD built-in roles (isBuiltIn is true) support this attribute. Supports $expand.
        Returns: Optional[List[UnifiedRoleDefinition]]
        """
        return self._inherits_permissions_from
    
    @inherits_permissions_from.setter
    def inherits_permissions_from(self,value: Optional[List[UnifiedRoleDefinition]] = None) -> None:
        """
        Sets the inheritsPermissionsFrom property value. Read-only collection of role definitions that the given role definition inherits from. Only Azure AD built-in roles (isBuiltIn is true) support this attribute. Supports $expand.
        Args:
            value: Value to set for the inherits_permissions_from property.
        """
        self._inherits_permissions_from = value
    
    @property
    def is_built_in(self,) -> Optional[bool]:
        """
        Gets the isBuiltIn property value. Flag indicating whether the role definition is part of the default set included in Azure Active Directory (Azure AD) or a custom definition. Read-only. Supports $filter (eq, in).
        Returns: Optional[bool]
        """
        return self._is_built_in
    
    @is_built_in.setter
    def is_built_in(self,value: Optional[bool] = None) -> None:
        """
        Sets the isBuiltIn property value. Flag indicating whether the role definition is part of the default set included in Azure Active Directory (Azure AD) or a custom definition. Read-only. Supports $filter (eq, in).
        Args:
            value: Value to set for the is_built_in property.
        """
        self._is_built_in = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Flag indicating whether the role is enabled for assignment. If false the role is not available for assignment. Read-only when isBuiltIn is true.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Flag indicating whether the role is enabled for assignment. If false the role is not available for assignment. Read-only when isBuiltIn is true.
        Args:
            value: Value to set for the is_enabled property.
        """
        self._is_enabled = value
    
    @property
    def resource_scopes(self,) -> Optional[List[str]]:
        """
        Gets the resourceScopes property value. List of the scopes or permissions the role definition applies to. Currently only / is supported. Read-only when isBuiltIn is true. DO NOT USE. This will be deprecated soon. Attach scope to role assignment.
        Returns: Optional[List[str]]
        """
        return self._resource_scopes
    
    @resource_scopes.setter
    def resource_scopes(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the resourceScopes property value. List of the scopes or permissions the role definition applies to. Currently only / is supported. Read-only when isBuiltIn is true. DO NOT USE. This will be deprecated soon. Attach scope to role assignment.
        Args:
            value: Value to set for the resource_scopes property.
        """
        self._resource_scopes = value
    
    @property
    def role_permissions(self,) -> Optional[List[unified_role_permission.UnifiedRolePermission]]:
        """
        Gets the rolePermissions property value. List of permissions included in the role. Read-only when isBuiltIn is true. Required.
        Returns: Optional[List[unified_role_permission.UnifiedRolePermission]]
        """
        return self._role_permissions
    
    @role_permissions.setter
    def role_permissions(self,value: Optional[List[unified_role_permission.UnifiedRolePermission]] = None) -> None:
        """
        Sets the rolePermissions property value. List of permissions included in the role. Read-only when isBuiltIn is true. Required.
        Args:
            value: Value to set for the role_permissions property.
        """
        self._role_permissions = value
    
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
        writer.write_collection_of_object_values("inheritsPermissionsFrom", self.inherits_permissions_from)
        writer.write_bool_value("isBuiltIn", self.is_built_in)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_collection_of_primitive_values("resourceScopes", self.resource_scopes)
        writer.write_collection_of_object_values("rolePermissions", self.role_permissions)
        writer.write_str_value("templateId", self.template_id)
        writer.write_str_value("version", self.version)
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories.
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. Custom template identifier that can be set when isBuiltIn is false but is read-only when isBuiltIn is true. This identifier is typically used if one needs an identifier to be the same across different directories.
        Args:
            value: Value to set for the template_id property.
        """
        self._template_id = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Indicates version of the role definition. Read-only when isBuiltIn is true.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Indicates version of the role definition. Read-only when isBuiltIn is true.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

