from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class PercentRank_ExcPostRequestBody(AdditionalDataHolder, Parsable):
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
    def array(self,) -> Optional[json.Json]:
        """
        Gets the array property value. 
        Returns: Optional[json.Json]
        """
        return self._array
    
    @array.setter
    def array(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the array property value. 
        Args:
            value: Value to set for the array property.
        """
        self._array = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new percentRank_ExcPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        self._array: Optional[json.Json] = None
        self._significance: Optional[json.Json] = None
        self._x: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PercentRank_ExcPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PercentRank_ExcPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PercentRank_ExcPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "array": lambda n : setattr(self, 'array', n.get_object_value(json.Json)),
            "significance": lambda n : setattr(self, 'significance', n.get_object_value(json.Json)),
            "x": lambda n : setattr(self, 'x', n.get_object_value(json.Json)),
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
        writer.write_object_value("array", self.array)
        writer.write_object_value("significance", self.significance)
        writer.write_object_value("x", self.x)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def significance(self,) -> Optional[json.Json]:
        """
        Gets the significance property value. 
        Returns: Optional[json.Json]
        """
        return self._significance
    
    @significance.setter
    def significance(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the significance property value. 
        Args:
            value: Value to set for the significance property.
        """
        self._significance = value
    
    @property
    def x(self,) -> Optional[json.Json]:
        """
        Gets the x property value. 
        Returns: Optional[json.Json]
        """
        return self._x
    
    @x.setter
    def x(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the x property value. 
        Args:
            value: Value to set for the x property.
        """
        self._x = value
    

