from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class IfPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new ifPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The logicalTest property
        self._logical_test: Optional[json.Json] = None
        # The valueIfFalse property
        self._value_if_false: Optional[json.Json] = None
        # The valueIfTrue property
        self._value_if_true: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IfPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IfPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IfPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "logicalTest": lambda n : setattr(self, 'logical_test', n.get_object_value(json.Json)),
            "valueIfFalse": lambda n : setattr(self, 'value_if_false', n.get_object_value(json.Json)),
            "valueIfTrue": lambda n : setattr(self, 'value_if_true', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def logical_test(self,) -> Optional[json.Json]:
        """
        Gets the logicalTest property value. The logicalTest property
        Returns: Optional[json.Json]
        """
        return self._logical_test
    
    @logical_test.setter
    def logical_test(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the logicalTest property value. The logicalTest property
        Args:
            value: Value to set for the logical_test property.
        """
        self._logical_test = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("logicalTest", self.logical_test)
        writer.write_object_value("valueIfFalse", self.value_if_false)
        writer.write_object_value("valueIfTrue", self.value_if_true)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def value_if_false(self,) -> Optional[json.Json]:
        """
        Gets the valueIfFalse property value. The valueIfFalse property
        Returns: Optional[json.Json]
        """
        return self._value_if_false
    
    @value_if_false.setter
    def value_if_false(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the valueIfFalse property value. The valueIfFalse property
        Args:
            value: Value to set for the value_if_false property.
        """
        self._value_if_false = value
    
    @property
    def value_if_true(self,) -> Optional[json.Json]:
        """
        Gets the valueIfTrue property value. The valueIfTrue property
        Returns: Optional[json.Json]
        """
        return self._value_if_true
    
    @value_if_true.setter
    def value_if_true(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the valueIfTrue property value. The valueIfTrue property
        Args:
            value: Value to set for the value_if_true property.
        """
        self._value_if_true = value
    

