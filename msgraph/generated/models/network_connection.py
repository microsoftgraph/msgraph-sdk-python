from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .connection_direction import ConnectionDirection
    from .connection_status import ConnectionStatus
    from .security_network_protocol import SecurityNetworkProtocol

@dataclass
class NetworkConnection(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Name of the application managing the network connection (for example, Facebook or SMTP).
    application_name: Optional[str] = None
    # Destination IP address (of the network connection).
    destination_address: Optional[str] = None
    # Destination domain portion of the destination URL. (for example 'www.contoso.com').
    destination_domain: Optional[str] = None
    # Location (by IP address mapping) associated with the destination of a network connection.
    destination_location: Optional[str] = None
    # Destination port (of the network connection).
    destination_port: Optional[str] = None
    # Network connection URL/URI string - excluding parameters. (for example 'www.contoso.com/products/default.html')
    destination_url: Optional[str] = None
    # Network connection direction. The possible values are: unknown, inbound, outbound.
    direction: Optional[ConnectionDirection] = None
    # Date when the destination domain was registered. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    domain_registered_date_time: Optional[datetime.datetime] = None
    # The local DNS name resolution as it appears in the host's local DNS cache (for example, in case the 'hosts' file was tampered with).
    local_dns_name: Optional[str] = None
    # Network Address Translation destination IP address.
    nat_destination_address: Optional[str] = None
    # Network Address Translation destination port.
    nat_destination_port: Optional[str] = None
    # Network Address Translation source IP address.
    nat_source_address: Optional[str] = None
    # Network Address Translation source port.
    nat_source_port: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Network protocol. The possible values are: unknown, ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII.
    protocol: Optional[SecurityNetworkProtocol] = None
    # Provider generated/calculated risk score of the network connection. Recommended value range of 0-1, which equates to a percentage.
    risk_score: Optional[str] = None
    # Source (i.e. origin) IP address (of the network connection).
    source_address: Optional[str] = None
    # Location (by IP address mapping) associated with the source of a network connection.
    source_location: Optional[str] = None
    # Source (i.e. origin) IP port (of the network connection).
    source_port: Optional[str] = None
    # Network connection status. The possible values are: unknown, attempted, succeeded, blocked, failed.
    status: Optional[ConnectionStatus] = None
    # Parameters (suffix) of the destination URL.
    url_parameters: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NetworkConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NetworkConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .connection_direction import ConnectionDirection
        from .connection_status import ConnectionStatus
        from .security_network_protocol import SecurityNetworkProtocol

        from .connection_direction import ConnectionDirection
        from .connection_status import ConnectionStatus
        from .security_network_protocol import SecurityNetworkProtocol

        fields: dict[str, Callable[[Any], None]] = {
            "applicationName": lambda n : setattr(self, 'application_name', n.get_str_value()),
            "destinationAddress": lambda n : setattr(self, 'destination_address', n.get_str_value()),
            "destinationDomain": lambda n : setattr(self, 'destination_domain', n.get_str_value()),
            "destinationLocation": lambda n : setattr(self, 'destination_location', n.get_str_value()),
            "destinationPort": lambda n : setattr(self, 'destination_port', n.get_str_value()),
            "destinationUrl": lambda n : setattr(self, 'destination_url', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(ConnectionDirection)),
            "domainRegisteredDateTime": lambda n : setattr(self, 'domain_registered_date_time', n.get_datetime_value()),
            "localDnsName": lambda n : setattr(self, 'local_dns_name', n.get_str_value()),
            "natDestinationAddress": lambda n : setattr(self, 'nat_destination_address', n.get_str_value()),
            "natDestinationPort": lambda n : setattr(self, 'nat_destination_port', n.get_str_value()),
            "natSourceAddress": lambda n : setattr(self, 'nat_source_address', n.get_str_value()),
            "natSourcePort": lambda n : setattr(self, 'nat_source_port', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(SecurityNetworkProtocol)),
            "riskScore": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "sourceAddress": lambda n : setattr(self, 'source_address', n.get_str_value()),
            "sourceLocation": lambda n : setattr(self, 'source_location', n.get_str_value()),
            "sourcePort": lambda n : setattr(self, 'source_port', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ConnectionStatus)),
            "urlParameters": lambda n : setattr(self, 'url_parameters', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("applicationName", self.application_name)
        writer.write_str_value("destinationAddress", self.destination_address)
        writer.write_str_value("destinationDomain", self.destination_domain)
        writer.write_str_value("destinationLocation", self.destination_location)
        writer.write_str_value("destinationPort", self.destination_port)
        writer.write_str_value("destinationUrl", self.destination_url)
        writer.write_enum_value("direction", self.direction)
        writer.write_datetime_value("domainRegisteredDateTime", self.domain_registered_date_time)
        writer.write_str_value("localDnsName", self.local_dns_name)
        writer.write_str_value("natDestinationAddress", self.nat_destination_address)
        writer.write_str_value("natDestinationPort", self.nat_destination_port)
        writer.write_str_value("natSourceAddress", self.nat_source_address)
        writer.write_str_value("natSourcePort", self.nat_source_port)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("protocol", self.protocol)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_str_value("sourceAddress", self.source_address)
        writer.write_str_value("sourceLocation", self.source_location)
        writer.write_str_value("sourcePort", self.source_port)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("urlParameters", self.url_parameters)
        writer.write_additional_data_value(self.additional_data)
    

