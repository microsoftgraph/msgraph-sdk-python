from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .media_direction import MediaDirection
    from .modality import Modality

@dataclass
class MediaStream(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The direction property
    direction: Optional[MediaDirection] = None
    # The media stream label.
    label: Optional[str] = None
    # The mediaType property
    media_type: Optional[Modality] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If the media is muted by the server.
    server_muted: Optional[bool] = None
    # The source ID.
    source_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MediaStream:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MediaStream
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MediaStream()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .media_direction import MediaDirection
        from .modality import Modality

        from .media_direction import MediaDirection
        from .modality import Modality

        fields: dict[str, Callable[[Any], None]] = {
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(MediaDirection)),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_enum_value(Modality)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "serverMuted": lambda n : setattr(self, 'server_muted', n.get_bool_value()),
            "sourceId": lambda n : setattr(self, 'source_id', n.get_str_value()),
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
        writer.write_enum_value("direction", self.direction)
        writer.write_str_value("label", self.label)
        writer.write_enum_value("mediaType", self.media_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("serverMuted", self.server_muted)
        writer.write_str_value("sourceId", self.source_id)
        writer.write_additional_data_value(self.additional_data)
    

