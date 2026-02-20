from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class ExchangeMessageTraceDetail(Entity, Parsable):
    # The action taken on the message during the event.
    action: Optional[str] = None
    # Additional data associated with the event, containing supplementary information specific to the event.
    data: Optional[str] = None
    # The date and time when the event occurred. The timestamp is in UTC format.
    date_time: Optional[datetime.datetime] = None
    # A detailed description that provides context about what happened during message processing.
    description: Optional[str] = None
    # The event that occurred during message processing.
    event: Optional[str] = None
    # The Message-ID header field of the message. The format depends on the messaging server that sent the message.
    message_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExchangeMessageTraceDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExchangeMessageTraceDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExchangeMessageTraceDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_str_value()),
            "data": lambda n : setattr(self, 'data', n.get_str_value()),
            "dateTime": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "event": lambda n : setattr(self, 'event', n.get_str_value()),
            "messageId": lambda n : setattr(self, 'message_id', n.get_str_value()),
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
        writer.write_str_value("action", self.action)
        writer.write_str_value("data", self.data)
        writer.write_datetime_value("dateTime", self.date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("event", self.event)
        writer.write_str_value("messageId", self.message_id)
    

