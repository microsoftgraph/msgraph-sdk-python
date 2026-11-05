from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity_mapping import EntityMapping

from .entity_mapping import EntityMapping

@dataclass
class DnsEntityMapping(EntityMapping, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.dnsEntityMapping"
    # Name of the detection query column that maps to the domain name of the alert entity.
    domain_name_column: Optional[str] = None
    # Name of the detection query column that maps to the host IP address of the alert entity.
    host_ip_address_column: Optional[str] = None
    # Name of the detection query column that maps to the server IP address of the alert entity.
    server_ip_column: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DnsEntityMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DnsEntityMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DnsEntityMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity_mapping import EntityMapping

        from .entity_mapping import EntityMapping

        fields: dict[str, Callable[[Any], None]] = {
            "domainNameColumn": lambda n : setattr(self, 'domain_name_column', n.get_str_value()),
            "hostIpAddressColumn": lambda n : setattr(self, 'host_ip_address_column', n.get_str_value()),
            "serverIpColumn": lambda n : setattr(self, 'server_ip_column', n.get_str_value()),
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
        writer.write_str_value("domainNameColumn", self.domain_name_column)
        writer.write_str_value("hostIpAddressColumn", self.host_ip_address_column)
        writer.write_str_value("serverIpColumn", self.server_ip_column)
    

