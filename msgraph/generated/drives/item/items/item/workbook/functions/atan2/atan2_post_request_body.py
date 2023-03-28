from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class Atan2PostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new atan2PostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The xNum property
        self._x_num: Optional[json.Json] = None
        # The yNum property
        self._y_num: Optional[json.Json] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Atan2PostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Atan2PostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Atan2PostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "xNum": lambda n : setattr(self, 'x_num', n.get_object_value(json.Json)),
            "yNum": lambda n : setattr(self, 'y_num', n.get_object_value(json.Json)),
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
        writer.write_object_value("xNum", self.x_num)
        writer.write_object_value("yNum", self.y_num)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def x_num(self,) -> Optional[json.Json]:
        """
        Gets the xNum property value. The xNum property
        Returns: Optional[json.Json]
        """
        return self._x_num
    
    @x_num.setter
    def x_num(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the xNum property value. The xNum property
        Args:
            value: Value to set for the x_num property.
        """
        self._x_num = value
    
    @property
    def y_num(self,) -> Optional[json.Json]:
        """
        Gets the yNum property value. The yNum property
        Returns: Optional[json.Json]
        """
        return self._y_num
    
    @y_num.setter
    def y_num(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the yNum property value. The yNum property
        Args:
            value: Value to set for the y_num property.
        """
        self._y_num = value
    

