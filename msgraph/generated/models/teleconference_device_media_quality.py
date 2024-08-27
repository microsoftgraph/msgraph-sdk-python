from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .teleconference_device_audio_quality import TeleconferenceDeviceAudioQuality
    from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality
    from .teleconference_device_video_quality import TeleconferenceDeviceVideoQuality

@dataclass
class TeleconferenceDeviceMediaQuality(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The average inbound stream network jitter.
    average_inbound_jitter: Optional[datetime.timedelta] = None
    # The average inbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
    average_inbound_packet_loss_rate_in_percentage: Optional[float] = None
    # The average inbound stream network round trip delay.
    average_inbound_round_trip_delay: Optional[datetime.timedelta] = None
    # The average outbound stream network jitter.
    average_outbound_jitter: Optional[datetime.timedelta] = None
    # The average outbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
    average_outbound_packet_loss_rate_in_percentage: Optional[float] = None
    # The average outbound stream network round trip delay.
    average_outbound_round_trip_delay: Optional[datetime.timedelta] = None
    # The channel index of media. Indexing begins with 1.  If a media session contains 3 video modalities, channel indexes will be 1, 2, and 3.
    channel_index: Optional[int] = None
    # The total number of the inbound packets.
    inbound_packets: Optional[int] = None
    # the local IP address for the media session.
    local_i_p_address: Optional[str] = None
    # The local media port.
    local_port: Optional[int] = None
    # The maximum inbound stream network jitter.
    maximum_inbound_jitter: Optional[datetime.timedelta] = None
    # The maximum inbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
    maximum_inbound_packet_loss_rate_in_percentage: Optional[float] = None
    # The maximum inbound stream network round trip delay.
    maximum_inbound_round_trip_delay: Optional[datetime.timedelta] = None
    # The maximum outbound stream network jitter.
    maximum_outbound_jitter: Optional[datetime.timedelta] = None
    # The maximum outbound stream packet loss rate in percentage (0-100). For example, 0.01 means 0.01%.
    maximum_outbound_packet_loss_rate_in_percentage: Optional[float] = None
    # The maximum outbound stream network round trip delay.
    maximum_outbound_round_trip_delay: Optional[datetime.timedelta] = None
    # The total modality duration. If the media enabled and disabled multiple times, MediaDuration will the summation of all of the durations.
    media_duration: Optional[datetime.timedelta] = None
    # The network link speed in bytes
    network_link_speed_in_bytes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The total number of the outbound packets.
    outbound_packets: Optional[int] = None
    # The remote IP address for the media session.
    remote_i_p_address: Optional[str] = None
    # The remote media port.
    remote_port: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TeleconferenceDeviceMediaQuality:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TeleconferenceDeviceMediaQuality
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teleconferenceDeviceAudioQuality".casefold():
            from .teleconference_device_audio_quality import TeleconferenceDeviceAudioQuality

            return TeleconferenceDeviceAudioQuality()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teleconferenceDeviceScreenSharingQuality".casefold():
            from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality

            return TeleconferenceDeviceScreenSharingQuality()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teleconferenceDeviceVideoQuality".casefold():
            from .teleconference_device_video_quality import TeleconferenceDeviceVideoQuality

            return TeleconferenceDeviceVideoQuality()
        return TeleconferenceDeviceMediaQuality()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .teleconference_device_audio_quality import TeleconferenceDeviceAudioQuality
        from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality
        from .teleconference_device_video_quality import TeleconferenceDeviceVideoQuality

        from .teleconference_device_audio_quality import TeleconferenceDeviceAudioQuality
        from .teleconference_device_screen_sharing_quality import TeleconferenceDeviceScreenSharingQuality
        from .teleconference_device_video_quality import TeleconferenceDeviceVideoQuality

        fields: Dict[str, Callable[[Any], None]] = {
            "averageInboundJitter": lambda n : setattr(self, 'average_inbound_jitter', n.get_timedelta_value()),
            "averageInboundPacketLossRateInPercentage": lambda n : setattr(self, 'average_inbound_packet_loss_rate_in_percentage', n.get_float_value()),
            "averageInboundRoundTripDelay": lambda n : setattr(self, 'average_inbound_round_trip_delay', n.get_timedelta_value()),
            "averageOutboundJitter": lambda n : setattr(self, 'average_outbound_jitter', n.get_timedelta_value()),
            "averageOutboundPacketLossRateInPercentage": lambda n : setattr(self, 'average_outbound_packet_loss_rate_in_percentage', n.get_float_value()),
            "averageOutboundRoundTripDelay": lambda n : setattr(self, 'average_outbound_round_trip_delay', n.get_timedelta_value()),
            "channelIndex": lambda n : setattr(self, 'channel_index', n.get_int_value()),
            "inboundPackets": lambda n : setattr(self, 'inbound_packets', n.get_int_value()),
            "localIPAddress": lambda n : setattr(self, 'local_i_p_address', n.get_str_value()),
            "localPort": lambda n : setattr(self, 'local_port', n.get_int_value()),
            "maximumInboundJitter": lambda n : setattr(self, 'maximum_inbound_jitter', n.get_timedelta_value()),
            "maximumInboundPacketLossRateInPercentage": lambda n : setattr(self, 'maximum_inbound_packet_loss_rate_in_percentage', n.get_float_value()),
            "maximumInboundRoundTripDelay": lambda n : setattr(self, 'maximum_inbound_round_trip_delay', n.get_timedelta_value()),
            "maximumOutboundJitter": lambda n : setattr(self, 'maximum_outbound_jitter', n.get_timedelta_value()),
            "maximumOutboundPacketLossRateInPercentage": lambda n : setattr(self, 'maximum_outbound_packet_loss_rate_in_percentage', n.get_float_value()),
            "maximumOutboundRoundTripDelay": lambda n : setattr(self, 'maximum_outbound_round_trip_delay', n.get_timedelta_value()),
            "mediaDuration": lambda n : setattr(self, 'media_duration', n.get_timedelta_value()),
            "networkLinkSpeedInBytes": lambda n : setattr(self, 'network_link_speed_in_bytes', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outboundPackets": lambda n : setattr(self, 'outbound_packets', n.get_int_value()),
            "remoteIPAddress": lambda n : setattr(self, 'remote_i_p_address', n.get_str_value()),
            "remotePort": lambda n : setattr(self, 'remote_port', n.get_int_value()),
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
        writer.write_timedelta_value("averageInboundJitter", self.average_inbound_jitter)
        writer.write_float_value("averageInboundPacketLossRateInPercentage", self.average_inbound_packet_loss_rate_in_percentage)
        writer.write_timedelta_value("averageInboundRoundTripDelay", self.average_inbound_round_trip_delay)
        writer.write_timedelta_value("averageOutboundJitter", self.average_outbound_jitter)
        writer.write_float_value("averageOutboundPacketLossRateInPercentage", self.average_outbound_packet_loss_rate_in_percentage)
        writer.write_timedelta_value("averageOutboundRoundTripDelay", self.average_outbound_round_trip_delay)
        writer.write_int_value("channelIndex", self.channel_index)
        writer.write_int_value("inboundPackets", self.inbound_packets)
        writer.write_str_value("localIPAddress", self.local_i_p_address)
        writer.write_int_value("localPort", self.local_port)
        writer.write_timedelta_value("maximumInboundJitter", self.maximum_inbound_jitter)
        writer.write_float_value("maximumInboundPacketLossRateInPercentage", self.maximum_inbound_packet_loss_rate_in_percentage)
        writer.write_timedelta_value("maximumInboundRoundTripDelay", self.maximum_inbound_round_trip_delay)
        writer.write_timedelta_value("maximumOutboundJitter", self.maximum_outbound_jitter)
        writer.write_float_value("maximumOutboundPacketLossRateInPercentage", self.maximum_outbound_packet_loss_rate_in_percentage)
        writer.write_timedelta_value("maximumOutboundRoundTripDelay", self.maximum_outbound_round_trip_delay)
        writer.write_timedelta_value("mediaDuration", self.media_duration)
        writer.write_int_value("networkLinkSpeedInBytes", self.network_link_speed_in_bytes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("outboundPackets", self.outbound_packets)
        writer.write_str_value("remoteIPAddress", self.remote_i_p_address)
        writer.write_int_value("remotePort", self.remote_port)
        writer.write_additional_data_value(self.additional_data)
    

