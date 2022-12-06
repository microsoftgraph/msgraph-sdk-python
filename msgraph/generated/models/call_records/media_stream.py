from __future__ import annotations
from datetime import datetime, timedelta
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

audio_codec = lazy_import('msgraph.generated.models.call_records.audio_codec')
media_stream_direction = lazy_import('msgraph.generated.models.call_records.media_stream_direction')
video_codec = lazy_import('msgraph.generated.models.call_records.video_codec')

class MediaStream(AdditionalDataHolder, Parsable):
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
    def audio_codec(self,) -> Optional[audio_codec.AudioCodec]:
        """
        Gets the audioCodec property value. Codec name used to encode audio for transmission on the network. Possible values are: unknown, invalid, cn, pcma, pcmu, amrWide, g722, g7221, g7221c, g729, multiChannelAudio, muchv2, opus, satin, satinFullband, rtAudio8, rtAudio16, silk, silkNarrow, silkWide, siren, xmsRTA, unknownFutureValue.
        Returns: Optional[audio_codec.AudioCodec]
        """
        return self._audio_codec
    
    @audio_codec.setter
    def audio_codec(self,value: Optional[audio_codec.AudioCodec] = None) -> None:
        """
        Sets the audioCodec property value. Codec name used to encode audio for transmission on the network. Possible values are: unknown, invalid, cn, pcma, pcmu, amrWide, g722, g7221, g7221c, g729, multiChannelAudio, muchv2, opus, satin, satinFullband, rtAudio8, rtAudio16, silk, silkNarrow, silkWide, siren, xmsRTA, unknownFutureValue.
        Args:
            value: Value to set for the audioCodec property.
        """
        self._audio_codec = value
    
    @property
    def average_audio_degradation(self,) -> Optional[float]:
        """
        Gets the averageAudioDegradation property value. Average Network Mean Opinion Score degradation for stream. Represents how much the network loss and jitter has impacted the quality of received audio.
        Returns: Optional[float]
        """
        return self._average_audio_degradation
    
    @average_audio_degradation.setter
    def average_audio_degradation(self,value: Optional[float] = None) -> None:
        """
        Sets the averageAudioDegradation property value. Average Network Mean Opinion Score degradation for stream. Represents how much the network loss and jitter has impacted the quality of received audio.
        Args:
            value: Value to set for the averageAudioDegradation property.
        """
        self._average_audio_degradation = value
    
    @property
    def average_audio_network_jitter(self,) -> Optional[Timedelta]:
        """
        Gets the averageAudioNetworkJitter property value. Average jitter for the stream computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Returns: Optional[Timedelta]
        """
        return self._average_audio_network_jitter
    
    @average_audio_network_jitter.setter
    def average_audio_network_jitter(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the averageAudioNetworkJitter property value. Average jitter for the stream computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Args:
            value: Value to set for the averageAudioNetworkJitter property.
        """
        self._average_audio_network_jitter = value
    
    @property
    def average_bandwidth_estimate(self,) -> Optional[int]:
        """
        Gets the averageBandwidthEstimate property value. Average estimated bandwidth available between two endpoints in bits per second.
        Returns: Optional[int]
        """
        return self._average_bandwidth_estimate
    
    @average_bandwidth_estimate.setter
    def average_bandwidth_estimate(self,value: Optional[int] = None) -> None:
        """
        Sets the averageBandwidthEstimate property value. Average estimated bandwidth available between two endpoints in bits per second.
        Args:
            value: Value to set for the averageBandwidthEstimate property.
        """
        self._average_bandwidth_estimate = value
    
    @property
    def average_jitter(self,) -> Optional[Timedelta]:
        """
        Gets the averageJitter property value. Average jitter for the stream computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Returns: Optional[Timedelta]
        """
        return self._average_jitter
    
    @average_jitter.setter
    def average_jitter(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the averageJitter property value. Average jitter for the stream computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Args:
            value: Value to set for the averageJitter property.
        """
        self._average_jitter = value
    
    @property
    def average_packet_loss_rate(self,) -> Optional[float]:
        """
        Gets the averagePacketLossRate property value. Average packet loss rate for stream.
        Returns: Optional[float]
        """
        return self._average_packet_loss_rate
    
    @average_packet_loss_rate.setter
    def average_packet_loss_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the averagePacketLossRate property value. Average packet loss rate for stream.
        Args:
            value: Value to set for the averagePacketLossRate property.
        """
        self._average_packet_loss_rate = value
    
    @property
    def average_ratio_of_concealed_samples(self,) -> Optional[float]:
        """
        Gets the averageRatioOfConcealedSamples property value. Ratio of the number of audio frames with samples generated by packet loss concealment to the total number of audio frames.
        Returns: Optional[float]
        """
        return self._average_ratio_of_concealed_samples
    
    @average_ratio_of_concealed_samples.setter
    def average_ratio_of_concealed_samples(self,value: Optional[float] = None) -> None:
        """
        Sets the averageRatioOfConcealedSamples property value. Ratio of the number of audio frames with samples generated by packet loss concealment to the total number of audio frames.
        Args:
            value: Value to set for the averageRatioOfConcealedSamples property.
        """
        self._average_ratio_of_concealed_samples = value
    
    @property
    def average_received_frame_rate(self,) -> Optional[float]:
        """
        Gets the averageReceivedFrameRate property value. Average frames per second received for all video streams computed over the duration of the session.
        Returns: Optional[float]
        """
        return self._average_received_frame_rate
    
    @average_received_frame_rate.setter
    def average_received_frame_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the averageReceivedFrameRate property value. Average frames per second received for all video streams computed over the duration of the session.
        Args:
            value: Value to set for the averageReceivedFrameRate property.
        """
        self._average_received_frame_rate = value
    
    @property
    def average_round_trip_time(self,) -> Optional[Timedelta]:
        """
        Gets the averageRoundTripTime property value. Average network propagation round-trip time computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Returns: Optional[Timedelta]
        """
        return self._average_round_trip_time
    
    @average_round_trip_time.setter
    def average_round_trip_time(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the averageRoundTripTime property value. Average network propagation round-trip time computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Args:
            value: Value to set for the averageRoundTripTime property.
        """
        self._average_round_trip_time = value
    
    @property
    def average_video_frame_loss_percentage(self,) -> Optional[float]:
        """
        Gets the averageVideoFrameLossPercentage property value. Average percentage of video frames lost as displayed to the user.
        Returns: Optional[float]
        """
        return self._average_video_frame_loss_percentage
    
    @average_video_frame_loss_percentage.setter
    def average_video_frame_loss_percentage(self,value: Optional[float] = None) -> None:
        """
        Sets the averageVideoFrameLossPercentage property value. Average percentage of video frames lost as displayed to the user.
        Args:
            value: Value to set for the averageVideoFrameLossPercentage property.
        """
        self._average_video_frame_loss_percentage = value
    
    @property
    def average_video_frame_rate(self,) -> Optional[float]:
        """
        Gets the averageVideoFrameRate property value. Average frames per second received for a video stream, computed over the duration of the session.
        Returns: Optional[float]
        """
        return self._average_video_frame_rate
    
    @average_video_frame_rate.setter
    def average_video_frame_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the averageVideoFrameRate property value. Average frames per second received for a video stream, computed over the duration of the session.
        Args:
            value: Value to set for the averageVideoFrameRate property.
        """
        self._average_video_frame_rate = value
    
    @property
    def average_video_packet_loss_rate(self,) -> Optional[float]:
        """
        Gets the averageVideoPacketLossRate property value. Average fraction of packets lost, as specified in [RFC 3550][], computed over the duration of the session.
        Returns: Optional[float]
        """
        return self._average_video_packet_loss_rate
    
    @average_video_packet_loss_rate.setter
    def average_video_packet_loss_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the averageVideoPacketLossRate property value. Average fraction of packets lost, as specified in [RFC 3550][], computed over the duration of the session.
        Args:
            value: Value to set for the averageVideoPacketLossRate property.
        """
        self._average_video_packet_loss_rate = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new mediaStream and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Codec name used to encode audio for transmission on the network. Possible values are: unknown, invalid, cn, pcma, pcmu, amrWide, g722, g7221, g7221c, g729, multiChannelAudio, muchv2, opus, satin, satinFullband, rtAudio8, rtAudio16, silk, silkNarrow, silkWide, siren, xmsRTA, unknownFutureValue.
        self._audio_codec: Optional[audio_codec.AudioCodec] = None
        # Average Network Mean Opinion Score degradation for stream. Represents how much the network loss and jitter has impacted the quality of received audio.
        self._average_audio_degradation: Optional[float] = None
        # Average jitter for the stream computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        self._average_audio_network_jitter: Optional[Timedelta] = None
        # Average estimated bandwidth available between two endpoints in bits per second.
        self._average_bandwidth_estimate: Optional[int] = None
        # Average jitter for the stream computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        self._average_jitter: Optional[Timedelta] = None
        # Average packet loss rate for stream.
        self._average_packet_loss_rate: Optional[float] = None
        # Ratio of the number of audio frames with samples generated by packet loss concealment to the total number of audio frames.
        self._average_ratio_of_concealed_samples: Optional[float] = None
        # Average frames per second received for all video streams computed over the duration of the session.
        self._average_received_frame_rate: Optional[float] = None
        # Average network propagation round-trip time computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        self._average_round_trip_time: Optional[Timedelta] = None
        # Average percentage of video frames lost as displayed to the user.
        self._average_video_frame_loss_percentage: Optional[float] = None
        # Average frames per second received for a video stream, computed over the duration of the session.
        self._average_video_frame_rate: Optional[float] = None
        # Average fraction of packets lost, as specified in [RFC 3550][], computed over the duration of the session.
        self._average_video_packet_loss_rate: Optional[float] = None
        # UTC time when the stream ended. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._end_date_time: Optional[datetime] = None
        # Fraction of the call where frame rate is less than 7.5 frames per second.
        self._low_frame_rate_ratio: Optional[float] = None
        # Fraction of the call that the client is running less than 70% expected video processing capability.
        self._low_video_processing_capability_ratio: Optional[float] = None
        # Maximum of audio network jitter computed over each of the 20 second windows during the session, denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        self._max_audio_network_jitter: Optional[Timedelta] = None
        # Maximum jitter for the stream computed as specified in RFC 3550, denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        self._max_jitter: Optional[Timedelta] = None
        # Maximum packet loss rate for the stream.
        self._max_packet_loss_rate: Optional[float] = None
        # Maximum ratio of packets concealed by the healer.
        self._max_ratio_of_concealed_samples: Optional[float] = None
        # Maximum network propagation round-trip time computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        self._max_round_trip_time: Optional[Timedelta] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Packet count for the stream.
        self._packet_utilization: Optional[int] = None
        # Packet loss rate after FEC has been applied aggregated across all video streams and codecs.
        self._post_forward_error_correction_packet_loss_rate: Optional[float] = None
        # UTC time when the stream started. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._start_date_time: Optional[datetime] = None
        # The streamDirection property
        self._stream_direction: Optional[media_stream_direction.MediaStreamDirection] = None
        # Unique identifier for the stream.
        self._stream_id: Optional[str] = None
        # Codec name used to encode video for transmission on the network. Possible values are: unknown, invalid, av1, h263, h264, h264s, h264uc, h265, rtvc1, rtVideo, xrtvc1, unknownFutureValue.
        self._video_codec: Optional[video_codec.VideoCodec] = None
        # True if the media stream bypassed the Mediation Server and went straight between client and PSTN Gateway/PBX, false otherwise.
        self._was_media_bypassed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MediaStream:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MediaStream
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MediaStream()
    
    @property
    def end_date_time(self,) -> Optional[datetime]:
        """
        Gets the endDateTime property value. UTC time when the stream ended. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._end_date_time
    
    @end_date_time.setter
    def end_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the endDateTime property value. UTC time when the stream ended. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the endDateTime property.
        """
        self._end_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audio_codec": lambda n : setattr(self, 'audio_codec', n.get_enum_value(audio_codec.AudioCodec)),
            "average_audio_degradation": lambda n : setattr(self, 'average_audio_degradation', n.get_float_value()),
            "average_audio_network_jitter": lambda n : setattr(self, 'average_audio_network_jitter', n.get_object_value(Timedelta)),
            "average_bandwidth_estimate": lambda n : setattr(self, 'average_bandwidth_estimate', n.get_int_value()),
            "average_jitter": lambda n : setattr(self, 'average_jitter', n.get_object_value(Timedelta)),
            "average_packet_loss_rate": lambda n : setattr(self, 'average_packet_loss_rate', n.get_float_value()),
            "average_ratio_of_concealed_samples": lambda n : setattr(self, 'average_ratio_of_concealed_samples', n.get_float_value()),
            "average_received_frame_rate": lambda n : setattr(self, 'average_received_frame_rate', n.get_float_value()),
            "average_round_trip_time": lambda n : setattr(self, 'average_round_trip_time', n.get_object_value(Timedelta)),
            "average_video_frame_loss_percentage": lambda n : setattr(self, 'average_video_frame_loss_percentage', n.get_float_value()),
            "average_video_frame_rate": lambda n : setattr(self, 'average_video_frame_rate', n.get_float_value()),
            "average_video_packet_loss_rate": lambda n : setattr(self, 'average_video_packet_loss_rate', n.get_float_value()),
            "end_date_time": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "low_frame_rate_ratio": lambda n : setattr(self, 'low_frame_rate_ratio', n.get_float_value()),
            "low_video_processing_capability_ratio": lambda n : setattr(self, 'low_video_processing_capability_ratio', n.get_float_value()),
            "max_audio_network_jitter": lambda n : setattr(self, 'max_audio_network_jitter', n.get_object_value(Timedelta)),
            "max_jitter": lambda n : setattr(self, 'max_jitter', n.get_object_value(Timedelta)),
            "max_packet_loss_rate": lambda n : setattr(self, 'max_packet_loss_rate', n.get_float_value()),
            "max_ratio_of_concealed_samples": lambda n : setattr(self, 'max_ratio_of_concealed_samples', n.get_float_value()),
            "max_round_trip_time": lambda n : setattr(self, 'max_round_trip_time', n.get_object_value(Timedelta)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "packet_utilization": lambda n : setattr(self, 'packet_utilization', n.get_int_value()),
            "post_forward_error_correction_packet_loss_rate": lambda n : setattr(self, 'post_forward_error_correction_packet_loss_rate', n.get_float_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "stream_direction": lambda n : setattr(self, 'stream_direction', n.get_enum_value(media_stream_direction.MediaStreamDirection)),
            "stream_id": lambda n : setattr(self, 'stream_id', n.get_str_value()),
            "video_codec": lambda n : setattr(self, 'video_codec', n.get_enum_value(video_codec.VideoCodec)),
            "was_media_bypassed": lambda n : setattr(self, 'was_media_bypassed', n.get_bool_value()),
        }
        return fields
    
    @property
    def low_frame_rate_ratio(self,) -> Optional[float]:
        """
        Gets the lowFrameRateRatio property value. Fraction of the call where frame rate is less than 7.5 frames per second.
        Returns: Optional[float]
        """
        return self._low_frame_rate_ratio
    
    @low_frame_rate_ratio.setter
    def low_frame_rate_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the lowFrameRateRatio property value. Fraction of the call where frame rate is less than 7.5 frames per second.
        Args:
            value: Value to set for the lowFrameRateRatio property.
        """
        self._low_frame_rate_ratio = value
    
    @property
    def low_video_processing_capability_ratio(self,) -> Optional[float]:
        """
        Gets the lowVideoProcessingCapabilityRatio property value. Fraction of the call that the client is running less than 70% expected video processing capability.
        Returns: Optional[float]
        """
        return self._low_video_processing_capability_ratio
    
    @low_video_processing_capability_ratio.setter
    def low_video_processing_capability_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the lowVideoProcessingCapabilityRatio property value. Fraction of the call that the client is running less than 70% expected video processing capability.
        Args:
            value: Value to set for the lowVideoProcessingCapabilityRatio property.
        """
        self._low_video_processing_capability_ratio = value
    
    @property
    def max_audio_network_jitter(self,) -> Optional[Timedelta]:
        """
        Gets the maxAudioNetworkJitter property value. Maximum of audio network jitter computed over each of the 20 second windows during the session, denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Returns: Optional[Timedelta]
        """
        return self._max_audio_network_jitter
    
    @max_audio_network_jitter.setter
    def max_audio_network_jitter(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maxAudioNetworkJitter property value. Maximum of audio network jitter computed over each of the 20 second windows during the session, denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Args:
            value: Value to set for the maxAudioNetworkJitter property.
        """
        self._max_audio_network_jitter = value
    
    @property
    def max_jitter(self,) -> Optional[Timedelta]:
        """
        Gets the maxJitter property value. Maximum jitter for the stream computed as specified in RFC 3550, denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Returns: Optional[Timedelta]
        """
        return self._max_jitter
    
    @max_jitter.setter
    def max_jitter(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maxJitter property value. Maximum jitter for the stream computed as specified in RFC 3550, denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Args:
            value: Value to set for the maxJitter property.
        """
        self._max_jitter = value
    
    @property
    def max_packet_loss_rate(self,) -> Optional[float]:
        """
        Gets the maxPacketLossRate property value. Maximum packet loss rate for the stream.
        Returns: Optional[float]
        """
        return self._max_packet_loss_rate
    
    @max_packet_loss_rate.setter
    def max_packet_loss_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the maxPacketLossRate property value. Maximum packet loss rate for the stream.
        Args:
            value: Value to set for the maxPacketLossRate property.
        """
        self._max_packet_loss_rate = value
    
    @property
    def max_ratio_of_concealed_samples(self,) -> Optional[float]:
        """
        Gets the maxRatioOfConcealedSamples property value. Maximum ratio of packets concealed by the healer.
        Returns: Optional[float]
        """
        return self._max_ratio_of_concealed_samples
    
    @max_ratio_of_concealed_samples.setter
    def max_ratio_of_concealed_samples(self,value: Optional[float] = None) -> None:
        """
        Sets the maxRatioOfConcealedSamples property value. Maximum ratio of packets concealed by the healer.
        Args:
            value: Value to set for the maxRatioOfConcealedSamples property.
        """
        self._max_ratio_of_concealed_samples = value
    
    @property
    def max_round_trip_time(self,) -> Optional[Timedelta]:
        """
        Gets the maxRoundTripTime property value. Maximum network propagation round-trip time computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Returns: Optional[Timedelta]
        """
        return self._max_round_trip_time
    
    @max_round_trip_time.setter
    def max_round_trip_time(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the maxRoundTripTime property value. Maximum network propagation round-trip time computed as specified in [RFC 3550][], denoted in [ISO 8601][] format. For example, 1 second is denoted as 'PT1S', where 'P' is the duration designator, 'T' is the time designator, and 'S' is the second designator.
        Args:
            value: Value to set for the maxRoundTripTime property.
        """
        self._max_round_trip_time = value
    
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
    def packet_utilization(self,) -> Optional[int]:
        """
        Gets the packetUtilization property value. Packet count for the stream.
        Returns: Optional[int]
        """
        return self._packet_utilization
    
    @packet_utilization.setter
    def packet_utilization(self,value: Optional[int] = None) -> None:
        """
        Sets the packetUtilization property value. Packet count for the stream.
        Args:
            value: Value to set for the packetUtilization property.
        """
        self._packet_utilization = value
    
    @property
    def post_forward_error_correction_packet_loss_rate(self,) -> Optional[float]:
        """
        Gets the postForwardErrorCorrectionPacketLossRate property value. Packet loss rate after FEC has been applied aggregated across all video streams and codecs.
        Returns: Optional[float]
        """
        return self._post_forward_error_correction_packet_loss_rate
    
    @post_forward_error_correction_packet_loss_rate.setter
    def post_forward_error_correction_packet_loss_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the postForwardErrorCorrectionPacketLossRate property value. Packet loss rate after FEC has been applied aggregated across all video streams and codecs.
        Args:
            value: Value to set for the postForwardErrorCorrectionPacketLossRate property.
        """
        self._post_forward_error_correction_packet_loss_rate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("audioCodec", self.audio_codec)
        writer.write_float_value("averageAudioDegradation", self.average_audio_degradation)
        writer.write_object_value("averageAudioNetworkJitter", self.average_audio_network_jitter)
        writer.write_int_value("averageBandwidthEstimate", self.average_bandwidth_estimate)
        writer.write_object_value("averageJitter", self.average_jitter)
        writer.write_float_value("averagePacketLossRate", self.average_packet_loss_rate)
        writer.write_float_value("averageRatioOfConcealedSamples", self.average_ratio_of_concealed_samples)
        writer.write_float_value("averageReceivedFrameRate", self.average_received_frame_rate)
        writer.write_object_value("averageRoundTripTime", self.average_round_trip_time)
        writer.write_float_value("averageVideoFrameLossPercentage", self.average_video_frame_loss_percentage)
        writer.write_float_value("averageVideoFrameRate", self.average_video_frame_rate)
        writer.write_float_value("averageVideoPacketLossRate", self.average_video_packet_loss_rate)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_float_value("lowFrameRateRatio", self.low_frame_rate_ratio)
        writer.write_float_value("lowVideoProcessingCapabilityRatio", self.low_video_processing_capability_ratio)
        writer.write_object_value("maxAudioNetworkJitter", self.max_audio_network_jitter)
        writer.write_object_value("maxJitter", self.max_jitter)
        writer.write_float_value("maxPacketLossRate", self.max_packet_loss_rate)
        writer.write_float_value("maxRatioOfConcealedSamples", self.max_ratio_of_concealed_samples)
        writer.write_object_value("maxRoundTripTime", self.max_round_trip_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("packetUtilization", self.packet_utilization)
        writer.write_float_value("postForwardErrorCorrectionPacketLossRate", self.post_forward_error_correction_packet_loss_rate)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("streamDirection", self.stream_direction)
        writer.write_str_value("streamId", self.stream_id)
        writer.write_enum_value("videoCodec", self.video_codec)
        writer.write_bool_value("wasMediaBypassed", self.was_media_bypassed)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. UTC time when the stream started. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. UTC time when the stream started. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def stream_direction(self,) -> Optional[media_stream_direction.MediaStreamDirection]:
        """
        Gets the streamDirection property value. The streamDirection property
        Returns: Optional[media_stream_direction.MediaStreamDirection]
        """
        return self._stream_direction
    
    @stream_direction.setter
    def stream_direction(self,value: Optional[media_stream_direction.MediaStreamDirection] = None) -> None:
        """
        Sets the streamDirection property value. The streamDirection property
        Args:
            value: Value to set for the streamDirection property.
        """
        self._stream_direction = value
    
    @property
    def stream_id(self,) -> Optional[str]:
        """
        Gets the streamId property value. Unique identifier for the stream.
        Returns: Optional[str]
        """
        return self._stream_id
    
    @stream_id.setter
    def stream_id(self,value: Optional[str] = None) -> None:
        """
        Sets the streamId property value. Unique identifier for the stream.
        Args:
            value: Value to set for the streamId property.
        """
        self._stream_id = value
    
    @property
    def video_codec(self,) -> Optional[video_codec.VideoCodec]:
        """
        Gets the videoCodec property value. Codec name used to encode video for transmission on the network. Possible values are: unknown, invalid, av1, h263, h264, h264s, h264uc, h265, rtvc1, rtVideo, xrtvc1, unknownFutureValue.
        Returns: Optional[video_codec.VideoCodec]
        """
        return self._video_codec
    
    @video_codec.setter
    def video_codec(self,value: Optional[video_codec.VideoCodec] = None) -> None:
        """
        Sets the videoCodec property value. Codec name used to encode video for transmission on the network. Possible values are: unknown, invalid, av1, h263, h264, h264s, h264uc, h265, rtvc1, rtVideo, xrtvc1, unknownFutureValue.
        Args:
            value: Value to set for the videoCodec property.
        """
        self._video_codec = value
    
    @property
    def was_media_bypassed(self,) -> Optional[bool]:
        """
        Gets the wasMediaBypassed property value. True if the media stream bypassed the Mediation Server and went straight between client and PSTN Gateway/PBX, false otherwise.
        Returns: Optional[bool]
        """
        return self._was_media_bypassed
    
    @was_media_bypassed.setter
    def was_media_bypassed(self,value: Optional[bool] = None) -> None:
        """
        Sets the wasMediaBypassed property value. True if the media stream bypassed the Mediation Server and went straight between client and PSTN Gateway/PBX, false otherwise.
        Args:
            value: Value to set for the wasMediaBypassed property.
        """
        self._was_media_bypassed = value
    

