from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .request_schedule import RequestSchedule
    from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
    from .unified_role_schedule_base import UnifiedRoleScheduleBase

from .unified_role_schedule_base import UnifiedRoleScheduleBase

@dataclass
class UnifiedRoleAssignmentSchedule(UnifiedRoleScheduleBase, Parsable):
    # If the request is from an eligible administrator to activate a role, this parameter shows the related eligible assignment for that activation. Otherwise, it's null. Supports $expand.
    activated_using: Optional[UnifiedRoleEligibilitySchedule] = None
    # The type of the assignment that can either be Assigned or Activated. Supports $filter (eq, ne).
    assignment_type: Optional[str] = None
    # How the assignment is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
    member_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The period of the role assignment. It can represent a single occurrence or multiple recurrences.
    schedule_info: Optional[RequestSchedule] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UnifiedRoleAssignmentSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignmentSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UnifiedRoleAssignmentSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .request_schedule import RequestSchedule
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase

        from .request_schedule import RequestSchedule
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase

        fields: dict[str, Callable[[Any], None]] = {
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(UnifiedRoleEligibilitySchedule)),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_str_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
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
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("scheduleInfo", self.schedule_info)
    

