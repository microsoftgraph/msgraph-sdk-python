from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_scope import AppScope
    from .directory_object import DirectoryObject
    from .request import Request
    from .request_schedule import RequestSchedule
    from .ticket_info import TicketInfo
    from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
    from .unified_role_definition import UnifiedRoleDefinition
    from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
    from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions

from .request import Request

@dataclass
class UnifiedRoleAssignmentScheduleRequest(Request, Parsable):
    # Represents the type of the operation on the role assignment request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew, selfExtend, selfRenew, unknownFutureValue. adminAssign: For administrators to assign roles to principals.adminRemove: For administrators to remove principals from roles. adminUpdate: For administrators to change existing role assignments.adminExtend: For administrators to extend expiring assignments.adminRenew: For administrators to renew expired assignments.selfActivate: For principals to activate their assignments.selfDeactivate: For principals to deactivate their active assignments.selfExtend: For principals to request to extend their expiring assignments.selfRenew: For principals to request to renew their expired assignments.
    action: Optional[UnifiedRoleScheduleRequestActions] = None
    # If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it's null. Supports $expand and $select nested in $expand.
    activated_using: Optional[UnifiedRoleEligibilitySchedule] = None
    # Read-only property with details of the app-specific scope when the assignment is scoped to an app. Nullable. Supports $expand.
    app_scope: Optional[AppScope] = None
    # Identifier of the app-specific scope when the assignment is scoped to an app. The scope of an assignment determines the set of resources for which the principal has been granted access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units. Supports $filter (eq, ne, and on null values).
    app_scope_id: Optional[str] = None
    # The directory object that is the scope of the assignment. Read-only. Supports $expand.
    directory_scope: Optional[DirectoryObject] = None
    # Identifier of the directory object representing the scope of the assignment. The scope of an assignment determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only. Supports $filter (eq, ne, and on null values).
    directory_scope_id: Optional[str] = None
    # Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.
    is_validation_only: Optional[bool] = None
    # A message provided by users and administrators when create they create the unifiedRoleAssignmentScheduleRequest object.
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The principal that's getting a role assignment through the request. Supports $expand and $select nested in $expand for id only.
    principal: Optional[DirectoryObject] = None
    # Identifier of the principal that has been granted the assignment. Can be a user, role-assignable group, or a service principal. Supports $filter (eq, ne).
    principal_id: Optional[str] = None
    # Detailed information for the unifiedRoleDefinition object that is referenced through the roleDefinitionId property. Supports $expand and $select nested in $expand.
    role_definition: Optional[UnifiedRoleDefinition] = None
    # Identifier of the unifiedRoleDefinition object that is being assigned to the principal. Supports $filter (eq, ne).
    role_definition_id: Optional[str] = None
    # The period of the role assignment. Recurring schedules are currently unsupported.
    schedule_info: Optional[RequestSchedule] = None
    # The schedule for an eligible role assignment that is referenced through the targetScheduleId property. Supports $expand and $select nested in $expand.
    target_schedule: Optional[UnifiedRoleAssignmentSchedule] = None
    # Identifier of the schedule object that's linked to the assignment request. Supports $filter (eq, ne).
    target_schedule_id: Optional[str] = None
    # Ticket details linked to the role assignment request including details of the ticket number and ticket system.
    ticket_info: Optional[TicketInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleAssignmentScheduleRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignmentScheduleRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleAssignmentScheduleRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .request import Request
        from .request_schedule import RequestSchedule
        from .ticket_info import TicketInfo
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions

        from .app_scope import AppScope
        from .directory_object import DirectoryObject
        from .request import Request
        from .request_schedule import RequestSchedule
        from .ticket_info import TicketInfo
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_schedule_request_actions import UnifiedRoleScheduleRequestActions

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(UnifiedRoleScheduleRequestActions)),
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(UnifiedRoleEligibilitySchedule)),
            "appScope": lambda n : setattr(self, 'app_scope', n.get_object_value(AppScope)),
            "appScopeId": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
            "directoryScope": lambda n : setattr(self, 'directory_scope', n.get_object_value(DirectoryObject)),
            "directoryScopeId": lambda n : setattr(self, 'directory_scope_id', n.get_str_value()),
            "isValidationOnly": lambda n : setattr(self, 'is_validation_only', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(DirectoryObject)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "roleDefinition": lambda n : setattr(self, 'role_definition', n.get_object_value(UnifiedRoleDefinition)),
            "roleDefinitionId": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
            "targetSchedule": lambda n : setattr(self, 'target_schedule', n.get_object_value(UnifiedRoleAssignmentSchedule)),
            "targetScheduleId": lambda n : setattr(self, 'target_schedule_id', n.get_str_value()),
            "ticketInfo": lambda n : setattr(self, 'ticket_info', n.get_object_value(TicketInfo)),
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
        writer.write_enum_value("action", self.action)
        writer.write_object_value("activatedUsing", self.activated_using)
        writer.write_object_value("appScope", self.app_scope)
        writer.write_str_value("appScopeId", self.app_scope_id)
        writer.write_object_value("directoryScope", self.directory_scope)
        writer.write_str_value("directoryScopeId", self.directory_scope_id)
        writer.write_bool_value("isValidationOnly", self.is_validation_only)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("principal", self.principal)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_object_value("roleDefinition", self.role_definition)
        writer.write_str_value("roleDefinitionId", self.role_definition_id)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_object_value("targetSchedule", self.target_schedule)
        writer.write_str_value("targetScheduleId", self.target_schedule_id)
        writer.write_object_value("ticketInfo", self.ticket_info)
    

