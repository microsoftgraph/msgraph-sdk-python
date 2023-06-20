from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_tracked_entity, offer_shift_request, open_shift_change_request, schedule_change_request_actor, schedule_change_state, swap_shifts_change_request, time_off_request

from . import change_tracked_entity

@dataclass
class ScheduleChangeRequest(change_tracked_entity.ChangeTrackedEntity):
    odata_type = "#microsoft.graph.scheduleChangeRequest"
    # The assignedTo property
    assigned_to: Optional[schedule_change_request_actor.ScheduleChangeRequestActor] = None
    # The managerActionDateTime property
    manager_action_date_time: Optional[datetime] = None
    # The managerActionMessage property
    manager_action_message: Optional[str] = None
    # The managerUserId property
    manager_user_id: Optional[str] = None
    # The senderDateTime property
    sender_date_time: Optional[datetime] = None
    # The senderMessage property
    sender_message: Optional[str] = None
    # The senderUserId property
    sender_user_id: Optional[str] = None
    # The state property
    state: Optional[schedule_change_state.ScheduleChangeState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduleChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleChangeRequest
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.offerShiftRequest".casefold():
            from . import offer_shift_request

            return offer_shift_request.OfferShiftRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftChangeRequest".casefold():
            from . import open_shift_change_request

            return open_shift_change_request.OpenShiftChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from . import swap_shifts_change_request

            return swap_shifts_change_request.SwapShiftsChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffRequest".casefold():
            from . import time_off_request

            return time_off_request.TimeOffRequest()
        return ScheduleChangeRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import change_tracked_entity, offer_shift_request, open_shift_change_request, schedule_change_request_actor, schedule_change_state, swap_shifts_change_request, time_off_request

        from . import change_tracked_entity, offer_shift_request, open_shift_change_request, schedule_change_request_actor, schedule_change_state, swap_shifts_change_request, time_off_request

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_enum_value(schedule_change_request_actor.ScheduleChangeRequestActor)),
            "managerActionDateTime": lambda n : setattr(self, 'manager_action_date_time', n.get_datetime_value()),
            "managerActionMessage": lambda n : setattr(self, 'manager_action_message', n.get_str_value()),
            "managerUserId": lambda n : setattr(self, 'manager_user_id', n.get_str_value()),
            "senderDateTime": lambda n : setattr(self, 'sender_date_time', n.get_datetime_value()),
            "senderMessage": lambda n : setattr(self, 'sender_message', n.get_str_value()),
            "senderUserId": lambda n : setattr(self, 'sender_user_id', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(schedule_change_state.ScheduleChangeState)),
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
        writer.write_enum_value("assignedTo", self.assigned_to)
        writer.write_str_value("managerActionMessage", self.manager_action_message)
        writer.write_str_value("senderMessage", self.sender_message)
        writer.write_enum_value("state", self.state)
    

