from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
    from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase

from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase

@dataclass
class UnifiedRoleAssignmentScheduleInstance(UnifiedRoleScheduleInstanceBase, Parsable):
    # If the request is from an eligible administrator to activate a role, this parameter shows the related eligible assignment for that activation. Otherwise, it's null. Supports $expand and $select nested in $expand.
    activated_using: Optional[UnifiedRoleEligibilityScheduleInstance] = None
    # The type of the assignment that can either be Assigned or Activated. Supports $filter (eq, ne).
    assignment_type: Optional[str] = None
    # The end date of the schedule instance.
    end_date_time: Optional[datetime.datetime] = None
    # How the assignment is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
    member_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The identifier of the role assignment in Microsoft Entra. Supports $filter (eq, ne).
    role_assignment_origin_id: Optional[str] = None
    # The identifier of the unifiedRoleAssignmentSchedule object from which this instance was created. Supports $filter (eq, ne).
    role_assignment_schedule_id: Optional[str] = None
    # When this instance starts.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleAssignmentScheduleInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignmentScheduleInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleAssignmentScheduleInstance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
        from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase

        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
        from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase

        fields: dict[str, Callable[[Any], None]] = {
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(UnifiedRoleEligibilityScheduleInstance)),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "roleAssignmentOriginId": lambda n : setattr(self, 'role_assignment_origin_id', n.get_str_value()),
            "roleAssignmentScheduleId": lambda n : setattr(self, 'role_assignment_schedule_id', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_object_value("activatedUsing", self.activated_using)
        writer.write_str_value("assignmentType", self.assignment_type)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("memberType", self.member_type)
        writer.write_str_value("roleAssignmentOriginId", self.role_assignment_origin_id)
        writer.write_str_value("roleAssignmentScheduleId", self.role_assignment_schedule_id)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

