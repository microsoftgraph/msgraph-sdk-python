from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

network_connection_type = lazy_import('msgraph.generated.models.call_records.network_connection_type')
network_transport_protocol = lazy_import('msgraph.generated.models.call_records.network_transport_protocol')
trace_route_hop = lazy_import('msgraph.generated.models.call_records.trace_route_hop')
wifi_band = lazy_import('msgraph.generated.models.call_records.wifi_band')
wifi_radio_type = lazy_import('msgraph.generated.models.call_records.wifi_radio_type')

class NetworkInfo(AdditionalDataHolder, Parsable):
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
    def bandwidth_low_event_ratio(self,) -> Optional[float]:
        """
        Gets the bandwidthLowEventRatio property value. Fraction of the call that the media endpoint detected the available bandwidth or bandwidth policy was low enough to cause poor quality of the audio sent.
        Returns: Optional[float]
        """
        return self._bandwidth_low_event_ratio
    
    @bandwidth_low_event_ratio.setter
    def bandwidth_low_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the bandwidthLowEventRatio property value. Fraction of the call that the media endpoint detected the available bandwidth or bandwidth policy was low enough to cause poor quality of the audio sent.
        Args:
            value: Value to set for the bandwidthLowEventRatio property.
        """
        self._bandwidth_low_event_ratio = value
    
    @property
    def basic_service_set_identifier(self,) -> Optional[str]:
        """
        Gets the basicServiceSetIdentifier property value. The wireless LAN basic service set identifier of the media endpoint used to connect to the network.
        Returns: Optional[str]
        """
        return self._basic_service_set_identifier
    
    @basic_service_set_identifier.setter
    def basic_service_set_identifier(self,value: Optional[str] = None) -> None:
        """
        Sets the basicServiceSetIdentifier property value. The wireless LAN basic service set identifier of the media endpoint used to connect to the network.
        Args:
            value: Value to set for the basicServiceSetIdentifier property.
        """
        self._basic_service_set_identifier = value
    
    @property
    def connection_type(self,) -> Optional[network_connection_type.NetworkConnectionType]:
        """
        Gets the connectionType property value. The connectionType property
        Returns: Optional[network_connection_type.NetworkConnectionType]
        """
        return self._connection_type
    
    @connection_type.setter
    def connection_type(self,value: Optional[network_connection_type.NetworkConnectionType] = None) -> None:
        """
        Sets the connectionType property value. The connectionType property
        Args:
            value: Value to set for the connectionType property.
        """
        self._connection_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new networkInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Fraction of the call that the media endpoint detected the available bandwidth or bandwidth policy was low enough to cause poor quality of the audio sent.
        self._bandwidth_low_event_ratio: Optional[float] = None
        # The wireless LAN basic service set identifier of the media endpoint used to connect to the network.
        self._basic_service_set_identifier: Optional[str] = None
        # The connectionType property
        self._connection_type: Optional[network_connection_type.NetworkConnectionType] = None
        # Fraction of the call that the media endpoint detected the network delay was significant enough to impact the ability to have real-time two-way communication.
        self._delay_event_ratio: Optional[float] = None
        # DNS suffix associated with the network adapter of the media endpoint.
        self._dns_suffix: Optional[str] = None
        # IP address of the media endpoint.
        self._ip_address: Optional[str] = None
        # Link speed in bits per second reported by the network adapter used by the media endpoint.
        self._link_speed: Optional[int] = None
        # The media access control (MAC) address of the media endpoint's network device.
        self._mac_address: Optional[str] = None
        # The networkTransportProtocol property
        self._network_transport_protocol: Optional[network_transport_protocol.NetworkTransportProtocol] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Network port number used by media endpoint.
        self._port: Optional[int] = None
        # Fraction of the call that the media endpoint detected the network was causing poor quality of the audio received.
        self._received_quality_event_ratio: Optional[float] = None
        # IP address of the media endpoint as seen by the media relay server. This is typically the public internet IP address associated to the endpoint.
        self._reflexive_i_p_address: Optional[str] = None
        # IP address of the media relay server allocated by the media endpoint.
        self._relay_i_p_address: Optional[str] = None
        # Network port number allocated on the media relay server by the media endpoint.
        self._relay_port: Optional[int] = None
        # Fraction of the call that the media endpoint detected the network was causing poor quality of the audio sent.
        self._sent_quality_event_ratio: Optional[float] = None
        # Subnet used for media stream by the media endpoint.
        self._subnet: Optional[str] = None
        # List of network trace route hops collected for this media stream.*
        self._trace_route_hops: Optional[List[trace_route_hop.TraceRouteHop]] = None
        # The wifiBand property
        self._wifi_band: Optional[wifi_band.WifiBand] = None
        # Estimated remaining battery charge in percentage reported by the media endpoint.
        self._wifi_battery_charge: Optional[int] = None
        # WiFi channel used by the media endpoint.
        self._wifi_channel: Optional[int] = None
        # Name of the Microsoft WiFi driver used by the media endpoint. Value may be localized based on the language used by endpoint.
        self._wifi_microsoft_driver: Optional[str] = None
        # Version of the Microsoft WiFi driver used by the media endpoint.
        self._wifi_microsoft_driver_version: Optional[str] = None
        # The wifiRadioType property
        self._wifi_radio_type: Optional[wifi_radio_type.WifiRadioType] = None
        # WiFi signal strength in percentage reported by the media endpoint.
        self._wifi_signal_strength: Optional[int] = None
        # Name of the WiFi driver used by the media endpoint. Value may be localized based on the language used by endpoint.
        self._wifi_vendor_driver: Optional[str] = None
        # Version of the WiFi driver used by the media endpoint.
        self._wifi_vendor_driver_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NetworkInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NetworkInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NetworkInfo()
    
    @property
    def delay_event_ratio(self,) -> Optional[float]:
        """
        Gets the delayEventRatio property value. Fraction of the call that the media endpoint detected the network delay was significant enough to impact the ability to have real-time two-way communication.
        Returns: Optional[float]
        """
        return self._delay_event_ratio
    
    @delay_event_ratio.setter
    def delay_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the delayEventRatio property value. Fraction of the call that the media endpoint detected the network delay was significant enough to impact the ability to have real-time two-way communication.
        Args:
            value: Value to set for the delayEventRatio property.
        """
        self._delay_event_ratio = value
    
    @property
    def dns_suffix(self,) -> Optional[str]:
        """
        Gets the dnsSuffix property value. DNS suffix associated with the network adapter of the media endpoint.
        Returns: Optional[str]
        """
        return self._dns_suffix
    
    @dns_suffix.setter
    def dns_suffix(self,value: Optional[str] = None) -> None:
        """
        Sets the dnsSuffix property value. DNS suffix associated with the network adapter of the media endpoint.
        Args:
            value: Value to set for the dnsSuffix property.
        """
        self._dns_suffix = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bandwidth_low_event_ratio": lambda n : setattr(self, 'bandwidth_low_event_ratio', n.get_float_value()),
            "basic_service_set_identifier": lambda n : setattr(self, 'basic_service_set_identifier', n.get_str_value()),
            "connection_type": lambda n : setattr(self, 'connection_type', n.get_enum_value(network_connection_type.NetworkConnectionType)),
            "delay_event_ratio": lambda n : setattr(self, 'delay_event_ratio', n.get_float_value()),
            "dns_suffix": lambda n : setattr(self, 'dns_suffix', n.get_str_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "link_speed": lambda n : setattr(self, 'link_speed', n.get_int_value()),
            "mac_address": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "network_transport_protocol": lambda n : setattr(self, 'network_transport_protocol', n.get_enum_value(network_transport_protocol.NetworkTransportProtocol)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "received_quality_event_ratio": lambda n : setattr(self, 'received_quality_event_ratio', n.get_float_value()),
            "reflexive_i_p_address": lambda n : setattr(self, 'reflexive_i_p_address', n.get_str_value()),
            "relay_i_p_address": lambda n : setattr(self, 'relay_i_p_address', n.get_str_value()),
            "relay_port": lambda n : setattr(self, 'relay_port', n.get_int_value()),
            "sent_quality_event_ratio": lambda n : setattr(self, 'sent_quality_event_ratio', n.get_float_value()),
            "subnet": lambda n : setattr(self, 'subnet', n.get_str_value()),
            "trace_route_hops": lambda n : setattr(self, 'trace_route_hops', n.get_collection_of_object_values(trace_route_hop.TraceRouteHop)),
            "wifi_band": lambda n : setattr(self, 'wifi_band', n.get_enum_value(wifi_band.WifiBand)),
            "wifi_battery_charge": lambda n : setattr(self, 'wifi_battery_charge', n.get_int_value()),
            "wifi_channel": lambda n : setattr(self, 'wifi_channel', n.get_int_value()),
            "wifi_microsoft_driver": lambda n : setattr(self, 'wifi_microsoft_driver', n.get_str_value()),
            "wifi_microsoft_driver_version": lambda n : setattr(self, 'wifi_microsoft_driver_version', n.get_str_value()),
            "wifi_radio_type": lambda n : setattr(self, 'wifi_radio_type', n.get_enum_value(wifi_radio_type.WifiRadioType)),
            "wifi_signal_strength": lambda n : setattr(self, 'wifi_signal_strength', n.get_int_value()),
            "wifi_vendor_driver": lambda n : setattr(self, 'wifi_vendor_driver', n.get_str_value()),
            "wifi_vendor_driver_version": lambda n : setattr(self, 'wifi_vendor_driver_version', n.get_str_value()),
        }
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. IP address of the media endpoint.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. IP address of the media endpoint.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    @property
    def link_speed(self,) -> Optional[int]:
        """
        Gets the linkSpeed property value. Link speed in bits per second reported by the network adapter used by the media endpoint.
        Returns: Optional[int]
        """
        return self._link_speed
    
    @link_speed.setter
    def link_speed(self,value: Optional[int] = None) -> None:
        """
        Sets the linkSpeed property value. Link speed in bits per second reported by the network adapter used by the media endpoint.
        Args:
            value: Value to set for the linkSpeed property.
        """
        self._link_speed = value
    
    @property
    def mac_address(self,) -> Optional[str]:
        """
        Gets the macAddress property value. The media access control (MAC) address of the media endpoint's network device.
        Returns: Optional[str]
        """
        return self._mac_address
    
    @mac_address.setter
    def mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the macAddress property value. The media access control (MAC) address of the media endpoint's network device.
        Args:
            value: Value to set for the macAddress property.
        """
        self._mac_address = value
    
    @property
    def network_transport_protocol(self,) -> Optional[network_transport_protocol.NetworkTransportProtocol]:
        """
        Gets the networkTransportProtocol property value. The networkTransportProtocol property
        Returns: Optional[network_transport_protocol.NetworkTransportProtocol]
        """
        return self._network_transport_protocol
    
    @network_transport_protocol.setter
    def network_transport_protocol(self,value: Optional[network_transport_protocol.NetworkTransportProtocol] = None) -> None:
        """
        Sets the networkTransportProtocol property value. The networkTransportProtocol property
        Args:
            value: Value to set for the networkTransportProtocol property.
        """
        self._network_transport_protocol = value
    
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
    def port(self,) -> Optional[int]:
        """
        Gets the port property value. Network port number used by media endpoint.
        Returns: Optional[int]
        """
        return self._port
    
    @port.setter
    def port(self,value: Optional[int] = None) -> None:
        """
        Sets the port property value. Network port number used by media endpoint.
        Args:
            value: Value to set for the port property.
        """
        self._port = value
    
    @property
    def received_quality_event_ratio(self,) -> Optional[float]:
        """
        Gets the receivedQualityEventRatio property value. Fraction of the call that the media endpoint detected the network was causing poor quality of the audio received.
        Returns: Optional[float]
        """
        return self._received_quality_event_ratio
    
    @received_quality_event_ratio.setter
    def received_quality_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the receivedQualityEventRatio property value. Fraction of the call that the media endpoint detected the network was causing poor quality of the audio received.
        Args:
            value: Value to set for the receivedQualityEventRatio property.
        """
        self._received_quality_event_ratio = value
    
    @property
    def reflexive_i_p_address(self,) -> Optional[str]:
        """
        Gets the reflexiveIPAddress property value. IP address of the media endpoint as seen by the media relay server. This is typically the public internet IP address associated to the endpoint.
        Returns: Optional[str]
        """
        return self._reflexive_i_p_address
    
    @reflexive_i_p_address.setter
    def reflexive_i_p_address(self,value: Optional[str] = None) -> None:
        """
        Sets the reflexiveIPAddress property value. IP address of the media endpoint as seen by the media relay server. This is typically the public internet IP address associated to the endpoint.
        Args:
            value: Value to set for the reflexiveIPAddress property.
        """
        self._reflexive_i_p_address = value
    
    @property
    def relay_i_p_address(self,) -> Optional[str]:
        """
        Gets the relayIPAddress property value. IP address of the media relay server allocated by the media endpoint.
        Returns: Optional[str]
        """
        return self._relay_i_p_address
    
    @relay_i_p_address.setter
    def relay_i_p_address(self,value: Optional[str] = None) -> None:
        """
        Sets the relayIPAddress property value. IP address of the media relay server allocated by the media endpoint.
        Args:
            value: Value to set for the relayIPAddress property.
        """
        self._relay_i_p_address = value
    
    @property
    def relay_port(self,) -> Optional[int]:
        """
        Gets the relayPort property value. Network port number allocated on the media relay server by the media endpoint.
        Returns: Optional[int]
        """
        return self._relay_port
    
    @relay_port.setter
    def relay_port(self,value: Optional[int] = None) -> None:
        """
        Sets the relayPort property value. Network port number allocated on the media relay server by the media endpoint.
        Args:
            value: Value to set for the relayPort property.
        """
        self._relay_port = value
    
    @property
    def sent_quality_event_ratio(self,) -> Optional[float]:
        """
        Gets the sentQualityEventRatio property value. Fraction of the call that the media endpoint detected the network was causing poor quality of the audio sent.
        Returns: Optional[float]
        """
        return self._sent_quality_event_ratio
    
    @sent_quality_event_ratio.setter
    def sent_quality_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the sentQualityEventRatio property value. Fraction of the call that the media endpoint detected the network was causing poor quality of the audio sent.
        Args:
            value: Value to set for the sentQualityEventRatio property.
        """
        self._sent_quality_event_ratio = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_float_value("bandwidthLowEventRatio", self.bandwidth_low_event_ratio)
        writer.write_str_value("basicServiceSetIdentifier", self.basic_service_set_identifier)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_float_value("delayEventRatio", self.delay_event_ratio)
        writer.write_str_value("dnsSuffix", self.dns_suffix)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_int_value("linkSpeed", self.link_speed)
        writer.write_str_value("macAddress", self.mac_address)
        writer.write_enum_value("networkTransportProtocol", self.network_transport_protocol)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_float_value("receivedQualityEventRatio", self.received_quality_event_ratio)
        writer.write_str_value("reflexiveIPAddress", self.reflexive_i_p_address)
        writer.write_str_value("relayIPAddress", self.relay_i_p_address)
        writer.write_int_value("relayPort", self.relay_port)
        writer.write_float_value("sentQualityEventRatio", self.sent_quality_event_ratio)
        writer.write_str_value("subnet", self.subnet)
        writer.write_collection_of_object_values("traceRouteHops", self.trace_route_hops)
        writer.write_enum_value("wifiBand", self.wifi_band)
        writer.write_int_value("wifiBatteryCharge", self.wifi_battery_charge)
        writer.write_int_value("wifiChannel", self.wifi_channel)
        writer.write_str_value("wifiMicrosoftDriver", self.wifi_microsoft_driver)
        writer.write_str_value("wifiMicrosoftDriverVersion", self.wifi_microsoft_driver_version)
        writer.write_enum_value("wifiRadioType", self.wifi_radio_type)
        writer.write_int_value("wifiSignalStrength", self.wifi_signal_strength)
        writer.write_str_value("wifiVendorDriver", self.wifi_vendor_driver)
        writer.write_str_value("wifiVendorDriverVersion", self.wifi_vendor_driver_version)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def subnet(self,) -> Optional[str]:
        """
        Gets the subnet property value. Subnet used for media stream by the media endpoint.
        Returns: Optional[str]
        """
        return self._subnet
    
    @subnet.setter
    def subnet(self,value: Optional[str] = None) -> None:
        """
        Sets the subnet property value. Subnet used for media stream by the media endpoint.
        Args:
            value: Value to set for the subnet property.
        """
        self._subnet = value
    
    @property
    def trace_route_hops(self,) -> Optional[List[trace_route_hop.TraceRouteHop]]:
        """
        Gets the traceRouteHops property value. List of network trace route hops collected for this media stream.*
        Returns: Optional[List[trace_route_hop.TraceRouteHop]]
        """
        return self._trace_route_hops
    
    @trace_route_hops.setter
    def trace_route_hops(self,value: Optional[List[trace_route_hop.TraceRouteHop]] = None) -> None:
        """
        Sets the traceRouteHops property value. List of network trace route hops collected for this media stream.*
        Args:
            value: Value to set for the traceRouteHops property.
        """
        self._trace_route_hops = value
    
    @property
    def wifi_band(self,) -> Optional[wifi_band.WifiBand]:
        """
        Gets the wifiBand property value. The wifiBand property
        Returns: Optional[wifi_band.WifiBand]
        """
        return self._wifi_band
    
    @wifi_band.setter
    def wifi_band(self,value: Optional[wifi_band.WifiBand] = None) -> None:
        """
        Sets the wifiBand property value. The wifiBand property
        Args:
            value: Value to set for the wifiBand property.
        """
        self._wifi_band = value
    
    @property
    def wifi_battery_charge(self,) -> Optional[int]:
        """
        Gets the wifiBatteryCharge property value. Estimated remaining battery charge in percentage reported by the media endpoint.
        Returns: Optional[int]
        """
        return self._wifi_battery_charge
    
    @wifi_battery_charge.setter
    def wifi_battery_charge(self,value: Optional[int] = None) -> None:
        """
        Sets the wifiBatteryCharge property value. Estimated remaining battery charge in percentage reported by the media endpoint.
        Args:
            value: Value to set for the wifiBatteryCharge property.
        """
        self._wifi_battery_charge = value
    
    @property
    def wifi_channel(self,) -> Optional[int]:
        """
        Gets the wifiChannel property value. WiFi channel used by the media endpoint.
        Returns: Optional[int]
        """
        return self._wifi_channel
    
    @wifi_channel.setter
    def wifi_channel(self,value: Optional[int] = None) -> None:
        """
        Sets the wifiChannel property value. WiFi channel used by the media endpoint.
        Args:
            value: Value to set for the wifiChannel property.
        """
        self._wifi_channel = value
    
    @property
    def wifi_microsoft_driver(self,) -> Optional[str]:
        """
        Gets the wifiMicrosoftDriver property value. Name of the Microsoft WiFi driver used by the media endpoint. Value may be localized based on the language used by endpoint.
        Returns: Optional[str]
        """
        return self._wifi_microsoft_driver
    
    @wifi_microsoft_driver.setter
    def wifi_microsoft_driver(self,value: Optional[str] = None) -> None:
        """
        Sets the wifiMicrosoftDriver property value. Name of the Microsoft WiFi driver used by the media endpoint. Value may be localized based on the language used by endpoint.
        Args:
            value: Value to set for the wifiMicrosoftDriver property.
        """
        self._wifi_microsoft_driver = value
    
    @property
    def wifi_microsoft_driver_version(self,) -> Optional[str]:
        """
        Gets the wifiMicrosoftDriverVersion property value. Version of the Microsoft WiFi driver used by the media endpoint.
        Returns: Optional[str]
        """
        return self._wifi_microsoft_driver_version
    
    @wifi_microsoft_driver_version.setter
    def wifi_microsoft_driver_version(self,value: Optional[str] = None) -> None:
        """
        Sets the wifiMicrosoftDriverVersion property value. Version of the Microsoft WiFi driver used by the media endpoint.
        Args:
            value: Value to set for the wifiMicrosoftDriverVersion property.
        """
        self._wifi_microsoft_driver_version = value
    
    @property
    def wifi_radio_type(self,) -> Optional[wifi_radio_type.WifiRadioType]:
        """
        Gets the wifiRadioType property value. The wifiRadioType property
        Returns: Optional[wifi_radio_type.WifiRadioType]
        """
        return self._wifi_radio_type
    
    @wifi_radio_type.setter
    def wifi_radio_type(self,value: Optional[wifi_radio_type.WifiRadioType] = None) -> None:
        """
        Sets the wifiRadioType property value. The wifiRadioType property
        Args:
            value: Value to set for the wifiRadioType property.
        """
        self._wifi_radio_type = value
    
    @property
    def wifi_signal_strength(self,) -> Optional[int]:
        """
        Gets the wifiSignalStrength property value. WiFi signal strength in percentage reported by the media endpoint.
        Returns: Optional[int]
        """
        return self._wifi_signal_strength
    
    @wifi_signal_strength.setter
    def wifi_signal_strength(self,value: Optional[int] = None) -> None:
        """
        Sets the wifiSignalStrength property value. WiFi signal strength in percentage reported by the media endpoint.
        Args:
            value: Value to set for the wifiSignalStrength property.
        """
        self._wifi_signal_strength = value
    
    @property
    def wifi_vendor_driver(self,) -> Optional[str]:
        """
        Gets the wifiVendorDriver property value. Name of the WiFi driver used by the media endpoint. Value may be localized based on the language used by endpoint.
        Returns: Optional[str]
        """
        return self._wifi_vendor_driver
    
    @wifi_vendor_driver.setter
    def wifi_vendor_driver(self,value: Optional[str] = None) -> None:
        """
        Sets the wifiVendorDriver property value. Name of the WiFi driver used by the media endpoint. Value may be localized based on the language used by endpoint.
        Args:
            value: Value to set for the wifiVendorDriver property.
        """
        self._wifi_vendor_driver = value
    
    @property
    def wifi_vendor_driver_version(self,) -> Optional[str]:
        """
        Gets the wifiVendorDriverVersion property value. Version of the WiFi driver used by the media endpoint.
        Returns: Optional[str]
        """
        return self._wifi_vendor_driver_version
    
    @wifi_vendor_driver_version.setter
    def wifi_vendor_driver_version(self,value: Optional[str] = None) -> None:
        """
        Sets the wifiVendorDriverVersion property value. Version of the WiFi driver used by the media endpoint.
        Args:
            value: Value to set for the wifiVendorDriverVersion property.
        """
        self._wifi_vendor_driver_version = value
    

