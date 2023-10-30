from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_scope import AppScope
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
    from .unified_role_definition import UnifiedRoleDefinition
    from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

from .entity import Entity

@dataclass
class UnifiedRoleScheduleBase(Entity):
    # Read-only property with details of the app-specific scope when the role eligibility or assignment is scoped to an app. Nullable.
    app_scope: Optional[AppScope] = None
    # Identifier of the app-specific scope when the assignment or eligibility is scoped to an app. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units.
    app_scope_id: Optional[str] = None
    # When the schedule was created.
    created_date_time: Optional[datetime.datetime] = None
    # Identifier of the object through which this schedule was created.
    created_using: Optional[str] = None
    # The directory object that is the scope of the role eligibility or assignment. Read-only.
    directory_scope: Optional[DirectoryObject] = None
    # Identifier of the directory object representing the scope of the assignment or eligibility. The scope of an assignment or eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only.
    directory_scope_id: Optional[str] = None
    # When the schedule was last modified.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The principal that's getting a role assignment or that's eligible for a role through the request.
    principal: Optional[DirectoryObject] = None
    # Identifier of the principal that has been granted the role assignment or eligibility.
    principal_id: Optional[str] = None
    # Detailed information for the roleDefinition object that is referenced through the roleDefinitionId property.
    role_definition: Optional[UnifiedRoleDefinition] = None
    # Identifier of the unifiedRoleDefinition object that is being assigned to the principal or that a principal is eligible for.
    role_definition_id: Optional[str] = None
    # The status of the role assignment or eligibility request.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleScheduleBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleScheduleBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentSchedule".casefold():
            from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule

            return UnifiedRoleAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilitySchedule".casefold():
            from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

            return UnifiedRoleEligibilitySchedule()
        return UnifiedRoleScheduleBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

        fields: Dict[str, Callable[[Any], None]] = {
            "app_scope": lambda n : setattr(self, 'app_scope', n.get_object_value(AppScope)),
            "app_scope_id": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "created_using": lambda n : setattr(self, 'created_using', n.get_str_value()),
            "directory_scope": lambda n : setattr(self, 'directory_scope', n.get_object_value(DirectoryObject)),
            "directory_scope_id": lambda n : setattr(self, 'directory_scope_id', n.get_str_value()),
            "modified_date_time": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(DirectoryObject)),
            "principal_id": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "role_definition": lambda n : setattr(self, 'role_definition', n.get_object_value(UnifiedRoleDefinition)),
            "role_definition_id": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("app_scope", self.app_scope)
        writer.write_str_value("app_scope_id", self.app_scope_id)
        writer.write_datetime_value("created_date_time", self.created_date_time)
        writer.write_str_value("created_using", self.created_using)
        writer.write_object_value("directory_scope", self.directory_scope)
        writer.write_str_value("directory_scope_id", self.directory_scope_id)
        writer.write_datetime_value("modified_date_time", self.modified_date_time)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principal_id", self.principal_id)
        writer.write_object_value("role_definition", self.role_definition)
        writer.write_str_value("role_definition_id", self.role_definition_id)
        writer.write_str_value("status", self.status)
    

