from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_scope import AppScope
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
    from .unified_role_definition import UnifiedRoleDefinition
    from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance

from .entity import Entity

@dataclass
class UnifiedRoleScheduleInstanceBase(Entity):
    # Read-only property with details of the app-specific scope when the assignment or role eligibility is scoped to an app. Nullable.
    app_scope: Optional[AppScope] = None
    # Identifier of the app-specific scope when the assignment or role eligibility is scoped to an app. The scope of an assignment or role eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.
    app_scope_id: Optional[str] = None
    # The directory object that is the scope of the assignment or role eligibility. Read-only.
    directory_scope: Optional[DirectoryObject] = None
    # Identifier of the directory object representing the scope of the assignment or role eligibility. The scope of an assignment or role eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.
    directory_scope_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The principal that's getting a role assignment or role eligibility through the request.
    principal: Optional[DirectoryObject] = None
    # Identifier of the principal that has been granted the role assignment or that's eligible for a role.
    principal_id: Optional[str] = None
    # Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.
    role_definition: Optional[UnifiedRoleDefinition] = None
    # Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that the principal is eligible for.
    role_definition_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleScheduleInstanceBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleScheduleInstanceBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentScheduleInstance".casefold():
            from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance

            return UnifiedRoleAssignmentScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilityScheduleInstance".casefold():
            from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance

            return UnifiedRoleEligibilityScheduleInstance()
        return UnifiedRoleScheduleInstanceBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance

        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance

        fields: Dict[str, Callable[[Any], None]] = {
            "appScope": lambda n : setattr(self, 'app_scope', n.get_object_value(AppScope)),
            "appScopeId": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
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
        writer.write_object_value("directoryScope", self.directory_scope)
        writer.write_str_value("directoryScopeId", self.directory_scope_id)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
    

