from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request

from . import entity

@dataclass
class RbacApplication(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The resourceNamespaces property
    resource_namespaces: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None
    # Instances for active role assignments.
    role_assignment_schedule_instances: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]] = None
    # Requests for active role assignments to principals through PIM.
    role_assignment_schedule_requests: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]] = None
    # Schedules for active role assignment operations.
    role_assignment_schedules: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]] = None
    # Resource to grant access to users or groups.
    role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
    # Resource representing the roles allowed by RBAC providers and the permissions assigned to the roles.
    role_definitions: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None
    # Instances for role eligibility requests.
    role_eligibility_schedule_instances: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]] = None
    # Requests for role eligibilities for principals through PIM.
    role_eligibility_schedule_requests: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]] = None
    # Schedules for role eligibility operations.
    role_eligibility_schedules: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RbacApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RbacApplication
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return RbacApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request

        from . import entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request

        fields: Dict[str, Callable[[Any], None]] = {
            "resourceNamespaces": lambda n : setattr(self, 'resource_namespaces', n.get_collection_of_object_values(unified_rbac_resource_namespace.UnifiedRbacResourceNamespace)),
            "roleAssignmentScheduleInstances": lambda n : setattr(self, 'role_assignment_schedule_instances', n.get_collection_of_object_values(unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance)),
            "roleAssignmentScheduleRequests": lambda n : setattr(self, 'role_assignment_schedule_requests', n.get_collection_of_object_values(unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest)),
            "roleAssignmentSchedules": lambda n : setattr(self, 'role_assignment_schedules', n.get_collection_of_object_values(unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(unified_role_definition.UnifiedRoleDefinition)),
            "roleEligibilityScheduleInstances": lambda n : setattr(self, 'role_eligibility_schedule_instances', n.get_collection_of_object_values(unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance)),
            "roleEligibilityScheduleRequests": lambda n : setattr(self, 'role_eligibility_schedule_requests', n.get_collection_of_object_values(unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest)),
            "roleEligibilitySchedules": lambda n : setattr(self, 'role_eligibility_schedules', n.get_collection_of_object_values(unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule)),
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
        writer.write_collection_of_object_values("resourceNamespaces", self.resource_namespaces)
        writer.write_collection_of_object_values("roleAssignmentScheduleInstances", self.role_assignment_schedule_instances)
        writer.write_collection_of_object_values("roleAssignmentScheduleRequests", self.role_assignment_schedule_requests)
        writer.write_collection_of_object_values("roleAssignmentSchedules", self.role_assignment_schedules)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleEligibilityScheduleInstances", self.role_eligibility_schedule_instances)
        writer.write_collection_of_object_values("roleEligibilityScheduleRequests", self.role_eligibility_schedule_requests)
        writer.write_collection_of_object_values("roleEligibilitySchedules", self.role_eligibility_schedules)
    

