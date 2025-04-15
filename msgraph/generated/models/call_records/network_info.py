from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .network_connection_type import NetworkConnectionType
    from .network_transport_protocol import NetworkTransportProtocol
    from .trace_route_hop import TraceRouteHop
    from .wifi_band import WifiBand
    from .wifi_radio_type import WifiRadioType

@dataclass
class NetworkInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Fraction of the call that the media endpoint detected the available bandwidth or bandwidth policy was low enough to cause poor quality of the audio sent.
    bandwidth_low_event_ratio: Optional[float] = None
    # The wireless LAN basic service set identifier of the media endpoint used to connect to the network. This property isn't available if the user disables precise location sharing in their operating system or Microsoft Teams app settings.
    basic_service_set_identifier: Optional[str] = None
    # The connectionType property
    connection_type: Optional[NetworkConnectionType] = None
    # Fraction of the call that the media endpoint detected the network delay was significant enough to impact the ability to have real-time two-way communication.
    delay_event_ratio: Optional[float] = None
    # DNS suffix associated with the network adapter of the media endpoint.
    dns_suffix: Optional[str] = None
    # IP address of the media endpoint.
    ip_address: Optional[str] = None
    # Link speed in bits per second reported by the network adapter used by the media endpoint.
    link_speed: Optional[int] = None
    # The media access control (MAC) address of the media endpoint's network device. This value may be missing or shown as 02:00:00:00:00:00 due to operating system privacy policies.
    mac_address: Optional[str] = None
    # The networkTransportProtocol property
    network_transport_protocol: Optional[NetworkTransportProtocol] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Network port number used by media endpoint.
    port: Optional[int] = None
    # Fraction of the call that the media endpoint detected the network was causing poor quality of the audio received.
    received_quality_event_ratio: Optional[float] = None
    # IP address of the media endpoint as seen by the media relay server. This is typically the public internet IP address associated to the endpoint.
    reflexive_i_p_address: Optional[str] = None
    # IP address of the media relay server allocated by the media endpoint.
    relay_i_p_address: Optional[str] = None
    # Network port number allocated on the media relay server by the media endpoint.
    relay_port: Optional[int] = None
    # Fraction of the call that the media endpoint detected the network was causing poor quality of the audio sent.
    sent_quality_event_ratio: Optional[float] = None
    # Subnet used for media stream by the media endpoint.
    subnet: Optional[str] = None
    # List of network trace route hops collected for this media stream.*
    trace_route_hops: Optional[list[TraceRouteHop]] = None
    # The wifiBand property
    wifi_band: Optional[WifiBand] = None
    # Estimated remaining battery charge in percentage reported by the media endpoint.
    wifi_battery_charge: Optional[int] = None
    # WiFi channel used by the media endpoint.
    wifi_channel: Optional[int] = None
    # Name of the Microsoft WiFi driver used by the media endpoint. Value may be localized based on the language used by endpoint.
    wifi_microsoft_driver: Optional[str] = None
    # Version of the Microsoft WiFi driver used by the media endpoint.
    wifi_microsoft_driver_version: Optional[str] = None
    # The wifiRadioType property
    wifi_radio_type: Optional[WifiRadioType] = None
    # WiFi signal strength in percentage reported by the media endpoint.
    wifi_signal_strength: Optional[int] = None
    # Name of the WiFi driver used by the media endpoint. Value may be localized based on the language used by endpoint.
    wifi_vendor_driver: Optional[str] = None
    # Version of the WiFi driver used by the media endpoint.
    wifi_vendor_driver_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NetworkInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NetworkInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NetworkInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .network_connection_type import NetworkConnectionType
        from .network_transport_protocol import NetworkTransportProtocol
        from .trace_route_hop import TraceRouteHop
        from .wifi_band import WifiBand
        from .wifi_radio_type import WifiRadioType

        from .network_connection_type import NetworkConnectionType
        from .network_transport_protocol import NetworkTransportProtocol
        from .trace_route_hop import TraceRouteHop
        from .wifi_band import WifiBand
        from .wifi_radio_type import WifiRadioType

        fields: dict[str, Callable[[Any], None]] = {
            "bandwidthLowEventRatio": lambda n : setattr(self, 'bandwidth_low_event_ratio', n.get_float_value()),
            "basicServiceSetIdentifier": lambda n : setattr(self, 'basic_service_set_identifier', n.get_str_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(NetworkConnectionType)),
            "delayEventRatio": lambda n : setattr(self, 'delay_event_ratio', n.get_float_value()),
            "dnsSuffix": lambda n : setattr(self, 'dns_suffix', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "linkSpeed": lambda n : setattr(self, 'link_speed', n.get_int_value()),
            "macAddress": lambda n : setattr(self, 'mac_address', n.get_str_value()),
            "networkTransportProtocol": lambda n : setattr(self, 'network_transport_protocol', n.get_enum_value(NetworkTransportProtocol)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "receivedQualityEventRatio": lambda n : setattr(self, 'received_quality_event_ratio', n.get_float_value()),
            "reflexiveIPAddress": lambda n : setattr(self, 'reflexive_i_p_address', n.get_str_value()),
            "relayIPAddress": lambda n : setattr(self, 'relay_i_p_address', n.get_str_value()),
            "relayPort": lambda n : setattr(self, 'relay_port', n.get_int_value()),
            "sentQualityEventRatio": lambda n : setattr(self, 'sent_quality_event_ratio', n.get_float_value()),
            "subnet": lambda n : setattr(self, 'subnet', n.get_str_value()),
            "traceRouteHops": lambda n : setattr(self, 'trace_route_hops', n.get_collection_of_object_values(TraceRouteHop)),
            "wifiBand": lambda n : setattr(self, 'wifi_band', n.get_enum_value(WifiBand)),
            "wifiBatteryCharge": lambda n : setattr(self, 'wifi_battery_charge', n.get_int_value()),
            "wifiChannel": lambda n : setattr(self, 'wifi_channel', n.get_int_value()),
            "wifiMicrosoftDriver": lambda n : setattr(self, 'wifi_microsoft_driver', n.get_str_value()),
            "wifiMicrosoftDriverVersion": lambda n : setattr(self, 'wifi_microsoft_driver_version', n.get_str_value()),
            "wifiRadioType": lambda n : setattr(self, 'wifi_radio_type', n.get_enum_value(WifiRadioType)),
            "wifiSignalStrength": lambda n : setattr(self, 'wifi_signal_strength', n.get_int_value()),
            "wifiVendorDriver": lambda n : setattr(self, 'wifi_vendor_driver', n.get_str_value()),
            "wifiVendorDriverVersion": lambda n : setattr(self, 'wifi_vendor_driver_version', n.get_str_value()),
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
    

