from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceInfo(AdditionalDataHolder, Parsable):
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
    def capture_device_driver(self,) -> Optional[str]:
        """
        Gets the captureDeviceDriver property value. Name of the capture device driver used by the media endpoint.
        Returns: Optional[str]
        """
        return self._capture_device_driver
    
    @capture_device_driver.setter
    def capture_device_driver(self,value: Optional[str] = None) -> None:
        """
        Sets the captureDeviceDriver property value. Name of the capture device driver used by the media endpoint.
        Args:
            value: Value to set for the captureDeviceDriver property.
        """
        self._capture_device_driver = value
    
    @property
    def capture_device_name(self,) -> Optional[str]:
        """
        Gets the captureDeviceName property value. Name of the capture device used by the media endpoint.
        Returns: Optional[str]
        """
        return self._capture_device_name
    
    @capture_device_name.setter
    def capture_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the captureDeviceName property value. Name of the capture device used by the media endpoint.
        Args:
            value: Value to set for the captureDeviceName property.
        """
        self._capture_device_name = value
    
    @property
    def capture_not_functioning_event_ratio(self,) -> Optional[float]:
        """
        Gets the captureNotFunctioningEventRatio property value. Fraction of the call that the media endpoint detected the capture device was not working properly.
        Returns: Optional[float]
        """
        return self._capture_not_functioning_event_ratio
    
    @capture_not_functioning_event_ratio.setter
    def capture_not_functioning_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the captureNotFunctioningEventRatio property value. Fraction of the call that the media endpoint detected the capture device was not working properly.
        Args:
            value: Value to set for the captureNotFunctioningEventRatio property.
        """
        self._capture_not_functioning_event_ratio = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Name of the capture device driver used by the media endpoint.
        self._capture_device_driver: Optional[str] = None
        # Name of the capture device used by the media endpoint.
        self._capture_device_name: Optional[str] = None
        # Fraction of the call that the media endpoint detected the capture device was not working properly.
        self._capture_not_functioning_event_ratio: Optional[float] = None
        # Fraction of the call that the media endpoint detected the CPU resources available were insufficient and caused poor quality of the audio sent and received.
        self._cpu_insufficent_event_ratio: Optional[float] = None
        # Fraction of the call that the media endpoint detected clipping in the captured audio that caused poor quality of the audio being sent.
        self._device_clipping_event_ratio: Optional[float] = None
        # Fraction of the call that the media endpoint detected glitches or gaps in the audio played or captured that caused poor quality of the audio being sent or received.
        self._device_glitch_event_ratio: Optional[float] = None
        # Number of times during the call that the media endpoint detected howling or screeching audio.
        self._howling_event_count: Optional[int] = None
        # The root mean square (RMS) of the incoming signal of up to the first 30 seconds of the call.
        self._initial_signal_level_root_mean_square: Optional[float] = None
        # Fraction of the call that the media endpoint detected low speech level that caused poor quality of the audio being sent.
        self._low_speech_level_event_ratio: Optional[float] = None
        # Fraction of the call that the media endpoint detected low speech to noise level that caused poor quality of the audio being sent.
        self._low_speech_to_noise_event_ratio: Optional[float] = None
        # Glitches per 5 minute interval for the media endpoint's microphone.
        self._mic_glitch_rate: Optional[float] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Average energy level of received audio for audio classified as mono noise or left channel of stereo noise by the media endpoint.
        self._received_noise_level: Optional[int] = None
        # Average energy level of received audio for audio classified as mono speech, or left channel of stereo speech by the media endpoint.
        self._received_signal_level: Optional[int] = None
        # Name of the render device driver used by the media endpoint.
        self._render_device_driver: Optional[str] = None
        # Name of the render device used by the media endpoint.
        self._render_device_name: Optional[str] = None
        # Fraction of the call that media endpoint detected device render is muted.
        self._render_mute_event_ratio: Optional[float] = None
        # Fraction of the call that the media endpoint detected the render device was not working properly.
        self._render_not_functioning_event_ratio: Optional[float] = None
        # Fraction of the call that media endpoint detected device render volume is set to 0.
        self._render_zero_volume_event_ratio: Optional[float] = None
        # Average energy level of sent audio for audio classified as mono noise or left channel of stereo noise by the media endpoint.
        self._sent_noise_level: Optional[int] = None
        # Average energy level of sent audio for audio classified as mono speech, or left channel of stereo speech by the media endpoint.
        self._sent_signal_level: Optional[int] = None
        # Glitches per 5 minute internal for the media endpoint's loudspeaker.
        self._speaker_glitch_rate: Optional[float] = None
    
    @property
    def cpu_insufficent_event_ratio(self,) -> Optional[float]:
        """
        Gets the cpuInsufficentEventRatio property value. Fraction of the call that the media endpoint detected the CPU resources available were insufficient and caused poor quality of the audio sent and received.
        Returns: Optional[float]
        """
        return self._cpu_insufficent_event_ratio
    
    @cpu_insufficent_event_ratio.setter
    def cpu_insufficent_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the cpuInsufficentEventRatio property value. Fraction of the call that the media endpoint detected the CPU resources available were insufficient and caused poor quality of the audio sent and received.
        Args:
            value: Value to set for the cpuInsufficentEventRatio property.
        """
        self._cpu_insufficent_event_ratio = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceInfo()
    
    @property
    def device_clipping_event_ratio(self,) -> Optional[float]:
        """
        Gets the deviceClippingEventRatio property value. Fraction of the call that the media endpoint detected clipping in the captured audio that caused poor quality of the audio being sent.
        Returns: Optional[float]
        """
        return self._device_clipping_event_ratio
    
    @device_clipping_event_ratio.setter
    def device_clipping_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the deviceClippingEventRatio property value. Fraction of the call that the media endpoint detected clipping in the captured audio that caused poor quality of the audio being sent.
        Args:
            value: Value to set for the deviceClippingEventRatio property.
        """
        self._device_clipping_event_ratio = value
    
    @property
    def device_glitch_event_ratio(self,) -> Optional[float]:
        """
        Gets the deviceGlitchEventRatio property value. Fraction of the call that the media endpoint detected glitches or gaps in the audio played or captured that caused poor quality of the audio being sent or received.
        Returns: Optional[float]
        """
        return self._device_glitch_event_ratio
    
    @device_glitch_event_ratio.setter
    def device_glitch_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the deviceGlitchEventRatio property value. Fraction of the call that the media endpoint detected glitches or gaps in the audio played or captured that caused poor quality of the audio being sent or received.
        Args:
            value: Value to set for the deviceGlitchEventRatio property.
        """
        self._device_glitch_event_ratio = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "capture_device_driver": lambda n : setattr(self, 'capture_device_driver', n.get_str_value()),
            "capture_device_name": lambda n : setattr(self, 'capture_device_name', n.get_str_value()),
            "capture_not_functioning_event_ratio": lambda n : setattr(self, 'capture_not_functioning_event_ratio', n.get_float_value()),
            "cpu_insufficent_event_ratio": lambda n : setattr(self, 'cpu_insufficent_event_ratio', n.get_float_value()),
            "device_clipping_event_ratio": lambda n : setattr(self, 'device_clipping_event_ratio', n.get_float_value()),
            "device_glitch_event_ratio": lambda n : setattr(self, 'device_glitch_event_ratio', n.get_float_value()),
            "howling_event_count": lambda n : setattr(self, 'howling_event_count', n.get_int_value()),
            "initial_signal_level_root_mean_square": lambda n : setattr(self, 'initial_signal_level_root_mean_square', n.get_float_value()),
            "low_speech_level_event_ratio": lambda n : setattr(self, 'low_speech_level_event_ratio', n.get_float_value()),
            "low_speech_to_noise_event_ratio": lambda n : setattr(self, 'low_speech_to_noise_event_ratio', n.get_float_value()),
            "mic_glitch_rate": lambda n : setattr(self, 'mic_glitch_rate', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "received_noise_level": lambda n : setattr(self, 'received_noise_level', n.get_int_value()),
            "received_signal_level": lambda n : setattr(self, 'received_signal_level', n.get_int_value()),
            "render_device_driver": lambda n : setattr(self, 'render_device_driver', n.get_str_value()),
            "render_device_name": lambda n : setattr(self, 'render_device_name', n.get_str_value()),
            "render_mute_event_ratio": lambda n : setattr(self, 'render_mute_event_ratio', n.get_float_value()),
            "render_not_functioning_event_ratio": lambda n : setattr(self, 'render_not_functioning_event_ratio', n.get_float_value()),
            "render_zero_volume_event_ratio": lambda n : setattr(self, 'render_zero_volume_event_ratio', n.get_float_value()),
            "sent_noise_level": lambda n : setattr(self, 'sent_noise_level', n.get_int_value()),
            "sent_signal_level": lambda n : setattr(self, 'sent_signal_level', n.get_int_value()),
            "speaker_glitch_rate": lambda n : setattr(self, 'speaker_glitch_rate', n.get_float_value()),
        }
        return fields
    
    @property
    def howling_event_count(self,) -> Optional[int]:
        """
        Gets the howlingEventCount property value. Number of times during the call that the media endpoint detected howling or screeching audio.
        Returns: Optional[int]
        """
        return self._howling_event_count
    
    @howling_event_count.setter
    def howling_event_count(self,value: Optional[int] = None) -> None:
        """
        Sets the howlingEventCount property value. Number of times during the call that the media endpoint detected howling or screeching audio.
        Args:
            value: Value to set for the howlingEventCount property.
        """
        self._howling_event_count = value
    
    @property
    def initial_signal_level_root_mean_square(self,) -> Optional[float]:
        """
        Gets the initialSignalLevelRootMeanSquare property value. The root mean square (RMS) of the incoming signal of up to the first 30 seconds of the call.
        Returns: Optional[float]
        """
        return self._initial_signal_level_root_mean_square
    
    @initial_signal_level_root_mean_square.setter
    def initial_signal_level_root_mean_square(self,value: Optional[float] = None) -> None:
        """
        Sets the initialSignalLevelRootMeanSquare property value. The root mean square (RMS) of the incoming signal of up to the first 30 seconds of the call.
        Args:
            value: Value to set for the initialSignalLevelRootMeanSquare property.
        """
        self._initial_signal_level_root_mean_square = value
    
    @property
    def low_speech_level_event_ratio(self,) -> Optional[float]:
        """
        Gets the lowSpeechLevelEventRatio property value. Fraction of the call that the media endpoint detected low speech level that caused poor quality of the audio being sent.
        Returns: Optional[float]
        """
        return self._low_speech_level_event_ratio
    
    @low_speech_level_event_ratio.setter
    def low_speech_level_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the lowSpeechLevelEventRatio property value. Fraction of the call that the media endpoint detected low speech level that caused poor quality of the audio being sent.
        Args:
            value: Value to set for the lowSpeechLevelEventRatio property.
        """
        self._low_speech_level_event_ratio = value
    
    @property
    def low_speech_to_noise_event_ratio(self,) -> Optional[float]:
        """
        Gets the lowSpeechToNoiseEventRatio property value. Fraction of the call that the media endpoint detected low speech to noise level that caused poor quality of the audio being sent.
        Returns: Optional[float]
        """
        return self._low_speech_to_noise_event_ratio
    
    @low_speech_to_noise_event_ratio.setter
    def low_speech_to_noise_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the lowSpeechToNoiseEventRatio property value. Fraction of the call that the media endpoint detected low speech to noise level that caused poor quality of the audio being sent.
        Args:
            value: Value to set for the lowSpeechToNoiseEventRatio property.
        """
        self._low_speech_to_noise_event_ratio = value
    
    @property
    def mic_glitch_rate(self,) -> Optional[float]:
        """
        Gets the micGlitchRate property value. Glitches per 5 minute interval for the media endpoint's microphone.
        Returns: Optional[float]
        """
        return self._mic_glitch_rate
    
    @mic_glitch_rate.setter
    def mic_glitch_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the micGlitchRate property value. Glitches per 5 minute interval for the media endpoint's microphone.
        Args:
            value: Value to set for the micGlitchRate property.
        """
        self._mic_glitch_rate = value
    
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
    def received_noise_level(self,) -> Optional[int]:
        """
        Gets the receivedNoiseLevel property value. Average energy level of received audio for audio classified as mono noise or left channel of stereo noise by the media endpoint.
        Returns: Optional[int]
        """
        return self._received_noise_level
    
    @received_noise_level.setter
    def received_noise_level(self,value: Optional[int] = None) -> None:
        """
        Sets the receivedNoiseLevel property value. Average energy level of received audio for audio classified as mono noise or left channel of stereo noise by the media endpoint.
        Args:
            value: Value to set for the receivedNoiseLevel property.
        """
        self._received_noise_level = value
    
    @property
    def received_signal_level(self,) -> Optional[int]:
        """
        Gets the receivedSignalLevel property value. Average energy level of received audio for audio classified as mono speech, or left channel of stereo speech by the media endpoint.
        Returns: Optional[int]
        """
        return self._received_signal_level
    
    @received_signal_level.setter
    def received_signal_level(self,value: Optional[int] = None) -> None:
        """
        Sets the receivedSignalLevel property value. Average energy level of received audio for audio classified as mono speech, or left channel of stereo speech by the media endpoint.
        Args:
            value: Value to set for the receivedSignalLevel property.
        """
        self._received_signal_level = value
    
    @property
    def render_device_driver(self,) -> Optional[str]:
        """
        Gets the renderDeviceDriver property value. Name of the render device driver used by the media endpoint.
        Returns: Optional[str]
        """
        return self._render_device_driver
    
    @render_device_driver.setter
    def render_device_driver(self,value: Optional[str] = None) -> None:
        """
        Sets the renderDeviceDriver property value. Name of the render device driver used by the media endpoint.
        Args:
            value: Value to set for the renderDeviceDriver property.
        """
        self._render_device_driver = value
    
    @property
    def render_device_name(self,) -> Optional[str]:
        """
        Gets the renderDeviceName property value. Name of the render device used by the media endpoint.
        Returns: Optional[str]
        """
        return self._render_device_name
    
    @render_device_name.setter
    def render_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the renderDeviceName property value. Name of the render device used by the media endpoint.
        Args:
            value: Value to set for the renderDeviceName property.
        """
        self._render_device_name = value
    
    @property
    def render_mute_event_ratio(self,) -> Optional[float]:
        """
        Gets the renderMuteEventRatio property value. Fraction of the call that media endpoint detected device render is muted.
        Returns: Optional[float]
        """
        return self._render_mute_event_ratio
    
    @render_mute_event_ratio.setter
    def render_mute_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the renderMuteEventRatio property value. Fraction of the call that media endpoint detected device render is muted.
        Args:
            value: Value to set for the renderMuteEventRatio property.
        """
        self._render_mute_event_ratio = value
    
    @property
    def render_not_functioning_event_ratio(self,) -> Optional[float]:
        """
        Gets the renderNotFunctioningEventRatio property value. Fraction of the call that the media endpoint detected the render device was not working properly.
        Returns: Optional[float]
        """
        return self._render_not_functioning_event_ratio
    
    @render_not_functioning_event_ratio.setter
    def render_not_functioning_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the renderNotFunctioningEventRatio property value. Fraction of the call that the media endpoint detected the render device was not working properly.
        Args:
            value: Value to set for the renderNotFunctioningEventRatio property.
        """
        self._render_not_functioning_event_ratio = value
    
    @property
    def render_zero_volume_event_ratio(self,) -> Optional[float]:
        """
        Gets the renderZeroVolumeEventRatio property value. Fraction of the call that media endpoint detected device render volume is set to 0.
        Returns: Optional[float]
        """
        return self._render_zero_volume_event_ratio
    
    @render_zero_volume_event_ratio.setter
    def render_zero_volume_event_ratio(self,value: Optional[float] = None) -> None:
        """
        Sets the renderZeroVolumeEventRatio property value. Fraction of the call that media endpoint detected device render volume is set to 0.
        Args:
            value: Value to set for the renderZeroVolumeEventRatio property.
        """
        self._render_zero_volume_event_ratio = value
    
    @property
    def sent_noise_level(self,) -> Optional[int]:
        """
        Gets the sentNoiseLevel property value. Average energy level of sent audio for audio classified as mono noise or left channel of stereo noise by the media endpoint.
        Returns: Optional[int]
        """
        return self._sent_noise_level
    
    @sent_noise_level.setter
    def sent_noise_level(self,value: Optional[int] = None) -> None:
        """
        Sets the sentNoiseLevel property value. Average energy level of sent audio for audio classified as mono noise or left channel of stereo noise by the media endpoint.
        Args:
            value: Value to set for the sentNoiseLevel property.
        """
        self._sent_noise_level = value
    
    @property
    def sent_signal_level(self,) -> Optional[int]:
        """
        Gets the sentSignalLevel property value. Average energy level of sent audio for audio classified as mono speech, or left channel of stereo speech by the media endpoint.
        Returns: Optional[int]
        """
        return self._sent_signal_level
    
    @sent_signal_level.setter
    def sent_signal_level(self,value: Optional[int] = None) -> None:
        """
        Sets the sentSignalLevel property value. Average energy level of sent audio for audio classified as mono speech, or left channel of stereo speech by the media endpoint.
        Args:
            value: Value to set for the sentSignalLevel property.
        """
        self._sent_signal_level = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("captureDeviceDriver", self.capture_device_driver)
        writer.write_str_value("captureDeviceName", self.capture_device_name)
        writer.write_float_value("captureNotFunctioningEventRatio", self.capture_not_functioning_event_ratio)
        writer.write_float_value("cpuInsufficentEventRatio", self.cpu_insufficent_event_ratio)
        writer.write_float_value("deviceClippingEventRatio", self.device_clipping_event_ratio)
        writer.write_float_value("deviceGlitchEventRatio", self.device_glitch_event_ratio)
        writer.write_int_value("howlingEventCount", self.howling_event_count)
        writer.write_float_value("initialSignalLevelRootMeanSquare", self.initial_signal_level_root_mean_square)
        writer.write_float_value("lowSpeechLevelEventRatio", self.low_speech_level_event_ratio)
        writer.write_float_value("lowSpeechToNoiseEventRatio", self.low_speech_to_noise_event_ratio)
        writer.write_float_value("micGlitchRate", self.mic_glitch_rate)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("receivedNoiseLevel", self.received_noise_level)
        writer.write_int_value("receivedSignalLevel", self.received_signal_level)
        writer.write_str_value("renderDeviceDriver", self.render_device_driver)
        writer.write_str_value("renderDeviceName", self.render_device_name)
        writer.write_float_value("renderMuteEventRatio", self.render_mute_event_ratio)
        writer.write_float_value("renderNotFunctioningEventRatio", self.render_not_functioning_event_ratio)
        writer.write_float_value("renderZeroVolumeEventRatio", self.render_zero_volume_event_ratio)
        writer.write_int_value("sentNoiseLevel", self.sent_noise_level)
        writer.write_int_value("sentSignalLevel", self.sent_signal_level)
        writer.write_float_value("speakerGlitchRate", self.speaker_glitch_rate)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def speaker_glitch_rate(self,) -> Optional[float]:
        """
        Gets the speakerGlitchRate property value. Glitches per 5 minute internal for the media endpoint's loudspeaker.
        Returns: Optional[float]
        """
        return self._speaker_glitch_rate
    
    @speaker_glitch_rate.setter
    def speaker_glitch_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the speakerGlitchRate property value. Glitches per 5 minute internal for the media endpoint's loudspeaker.
        Args:
            value: Value to set for the speakerGlitchRate property.
        """
        self._speaker_glitch_rate = value
    

