from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Video(AdditionalDataHolder, Parsable):
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
    def audio_bits_per_sample(self,) -> Optional[int]:
        """
        Gets the audioBitsPerSample property value. Number of audio bits per sample.
        Returns: Optional[int]
        """
        return self._audio_bits_per_sample
    
    @audio_bits_per_sample.setter
    def audio_bits_per_sample(self,value: Optional[int] = None) -> None:
        """
        Sets the audioBitsPerSample property value. Number of audio bits per sample.
        Args:
            value: Value to set for the audioBitsPerSample property.
        """
        self._audio_bits_per_sample = value
    
    @property
    def audio_channels(self,) -> Optional[int]:
        """
        Gets the audioChannels property value. Number of audio channels.
        Returns: Optional[int]
        """
        return self._audio_channels
    
    @audio_channels.setter
    def audio_channels(self,value: Optional[int] = None) -> None:
        """
        Sets the audioChannels property value. Number of audio channels.
        Args:
            value: Value to set for the audioChannels property.
        """
        self._audio_channels = value
    
    @property
    def audio_format(self,) -> Optional[str]:
        """
        Gets the audioFormat property value. Name of the audio format (AAC, MP3, etc.).
        Returns: Optional[str]
        """
        return self._audio_format
    
    @audio_format.setter
    def audio_format(self,value: Optional[str] = None) -> None:
        """
        Sets the audioFormat property value. Name of the audio format (AAC, MP3, etc.).
        Args:
            value: Value to set for the audioFormat property.
        """
        self._audio_format = value
    
    @property
    def audio_samples_per_second(self,) -> Optional[int]:
        """
        Gets the audioSamplesPerSecond property value. Number of audio samples per second.
        Returns: Optional[int]
        """
        return self._audio_samples_per_second
    
    @audio_samples_per_second.setter
    def audio_samples_per_second(self,value: Optional[int] = None) -> None:
        """
        Sets the audioSamplesPerSecond property value. Number of audio samples per second.
        Args:
            value: Value to set for the audioSamplesPerSecond property.
        """
        self._audio_samples_per_second = value
    
    @property
    def bitrate(self,) -> Optional[int]:
        """
        Gets the bitrate property value. Bit rate of the video in bits per second.
        Returns: Optional[int]
        """
        return self._bitrate
    
    @bitrate.setter
    def bitrate(self,value: Optional[int] = None) -> None:
        """
        Sets the bitrate property value. Bit rate of the video in bits per second.
        Args:
            value: Value to set for the bitrate property.
        """
        self._bitrate = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new video and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Number of audio bits per sample.
        self._audio_bits_per_sample: Optional[int] = None
        # Number of audio channels.
        self._audio_channels: Optional[int] = None
        # Name of the audio format (AAC, MP3, etc.).
        self._audio_format: Optional[str] = None
        # Number of audio samples per second.
        self._audio_samples_per_second: Optional[int] = None
        # Bit rate of the video in bits per second.
        self._bitrate: Optional[int] = None
        # Duration of the file in milliseconds.
        self._duration: Optional[int] = None
        # 'Four character code' name of the video format.
        self._four_c_c: Optional[str] = None
        # Frame rate of the video.
        self._frame_rate: Optional[float] = None
        # Height of the video, in pixels.
        self._height: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Width of the video, in pixels.
        self._width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Video:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Video
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Video()
    
    @property
    def duration(self,) -> Optional[int]:
        """
        Gets the duration property value. Duration of the file in milliseconds.
        Returns: Optional[int]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[int] = None) -> None:
        """
        Sets the duration property value. Duration of the file in milliseconds.
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def four_c_c(self,) -> Optional[str]:
        """
        Gets the fourCC property value. 'Four character code' name of the video format.
        Returns: Optional[str]
        """
        return self._four_c_c
    
    @four_c_c.setter
    def four_c_c(self,value: Optional[str] = None) -> None:
        """
        Sets the fourCC property value. 'Four character code' name of the video format.
        Args:
            value: Value to set for the fourCC property.
        """
        self._four_c_c = value
    
    @property
    def frame_rate(self,) -> Optional[float]:
        """
        Gets the frameRate property value. Frame rate of the video.
        Returns: Optional[float]
        """
        return self._frame_rate
    
    @frame_rate.setter
    def frame_rate(self,value: Optional[float] = None) -> None:
        """
        Sets the frameRate property value. Frame rate of the video.
        Args:
            value: Value to set for the frameRate property.
        """
        self._frame_rate = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "audio_bits_per_sample": lambda n : setattr(self, 'audio_bits_per_sample', n.get_int_value()),
            "audio_channels": lambda n : setattr(self, 'audio_channels', n.get_int_value()),
            "audio_format": lambda n : setattr(self, 'audio_format', n.get_str_value()),
            "audio_samples_per_second": lambda n : setattr(self, 'audio_samples_per_second', n.get_int_value()),
            "bitrate": lambda n : setattr(self, 'bitrate', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "four_c_c": lambda n : setattr(self, 'four_c_c', n.get_str_value()),
            "frame_rate": lambda n : setattr(self, 'frame_rate', n.get_float_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
        }
        return fields
    
    @property
    def height(self,) -> Optional[int]:
        """
        Gets the height property value. Height of the video, in pixels.
        Returns: Optional[int]
        """
        return self._height
    
    @height.setter
    def height(self,value: Optional[int] = None) -> None:
        """
        Sets the height property value. Height of the video, in pixels.
        Args:
            value: Value to set for the height property.
        """
        self._height = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def width(self,) -> Optional[int]:
        """
        Gets the width property value. Width of the video, in pixels.
        Returns: Optional[int]
        """
        return self._width
    
    @width.setter
    def width(self,value: Optional[int] = None) -> None:
        """
        Sets the width property value. Width of the video, in pixels.
        Args:
            value: Value to set for the width property.
        """
        self._width = value
    

