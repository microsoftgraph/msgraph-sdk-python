from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
unified_role_assignment = lazy_import('msgraph.generated.models.unified_role_assignment')
unified_role_assignment_schedule = lazy_import('msgraph.generated.models.unified_role_assignment_schedule')
unified_role_assignment_schedule_instance = lazy_import('msgraph.generated.models.unified_role_assignment_schedule_instance')
unified_role_assignment_schedule_request = lazy_import('msgraph.generated.models.unified_role_assignment_schedule_request')
unified_role_definition = lazy_import('msgraph.generated.models.unified_role_definition')
unified_role_eligibility_schedule = lazy_import('msgraph.generated.models.unified_role_eligibility_schedule')
unified_role_eligibility_schedule_instance = lazy_import('msgraph.generated.models.unified_role_eligibility_schedule_instance')
unified_role_eligibility_schedule_request = lazy_import('msgraph.generated.models.unified_role_eligibility_schedule_request')

class RbacApplication(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new RbacApplication and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Resource to grant access to users or groups.
        self._role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
        # Instances for active role assignments.
        self._role_assignment_schedule_instances: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]] = None
        # Requests for active role assignments to principals through PIM.
        self._role_assignment_schedule_requests: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]] = None
        # Schedules for active role assignment operations.
        self._role_assignment_schedules: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]] = None
        # Resource representing the roles allowed by RBAC providers and the permissions assigned to the roles.
        self._role_definitions: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None
        # Instances for role eligibility requests.
        self._role_eligibility_schedule_instances: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]] = None
        # Requests for role eligibilities for principals through PIM.
        self._role_eligibility_schedule_requests: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]] = None
        # Schedules for role eligibility operations.
        self._role_eligibility_schedules: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RbacApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RbacApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RbacApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "role_assignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
            "role_assignment_schedule_instances": lambda n : setattr(self, 'role_assignment_schedule_instances', n.get_collection_of_object_values(unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance)),
            "role_assignment_schedule_requests": lambda n : setattr(self, 'role_assignment_schedule_requests', n.get_collection_of_object_values(unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest)),
            "role_assignment_schedules": lambda n : setattr(self, 'role_assignment_schedules', n.get_collection_of_object_values(unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule)),
            "role_definitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(unified_role_definition.UnifiedRoleDefinition)),
            "role_eligibility_schedule_instances": lambda n : setattr(self, 'role_eligibility_schedule_instances', n.get_collection_of_object_values(unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance)),
            "role_eligibility_schedule_requests": lambda n : setattr(self, 'role_eligibility_schedule_requests', n.get_collection_of_object_values(unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest)),
            "role_eligibility_schedules": lambda n : setattr(self, 'role_eligibility_schedules', n.get_collection_of_object_values(unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def role_assignments(self,) -> Optional[List[unified_role_assignment.UnifiedRoleAssignment]]:
        """
        Gets the roleAssignments property value. Resource to grant access to users or groups.
        Returns: Optional[List[unified_role_assignment.UnifiedRoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. Resource to grant access to users or groups.
        Args:
            value: Value to set for the roleAssignments property.
        """
        self._role_assignments = value
    
    @property
    def role_assignment_schedule_instances(self,) -> Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]]:
        """
        Gets the roleAssignmentScheduleInstances property value. Instances for active role assignments.
        Returns: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]]
        """
        return self._role_assignment_schedule_instances
    
    @role_assignment_schedule_instances.setter
    def role_assignment_schedule_instances(self,value: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]] = None) -> None:
        """
        Sets the roleAssignmentScheduleInstances property value. Instances for active role assignments.
        Args:
            value: Value to set for the roleAssignmentScheduleInstances property.
        """
        self._role_assignment_schedule_instances = value
    
    @property
    def role_assignment_schedule_requests(self,) -> Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]]:
        """
        Gets the roleAssignmentScheduleRequests property value. Requests for active role assignments to principals through PIM.
        Returns: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]]
        """
        return self._role_assignment_schedule_requests
    
    @role_assignment_schedule_requests.setter
    def role_assignment_schedule_requests(self,value: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]] = None) -> None:
        """
        Sets the roleAssignmentScheduleRequests property value. Requests for active role assignments to principals through PIM.
        Args:
            value: Value to set for the roleAssignmentScheduleRequests property.
        """
        self._role_assignment_schedule_requests = value
    
    @property
    def role_assignment_schedules(self,) -> Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]]:
        """
        Gets the roleAssignmentSchedules property value. Schedules for active role assignment operations.
        Returns: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]]
        """
        return self._role_assignment_schedules
    
    @role_assignment_schedules.setter
    def role_assignment_schedules(self,value: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]] = None) -> None:
        """
        Sets the roleAssignmentSchedules property value. Schedules for active role assignment operations.
        Args:
            value: Value to set for the roleAssignmentSchedules property.
        """
        self._role_assignment_schedules = value
    
    @property
    def role_definitions(self,) -> Optional[List[unified_role_definition.UnifiedRoleDefinition]]:
        """
        Gets the roleDefinitions property value. Resource representing the roles allowed by RBAC providers and the permissions assigned to the roles.
        Returns: Optional[List[unified_role_definition.UnifiedRoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. Resource representing the roles allowed by RBAC providers and the permissions assigned to the roles.
        Args:
            value: Value to set for the roleDefinitions property.
        """
        self._role_definitions = value
    
    @property
    def role_eligibility_schedule_instances(self,) -> Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]]:
        """
        Gets the roleEligibilityScheduleInstances property value. Instances for role eligibility requests.
        Returns: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]]
        """
        return self._role_eligibility_schedule_instances
    
    @role_eligibility_schedule_instances.setter
    def role_eligibility_schedule_instances(self,value: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]] = None) -> None:
        """
        Sets the roleEligibilityScheduleInstances property value. Instances for role eligibility requests.
        Args:
            value: Value to set for the roleEligibilityScheduleInstances property.
        """
        self._role_eligibility_schedule_instances = value
    
    @property
    def role_eligibility_schedule_requests(self,) -> Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]]:
        """
        Gets the roleEligibilityScheduleRequests property value. Requests for role eligibilities for principals through PIM.
        Returns: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]]
        """
        return self._role_eligibility_schedule_requests
    
    @role_eligibility_schedule_requests.setter
    def role_eligibility_schedule_requests(self,value: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]] = None) -> None:
        """
        Sets the roleEligibilityScheduleRequests property value. Requests for role eligibilities for principals through PIM.
        Args:
            value: Value to set for the roleEligibilityScheduleRequests property.
        """
        self._role_eligibility_schedule_requests = value
    
    @property
    def role_eligibility_schedules(self,) -> Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]]:
        """
        Gets the roleEligibilitySchedules property value. Schedules for role eligibility operations.
        Returns: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]]
        """
        return self._role_eligibility_schedules
    
    @role_eligibility_schedules.setter
    def role_eligibility_schedules(self,value: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]] = None) -> None:
        """
        Sets the roleEligibilitySchedules property value. Schedules for role eligibility operations.
        Args:
            value: Value to set for the roleEligibilitySchedules property.
        """
        self._role_eligibility_schedules = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleAssignmentScheduleInstances", self.role_assignment_schedule_instances)
        writer.write_collection_of_object_values("roleAssignmentScheduleRequests", self.role_assignment_schedule_requests)
        writer.write_collection_of_object_values("roleAssignmentSchedules", self.role_assignment_schedules)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleEligibilityScheduleInstances", self.role_eligibility_schedule_instances)
        writer.write_collection_of_object_values("roleEligibilityScheduleRequests", self.role_eligibility_schedule_requests)
        writer.write_collection_of_object_values("roleEligibilitySchedules", self.role_eligibility_schedules)
    

