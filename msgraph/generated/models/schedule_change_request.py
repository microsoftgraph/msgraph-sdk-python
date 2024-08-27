from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

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
class ScheduleChangeRequest(ChangeTrackedEntity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.scheduleChangeRequest"
    # The assignedTo property
    assigned_to: Optional[ScheduleChangeRequestActor] = None
    # The managerActionDateTime property
    manager_action_date_time: Optional[datetime.datetime] = None
    # The managerActionMessage property
    manager_action_message: Optional[str] = None
    # The managerUserId property
    manager_user_id: Optional[str] = None
    # The senderDateTime property
    sender_date_time: Optional[datetime.datetime] = None
    # The senderMessage property
    sender_message: Optional[str] = None
    # The senderUserId property
    sender_user_id: Optional[str] = None
    # The state property
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
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
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

        fields: Dict[str, Callable[[Any], None]] = {
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
    

