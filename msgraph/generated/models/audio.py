from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Audio(AdditionalDataHolder, Parsable):
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
    def album(self,) -> Optional[str]:
        """
        Gets the album property value. The title of the album for this audio file.
        Returns: Optional[str]
        """
        return self._album
    
    @album.setter
    def album(self,value: Optional[str] = None) -> None:
        """
        Sets the album property value. The title of the album for this audio file.
        Args:
            value: Value to set for the album property.
        """
        self._album = value
    
    @property
    def album_artist(self,) -> Optional[str]:
        """
        Gets the albumArtist property value. The artist named on the album for the audio file.
        Returns: Optional[str]
        """
        return self._album_artist
    
    @album_artist.setter
    def album_artist(self,value: Optional[str] = None) -> None:
        """
        Sets the albumArtist property value. The artist named on the album for the audio file.
        Args:
            value: Value to set for the albumArtist property.
        """
        self._album_artist = value
    
    @property
    def artist(self,) -> Optional[str]:
        """
        Gets the artist property value. The performing artist for the audio file.
        Returns: Optional[str]
        """
        return self._artist
    
    @artist.setter
    def artist(self,value: Optional[str] = None) -> None:
        """
        Sets the artist property value. The performing artist for the audio file.
        Args:
            value: Value to set for the artist property.
        """
        self._artist = value
    
    @property
    def bitrate(self,) -> Optional[int]:
        """
        Gets the bitrate property value. Bitrate expressed in kbps.
        Returns: Optional[int]
        """
        return self._bitrate
    
    @bitrate.setter
    def bitrate(self,value: Optional[int] = None) -> None:
        """
        Sets the bitrate property value. Bitrate expressed in kbps.
        Args:
            value: Value to set for the bitrate property.
        """
        self._bitrate = value
    
    @property
    def composers(self,) -> Optional[str]:
        """
        Gets the composers property value. The name of the composer of the audio file.
        Returns: Optional[str]
        """
        return self._composers
    
    @composers.setter
    def composers(self,value: Optional[str] = None) -> None:
        """
        Sets the composers property value. The name of the composer of the audio file.
        Args:
            value: Value to set for the composers property.
        """
        self._composers = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new audio and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The title of the album for this audio file.
        self._album: Optional[str] = None
        # The artist named on the album for the audio file.
        self._album_artist: Optional[str] = None
        # The performing artist for the audio file.
        self._artist: Optional[str] = None
        # Bitrate expressed in kbps.
        self._bitrate: Optional[int] = None
        # The name of the composer of the audio file.
        self._composers: Optional[str] = None
        # Copyright information for the audio file.
        self._copyright: Optional[str] = None
        # The number of the disc this audio file came from.
        self._disc: Optional[int] = None
        # The total number of discs in this album.
        self._disc_count: Optional[int] = None
        # Duration of the audio file, expressed in milliseconds
        self._duration: Optional[int] = None
        # The genre of this audio file.
        self._genre: Optional[str] = None
        # Indicates if the file is protected with digital rights management.
        self._has_drm: Optional[bool] = None
        # Indicates if the file is encoded with a variable bitrate.
        self._is_variable_bitrate: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The title of the audio file.
        self._title: Optional[str] = None
        # The number of the track on the original disc for this audio file.
        self._track: Optional[int] = None
        # The total number of tracks on the original disc for this audio file.
        self._track_count: Optional[int] = None
        # The year the audio file was recorded.
        self._year: Optional[int] = None
    
    @property
    def copyright(self,) -> Optional[str]:
        """
        Gets the copyright property value. Copyright information for the audio file.
        Returns: Optional[str]
        """
        return self._copyright
    
    @copyright.setter
    def copyright(self,value: Optional[str] = None) -> None:
        """
        Sets the copyright property value. Copyright information for the audio file.
        Args:
            value: Value to set for the copyright property.
        """
        self._copyright = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Audio:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Audio
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Audio()
    
    @property
    def disc(self,) -> Optional[int]:
        """
        Gets the disc property value. The number of the disc this audio file came from.
        Returns: Optional[int]
        """
        return self._disc
    
    @disc.setter
    def disc(self,value: Optional[int] = None) -> None:
        """
        Sets the disc property value. The number of the disc this audio file came from.
        Args:
            value: Value to set for the disc property.
        """
        self._disc = value
    
    @property
    def disc_count(self,) -> Optional[int]:
        """
        Gets the discCount property value. The total number of discs in this album.
        Returns: Optional[int]
        """
        return self._disc_count
    
    @disc_count.setter
    def disc_count(self,value: Optional[int] = None) -> None:
        """
        Sets the discCount property value. The total number of discs in this album.
        Args:
            value: Value to set for the discCount property.
        """
        self._disc_count = value
    
    @property
    def duration(self,) -> Optional[int]:
        """
        Gets the duration property value. Duration of the audio file, expressed in milliseconds
        Returns: Optional[int]
        """
        return self._duration
    
    @duration.setter
    def duration(self,value: Optional[int] = None) -> None:
        """
        Sets the duration property value. Duration of the audio file, expressed in milliseconds
        Args:
            value: Value to set for the duration property.
        """
        self._duration = value
    
    @property
    def genre(self,) -> Optional[str]:
        """
        Gets the genre property value. The genre of this audio file.
        Returns: Optional[str]
        """
        return self._genre
    
    @genre.setter
    def genre(self,value: Optional[str] = None) -> None:
        """
        Sets the genre property value. The genre of this audio file.
        Args:
            value: Value to set for the genre property.
        """
        self._genre = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "album": lambda n : setattr(self, 'album', n.get_str_value()),
            "album_artist": lambda n : setattr(self, 'album_artist', n.get_str_value()),
            "artist": lambda n : setattr(self, 'artist', n.get_str_value()),
            "bitrate": lambda n : setattr(self, 'bitrate', n.get_int_value()),
            "composers": lambda n : setattr(self, 'composers', n.get_str_value()),
            "copyright": lambda n : setattr(self, 'copyright', n.get_str_value()),
            "disc": lambda n : setattr(self, 'disc', n.get_int_value()),
            "disc_count": lambda n : setattr(self, 'disc_count', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "genre": lambda n : setattr(self, 'genre', n.get_str_value()),
            "has_drm": lambda n : setattr(self, 'has_drm', n.get_bool_value()),
            "is_variable_bitrate": lambda n : setattr(self, 'is_variable_bitrate', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "track": lambda n : setattr(self, 'track', n.get_int_value()),
            "track_count": lambda n : setattr(self, 'track_count', n.get_int_value()),
            "year": lambda n : setattr(self, 'year', n.get_int_value()),
        }
        return fields
    
    @property
    def has_drm(self,) -> Optional[bool]:
        """
        Gets the hasDrm property value. Indicates if the file is protected with digital rights management.
        Returns: Optional[bool]
        """
        return self._has_drm
    
    @has_drm.setter
    def has_drm(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasDrm property value. Indicates if the file is protected with digital rights management.
        Args:
            value: Value to set for the hasDrm property.
        """
        self._has_drm = value
    
    @property
    def is_variable_bitrate(self,) -> Optional[bool]:
        """
        Gets the isVariableBitrate property value. Indicates if the file is encoded with a variable bitrate.
        Returns: Optional[bool]
        """
        return self._is_variable_bitrate
    
    @is_variable_bitrate.setter
    def is_variable_bitrate(self,value: Optional[bool] = None) -> None:
        """
        Sets the isVariableBitrate property value. Indicates if the file is encoded with a variable bitrate.
        Args:
            value: Value to set for the isVariableBitrate property.
        """
        self._is_variable_bitrate = value
    
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
        writer.write_str_value("album", self.album)
        writer.write_str_value("albumArtist", self.album_artist)
        writer.write_str_value("artist", self.artist)
        writer.write_int_value("bitrate", self.bitrate)
        writer.write_str_value("composers", self.composers)
        writer.write_str_value("copyright", self.copyright)
        writer.write_int_value("disc", self.disc)
        writer.write_int_value("discCount", self.disc_count)
        writer.write_int_value("duration", self.duration)
        writer.write_str_value("genre", self.genre)
        writer.write_bool_value("hasDrm", self.has_drm)
        writer.write_bool_value("isVariableBitrate", self.is_variable_bitrate)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("title", self.title)
        writer.write_int_value("track", self.track)
        writer.write_int_value("trackCount", self.track_count)
        writer.write_int_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. The title of the audio file.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. The title of the audio file.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    
    @property
    def track(self,) -> Optional[int]:
        """
        Gets the track property value. The number of the track on the original disc for this audio file.
        Returns: Optional[int]
        """
        return self._track
    
    @track.setter
    def track(self,value: Optional[int] = None) -> None:
        """
        Sets the track property value. The number of the track on the original disc for this audio file.
        Args:
            value: Value to set for the track property.
        """
        self._track = value
    
    @property
    def track_count(self,) -> Optional[int]:
        """
        Gets the trackCount property value. The total number of tracks on the original disc for this audio file.
        Returns: Optional[int]
        """
        return self._track_count
    
    @track_count.setter
    def track_count(self,value: Optional[int] = None) -> None:
        """
        Sets the trackCount property value. The total number of tracks on the original disc for this audio file.
        Args:
            value: Value to set for the trackCount property.
        """
        self._track_count = value
    
    @property
    def year(self,) -> Optional[int]:
        """
        Gets the year property value. The year the audio file was recorded.
        Returns: Optional[int]
        """
        return self._year
    
    @year.setter
    def year(self,value: Optional[int] = None) -> None:
        """
        Sets the year property value. The year the audio file was recorded.
        Args:
            value: Value to set for the year property.
        """
        self._year = value
    

