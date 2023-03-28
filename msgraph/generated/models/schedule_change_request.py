from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_tracked_entity, offer_shift_request, open_shift_change_request, schedule_change_request_actor, schedule_change_state, swap_shifts_change_request, time_off_request

from . import change_tracked_entity

class ScheduleChangeRequest(change_tracked_entity.ChangeTrackedEntity):
    def __init__(self,) -> None:
        """
        Instantiates a new ScheduleChangeRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.scheduleChangeRequest"
        # The assignedTo property
        self._assigned_to: Optional[schedule_change_request_actor.ScheduleChangeRequestActor] = None
        # The managerActionDateTime property
        self._manager_action_date_time: Optional[datetime] = None
        # The managerActionMessage property
        self._manager_action_message: Optional[str] = None
        # The managerUserId property
        self._manager_user_id: Optional[str] = None
        # The senderDateTime property
        self._sender_date_time: Optional[datetime] = None
        # The senderMessage property
        self._sender_message: Optional[str] = None
        # The senderUserId property
        self._sender_user_id: Optional[str] = None
        # The state property
        self._state: Optional[schedule_change_state.ScheduleChangeState] = None
    
    @property
    def assigned_to(self,) -> Optional[schedule_change_request_actor.ScheduleChangeRequestActor]:
        """
        Gets the assignedTo property value. The assignedTo property
        Returns: Optional[schedule_change_request_actor.ScheduleChangeRequestActor]
        """
        return self._assigned_to
    
    @assigned_to.setter
    def assigned_to(self,value: Optional[schedule_change_request_actor.ScheduleChangeRequestActor] = None) -> None:
        """
        Sets the assignedTo property value. The assignedTo property
        Args:
            value: Value to set for the assigned_to property.
        """
        self._assigned_to = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduleChangeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleChangeRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.offerShiftRequest":
                from . import offer_shift_request

                return offer_shift_request.OfferShiftRequest()
            if mapping_value == "#microsoft.graph.openShiftChangeRequest":
                from . import open_shift_change_request

                return open_shift_change_request.OpenShiftChangeRequest()
            if mapping_value == "#microsoft.graph.swapShiftsChangeRequest":
                from . import swap_shifts_change_request

                return swap_shifts_change_request.SwapShiftsChangeRequest()
            if mapping_value == "#microsoft.graph.timeOffRequest":
                from . import time_off_request

                return time_off_request.TimeOffRequest()
        return ScheduleChangeRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def manager_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the managerActionDateTime property value. The managerActionDateTime property
        Returns: Optional[datetime]
        """
        return self._manager_action_date_time
    
    @manager_action_date_time.setter
    def manager_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the managerActionDateTime property value. The managerActionDateTime property
        Args:
            value: Value to set for the manager_action_date_time property.
        """
        self._manager_action_date_time = value
    
    @property
    def manager_action_message(self,) -> Optional[str]:
        """
        Gets the managerActionMessage property value. The managerActionMessage property
        Returns: Optional[str]
        """
        return self._manager_action_message
    
    @manager_action_message.setter
    def manager_action_message(self,value: Optional[str] = None) -> None:
        """
        Sets the managerActionMessage property value. The managerActionMessage property
        Args:
            value: Value to set for the manager_action_message property.
        """
        self._manager_action_message = value
    
    @property
    def manager_user_id(self,) -> Optional[str]:
        """
        Gets the managerUserId property value. The managerUserId property
        Returns: Optional[str]
        """
        return self._manager_user_id
    
    @manager_user_id.setter
    def manager_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the managerUserId property value. The managerUserId property
        Args:
            value: Value to set for the manager_user_id property.
        """
        self._manager_user_id = value
    
    @property
    def sender_date_time(self,) -> Optional[datetime]:
        """
        Gets the senderDateTime property value. The senderDateTime property
        Returns: Optional[datetime]
        """
        return self._sender_date_time
    
    @sender_date_time.setter
    def sender_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the senderDateTime property value. The senderDateTime property
        Args:
            value: Value to set for the sender_date_time property.
        """
        self._sender_date_time = value
    
    @property
    def sender_message(self,) -> Optional[str]:
        """
        Gets the senderMessage property value. The senderMessage property
        Returns: Optional[str]
        """
        return self._sender_message
    
    @sender_message.setter
    def sender_message(self,value: Optional[str] = None) -> None:
        """
        Sets the senderMessage property value. The senderMessage property
        Args:
            value: Value to set for the sender_message property.
        """
        self._sender_message = value
    
    @property
    def sender_user_id(self,) -> Optional[str]:
        """
        Gets the senderUserId property value. The senderUserId property
        Returns: Optional[str]
        """
        return self._sender_user_id
    
    @sender_user_id.setter
    def sender_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the senderUserId property value. The senderUserId property
        Args:
            value: Value to set for the sender_user_id property.
        """
        self._sender_user_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("assignedTo", self.assigned_to)
        writer.write_str_value("managerActionMessage", self.manager_action_message)
        writer.write_str_value("senderMessage", self.sender_message)
        writer.write_enum_value("state", self.state)
    
    @property
    def state(self,) -> Optional[schedule_change_state.ScheduleChangeState]:
        """
        Gets the state property value. The state property
        Returns: Optional[schedule_change_state.ScheduleChangeState]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[schedule_change_state.ScheduleChangeState] = None) -> None:
        """
        Sets the state property value. The state property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    

