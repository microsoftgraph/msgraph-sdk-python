from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class ConvertPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new convertPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The fromUnit property
        self._from_unit: Optional[json.Json] = None
        # The number property
        self._number: Optional[json.Json] = None
        # The toUnit property
        self._to_unit: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConvertPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConvertPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ConvertPostRequestBody()
    
    @property
    def from_unit(self,) -> Optional[json.Json]:
        """
        Gets the fromUnit property value. The fromUnit property
        Returns: Optional[json.Json]
        """
        return self._from_unit
    
    @from_unit.setter
    def from_unit(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the fromUnit property value. The fromUnit property
        Args:
            value: Value to set for the from_unit property.
        """
        self._from_unit = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "fromUnit": lambda n : setattr(self, 'from_unit', n.get_object_value(json.Json)),
            "number": lambda n : setattr(self, 'number', n.get_object_value(json.Json)),
            "toUnit": lambda n : setattr(self, 'to_unit', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def number(self,) -> Optional[json.Json]:
        """
        Gets the number property value. The number property
        Returns: Optional[json.Json]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("fromUnit", self.from_unit)
        writer.write_object_value("number", self.number)
        writer.write_object_value("toUnit", self.to_unit)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def to_unit(self,) -> Optional[json.Json]:
        """
        Gets the toUnit property value. The toUnit property
        Returns: Optional[json.Json]
        """
        return self._to_unit
    
    @to_unit.setter
    def to_unit(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the toUnit property value. The toUnit property
        Args:
            value: Value to set for the to_unit property.
        """
        self._to_unit = value
    

