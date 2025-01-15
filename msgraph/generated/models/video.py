from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Video(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Number of audio bits per sample.
    audio_bits_per_sample: Optional[int] = None
    # Number of audio channels.
    audio_channels: Optional[int] = None
    # Name of the audio format (AAC, MP3, etc.).
    audio_format: Optional[str] = None
    # Number of audio samples per second.
    audio_samples_per_second: Optional[int] = None
    # Bit rate of the video in bits per second.
    bitrate: Optional[int] = None
    # Duration of the file in milliseconds.
    duration: Optional[int] = None
    # 'Four character code' name of the video format.
    four_c_c: Optional[str] = None
    # Frame rate of the video.
    frame_rate: Optional[float] = None
    # Height of the video, in pixels.
    height: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Width of the video, in pixels.
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Video:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Video
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Video()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "audioBitsPerSample": lambda n : setattr(self, 'audio_bits_per_sample', n.get_int_value()),
            "audioChannels": lambda n : setattr(self, 'audio_channels', n.get_int_value()),
            "audioFormat": lambda n : setattr(self, 'audio_format', n.get_str_value()),
            "audioSamplesPerSecond": lambda n : setattr(self, 'audio_samples_per_second', n.get_int_value()),
            "bitrate": lambda n : setattr(self, 'bitrate', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "fourCC": lambda n : setattr(self, 'four_c_c', n.get_str_value()),
            "frameRate": lambda n : setattr(self, 'frame_rate', n.get_float_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
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
        writer.write_int_value("audioBitsPerSample", self.audio_bits_per_sample)
        writer.write_int_value("audioChannels", self.audio_channels)
        writer.write_str_value("audioFormat", self.audio_format)
        writer.write_int_value("audioSamplesPerSecond", self.audio_samples_per_second)
        writer.write_int_value("bitrate", self.bitrate)
        writer.write_int_value("duration", self.duration)
        writer.write_str_value("fourCC", self.four_c_c)
        writer.write_float_value("frameRate", self.frame_rate)
        writer.write_int_value("height", self.height)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("width", self.width)
        writer.write_additional_data_value(self.additional_data)
    

