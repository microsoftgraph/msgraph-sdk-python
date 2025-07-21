from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .payload_detail import PayloadDetail

from .payload_detail import PayloadDetail

@dataclass
class EmailPayloadDetail(PayloadDetail, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.emailPayloadDetail"
    # Email address of the user.
    from_email: Optional[str] = None
    # Display name of the user.
    from_name: Optional[str] = None
    # Indicates whether the sender isn't from the user's organization.
    is_external_sender: Optional[bool] = None
    # The subject of the email address sent to the user.
    subject: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmailPayloadDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmailPayloadDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmailPayloadDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .payload_detail import PayloadDetail

        from .payload_detail import PayloadDetail

        fields: dict[str, Callable[[Any], None]] = {
            "fromEmail": lambda n : setattr(self, 'from_email', n.get_str_value()),
            "fromName": lambda n : setattr(self, 'from_name', n.get_str_value()),
            "isExternalSender": lambda n : setattr(self, 'is_external_sender', n.get_bool_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
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
        writer.write_str_value("fromEmail", self.from_email)
        writer.write_str_value("fromName", self.from_name)
        writer.write_bool_value("isExternalSender", self.is_external_sender)
        writer.write_str_value("subject", self.subject)
    

