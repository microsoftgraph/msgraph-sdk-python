from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import schedule_change_request, swap_shifts_change_request

from . import schedule_change_request

class OfferShiftRequest(schedule_change_request.ScheduleChangeRequest):
    def __init__(self,) -> None:
        """
        Instantiates a new OfferShiftRequest and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.offerShiftRequest"
        # The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._recipient_action_date_time: Optional[datetime] = None
        # Custom message sent by recipient of the offer shift request.
        self._recipient_action_message: Optional[str] = None
        # User ID of the recipient of the offer shift request.
        self._recipient_user_id: Optional[str] = None
        # User ID of the sender of the offer shift request.
        self._sender_shift_id: Optional[str] = None
    
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
    
    @property
    def recipient_action_date_time(self,) -> Optional[datetime]:
        """
        Gets the recipientActionDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._recipient_action_date_time
    
    @recipient_action_date_time.setter
    def recipient_action_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the recipientActionDateTime property value. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the recipient_action_date_time property.
        """
        self._recipient_action_date_time = value
    
    @property
    def recipient_action_message(self,) -> Optional[str]:
        """
        Gets the recipientActionMessage property value. Custom message sent by recipient of the offer shift request.
        Returns: Optional[str]
        """
        return self._recipient_action_message
    
    @recipient_action_message.setter
    def recipient_action_message(self,value: Optional[str] = None) -> None:
        """
        Sets the recipientActionMessage property value. Custom message sent by recipient of the offer shift request.
        Args:
            value: Value to set for the recipient_action_message property.
        """
        self._recipient_action_message = value
    
    @property
    def recipient_user_id(self,) -> Optional[str]:
        """
        Gets the recipientUserId property value. User ID of the recipient of the offer shift request.
        Returns: Optional[str]
        """
        return self._recipient_user_id
    
    @recipient_user_id.setter
    def recipient_user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the recipientUserId property value. User ID of the recipient of the offer shift request.
        Args:
            value: Value to set for the recipient_user_id property.
        """
        self._recipient_user_id = value
    
    @property
    def sender_shift_id(self,) -> Optional[str]:
        """
        Gets the senderShiftId property value. User ID of the sender of the offer shift request.
        Returns: Optional[str]
        """
        return self._sender_shift_id
    
    @sender_shift_id.setter
    def sender_shift_id(self,value: Optional[str] = None) -> None:
        """
        Sets the senderShiftId property value. User ID of the sender of the offer shift request.
        Args:
            value: Value to set for the sender_shift_id property.
        """
        self._sender_shift_id = value
    
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
    

