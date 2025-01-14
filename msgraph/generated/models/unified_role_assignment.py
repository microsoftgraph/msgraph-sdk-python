from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_scope import AppScope
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .unified_role_definition import UnifiedRoleDefinition

from .entity import Entity

@dataclass
class UnifiedRoleAssignment(Entity, Parsable):
    # Read-only property with details of the app specific scope when the assignment scope is app specific. Containment entity. Supports $expand for the entitlement provider only.
    app_scope: Optional[AppScope] = None
    # Identifier of the app specific scope when the assignment scope is app specific. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by a resource application only. For the entitlement management provider, use this property to specify a catalog. For example, /AccessPackageCatalog/beedadfe-01d5-4025-910b-84abb9369997. Supports $filter (eq, in). For example, /roleManagement/entitlementManagement/roleAssignments?$filter=appScopeId eq '/AccessPackageCatalog/{catalog id}'.
    app_scope_id: Optional[str] = None
    # The condition property
    condition: Optional[str] = None
    # The directory object that is the scope of the assignment. Read-only. Supports $expand for the directory provider.
    directory_scope: Optional[DirectoryObject] = None
    # Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications, unlike app scopes that are defined and understood by a resource application only. Supports $filter (eq, in).
    directory_scope_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Referencing the assigned principal. Read-only. Supports $expand except for the Exchange provider.
    principal: Optional[DirectoryObject] = None
    # Identifier of the principal to which the assignment is granted. Supported principals are users, role-assignable groups, and service principals. Supports $filter (eq, in).
    principal_id: Optional[str] = None
    # The roleDefinition the assignment is for. Supports $expand.
    role_definition: Optional[UnifiedRoleDefinition] = None
    # Identifier of the unifiedRoleDefinition the assignment is for. Read-only. Supports $filter (eq, in).
    role_definition_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleAssignment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleAssignment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_definition import UnifiedRoleDefinition

        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_definition import UnifiedRoleDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "appScope": lambda n : setattr(self, 'app_scope', n.get_object_value(AppScope)),
            "appScopeId": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
            "condition": lambda n : setattr(self, 'condition', n.get_str_value()),
            "directoryScope": lambda n : setattr(self, 'directory_scope', n.get_object_value(DirectoryObject)),
            "directoryScopeId": lambda n : setattr(self, 'directory_scope_id', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(UnifiedRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
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
        writer.write_object_value("appScope", self.app_scope)
        writer.write_str_value("appScopeId", self.app_scope_id)
        writer.write_str_value("condition", self.condition)
        writer.write_object_value("directoryScope", self.directory_scope)
        writer.write_str_value("directoryScopeId", self.directory_scope_id)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
    

