from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import request_schedule, unified_role_eligibility_schedule, unified_role_schedule_base

from . import unified_role_schedule_base

class UnifiedRoleAssignmentSchedule(unified_role_schedule_base.UnifiedRoleScheduleBase):
    def __init__(self,) -> None:
        """
        Instantiates a new UnifiedRoleAssignmentSchedule and sets the default values.
        """
        super().__init__()
        # If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it is null. Supports $expand.
        self._activated_using: Optional[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule] = None
        # Type of the assignment which can either be Assigned or Activated. Supports $filter (eq, ne).
        self._assignment_type: Optional[str] = None
        # How the assignments is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
        self._member_type: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The period of the role assignment. It can represent a single occurrence or multiple recurrences.
        self._schedule_info: Optional[request_schedule.RequestSchedule] = None
    
    @property
    def activated_using(self,) -> Optional[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]:
        """
        Gets the activatedUsing property value. If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it is null. Supports $expand.
        Returns: Optional[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]
        """
        return self._activated_using
    
    @activated_using.setter
    def activated_using(self,value: Optional[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule] = None) -> None:
        """
        Sets the activatedUsing property value. If the request is from an eligible administrator to activate a role, this parameter will show the related eligible assignment for that activation. Otherwise, it is null. Supports $expand.
        Args:
            value: Value to set for the activated_using property.
        """
        self._activated_using = value
    
    @property
    def assignment_type(self,) -> Optional[str]:
        """
        Gets the assignmentType property value. Type of the assignment which can either be Assigned or Activated. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._assignment_type
    
    @assignment_type.setter
    def assignment_type(self,value: Optional[str] = None) -> None:
        """
        Sets the assignmentType property value. Type of the assignment which can either be Assigned or Activated. Supports $filter (eq, ne).
        Args:
            value: Value to set for the assignment_type property.
        """
        self._assignment_type = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UnifiedRoleAssignmentSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UnifiedRoleAssignmentSchedule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UnifiedRoleAssignmentSchedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import request_schedule, unified_role_eligibility_schedule, unified_role_schedule_base

        fields: Dict[str, Callable[[Any], None]] = {
            "activatedUsing": lambda n : setattr(self, 'activated_using', n.get_object_value(unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule)),
            "assignmentType": lambda n : setattr(self, 'assignment_type', n.get_str_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(request_schedule.RequestSchedule)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def member_type(self,) -> Optional[str]:
        """
        Gets the memberType property value. How the assignments is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
        Returns: Optional[str]
        """
        return self._member_type
    
    @member_type.setter
    def member_type(self,value: Optional[str] = None) -> None:
        """
        Sets the memberType property value. How the assignments is inherited. It can either be Inherited, Direct, or Group. It can further imply whether the unifiedRoleAssignmentSchedule can be managed by the caller. Supports $filter (eq, ne).
        Args:
            value: Value to set for the member_type property.
        """
        self._member_type = value
    
    @property
    def schedule_info(self,) -> Optional[request_schedule.RequestSchedule]:
        """
        Gets the scheduleInfo property value. The period of the role assignment. It can represent a single occurrence or multiple recurrences.
        Returns: Optional[request_schedule.RequestSchedule]
        """
        return self._schedule_info
    
    @schedule_info.setter
    def schedule_info(self,value: Optional[request_schedule.RequestSchedule] = None) -> None:
        """
        Sets the scheduleInfo property value. The period of the role assignment. It can represent a single occurrence or multiple recurrences.
        Args:
            value: Value to set for the schedule_info property.
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
        writer.write_object_value("activatedUsing", self.activated_using)
        writer.write_str_value("assignmentType", self.assignment_type)
        writer.write_str_value("memberType", self.member_type)
        writer.write_object_value("scheduleInfo", self.schedule_info)
    

