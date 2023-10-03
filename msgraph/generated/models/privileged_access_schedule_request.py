from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
    from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
    from .request import Request
    from .request_schedule import RequestSchedule
    from .schedule_request_actions import ScheduleRequestActions
    from .ticket_info import TicketInfo

from .request import Request

@dataclass
class PrivilegedAccessScheduleRequest(Request):
    # The action property
    action: Optional[ScheduleRequestActions] = None
    # The isValidationOnly property
    is_validation_only: Optional[bool] = None
    # The justification property
    justification: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scheduleInfo property
    schedule_info: Optional[RequestSchedule] = None
    # The ticketInfo property
    ticket_info: Optional[TicketInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrivilegedAccessScheduleRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessScheduleRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest".casefold():
            from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest

            return PrivilegedAccessGroupAssignmentScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest".casefold():
            from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest

            return PrivilegedAccessGroupEligibilityScheduleRequest()
        return PrivilegedAccessScheduleRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
        from .request import Request
        from .request_schedule import RequestSchedule
        from .schedule_request_actions import ScheduleRequestActions
        from .ticket_info import TicketInfo

        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
        from .request import Request
        from .request_schedule import RequestSchedule
        from .schedule_request_actions import ScheduleRequestActions
        from .ticket_info import TicketInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(ScheduleRequestActions)),
            "isValidationOnly": lambda n : setattr(self, 'is_validation_only', n.get_bool_value()),
            "justification": lambda n : setattr(self, 'justification', n.get_str_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("action", self.action)
        writer.write_bool_value("isValidationOnly", self.is_validation_only)
        writer.write_str_value("justification", self.justification)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_object_value("ticketInfo", self.ticket_info)
    

