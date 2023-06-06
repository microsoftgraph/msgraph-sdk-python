from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Thumbnail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The content stream for the thumbnail.
    content: Optional[bytes] = None
    # The height of the thumbnail, in pixels.
    height: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the item that provided the thumbnail. This is only available when a folder thumbnail is requested.
    source_item_id: Optional[str] = None
    # The URL used to fetch the thumbnail content.
    url: Optional[str] = None
    # The width of the thumbnail, in pixels.
    width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Thumbnail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Thumbnail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Thumbnail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sourceItemId": lambda n : setattr(self, 'source_item_id', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("content", self.content)
        writer.write_int_value("height", self.height)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceItemId", self.source_item_id)
        writer.write_str_value("url", self.url)
        writer.write_int_value("width", self.width)
        writer.write_additional_data_value(self.additional_data)
    

