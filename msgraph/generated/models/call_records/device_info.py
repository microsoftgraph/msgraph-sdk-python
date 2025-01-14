from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Name of the capture device driver used by the media endpoint.
    capture_device_driver: Optional[str] = None
    # Name of the capture device used by the media endpoint.
    capture_device_name: Optional[str] = None
    # Fraction of the call that the media endpoint detected the capture device was not working properly.
    capture_not_functioning_event_ratio: Optional[float] = None
    # Fraction of the call that the media endpoint detected the CPU resources available were insufficient and caused poor quality of the audio sent and received.
    cpu_insufficent_event_ratio: Optional[float] = None
    # Fraction of the call that the media endpoint detected clipping in the captured audio that caused poor quality of the audio being sent.
    device_clipping_event_ratio: Optional[float] = None
    # Fraction of the call that the media endpoint detected glitches or gaps in the audio played or captured that caused poor quality of the audio being sent or received.
    device_glitch_event_ratio: Optional[float] = None
    # Number of times during the call that the media endpoint detected howling or screeching audio.
    howling_event_count: Optional[int] = None
    # The root mean square (RMS) of the incoming signal of up to the first 30 seconds of the call.
    initial_signal_level_root_mean_square: Optional[float] = None
    # Fraction of the call that the media endpoint detected low speech level that caused poor quality of the audio being sent.
    low_speech_level_event_ratio: Optional[float] = None
    # Fraction of the call that the media endpoint detected low speech to noise level that caused poor quality of the audio being sent.
    low_speech_to_noise_event_ratio: Optional[float] = None
    # Glitches per 5 minute interval for the media endpoint's microphone.
    mic_glitch_rate: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Average energy level of received audio for audio classified as mono noise or left channel of stereo noise by the media endpoint.
    received_noise_level: Optional[int] = None
    # Average energy level of received audio for audio classified as mono speech, or left channel of stereo speech by the media endpoint.
    received_signal_level: Optional[int] = None
    # Name of the render device driver used by the media endpoint.
    render_device_driver: Optional[str] = None
    # Name of the render device used by the media endpoint.
    render_device_name: Optional[str] = None
    # Fraction of the call that media endpoint detected device render is muted.
    render_mute_event_ratio: Optional[float] = None
    # Fraction of the call that the media endpoint detected the render device was not working properly.
    render_not_functioning_event_ratio: Optional[float] = None
    # Fraction of the call that media endpoint detected device render volume is set to 0.
    render_zero_volume_event_ratio: Optional[float] = None
    # Average energy level of sent audio for audio classified as mono noise or left channel of stereo noise by the media endpoint.
    sent_noise_level: Optional[int] = None
    # Average energy level of sent audio for audio classified as mono speech, or left channel of stereo speech by the media endpoint.
    sent_signal_level: Optional[int] = None
    # Glitches per 5 minute internal for the media endpoint's loudspeaker.
    speaker_glitch_rate: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "captureDeviceDriver": lambda n : setattr(self, 'capture_device_driver', n.get_str_value()),
            "captureDeviceName": lambda n : setattr(self, 'capture_device_name', n.get_str_value()),
            "captureNotFunctioningEventRatio": lambda n : setattr(self, 'capture_not_functioning_event_ratio', n.get_float_value()),
            "cpuInsufficentEventRatio": lambda n : setattr(self, 'cpu_insufficent_event_ratio', n.get_float_value()),
            "deviceClippingEventRatio": lambda n : setattr(self, 'device_clipping_event_ratio', n.get_float_value()),
            "deviceGlitchEventRatio": lambda n : setattr(self, 'device_glitch_event_ratio', n.get_float_value()),
            "howlingEventCount": lambda n : setattr(self, 'howling_event_count', n.get_int_value()),
            "initialSignalLevelRootMeanSquare": lambda n : setattr(self, 'initial_signal_level_root_mean_square', n.get_float_value()),
            "lowSpeechLevelEventRatio": lambda n : setattr(self, 'low_speech_level_event_ratio', n.get_float_value()),
            "lowSpeechToNoiseEventRatio": lambda n : setattr(self, 'low_speech_to_noise_event_ratio', n.get_float_value()),
            "micGlitchRate": lambda n : setattr(self, 'mic_glitch_rate', n.get_float_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "receivedNoiseLevel": lambda n : setattr(self, 'received_noise_level', n.get_int_value()),
            "receivedSignalLevel": lambda n : setattr(self, 'received_signal_level', n.get_int_value()),
            "renderDeviceDriver": lambda n : setattr(self, 'render_device_driver', n.get_str_value()),
            "renderDeviceName": lambda n : setattr(self, 'render_device_name', n.get_str_value()),
            "renderMuteEventRatio": lambda n : setattr(self, 'render_mute_event_ratio', n.get_float_value()),
            "renderNotFunctioningEventRatio": lambda n : setattr(self, 'render_not_functioning_event_ratio', n.get_float_value()),
            "renderZeroVolumeEventRatio": lambda n : setattr(self, 'render_zero_volume_event_ratio', n.get_float_value()),
            "sentNoiseLevel": lambda n : setattr(self, 'sent_noise_level', n.get_int_value()),
            "sentSignalLevel": lambda n : setattr(self, 'sent_signal_level', n.get_int_value()),
            "speakerGlitchRate": lambda n : setattr(self, 'speaker_glitch_rate', n.get_float_value()),
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
    

