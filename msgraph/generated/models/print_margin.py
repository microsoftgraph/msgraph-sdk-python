from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class PrintMargin(AdditionalDataHolder, Parsable):
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
    def bottom(self,) -> Optional[int]:
        """
        Gets the bottom property value. The margin in microns from the bottom edge.
        Returns: Optional[int]
        """
        return self._bottom
    
    @bottom.setter
    def bottom(self,value: Optional[int] = None) -> None:
        """
        Sets the bottom property value. The margin in microns from the bottom edge.
        Args:
            value: Value to set for the bottom property.
        """
        self._bottom = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new printMargin and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The margin in microns from the bottom edge.
        self._bottom: Optional[int] = None
        # The margin in microns from the left edge.
        self._left: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The margin in microns from the right edge.
        self._right: Optional[int] = None
        # The margin in microns from the top edge.
        self._top: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintMargin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintMargin
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintMargin()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bottom": lambda n : setattr(self, 'bottom', n.get_int_value()),
            "left": lambda n : setattr(self, 'left', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "right": lambda n : setattr(self, 'right', n.get_int_value()),
            "top": lambda n : setattr(self, 'top', n.get_int_value()),
        }
        return fields
    
    @property
    def left(self,) -> Optional[int]:
        """
        Gets the left property value. The margin in microns from the left edge.
        Returns: Optional[int]
        """
        return self._left
    
    @left.setter
    def left(self,value: Optional[int] = None) -> None:
        """
        Sets the left property value. The margin in microns from the left edge.
        Args:
            value: Value to set for the left property.
        """
        self._left = value
    
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
    
    @property
    def right(self,) -> Optional[int]:
        """
        Gets the right property value. The margin in microns from the right edge.
        Returns: Optional[int]
        """
        return self._right
    
    @right.setter
    def right(self,value: Optional[int] = None) -> None:
        """
        Sets the right property value. The margin in microns from the right edge.
        Args:
            value: Value to set for the right property.
        """
        self._right = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("bottom", self.bottom)
        writer.write_int_value("left", self.left)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("right", self.right)
        writer.write_int_value("top", self.top)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def top(self,) -> Optional[int]:
        """
        Gets the top property value. The margin in microns from the top edge.
        Returns: Optional[int]
        """
        return self._top
    
    @top.setter
    def top(self,value: Optional[int] = None) -> None:
        """
        Sets the top property value. The margin in microns from the top edge.
        Args:
            value: Value to set for the top property.
        """
        self._top = value
    

