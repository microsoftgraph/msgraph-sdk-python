from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Audio(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The title of the album for this audio file.
    album: Optional[str] = None
    # The artist named on the album for the audio file.
    album_artist: Optional[str] = None
    # The performing artist for the audio file.
    artist: Optional[str] = None
    # Bitrate expressed in kbps.
    bitrate: Optional[int] = None
    # The name of the composer of the audio file.
    composers: Optional[str] = None
    # Copyright information for the audio file.
    copyright: Optional[str] = None
    # The number of the disc this audio file came from.
    disc: Optional[int] = None
    # The total number of discs in this album.
    disc_count: Optional[int] = None
    # Duration of the audio file, expressed in milliseconds
    duration: Optional[int] = None
    # The genre of this audio file.
    genre: Optional[str] = None
    # Indicates if the file is protected with digital rights management.
    has_drm: Optional[bool] = None
    # Indicates if the file is encoded with a variable bitrate.
    is_variable_bitrate: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The title of the audio file.
    title: Optional[str] = None
    # The number of the track on the original disc for this audio file.
    track: Optional[int] = None
    # The total number of tracks on the original disc for this audio file.
    track_count: Optional[int] = None
    # The year the audio file was recorded.
    year: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Audio:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Audio
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Audio()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "album": lambda n : setattr(self, 'album', n.get_str_value()),
            "albumArtist": lambda n : setattr(self, 'album_artist', n.get_str_value()),
            "artist": lambda n : setattr(self, 'artist', n.get_str_value()),
            "bitrate": lambda n : setattr(self, 'bitrate', n.get_int_value()),
            "composers": lambda n : setattr(self, 'composers', n.get_str_value()),
            "copyright": lambda n : setattr(self, 'copyright', n.get_str_value()),
            "disc": lambda n : setattr(self, 'disc', n.get_int_value()),
            "discCount": lambda n : setattr(self, 'disc_count', n.get_int_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "genre": lambda n : setattr(self, 'genre', n.get_str_value()),
            "hasDrm": lambda n : setattr(self, 'has_drm', n.get_bool_value()),
            "isVariableBitrate": lambda n : setattr(self, 'is_variable_bitrate', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "track": lambda n : setattr(self, 'track', n.get_int_value()),
            "trackCount": lambda n : setattr(self, 'track_count', n.get_int_value()),
            "year": lambda n : setattr(self, 'year', n.get_int_value()),
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
    

