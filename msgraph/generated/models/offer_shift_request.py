from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .schedule_change_request import ScheduleChangeRequest
    from .swap_shifts_change_request import SwapShiftsChangeRequest

from .schedule_change_request import ScheduleChangeRequest

@dataclass
class OfferShiftRequest(ScheduleChangeRequest, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.offerShiftRequest"
    # The date and time when the recipient approved or declined the request.
    recipient_action_date_time: Optional[datetime.datetime] = None
    # The message sent by the recipient regarding the request.
    recipient_action_message: Optional[str] = None
    # The recipient's user ID.
    recipient_user_id: Optional[str] = None
    # The sender's shift ID.
    sender_shift_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OfferShiftRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OfferShiftRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from .swap_shifts_change_request import SwapShiftsChangeRequest

            return SwapShiftsChangeRequest()
        return OfferShiftRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .schedule_change_request import ScheduleChangeRequest
        from .swap_shifts_change_request import SwapShiftsChangeRequest

        from .schedule_change_request import ScheduleChangeRequest
        from .swap_shifts_change_request import SwapShiftsChangeRequest

        fields: dict[str, Callable[[Any], None]] = {
            "recipientActionDateTime": lambda n : setattr(self, 'recipient_action_date_time', n.get_datetime_value()),
            "recipientActionMessage": lambda n : setattr(self, 'recipient_action_message', n.get_str_value()),
            "recipientUserId": lambda n : setattr(self, 'recipient_user_id', n.get_str_value()),
            "senderShiftId": lambda n : setattr(self, 'sender_shift_id', n.get_str_value()),
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
        writer.write_str_value("recipientActionMessage", self.recipient_action_message)
        writer.write_str_value("recipientUserId", self.recipient_user_id)
        writer.write_str_value("senderShiftId", self.sender_shift_id)
    

