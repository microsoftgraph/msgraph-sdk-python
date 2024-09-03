from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence
    from .ip_evidence import IpEvidence

from .alert_evidence import AlertEvidence

@dataclass
class DnsEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.dnsEvidence"
    # The dnsServerIp property
    dns_server_ip: Optional[IpEvidence] = None
    # The domainName property
    domain_name: Optional[str] = None
    # The hostIpAddress property
    host_ip_address: Optional[IpEvidence] = None
    # The ipAddresses property
    ip_addresses: Optional[List[IpEvidence]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DnsEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DnsEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DnsEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence
        from .ip_evidence import IpEvidence

        from .alert_evidence import AlertEvidence
        from .ip_evidence import IpEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "dnsServerIp": lambda n : setattr(self, 'dns_server_ip', n.get_object_value(IpEvidence)),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "hostIpAddress": lambda n : setattr(self, 'host_ip_address', n.get_object_value(IpEvidence)),
            "ipAddresses": lambda n : setattr(self, 'ip_addresses', n.get_collection_of_object_values(IpEvidence)),
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
        writer.write_object_value("dnsServerIp", self.dns_server_ip)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_object_value("hostIpAddress", self.host_ip_address)
        writer.write_collection_of_object_values("ipAddresses", self.ip_addresses)
    

