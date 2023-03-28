from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class BitandPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new bitandPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number1 property
        self._number1: Optional[json.Json] = None
        # The number2 property
        self._number2: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitandPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BitandPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BitandPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "number1": lambda n : setattr(self, 'number1', n.get_object_value(json.Json)),
            "number2": lambda n : setattr(self, 'number2', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def number1(self,) -> Optional[json.Json]:
        """
        Gets the number1 property value. The number1 property
        Returns: Optional[json.Json]
        """
        return self._number1
    
    @number1.setter
    def number1(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the number1 property value. The number1 property
        Args:
            value: Value to set for the number1 property.
        """
        self._number1 = value
    
    @property
    def number2(self,) -> Optional[json.Json]:
        """
        Gets the number2 property value. The number2 property
        Returns: Optional[json.Json]
        """
        return self._number2
    
    @number2.setter
    def number2(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the number2 property value. The number2 property
        Args:
            value: Value to set for the number2 property.
        """
        self._number2 = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("number1", self.number1)
        writer.write_object_value("number2", self.number2)
        writer.write_additional_data_value(self.additional_data)
    

