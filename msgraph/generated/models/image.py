from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Image(AdditionalDataHolder, Parsable):
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
        Instantiates a new image and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Optional. Height of the image, in pixels. Read-only.
        self._height: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Optional. Width of the image, in pixels. Read-only.
        self._width: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Image:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Image
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Image()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
        }
        return fields
    
    @property
    def height(self,) -> Optional[int]:
        """
        Gets the height property value. Optional. Height of the image, in pixels. Read-only.
        Returns: Optional[int]
        """
        return self._height
    
    @height.setter
    def height(self,value: Optional[int] = None) -> None:
        """
        Sets the height property value. Optional. Height of the image, in pixels. Read-only.
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
        writer.write_int_value("height", self.height)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("width", self.width)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def width(self,) -> Optional[int]:
        """
        Gets the width property value. Optional. Width of the image, in pixels. Read-only.
        Returns: Optional[int]
        """
        return self._width
    
    @width.setter
    def width(self,value: Optional[int] = None) -> None:
        """
        Sets the width property value. Optional. Width of the image, in pixels. Read-only.
        Args:
            value: Value to set for the width property.
        """
        self._width = value
    

