from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

connection_direction = lazy_import('msgraph.generated.models.connection_direction')
connection_status = lazy_import('msgraph.generated.models.connection_status')
security_network_protocol = lazy_import('msgraph.generated.models.security_network_protocol')

class NetworkConnection(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def application_name(self,) -> Optional[str]:
        """
        Gets the applicationName property value. Name of the application managing the network connection (for example, Facebook or SMTP).
        Returns: Optional[str]
        """
        return self._application_name
    
    @application_name.setter
    def application_name(self,value: Optional[str] = None) -> None:
        """
        Sets the applicationName property value. Name of the application managing the network connection (for example, Facebook or SMTP).
        Args:
            value: Value to set for the applicationName property.
        """
        self._application_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new networkConnection and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Name of the application managing the network connection (for example, Facebook or SMTP).
        self._application_name: Optional[str] = None
        # Destination IP address (of the network connection).
        self._destination_address: Optional[str] = None
        # Destination domain portion of the destination URL. (for example 'www.contoso.com').
        self._destination_domain: Optional[str] = None
        # Location (by IP address mapping) associated with the destination of a network connection.
        self._destination_location: Optional[str] = None
        # Destination port (of the network connection).
        self._destination_port: Optional[str] = None
        # Network connection URL/URI string - excluding parameters. (for example 'www.contoso.com/products/default.html')
        self._destination_url: Optional[str] = None
        # Network connection direction. Possible values are: unknown, inbound, outbound.
        self._direction: Optional[connection_direction.ConnectionDirection] = None
        # Date when the destination domain was registered. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._domain_registered_date_time: Optional[datetime] = None
        # The local DNS name resolution as it appears in the host's local DNS cache (for example, in case the 'hosts' file was tampered with).
        self._local_dns_name: Optional[str] = None
        # Network Address Translation destination IP address.
        self._nat_destination_address: Optional[str] = None
        # Network Address Translation destination port.
        self._nat_destination_port: Optional[str] = None
        # Network Address Translation source IP address.
        self._nat_source_address: Optional[str] = None
        # Network Address Translation source port.
        self._nat_source_port: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Network protocol. Possible values are: unknown, ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII.
        self._protocol: Optional[security_network_protocol.SecurityNetworkProtocol] = None
        # Provider generated/calculated risk score of the network connection. Recommended value range of 0-1, which equates to a percentage.
        self._risk_score: Optional[str] = None
        # Source (i.e. origin) IP address (of the network connection).
        self._source_address: Optional[str] = None
        # Location (by IP address mapping) associated with the source of a network connection.
        self._source_location: Optional[str] = None
        # Source (i.e. origin) IP port (of the network connection).
        self._source_port: Optional[str] = None
        # Network connection status. Possible values are: unknown, attempted, succeeded, blocked, failed.
        self._status: Optional[connection_status.ConnectionStatus] = None
        # Parameters (suffix) of the destination URL.
        self._url_parameters: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NetworkConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NetworkConnection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NetworkConnection()
    
    @property
    def destination_address(self,) -> Optional[str]:
        """
        Gets the destinationAddress property value. Destination IP address (of the network connection).
        Returns: Optional[str]
        """
        return self._destination_address
    
    @destination_address.setter
    def destination_address(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationAddress property value. Destination IP address (of the network connection).
        Args:
            value: Value to set for the destinationAddress property.
        """
        self._destination_address = value
    
    @property
    def destination_domain(self,) -> Optional[str]:
        """
        Gets the destinationDomain property value. Destination domain portion of the destination URL. (for example 'www.contoso.com').
        Returns: Optional[str]
        """
        return self._destination_domain
    
    @destination_domain.setter
    def destination_domain(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationDomain property value. Destination domain portion of the destination URL. (for example 'www.contoso.com').
        Args:
            value: Value to set for the destinationDomain property.
        """
        self._destination_domain = value
    
    @property
    def destination_location(self,) -> Optional[str]:
        """
        Gets the destinationLocation property value. Location (by IP address mapping) associated with the destination of a network connection.
        Returns: Optional[str]
        """
        return self._destination_location
    
    @destination_location.setter
    def destination_location(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationLocation property value. Location (by IP address mapping) associated with the destination of a network connection.
        Args:
            value: Value to set for the destinationLocation property.
        """
        self._destination_location = value
    
    @property
    def destination_port(self,) -> Optional[str]:
        """
        Gets the destinationPort property value. Destination port (of the network connection).
        Returns: Optional[str]
        """
        return self._destination_port
    
    @destination_port.setter
    def destination_port(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationPort property value. Destination port (of the network connection).
        Args:
            value: Value to set for the destinationPort property.
        """
        self._destination_port = value
    
    @property
    def destination_url(self,) -> Optional[str]:
        """
        Gets the destinationUrl property value. Network connection URL/URI string - excluding parameters. (for example 'www.contoso.com/products/default.html')
        Returns: Optional[str]
        """
        return self._destination_url
    
    @destination_url.setter
    def destination_url(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationUrl property value. Network connection URL/URI string - excluding parameters. (for example 'www.contoso.com/products/default.html')
        Args:
            value: Value to set for the destinationUrl property.
        """
        self._destination_url = value
    
    @property
    def direction(self,) -> Optional[connection_direction.ConnectionDirection]:
        """
        Gets the direction property value. Network connection direction. Possible values are: unknown, inbound, outbound.
        Returns: Optional[connection_direction.ConnectionDirection]
        """
        return self._direction
    
    @direction.setter
    def direction(self,value: Optional[connection_direction.ConnectionDirection] = None) -> None:
        """
        Sets the direction property value. Network connection direction. Possible values are: unknown, inbound, outbound.
        Args:
            value: Value to set for the direction property.
        """
        self._direction = value
    
    @property
    def domain_registered_date_time(self,) -> Optional[datetime]:
        """
        Gets the domainRegisteredDateTime property value. Date when the destination domain was registered. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._domain_registered_date_time
    
    @domain_registered_date_time.setter
    def domain_registered_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the domainRegisteredDateTime property value. Date when the destination domain was registered. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the domainRegisteredDateTime property.
        """
        self._domain_registered_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "application_name": lambda n : setattr(self, 'application_name', n.get_str_value()),
            "destination_address": lambda n : setattr(self, 'destination_address', n.get_str_value()),
            "destination_domain": lambda n : setattr(self, 'destination_domain', n.get_str_value()),
            "destination_location": lambda n : setattr(self, 'destination_location', n.get_str_value()),
            "destination_port": lambda n : setattr(self, 'destination_port', n.get_str_value()),
            "destination_url": lambda n : setattr(self, 'destination_url', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(connection_direction.ConnectionDirection)),
            "domain_registered_date_time": lambda n : setattr(self, 'domain_registered_date_time', n.get_datetime_value()),
            "local_dns_name": lambda n : setattr(self, 'local_dns_name', n.get_str_value()),
            "nat_destination_address": lambda n : setattr(self, 'nat_destination_address', n.get_str_value()),
            "nat_destination_port": lambda n : setattr(self, 'nat_destination_port', n.get_str_value()),
            "nat_source_address": lambda n : setattr(self, 'nat_source_address', n.get_str_value()),
            "nat_source_port": lambda n : setattr(self, 'nat_source_port', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(security_network_protocol.SecurityNetworkProtocol)),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
            "source_address": lambda n : setattr(self, 'source_address', n.get_str_value()),
            "source_location": lambda n : setattr(self, 'source_location', n.get_str_value()),
            "source_port": lambda n : setattr(self, 'source_port', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(connection_status.ConnectionStatus)),
            "url_parameters": lambda n : setattr(self, 'url_parameters', n.get_str_value()),
        }
        return fields
    
    @property
    def local_dns_name(self,) -> Optional[str]:
        """
        Gets the localDnsName property value. The local DNS name resolution as it appears in the host's local DNS cache (for example, in case the 'hosts' file was tampered with).
        Returns: Optional[str]
        """
        return self._local_dns_name
    
    @local_dns_name.setter
    def local_dns_name(self,value: Optional[str] = None) -> None:
        """
        Sets the localDnsName property value. The local DNS name resolution as it appears in the host's local DNS cache (for example, in case the 'hosts' file was tampered with).
        Args:
            value: Value to set for the localDnsName property.
        """
        self._local_dns_name = value
    
    @property
    def nat_destination_address(self,) -> Optional[str]:
        """
        Gets the natDestinationAddress property value. Network Address Translation destination IP address.
        Returns: Optional[str]
        """
        return self._nat_destination_address
    
    @nat_destination_address.setter
    def nat_destination_address(self,value: Optional[str] = None) -> None:
        """
        Sets the natDestinationAddress property value. Network Address Translation destination IP address.
        Args:
            value: Value to set for the natDestinationAddress property.
        """
        self._nat_destination_address = value
    
    @property
    def nat_destination_port(self,) -> Optional[str]:
        """
        Gets the natDestinationPort property value. Network Address Translation destination port.
        Returns: Optional[str]
        """
        return self._nat_destination_port
    
    @nat_destination_port.setter
    def nat_destination_port(self,value: Optional[str] = None) -> None:
        """
        Sets the natDestinationPort property value. Network Address Translation destination port.
        Args:
            value: Value to set for the natDestinationPort property.
        """
        self._nat_destination_port = value
    
    @property
    def nat_source_address(self,) -> Optional[str]:
        """
        Gets the natSourceAddress property value. Network Address Translation source IP address.
        Returns: Optional[str]
        """
        return self._nat_source_address
    
    @nat_source_address.setter
    def nat_source_address(self,value: Optional[str] = None) -> None:
        """
        Sets the natSourceAddress property value. Network Address Translation source IP address.
        Args:
            value: Value to set for the natSourceAddress property.
        """
        self._nat_source_address = value
    
    @property
    def nat_source_port(self,) -> Optional[str]:
        """
        Gets the natSourcePort property value. Network Address Translation source port.
        Returns: Optional[str]
        """
        return self._nat_source_port
    
    @nat_source_port.setter
    def nat_source_port(self,value: Optional[str] = None) -> None:
        """
        Sets the natSourcePort property value. Network Address Translation source port.
        Args:
            value: Value to set for the natSourcePort property.
        """
        self._nat_source_port = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def protocol(self,) -> Optional[security_network_protocol.SecurityNetworkProtocol]:
        """
        Gets the protocol property value. Network protocol. Possible values are: unknown, ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII.
        Returns: Optional[security_network_protocol.SecurityNetworkProtocol]
        """
        return self._protocol
    
    @protocol.setter
    def protocol(self,value: Optional[security_network_protocol.SecurityNetworkProtocol] = None) -> None:
        """
        Sets the protocol property value. Network protocol. Possible values are: unknown, ip, icmp, igmp, ggp, ipv4, tcp, pup, udp, idp, ipv6, ipv6RoutingHeader, ipv6FragmentHeader, ipSecEncapsulatingSecurityPayload, ipSecAuthenticationHeader, icmpV6, ipv6NoNextHeader, ipv6DestinationOptions, nd, raw, ipx, spx, spxII.
        Args:
            value: Value to set for the protocol property.
        """
        self._protocol = value
    
    @property
    def risk_score(self,) -> Optional[str]:
        """
        Gets the riskScore property value. Provider generated/calculated risk score of the network connection. Recommended value range of 0-1, which equates to a percentage.
        Returns: Optional[str]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[str] = None) -> None:
        """
        Sets the riskScore property value. Provider generated/calculated risk score of the network connection. Recommended value range of 0-1, which equates to a percentage.
        Args:
            value: Value to set for the riskScore property.
        """
        self._risk_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def source_address(self,) -> Optional[str]:
        """
        Gets the sourceAddress property value. Source (i.e. origin) IP address (of the network connection).
        Returns: Optional[str]
        """
        return self._source_address
    
    @source_address.setter
    def source_address(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceAddress property value. Source (i.e. origin) IP address (of the network connection).
        Args:
            value: Value to set for the sourceAddress property.
        """
        self._source_address = value
    
    @property
    def source_location(self,) -> Optional[str]:
        """
        Gets the sourceLocation property value. Location (by IP address mapping) associated with the source of a network connection.
        Returns: Optional[str]
        """
        return self._source_location
    
    @source_location.setter
    def source_location(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceLocation property value. Location (by IP address mapping) associated with the source of a network connection.
        Args:
            value: Value to set for the sourceLocation property.
        """
        self._source_location = value
    
    @property
    def source_port(self,) -> Optional[str]:
        """
        Gets the sourcePort property value. Source (i.e. origin) IP port (of the network connection).
        Returns: Optional[str]
        """
        return self._source_port
    
    @source_port.setter
    def source_port(self,value: Optional[str] = None) -> None:
        """
        Sets the sourcePort property value. Source (i.e. origin) IP port (of the network connection).
        Args:
            value: Value to set for the sourcePort property.
        """
        self._source_port = value
    
    @property
    def status(self,) -> Optional[connection_status.ConnectionStatus]:
        """
        Gets the status property value. Network connection status. Possible values are: unknown, attempted, succeeded, blocked, failed.
        Returns: Optional[connection_status.ConnectionStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[connection_status.ConnectionStatus] = None) -> None:
        """
        Sets the status property value. Network connection status. Possible values are: unknown, attempted, succeeded, blocked, failed.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def url_parameters(self,) -> Optional[str]:
        """
        Gets the urlParameters property value. Parameters (suffix) of the destination URL.
        Returns: Optional[str]
        """
        return self._url_parameters
    
    @url_parameters.setter
    def url_parameters(self,value: Optional[str] = None) -> None:
        """
        Sets the urlParameters property value. Parameters (suffix) of the destination URL.
        Args:
            value: Value to set for the urlParameters property.
        """
        self._url_parameters = value
    

