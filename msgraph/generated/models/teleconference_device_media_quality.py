from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeleconferenceDeviceMediaQuality(AdditionalDataHolder, Parsable):
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
    def average_inbound_jitter(self,) -> Optional[Timedelta]:
        """
        Gets the averageInboundJitter property value. The average inbound stream network jitter.
        Returns: Optional[Timedelta]
        """
        return self._average_inbound_jitter
    
    @average_inbound_jitter.setter
    def average_inbound_jitter(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the averageInboundJitter property value. The average inbound stream network jitter.
        Args:
            value: Value to set for the averageInboundJitter property.
        """
        self._average_inbound_jitter = value
    
    @property
    def average_inbound_packet_loss_rate_in_percentage(self,) -> Optional[float]:
        """
        Gets the averageInboundPacketLossRateInPercentage property value. The average inbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        Returns: Optional[float]
        """
        return self._average_inbound_packet_loss_rate_in_percentage
    
    @average_inbound_packet_loss_rate_in_percentage.setter
    def average_inbound_packet_loss_rate_in_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the averageInboundPacketLossRateInPercentage property value. The average inbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        Args:
            value: Value to set for the averageInboundPacketLossRateInPercentage property.
        """
        self._average_inbound_packet_loss_rate_in_percentage = value
    
    @property
    def average_inbound_round_trip_delay(self,) -> Optional[Timedelta]:
        """
        Gets the averageInboundRoundTripDelay property value. The average inbound stream network round trip delay.
        Returns: Optional[Timedelta]
        """
        return self._average_inbound_round_trip_delay
    
    @average_inbound_round_trip_delay.setter
    def average_inbound_round_trip_delay(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the averageInboundRoundTripDelay property value. The average inbound stream network round trip delay.
        Args:
            value: Value to set for the averageInboundRoundTripDelay property.
        """
        self._average_inbound_round_trip_delay = value
    
    @property
    def average_outbound_jitter(self,) -> Optional[Timedelta]:
        """
        Gets the averageOutboundJitter property value. The average outbound stream network jitter.
        Returns: Optional[Timedelta]
        """
        return self._average_outbound_jitter
    
    @average_outbound_jitter.setter
    def average_outbound_jitter(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the averageOutboundJitter property value. The average outbound stream network jitter.
        Args:
            value: Value to set for the averageOutboundJitter property.
        """
        self._average_outbound_jitter = value
    
    @property
    def average_outbound_packet_loss_rate_in_percentage(self,) -> Optional[float]:
        """
        Gets the averageOutboundPacketLossRateInPercentage property value. The average outbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        Returns: Optional[float]
        """
        return self._average_outbound_packet_loss_rate_in_percentage
    
    @average_outbound_packet_loss_rate_in_percentage.setter
    def average_outbound_packet_loss_rate_in_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the averageOutboundPacketLossRateInPercentage property value. The average outbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        Args:
            value: Value to set for the averageOutboundPacketLossRateInPercentage property.
        """
        self._average_outbound_packet_loss_rate_in_percentage = value
    
    @property
    def average_outbound_round_trip_delay(self,) -> Optional[Timedelta]:
        """
        Gets the averageOutboundRoundTripDelay property value. The average outbound stream network round trip delay.
        Returns: Optional[Timedelta]
        """
        return self._average_outbound_round_trip_delay
    
    @average_outbound_round_trip_delay.setter
    def average_outbound_round_trip_delay(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the averageOutboundRoundTripDelay property value. The average outbound stream network round trip delay.
        Args:
            value: Value to set for the averageOutboundRoundTripDelay property.
        """
        self._average_outbound_round_trip_delay = value
    
    @property
    def channel_index(self,) -> Optional[int]:
        """
        Gets the channelIndex property value. The channel index of media. Indexing begins with 1.  If a media session contains 3 video modalities, channel indexes will be 1, 2, and 3.
        Returns: Optional[int]
        """
        return self._channel_index
    
    @channel_index.setter
    def channel_index(self,value: Optional[int] = None) -> None:
        """
        Sets the channelIndex property value. The channel index of media. Indexing begins with 1.  If a media session contains 3 video modalities, channel indexes will be 1, 2, and 3.
        Args:
            value: Value to set for the channelIndex property.
        """
        self._channel_index = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new teleconferenceDeviceMediaQuality and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The average inbound stream network jitter.
        self._average_inbound_jitter: Optional[Timedelta] = None
        # The average inbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        self._average_inbound_packet_loss_rate_in_percentage: Optional[float] = None
        # The average inbound stream network round trip delay.
        self._average_inbound_round_trip_delay: Optional[Timedelta] = None
        # The average outbound stream network jitter.
        self._average_outbound_jitter: Optional[Timedelta] = None
        # The average outbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        self._average_outbound_packet_loss_rate_in_percentage: Optional[float] = None
        # The average outbound stream network round trip delay.
        self._average_outbound_round_trip_delay: Optional[Timedelta] = None
        # The channel index of media. Indexing begins with 1.  If a media session contains 3 video modalities, channel indexes will be 1, 2, and 3.
        self._channel_index: Optional[int] = None
        # The total number of the inbound packets.
        self._inbound_packets: Optional[int] = None
        # the local IP address for the media session.
        self._local_i_p_address: Optional[str] = None
        # The local media port.
        self._local_port: Optional[int] = None
        # The maximum inbound stream network jitter.
        self._maximum_inbound_jitter: Optional[Timedelta] = None
        # The maximum inbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        self._maximum_inbound_packet_loss_rate_in_percentage: Optional[float] = None
        # The maximum inbound stream network round trip delay.
        self._maximum_inbound_round_trip_delay: Optional[Timedelta] = None
        # The maximum outbound stream network jitter.
        self._maximum_outbound_jitter: Optional[Timedelta] = None
        # The maximum outbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        self._maximum_outbound_packet_loss_rate_in_percentage: Optional[float] = None
        # The maximum outbound stream network round trip delay.
        self._maximum_outbound_round_trip_delay: Optional[Timedelta] = None
        # The total modality duration. If the media enabled and disabled multiple times, MediaDuration will the summation of all of the durations.
        self._media_duration: Optional[Timedelta] = None
        # The network link speed in bytes
        self._network_link_speed_in_bytes: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The total number of the outbound packets.
        self._outbound_packets: Optional[int] = None
        # The remote IP address for the media session.
        self._remote_i_p_address: Optional[str] = None
        # The remote media port.
        self._remote_port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeleconferenceDeviceMediaQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeleconferenceDeviceMediaQuality
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeleconferenceDeviceMediaQuality()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "average_inbound_jitter": lambda n : setattr(self, 'average_inbound_jitter', n.get_object_value(Timedelta)),
            "average_inbound_packet_loss_rate_in_percentage": lambda n : setattr(self, 'average_inbound_packet_loss_rate_in_percentage', n.get_float_value()),
            "average_inbound_round_trip_delay": lambda n : setattr(self, 'average_inbound_round_trip_delay', n.get_object_value(Timedelta)),
            "average_outbound_jitter": lambda n : setattr(self, 'average_outbound_jitter', n.get_object_value(Timedelta)),
            "average_outbound_packet_loss_rate_in_percentage": lambda n : setattr(self, 'average_outbound_packet_loss_rate_in_percentage', n.get_float_value()),
            "average_outbound_round_trip_delay": lambda n : setattr(self, 'average_outbound_round_trip_delay', n.get_object_value(Timedelta)),
            "channel_index": lambda n : setattr(self, 'channel_index', n.get_int_value()),
            "inbound_packets": lambda n : setattr(self, 'inbound_packets', n.get_int_value()),
            "local_i_p_address": lambda n : setattr(self, 'local_i_p_address', n.get_str_value()),
            "local_port": lambda n : setattr(self, 'local_port', n.get_int_value()),
            "maximum_inbound_jitter": lambda n : setattr(self, 'maximum_inbound_jitter', n.get_object_value(Timedelta)),
            "maximum_inbound_packet_loss_rate_in_percentage": lambda n : setattr(self, 'maximum_inbound_packet_loss_rate_in_percentage', n.get_float_value()),
            "maximum_inbound_round_trip_delay": lambda n : setattr(self, 'maximum_inbound_round_trip_delay', n.get_object_value(Timedelta)),
            "maximum_outbound_jitter": lambda n : setattr(self, 'maximum_outbound_jitter', n.get_object_value(Timedelta)),
            "maximum_outbound_packet_loss_rate_in_percentage": lambda n : setattr(self, 'maximum_outbound_packet_loss_rate_in_percentage', n.get_float_value()),
            "maximum_outbound_round_trip_delay": lambda n : setattr(self, 'maximum_outbound_round_trip_delay', n.get_object_value(Timedelta)),
            "media_duration": lambda n : setattr(self, 'media_duration', n.get_object_value(Timedelta)),
            "network_link_speed_in_bytes": lambda n : setattr(self, 'network_link_speed_in_bytes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outbound_packets": lambda n : setattr(self, 'outbound_packets', n.get_int_value()),
            "remote_i_p_address": lambda n : setattr(self, 'remote_i_p_address', n.get_str_value()),
            "remote_port": lambda n : setattr(self, 'remote_port', n.get_int_value()),
        }
        return fields
    
    @property
    def inbound_packets(self,) -> Optional[int]:
        """
        Gets the inboundPackets property value. The total number of the inbound packets.
        Returns: Optional[int]
        """
        return self._inbound_packets
    
    @inbound_packets.setter
    def inbound_packets(self,value: Optional[int] = None) -> None:
        """
        Sets the inboundPackets property value. The total number of the inbound packets.
        Args:
            value: Value to set for the inboundPackets property.
        """
        self._inbound_packets = value
    
    @property
    def local_i_p_address(self,) -> Optional[str]:
        """
        Gets the localIPAddress property value. the local IP address for the media session.
        Returns: Optional[str]
        """
        return self._local_i_p_address
    
    @local_i_p_address.setter
    def local_i_p_address(self,value: Optional[str] = None) -> None:
        """
        Sets the localIPAddress property value. the local IP address for the media session.
        Args:
            value: Value to set for the localIPAddress property.
        """
        self._local_i_p_address = value
    
    @property
    def local_port(self,) -> Optional[int]:
        """
        Gets the localPort property value. The local media port.
        Returns: Optional[int]
        """
        return self._local_port
    
    @local_port.setter
    def local_port(self,value: Optional[int] = None) -> None:
        """
        Sets the localPort property value. The local media port.
        Args:
            value: Value to set for the localPort property.
        """
        self._local_port = value
    
    @property
    def maximum_inbound_jitter(self,) -> Optional[Timedelta]:
        """
        Gets the maximumInboundJitter property value. The maximum inbound stream network jitter.
        Returns: Optional[Timedelta]
        """
        return self._maximum_inbound_jitter
    
    @maximum_inbound_jitter.setter
    def maximum_inbound_jitter(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maximumInboundJitter property value. The maximum inbound stream network jitter.
        Args:
            value: Value to set for the maximumInboundJitter property.
        """
        self._maximum_inbound_jitter = value
    
    @property
    def maximum_inbound_packet_loss_rate_in_percentage(self,) -> Optional[float]:
        """
        Gets the maximumInboundPacketLossRateInPercentage property value. The maximum inbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        Returns: Optional[float]
        """
        return self._maximum_inbound_packet_loss_rate_in_percentage
    
    @maximum_inbound_packet_loss_rate_in_percentage.setter
    def maximum_inbound_packet_loss_rate_in_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the maximumInboundPacketLossRateInPercentage property value. The maximum inbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        Args:
            value: Value to set for the maximumInboundPacketLossRateInPercentage property.
        """
        self._maximum_inbound_packet_loss_rate_in_percentage = value
    
    @property
    def maximum_inbound_round_trip_delay(self,) -> Optional[Timedelta]:
        """
        Gets the maximumInboundRoundTripDelay property value. The maximum inbound stream network round trip delay.
        Returns: Optional[Timedelta]
        """
        return self._maximum_inbound_round_trip_delay
    
    @maximum_inbound_round_trip_delay.setter
    def maximum_inbound_round_trip_delay(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maximumInboundRoundTripDelay property value. The maximum inbound stream network round trip delay.
        Args:
            value: Value to set for the maximumInboundRoundTripDelay property.
        """
        self._maximum_inbound_round_trip_delay = value
    
    @property
    def maximum_outbound_jitter(self,) -> Optional[Timedelta]:
        """
        Gets the maximumOutboundJitter property value. The maximum outbound stream network jitter.
        Returns: Optional[Timedelta]
        """
        return self._maximum_outbound_jitter
    
    @maximum_outbound_jitter.setter
    def maximum_outbound_jitter(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maximumOutboundJitter property value. The maximum outbound stream network jitter.
        Args:
            value: Value to set for the maximumOutboundJitter property.
        """
        self._maximum_outbound_jitter = value
    
    @property
    def maximum_outbound_packet_loss_rate_in_percentage(self,) -> Optional[float]:
        """
        Gets the maximumOutboundPacketLossRateInPercentage property value. The maximum outbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        Returns: Optional[float]
        """
        return self._maximum_outbound_packet_loss_rate_in_percentage
    
    @maximum_outbound_packet_loss_rate_in_percentage.setter
    def maximum_outbound_packet_loss_rate_in_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the maximumOutboundPacketLossRateInPercentage property value. The maximum outbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
        Args:
            value: Value to set for the maximumOutboundPacketLossRateInPercentage property.
        """
        self._maximum_outbound_packet_loss_rate_in_percentage = value
    
    @property
    def maximum_outbound_round_trip_delay(self,) -> Optional[Timedelta]:
        """
        Gets the maximumOutboundRoundTripDelay property value. The maximum outbound stream network round trip delay.
        Returns: Optional[Timedelta]
        """
        return self._maximum_outbound_round_trip_delay
    
    @maximum_outbound_round_trip_delay.setter
    def maximum_outbound_round_trip_delay(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maximumOutboundRoundTripDelay property value. The maximum outbound stream network round trip delay.
        Args:
            value: Value to set for the maximumOutboundRoundTripDelay property.
        """
        self._maximum_outbound_round_trip_delay = value
    
    @property
    def media_duration(self,) -> Optional[Timedelta]:
        """
        Gets the mediaDuration property value. The total modality duration. If the media enabled and disabled multiple times, MediaDuration will the summation of all of the durations.
        Returns: Optional[Timedelta]
        """
        return self._media_duration
    
    @media_duration.setter
    def media_duration(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the mediaDuration property value. The total modality duration. If the media enabled and disabled multiple times, MediaDuration will the summation of all of the durations.
        Args:
            value: Value to set for the mediaDuration property.
        """
        self._media_duration = value
    
    @property
    def network_link_speed_in_bytes(self,) -> Optional[int]:
        """
        Gets the networkLinkSpeedInBytes property value. The network link speed in bytes
        Returns: Optional[int]
        """
        return self._network_link_speed_in_bytes
    
    @network_link_speed_in_bytes.setter
    def network_link_speed_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the networkLinkSpeedInBytes property value. The network link speed in bytes
        Args:
            value: Value to set for the networkLinkSpeedInBytes property.
        """
        self._network_link_speed_in_bytes = value
    
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
    def outbound_packets(self,) -> Optional[int]:
        """
        Gets the outboundPackets property value. The total number of the outbound packets.
        Returns: Optional[int]
        """
        return self._outbound_packets
    
    @outbound_packets.setter
    def outbound_packets(self,value: Optional[int] = None) -> None:
        """
        Sets the outboundPackets property value. The total number of the outbound packets.
        Args:
            value: Value to set for the outboundPackets property.
        """
        self._outbound_packets = value
    
    @property
    def remote_i_p_address(self,) -> Optional[str]:
        """
        Gets the remoteIPAddress property value. The remote IP address for the media session.
        Returns: Optional[str]
        """
        return self._remote_i_p_address
    
    @remote_i_p_address.setter
    def remote_i_p_address(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteIPAddress property value. The remote IP address for the media session.
        Args:
            value: Value to set for the remoteIPAddress property.
        """
        self._remote_i_p_address = value
    
    @property
    def remote_port(self,) -> Optional[int]:
        """
        Gets the remotePort property value. The remote media port.
        Returns: Optional[int]
        """
        return self._remote_port
    
    @remote_port.setter
    def remote_port(self,value: Optional[int] = None) -> None:
        """
        Sets the remotePort property value. The remote media port.
        Args:
            value: Value to set for the remotePort property.
        """
        self._remote_port = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("averageInboundJitter", self.average_inbound_jitter)
        writer.write_float_value("averageInboundPacketLossRateInPercentage", self.average_inbound_packet_loss_rate_in_percentage)
        writer.write_object_value("averageInboundRoundTripDelay", self.average_inbound_round_trip_delay)
        writer.write_object_value("averageOutboundJitter", self.average_outbound_jitter)
        writer.write_float_value("averageOutboundPacketLossRateInPercentage", self.average_outbound_packet_loss_rate_in_percentage)
        writer.write_object_value("averageOutboundRoundTripDelay", self.average_outbound_round_trip_delay)
        writer.write_int_value("channelIndex", self.channel_index)
        writer.write_int_value("inboundPackets", self.inbound_packets)
        writer.write_str_value("localIPAddress", self.local_i_p_address)
        writer.write_int_value("localPort", self.local_port)
        writer.write_object_value("maximumInboundJitter", self.maximum_inbound_jitter)
        writer.write_float_value("maximumInboundPacketLossRateInPercentage", self.maximum_inbound_packet_loss_rate_in_percentage)
        writer.write_object_value("maximumInboundRoundTripDelay", self.maximum_inbound_round_trip_delay)
        writer.write_object_value("maximumOutboundJitter", self.maximum_outbound_jitter)
        writer.write_float_value("maximumOutboundPacketLossRateInPercentage", self.maximum_outbound_packet_loss_rate_in_percentage)
        writer.write_object_value("maximumOutboundRoundTripDelay", self.maximum_outbound_round_trip_delay)
        writer.write_object_value("mediaDuration", self.media_duration)
        writer.write_int_value("networkLinkSpeedInBytes", self.network_link_speed_in_bytes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("outboundPackets", self.outbound_packets)
        writer.write_str_value("remoteIPAddress", self.remote_i_p_address)
        writer.write_int_value("remotePort", self.remote_port)
        writer.write_additional_data_value(self.additional_data)
    

