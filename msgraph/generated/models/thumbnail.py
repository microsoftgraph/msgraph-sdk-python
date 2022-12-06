from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Thumbnail(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new thumbnail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The content stream for the thumbnail.
        self._content: Optional[bytes] = None
        # The height of the thumbnail, in pixels.
        self._height: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The unique identifier of the item that provided the thumbnail. This is only available when a folder thumbnail is requested.
        self._source_item_id: Optional[str] = None
        # The URL used to fetch the thumbnail content.
        self._url: Optional[str] = None
        # The width of the thumbnail, in pixels.
        self._width: Optional[int] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The content stream for the thumbnail.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The content stream for the thumbnail.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
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
        fields = {
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source_item_id": lambda n : setattr(self, 'source_item_id', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
        }
        return fields
    
    @property
    def height(self,) -> Optional[int]:
        """
        Gets the height property value. The height of the thumbnail, in pixels.
        Returns: Optional[int]
        """
        return self._height
    
    @height.setter
    def height(self,value: Optional[int] = None) -> None:
        """
        Sets the height property value. The height of the thumbnail, in pixels.
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
        writer.write_object_value("content", self.content)
        writer.write_int_value("height", self.height)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sourceItemId", self.source_item_id)
        writer.write_str_value("url", self.url)
        writer.write_int_value("width", self.width)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def source_item_id(self,) -> Optional[str]:
        """
        Gets the sourceItemId property value. The unique identifier of the item that provided the thumbnail. This is only available when a folder thumbnail is requested.
        Returns: Optional[str]
        """
        return self._source_item_id
    
    @source_item_id.setter
    def source_item_id(self,value: Optional[str] = None) -> None:
        """
        Sets the sourceItemId property value. The unique identifier of the item that provided the thumbnail. This is only available when a folder thumbnail is requested.
        Args:
            value: Value to set for the sourceItemId property.
        """
        self._source_item_id = value
    
    @property
    def url(self,) -> Optional[str]:
        """
        Gets the url property value. The URL used to fetch the thumbnail content.
        Returns: Optional[str]
        """
        return self._url
    
    @url.setter
    def url(self,value: Optional[str] = None) -> None:
        """
        Sets the url property value. The URL used to fetch the thumbnail content.
        Args:
            value: Value to set for the url property.
        """
        self._url = value
    
    @property
    def width(self,) -> Optional[int]:
        """
        Gets the width property value. The width of the thumbnail, in pixels.
        Returns: Optional[int]
        """
        return self._width
    
    @width.setter
    def width(self,value: Optional[int] = None) -> None:
        """
        Sets the width property value. The width of the thumbnail, in pixels.
        Args:
            value: Value to set for the width property.
        """
        self._width = value
    

