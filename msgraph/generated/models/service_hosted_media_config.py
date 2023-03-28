from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import media_config, media_info

from . import media_config

class ServiceHostedMediaConfig(media_config.MediaConfig):
    def __init__(self,) -> None:
        """
        Instantiates a new ServiceHostedMediaConfig and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.serviceHostedMediaConfig"
        # The list of media to pre-fetch.
        self._pre_fetch_media: Optional[List[media_info.MediaInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ServiceHostedMediaConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ServiceHostedMediaConfig
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ServiceHostedMediaConfig()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import media_config, media_info

        fields: Dict[str, Callable[[Any], None]] = {
            "preFetchMedia": lambda n : setattr(self, 'pre_fetch_media', n.get_collection_of_object_values(media_info.MediaInfo)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def pre_fetch_media(self,) -> Optional[List[media_info.MediaInfo]]:
        """
        Gets the preFetchMedia property value. The list of media to pre-fetch.
        Returns: Optional[List[media_info.MediaInfo]]
        """
        return self._pre_fetch_media
    
    @pre_fetch_media.setter
    def pre_fetch_media(self,value: Optional[List[media_info.MediaInfo]] = None) -> None:
        """
        Sets the preFetchMedia property value. The list of media to pre-fetch.
        Args:
            value: Value to set for the pre_fetch_media property.
        """
        self._pre_fetch_media = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("preFetchMedia", self.pre_fetch_media)
    

