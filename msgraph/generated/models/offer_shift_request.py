from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import schedule_change_request, swap_shifts_change_request

from . import schedule_change_request

@dataclass
class OfferShiftRequest(schedule_change_request.ScheduleChangeRequest):
    odata_type = "#microsoft.graph.offerShiftRequest"
    # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    recipient_action_date_time: Optional[datetime] = None
    # Custom message sent by recipient of the offer shift request.
    recipient_action_message: Optional[str] = None
    # User ID of the recipient of the offer shift request.
    recipient_user_id: Optional[str] = None
    # User ID of the sender of the offer shift request.
    sender_shift_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OfferShiftRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OfferShiftRequest
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.swapShiftsChangeRequest":
                from . import swap_shifts_change_request

                return swap_shifts_change_request.SwapShiftsChangeRequest()
        return OfferShiftRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import schedule_change_request, swap_shifts_change_request

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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("recipientActionMessage", self.recipient_action_message)
        writer.write_str_value("recipientUserId", self.recipient_user_id)
        writer.write_str_value("senderShiftId", self.sender_shift_id)
    

