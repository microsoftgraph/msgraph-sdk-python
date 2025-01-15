from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .approval import Approval
    from .entity import Entity
    from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
    from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
    from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
    from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
    from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
    from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest

from .entity import Entity

@dataclass
class PrivilegedAccessGroup(Entity, Parsable):
    # The assignmentApprovals property
    assignment_approvals: Optional[list[Approval]] = None
    # The instances of assignment schedules to activate a just-in-time access.
    assignment_schedule_instances: Optional[list[PrivilegedAccessGroupAssignmentScheduleInstance]] = None
    # The schedule requests for operations to create, update, delete, extend, and renew an assignment.
    assignment_schedule_requests: Optional[list[PrivilegedAccessGroupAssignmentScheduleRequest]] = None
    # The assignment schedules to activate a just-in-time access.
    assignment_schedules: Optional[list[PrivilegedAccessGroupAssignmentSchedule]] = None
    # The instances of eligibility schedules to activate a just-in-time access.
    eligibility_schedule_instances: Optional[list[PrivilegedAccessGroupEligibilityScheduleInstance]] = None
    # The schedule requests for operations to create, update, delete, extend, and renew an eligibility.
    eligibility_schedule_requests: Optional[list[PrivilegedAccessGroupEligibilityScheduleRequest]] = None
    # The eligibility schedules to activate a just-in-time access.
    eligibility_schedules: Optional[list[PrivilegedAccessGroupEligibilitySchedule]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedAccessGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrivilegedAccessGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .approval import Approval
        from .entity import Entity
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest

        from .approval import Approval
        from .entity import Entity
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest

        fields: dict[str, Callable[[Any], None]] = {
            "assignmentApprovals": lambda n : setattr(self, 'assignment_approvals', n.get_collection_of_object_values(Approval)),
            "assignmentScheduleInstances": lambda n : setattr(self, 'assignment_schedule_instances', n.get_collection_of_object_values(PrivilegedAccessGroupAssignmentScheduleInstance)),
            "assignmentScheduleRequests": lambda n : setattr(self, 'assignment_schedule_requests', n.get_collection_of_object_values(PrivilegedAccessGroupAssignmentScheduleRequest)),
            "assignmentSchedules": lambda n : setattr(self, 'assignment_schedules', n.get_collection_of_object_values(PrivilegedAccessGroupAssignmentSchedule)),
            "eligibilityScheduleInstances": lambda n : setattr(self, 'eligibility_schedule_instances', n.get_collection_of_object_values(PrivilegedAccessGroupEligibilityScheduleInstance)),
            "eligibilityScheduleRequests": lambda n : setattr(self, 'eligibility_schedule_requests', n.get_collection_of_object_values(PrivilegedAccessGroupEligibilityScheduleRequest)),
            "eligibilitySchedules": lambda n : setattr(self, 'eligibility_schedules', n.get_collection_of_object_values(PrivilegedAccessGroupEligibilitySchedule)),
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
        writer.write_collection_of_object_values("assignmentApprovals", self.assignment_approvals)
        writer.write_collection_of_object_values("assignmentScheduleInstances", self.assignment_schedule_instances)
        writer.write_collection_of_object_values("assignmentScheduleRequests", self.assignment_schedule_requests)
        writer.write_collection_of_object_values("assignmentSchedules", self.assignment_schedules)
        writer.write_collection_of_object_values("eligibilityScheduleInstances", self.eligibility_schedule_instances)
        writer.write_collection_of_object_values("eligibilityScheduleRequests", self.eligibility_schedule_requests)
        writer.write_collection_of_object_values("eligibilitySchedules", self.eligibility_schedules)
    

