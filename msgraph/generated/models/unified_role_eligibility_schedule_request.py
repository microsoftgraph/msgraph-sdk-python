from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_scope = lazy_import('msgraph.generated.models.app_scope')
directory_object = lazy_import('msgraph.generated.models.directory_object')
request = lazy_import('msgraph.generated.models.request')
request_schedule = lazy_import('msgraph.generated.models.request_schedule')
ticket_info = lazy_import('msgraph.generated.models.ticket_info')
unified_role_definition = lazy_import('msgraph.generated.models.unified_role_definition')
unified_role_eligibility_schedule = lazy_import('msgraph.generated.models.unified_role_eligibility_schedule')
unified_role_schedule_request_actions = lazy_import('msgraph.generated.models.unified_role_schedule_request_actions')

class UnifiedRoleEligibilityScheduleRequest(request.Request):
    @property
    def action(self,) -> Optional[unified_role_schedule_request_actions.UnifiedRoleScheduleRequestActions]:
        """
        Gets the action property value. Represents the type of operation on the role eligibility request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew, selfExtend, selfRenew, unknownFutureValue. adminAssign: For administrators to assign eligible roles to principals.adminRemove: For administrators to remove eligible roles from principals. adminUpdate: For administrators to change existing role eligibilities.adminExtend: For administrators to extend expiring role eligibilities.adminRenew: For administrators to renew expired eligibilities.selfActivate: For users to activate their assignments.selfDeactivate: For users to deactivate their active assignments.selfExtend: For users to request to extend their expiring assignments.selfRenew: For users to request to renew their expired assignments.
        Returns: Optional[unified_role_schedule_request_actions.UnifiedRoleScheduleRequestActions]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[unified_role_schedule_request_actions.UnifiedRoleScheduleRequestActions] = None) -> None:
        """
        Sets the action property value. Represents the type of operation on the role eligibility request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew, selfExtend, selfRenew, unknownFutureValue. adminAssign: For administrators to assign eligible roles to principals.adminRemove: For administrators to remove eligible roles from principals. adminUpdate: For administrators to change existing role eligibilities.adminExtend: For administrators to extend expiring role eligibilities.adminRenew: For administrators to renew expired eligibilities.selfActivate: For users to activate their assignments.selfDeactivate: For users to deactivate their active assignments.selfExtend: For users to request to extend their expiring assignments.selfRenew: For users to request to renew their expired assignments.
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def app_scope(self,) -> Optional[app_scope.AppScope]:
        """
        Gets the appScope property value. Read-only property with details of the app-specific scope when the role eligibility is scoped to an app. Nullable. Supports $expand.
        Returns: Optional[app_scope.AppScope]
        """
        return self._app_scope
    
    @app_scope.setter
    def app_scope(self,value: Optional[app_scope.AppScope] = None) -> None:
        """
        Sets the appScope property value. Read-only property with details of the app-specific scope when the role eligibility is scoped to an app. Nullable. Supports $expand.
        Args:
            value: Value to set for the appScope property.
        """
        self._app_scope = value
    
    @property
    def app_scope_id(self,) -> Optional[str]:
        """
        Gets the appScopeId property value. Identifier of the app-specific scope when the role eligibility is scoped to an app. The scope of a role eligibility determines the set of resources for which the principal is eligible to access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units. Supports $filter (eq, ne, and on null values).
        Returns: Optional[str]
        """
        return self._app_scope_id
    
    @app_scope_id.setter
    def app_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the appScopeId property value. Identifier of the app-specific scope when the role eligibility is scoped to an app. The scope of a role eligibility determines the set of resources for which the principal is eligible to access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units. Supports $filter (eq, ne, and on null values).
        Args:
            value: Value to set for the appScopeId property.
        """
        self._app_scope_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRoleEligibilityScheduleRequest and sets the default values.
        """
        super().__init__()
        # Represents the type of operation on the role eligibility request. The possible values are: adminAssign, adminUpdate, adminRemove, selfActivate, selfDeactivate, adminExtend, adminRenew, selfExtend, selfRenew, unknownFutureValue. adminAssign: For administrators to assign eligible roles to principals.adminRemove: For administrators to remove eligible roles from principals. adminUpdate: For administrators to change existing role eligibilities.adminExtend: For administrators to extend expiring role eligibilities.adminRenew: For administrators to renew expired eligibilities.selfActivate: For users to activate their assignments.selfDeactivate: For users to deactivate their active assignments.selfExtend: For users to request to extend their expiring assignments.selfRenew: For users to request to renew their expired assignments.
        self._action: Optional[unified_role_schedule_request_actions.UnifiedRoleScheduleRequestActions] = None
        # Read-only property with details of the app-specific scope when the role eligibility is scoped to an app. Nullable. Supports $expand.
        self._app_scope: Optional[app_scope.AppScope] = None
        # Identifier of the app-specific scope when the role eligibility is scoped to an app. The scope of a role eligibility determines the set of resources for which the principal is eligible to access. App scopes are scopes that are defined and understood by this application only. Use / for tenant-wide app scopes. Use directoryScopeId to limit the scope to particular directory objects, for example, administrative units. Supports $filter (eq, ne, and on null values).
        self._app_scope_id: Optional[str] = None
        # The directory object that is the scope of the role eligibility. Read-only. Supports $expand.
        self._directory_scope: Optional[directory_object.DirectoryObject] = None
        # Identifier of the directory object representing the scope of the role eligibility. The scope of a role eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only. Supports $filter (eq, ne, and on null values).
        self._directory_scope_id: Optional[str] = None
        # Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.
        self._is_validation_only: Optional[bool] = None
        # A message provided by users and administrators when create they create the unifiedRoleEligibilityScheduleRequest object.
        self._justification: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The principal that's getting a role eligibility through the request. Supports $expand.
        self._principal: Optional[directory_object.DirectoryObject] = None
        # Identifier of the principal that has been granted the role eligibility. Can be a user or a role-assignable group. You can grant only active assignments service principals.Supports $filter (eq, ne).
        self._principal_id: Optional[str] = None
        # Detailed information for the unifiedRoleDefinition object that is referenced through the roleDefinitionId property. Supports $expand.
        self._role_definition: Optional[unified_role_definition.UnifiedRoleDefinition] = None
        # Identifier of the unifiedRoleDefinition object that is being assigned to the principal. Supports $filter (eq, ne).
        self._role_definition_id: Optional[str] = None
        # The period of the role eligibility. Recurring schedules are currently unsupported.
        self._schedule_info: Optional[request_schedule.RequestSchedule] = None
        # The schedule for a role eligibility that is referenced through the targetScheduleId property. Supports $expand.
        self._target_schedule: Optional[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule] = None
        # Identifier of the schedule object that's linked to the eligibility request. Supports $filter (eq, ne).
        self._target_schedule_id: Optional[str] = None
        # Ticket details linked to the role eligibility request including details of the ticket number and ticket system. Optional.
        self._ticket_info: Optional[ticket_info.TicketInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleEligibilityScheduleRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleEligibilityScheduleRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleEligibilityScheduleRequest()
    
    @property
    def directory_scope(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the directoryScope property value. The directory object that is the scope of the role eligibility. Read-only. Supports $expand.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._directory_scope
    
    @directory_scope.setter
    def directory_scope(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the directoryScope property value. The directory object that is the scope of the role eligibility. Read-only. Supports $expand.
        Args:
            value: Value to set for the directoryScope property.
        """
        self._directory_scope = value
    
    @property
    def directory_scope_id(self,) -> Optional[str]:
        """
        Gets the directoryScopeId property value. Identifier of the directory object representing the scope of the role eligibility. The scope of a role eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only. Supports $filter (eq, ne, and on null values).
        Returns: Optional[str]
        """
        return self._directory_scope_id
    
    @directory_scope_id.setter
    def directory_scope_id(self,value: Optional[str] = None) -> None:
        """
        Sets the directoryScopeId property value. Identifier of the directory object representing the scope of the role eligibility. The scope of a role eligibility determines the set of resources for which the principal has been granted access. Directory scopes are shared scopes stored in the directory that are understood by multiple applications. Use / for tenant-wide scope. Use appScopeId to limit the scope to an application only. Supports $filter (eq, ne, and on null values).
        Args:
            value: Value to set for the directoryScopeId property.
        """
        self._directory_scope_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(unified_role_schedule_request_actions.UnifiedRoleScheduleRequestActions)),
            "app_scope": lambda n : setattr(self, 'app_scope', n.get_object_value(app_scope.AppScope)),
            "app_scope_id": lambda n : setattr(self, 'app_scope_id', n.get_str_value()),
            "directory_scope": lambda n : setattr(self, 'directory_scope', n.get_object_value(directory_object.DirectoryObject)),
            "directory_scope_id": lambda n : setattr(self, 'directory_scope_id', n.get_str_value()),
            "is_validation_only": lambda n : setattr(self, 'is_validation_only', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "principal": lambda n : setattr(self, 'principal', n.get_object_value(directory_object.DirectoryObject)),
            "principal_id": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "role_definition": lambda n : setattr(self, 'role_definition', n.get_object_value(unified_role_definition.UnifiedRoleDefinition)),
            "role_definition_id": lambda n : setattr(self, 'role_definition_id', n.get_str_value()),
            "schedule_info": lambda n : setattr(self, 'schedule_info', n.get_object_value(request_schedule.RequestSchedule)),
            "target_schedule": lambda n : setattr(self, 'target_schedule', n.get_object_value(unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule)),
            "target_schedule_id": lambda n : setattr(self, 'target_schedule_id', n.get_str_value()),
            "ticket_info": lambda n : setattr(self, 'ticket_info', n.get_object_value(ticket_info.TicketInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_validation_only(self,) -> Optional[bool]:
        """
        Gets the isValidationOnly property value. Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.
        Returns: Optional[bool]
        """
        return self._is_validation_only
    
    @is_validation_only.setter
    def is_validation_only(self,value: Optional[bool] = None) -> None:
        """
        Sets the isValidationOnly property value. Determines whether the call is a validation or an actual call. Only set this property if you want to check whether an activation is subject to additional rules like MFA before actually submitting the request.
        Args:
            value: Value to set for the isValidationOnly property.
        """
        self._is_validation_only = value
    
    @property
    def justification(self,) -> Optional[str]:
        """
        Gets the justification property value. A message provided by users and administrators when create they create the unifiedRoleEligibilityScheduleRequest object.
        Returns: Optional[str]
        """
        return self._justification
    
    @justification.setter
    def justification(self,value: Optional[str] = None) -> None:
        """
        Sets the justification property value. A message provided by users and administrators when create they create the unifiedRoleEligibilityScheduleRequest object.
        Args:
            value: Value to set for the justification property.
        """
        self._justification = value
    
    @property
    def principal(self,) -> Optional[directory_object.DirectoryObject]:
        """
        Gets the principal property value. The principal that's getting a role eligibility through the request. Supports $expand.
        Returns: Optional[directory_object.DirectoryObject]
        """
        return self._principal
    
    @principal.setter
    def principal(self,value: Optional[directory_object.DirectoryObject] = None) -> None:
        """
        Sets the principal property value. The principal that's getting a role eligibility through the request. Supports $expand.
        Args:
            value: Value to set for the principal property.
        """
        self._principal = value
    
    @property
    def principal_id(self,) -> Optional[str]:
        """
        Gets the principalId property value. Identifier of the principal that has been granted the role eligibility. Can be a user or a role-assignable group. You can grant only active assignments service principals.Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._principal_id
    
    @principal_id.setter
    def principal_id(self,value: Optional[str] = None) -> None:
        """
        Sets the principalId property value. Identifier of the principal that has been granted the role eligibility. Can be a user or a role-assignable group. You can grant only active assignments service principals.Supports $filter (eq, ne).
        Args:
            value: Value to set for the principalId property.
        """
        self._principal_id = value
    
    @property
    def role_definition(self,) -> Optional[unified_role_definition.UnifiedRoleDefinition]:
        """
        Gets the roleDefinition property value. Detailed information for the unifiedRoleDefinition object that is referenced through the roleDefinitionId property. Supports $expand.
        Returns: Optional[unified_role_definition.UnifiedRoleDefinition]
        """
        return self._role_definition
    
    @role_definition.setter
    def role_definition(self,value: Optional[unified_role_definition.UnifiedRoleDefinition] = None) -> None:
        """
        Sets the roleDefinition property value. Detailed information for the unifiedRoleDefinition object that is referenced through the roleDefinitionId property. Supports $expand.
        Args:
            value: Value to set for the roleDefinition property.
        """
        self._role_definition = value
    
    @property
    def role_definition_id(self,) -> Optional[str]:
        """
        Gets the roleDefinitionId property value. Identifier of the unifiedRoleDefinition object that is being assigned to the principal. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._role_definition_id
    
    @role_definition_id.setter
    def role_definition_id(self,value: Optional[str] = None) -> None:
        """
        Sets the roleDefinitionId property value. Identifier of the unifiedRoleDefinition object that is being assigned to the principal. Supports $filter (eq, ne).
        Args:
            value: Value to set for the roleDefinitionId property.
        """
        self._role_definition_id = value
    
    @property
    def schedule_info(self,) -> Optional[request_schedule.RequestSchedule]:
        """
        Gets the scheduleInfo property value. The period of the role eligibility. Recurring schedules are currently unsupported.
        Returns: Optional[request_schedule.RequestSchedule]
        """
        return self._schedule_info
    
    @schedule_info.setter
    def schedule_info(self,value: Optional[request_schedule.RequestSchedule] = None) -> None:
        """
        Sets the scheduleInfo property value. The period of the role eligibility. Recurring schedules are currently unsupported.
        Args:
            value: Value to set for the scheduleInfo property.
        """
        self._schedule_info = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("action", self.action)
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
    
    @property
    def target_schedule(self,) -> Optional[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]:
        """
        Gets the targetSchedule property value. The schedule for a role eligibility that is referenced through the targetScheduleId property. Supports $expand.
        Returns: Optional[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]
        """
        return self._target_schedule
    
    @target_schedule.setter
    def target_schedule(self,value: Optional[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule] = None) -> None:
        """
        Sets the targetSchedule property value. The schedule for a role eligibility that is referenced through the targetScheduleId property. Supports $expand.
        Args:
            value: Value to set for the targetSchedule property.
        """
        self._target_schedule = value
    
    @property
    def target_schedule_id(self,) -> Optional[str]:
        """
        Gets the targetScheduleId property value. Identifier of the schedule object that's linked to the eligibility request. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._target_schedule_id
    
    @target_schedule_id.setter
    def target_schedule_id(self,value: Optional[str] = None) -> None:
        """
        Sets the targetScheduleId property value. Identifier of the schedule object that's linked to the eligibility request. Supports $filter (eq, ne).
        Args:
            value: Value to set for the targetScheduleId property.
        """
        self._target_schedule_id = value
    
    @property
    def ticket_info(self,) -> Optional[ticket_info.TicketInfo]:
        """
        Gets the ticketInfo property value. Ticket details linked to the role eligibility request including details of the ticket number and ticket system. Optional.
        Returns: Optional[ticket_info.TicketInfo]
        """
        return self._ticket_info
    
    @ticket_info.setter
    def ticket_info(self,value: Optional[ticket_info.TicketInfo] = None) -> None:
        """
        Sets the ticketInfo property value. Ticket details linked to the role eligibility request including details of the ticket number and ticket system. Optional.
        Args:
            value: Value to set for the ticketInfo property.
        """
        self._ticket_info = value
    

