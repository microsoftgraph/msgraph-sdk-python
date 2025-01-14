from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_dns_record import DomainDnsRecord

from .domain_dns_record import DomainDnsRecord

@dataclass
class DomainDnsTxtRecord(DomainDnsRecord, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Value used when configuring the text property at the DNS host.
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainDnsTxtRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsTxtRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainDnsTxtRecord()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .domain_dns_record import DomainDnsRecord

        from .domain_dns_record import DomainDnsRecord

        fields: dict[str, Callable[[Any], None]] = {
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_str_value("text", self.text)
    

