from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .domain_dns_record import DomainDnsRecord

from .domain_dns_record import DomainDnsRecord

@dataclass
class DomainDnsSrvRecord(DomainDnsRecord):
    # Value to use when configuring the Target property of the SRV record at the DNS host.
    name_target: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Value to use when configuring the port property of the SRV record at the DNS host.
    port: Optional[int] = None
    # Value to use when configuring the priority property of the SRV record at the DNS host.
    priority: Optional[int] = None
    # Value to use when configuring the protocol property of the SRV record at the DNS host.
    protocol: Optional[str] = None
    # Value to use when configuring the service property of the SRV record at the DNS host.
    service: Optional[str] = None
    # Value to use when configuring the weight property of the SRV record at the DNS host.
    weight: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DomainDnsSrvRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsSrvRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DomainDnsSrvRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .domain_dns_record import DomainDnsRecord

        from .domain_dns_record import DomainDnsRecord

        fields: Dict[str, Callable[[Any], None]] = {
            "nameTarget": lambda n : setattr(self, 'name_target', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "weight": lambda n : setattr(self, 'weight', n.get_int_value()),
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
        writer.write_str_value("nameTarget", self.name_target)
        writer.write_int_value("port", self.port)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("protocol", self.protocol)
        writer.write_str_value("service", self.service)
        writer.write_int_value("weight", self.weight)
    

