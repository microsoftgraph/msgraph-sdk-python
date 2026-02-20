from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .exchange_message_trace_status import ExchangeMessageTraceStatus

from .entity import Entity

@dataclass
class ExchangeMessageTrace(Entity, Parsable):
    # The source IP address. For incoming messages, this value is the public IP address of the SMTP email server that sent the message. Supports $filter (eq).
    from_i_p: Optional[str] = None
    # The Message-ID header field of the message. The format of the Message-ID depends on the messaging server that sent the message. Supports $filter (eq).
    message_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the message was received by Exchange Online. The timestamp is in UTC format. Supports $filter (ge, le).
    received_date_time: Optional[datetime.datetime] = None
    # The SMTP email address of the user that the message was addressed to. Supports $filter (eq).
    recipient_address: Optional[str] = None
    # The SMTP email address of the user the message was purportedly from. Supports $filter (eq).
    sender_address: Optional[str] = None
    # The size of the message in bytes.
    size: Optional[int] = None
    # The status property
    status: Optional[ExchangeMessageTraceStatus] = None
    # The subject line of the message. Supports $filter (contains, startsWith, endsWith).
    subject: Optional[str] = None
    # The destination IP address. For outgoing messages, this value is the public IP address in the resolved MX record for the destination domain. For incoming messages to Exchange Online, this value is blank. Supports $filter (eq).
    to_i_p: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExchangeMessageTrace:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExchangeMessageTrace
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExchangeMessageTrace()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .exchange_message_trace_status import ExchangeMessageTraceStatus

        from .entity import Entity
        from .exchange_message_trace_status import ExchangeMessageTraceStatus

        fields: dict[str, Callable[[Any], None]] = {
            "fromIP": lambda n : setattr(self, 'from_i_p', n.get_str_value()),
            "messageId": lambda n : setattr(self, 'message_id', n.get_str_value()),
            "receivedDateTime": lambda n : setattr(self, 'received_date_time', n.get_datetime_value()),
            "recipientAddress": lambda n : setattr(self, 'recipient_address', n.get_str_value()),
            "senderAddress": lambda n : setattr(self, 'sender_address', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ExchangeMessageTraceStatus)),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "toIP": lambda n : setattr(self, 'to_i_p', n.get_str_value()),
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
        writer.write_str_value("fromIP", self.from_i_p)
        writer.write_str_value("messageId", self.message_id)
        writer.write_datetime_value("receivedDateTime", self.received_date_time)
        writer.write_str_value("recipientAddress", self.recipient_address)
        writer.write_str_value("senderAddress", self.sender_address)
        writer.write_int_value("size", self.size)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("toIP", self.to_i_p)
    

