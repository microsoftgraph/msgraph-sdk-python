from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .offer_shift_request import OfferShiftRequest
    from .open_shift_change_request import OpenShiftChangeRequest
    from .schedule_change_request_actor import ScheduleChangeRequestActor
    from .schedule_change_state import ScheduleChangeState
    from .swap_shifts_change_request import SwapShiftsChangeRequest
    from .time_off_request import TimeOffRequest

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class ScheduleChangeRequest(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.scheduleChangeRequest"
    # Indicates who the request is assigned to. The possible values are: sender, recipient, manager, system, unknownFutureValue.
    assigned_to: Optional[ScheduleChangeRequestActor] = None
    # The date and time when the manager approved or declined the scheduleChangeRequest. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    manager_action_date_time: Optional[datetime.datetime] = None
    # The message sent by the manager regarding the scheduleChangeRequest. Optional.
    manager_action_message: Optional[str] = None
    # The user ID of the manager who approved or declined the scheduleChangeRequest.
    manager_user_id: Optional[str] = None
    # The date and time when the sender sent the scheduleChangeRequest. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    sender_date_time: Optional[datetime.datetime] = None
    # The message sent by the sender of the scheduleChangeRequest. Optional.
    sender_message: Optional[str] = None
    # The user ID of the sender of the scheduleChangeRequest.
    sender_user_id: Optional[str] = None
    # The state of the scheduleChangeRequest. The possible values are: pending, approved, declined, unknownFutureValue.
    state: Optional[ScheduleChangeState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ScheduleChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleChangeRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.offerShiftRequest".casefold():
            from .offer_shift_request import OfferShiftRequest

            return OfferShiftRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftChangeRequest".casefold():
            from .open_shift_change_request import OpenShiftChangeRequest

            return OpenShiftChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from .swap_shifts_change_request import SwapShiftsChangeRequest

            return SwapShiftsChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffRequest".casefold():
            from .time_off_request import TimeOffRequest

            return TimeOffRequest()
        return ScheduleChangeRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .offer_shift_request import OfferShiftRequest
        from .open_shift_change_request import OpenShiftChangeRequest
        from .schedule_change_request_actor import ScheduleChangeRequestActor
        from .schedule_change_state import ScheduleChangeState
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .time_off_request import TimeOffRequest

        from .change_tracked_entity import ChangeTrackedEntity
        from .offer_shift_request import OfferShiftRequest
        from .open_shift_change_request import OpenShiftChangeRequest
        from .schedule_change_request_actor import ScheduleChangeRequestActor
        from .schedule_change_state import ScheduleChangeState
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .time_off_request import TimeOffRequest

        fields: dict[str, Callable[[Any], None]] = {
            "assignedTo": lambda n : setattr(self, 'assigned_to', n.get_enum_value(ScheduleChangeRequestActor)),
            "managerActionDateTime": lambda n : setattr(self, 'manager_action_date_time', n.get_datetime_value()),
            "managerActionMessage": lambda n : setattr(self, 'manager_action_message', n.get_str_value()),
            "managerUserId": lambda n : setattr(self, 'manager_user_id', n.get_str_value()),
            "senderDateTime": lambda n : setattr(self, 'sender_date_time', n.get_datetime_value()),
            "senderMessage": lambda n : setattr(self, 'sender_message', n.get_str_value()),
            "senderUserId": lambda n : setattr(self, 'sender_user_id', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(ScheduleChangeState)),
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
        writer.write_enum_value("assignedTo", self.assigned_to)
        writer.write_str_value("managerActionMessage", self.manager_action_message)
        writer.write_str_value("senderMessage", self.sender_message)
        writer.write_enum_value("state", self.state)
    

