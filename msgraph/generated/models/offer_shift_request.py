from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .schedule_change_request import ScheduleChangeRequest
    from .swap_shifts_change_request import SwapShiftsChangeRequest

from .schedule_change_request import ScheduleChangeRequest

@dataclass
class OfferShiftRequest(ScheduleChangeRequest):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.offerShiftRequest"
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    recipient_action_date_time: Optional[datetime.datetime] = None
    # Custom message sent by recipient of the offer shift request.
    recipient_action_message: Optional[str] = None
    # User ID of the recipient of the offer shift request.
    recipient_user_id: Optional[str] = None
    # User ID of the sender of the offer shift request.
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
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from .swap_shifts_change_request import SwapShiftsChangeRequest

            return SwapShiftsChangeRequest()
        return OfferShiftRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .schedule_change_request import ScheduleChangeRequest
        from .swap_shifts_change_request import SwapShiftsChangeRequest

        from .schedule_change_request import ScheduleChangeRequest
        from .swap_shifts_change_request import SwapShiftsChangeRequest

        fields: Dict[str, Callable[[Any], None]] = {
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
    

