from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

schedule_change_request = lazy_import('msgraph.generated.models.schedule_change_request')

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
        return OfferShiftRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "recipient_action_date_time": lambda n : setattr(self, 'recipient_action_date_time', n.get_datetime_value()),
            "recipient_action_message": lambda n : setattr(self, 'recipient_action_message', n.get_str_value()),
            "recipient_user_id": lambda n : setattr(self, 'recipient_user_id', n.get_str_value()),
            "sender_shift_id": lambda n : setattr(self, 'sender_shift_id', n.get_str_value()),
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
            value: Value to set for the recipientActionDateTime property.
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
            value: Value to set for the recipientActionMessage property.
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
            value: Value to set for the recipientUserId property.
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
            value: Value to set for the senderShiftId property.
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
    

