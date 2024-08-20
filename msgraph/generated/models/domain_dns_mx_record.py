from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_dns_record import DomainDnsRecord

from .domain_dns_record import DomainDnsRecord

@dataclass
class DomainDnsMxRecord(DomainDnsRecord):
    # Value used when configuring the answer/destination/value of the MX record at the DNS host.
    mail_exchange: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Value used when configuring the Preference/Priority property of the MX record at the DNS host.
    preference: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainDnsMxRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsMxRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainDnsMxRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .domain_dns_record import DomainDnsRecord

        from .domain_dns_record import DomainDnsRecord

        fields: Dict[str, Callable[[Any], None]] = {
            "mailExchange": lambda n : setattr(self, 'mail_exchange', n.get_str_value()),
            "preference": lambda n : setattr(self, 'preference', n.get_int_value()),
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
        writer.write_str_value("mailExchange", self.mail_exchange)
        writer.write_int_value("preference", self.preference)
    

