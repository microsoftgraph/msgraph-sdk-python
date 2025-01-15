from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .media_config import MediaConfig
    from .media_info import MediaInfo

from .media_config import MediaConfig

@dataclass
class ServiceHostedMediaConfig(MediaConfig, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.serviceHostedMediaConfig"
    # The list of media to pre-fetch.
    pre_fetch_media: Optional[list[MediaInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceHostedMediaConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceHostedMediaConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceHostedMediaConfig()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .media_config import MediaConfig
        from .media_info import MediaInfo

        from .media_config import MediaConfig
        from .media_info import MediaInfo

        fields: dict[str, Callable[[Any], None]] = {
            "preFetchMedia": lambda n : setattr(self, 'pre_fetch_media', n.get_collection_of_object_values(MediaInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("preFetchMedia", self.pre_fetch_media)
    

