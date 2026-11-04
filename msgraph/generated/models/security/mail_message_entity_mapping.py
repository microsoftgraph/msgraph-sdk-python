from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity_mapping import EntityMapping

from .entity_mapping import EntityMapping

@dataclass
class MailMessageEntityMapping(EntityMapping, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.mailMessageEntityMapping"
    # Name of the detection query column that maps to the network message ID of the alert entity.
    network_message_id_column: Optional[str] = None
    # Name of the detection query column that maps to the recipient of the alert entity.
    recipient_column: Optional[str] = None
    # Name of the detection query column that maps to the sender of the alert entity.
    sender_column: Optional[str] = None
    # Name of the detection query column that maps to the subject of the alert entity.
    subject_column: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailMessageEntityMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailMessageEntityMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MailMessageEntityMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity_mapping import EntityMapping

        from .entity_mapping import EntityMapping

        fields: dict[str, Callable[[Any], None]] = {
            "networkMessageIdColumn": lambda n : setattr(self, 'network_message_id_column', n.get_str_value()),
            "recipientColumn": lambda n : setattr(self, 'recipient_column', n.get_str_value()),
            "senderColumn": lambda n : setattr(self, 'sender_column', n.get_str_value()),
            "subjectColumn": lambda n : setattr(self, 'subject_column', n.get_str_value()),
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
        writer.write_str_value("networkMessageIdColumn", self.network_message_id_column)
        writer.write_str_value("recipientColumn", self.recipient_column)
        writer.write_str_value("senderColumn", self.sender_column)
        writer.write_str_value("subjectColumn", self.subject_column)
    

