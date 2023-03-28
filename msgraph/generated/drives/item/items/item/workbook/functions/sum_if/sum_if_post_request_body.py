from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class SumIfPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new sumIfPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The criteria property
        self._criteria: Optional[json.Json] = None
        # The range property
        self._range: Optional[json.Json] = None
        # The sumRange property
        self._sum_range: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SumIfPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SumIfPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SumIfPostRequestBody()
    
    @property
    def criteria(self,) -> Optional[json.Json]:
        """
        Gets the criteria property value. The criteria property
        Returns: Optional[json.Json]
        """
        return self._criteria
    
    @criteria.setter
    def criteria(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the criteria property value. The criteria property
        Args:
            value: Value to set for the criteria property.
        """
        self._criteria = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "criteria": lambda n : setattr(self, 'criteria', n.get_object_value(json.Json)),
            "range": lambda n : setattr(self, 'range', n.get_object_value(json.Json)),
            "sumRange": lambda n : setattr(self, 'sum_range', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def range(self,) -> Optional[json.Json]:
        """
        Gets the range property value. The range property
        Returns: Optional[json.Json]
        """
        return self._range
    
    @range.setter
    def range(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the range property value. The range property
        Args:
            value: Value to set for the range property.
        """
        self._range = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("criteria", self.criteria)
        writer.write_object_value("range", self.range)
        writer.write_object_value("sumRange", self.sum_range)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def sum_range(self,) -> Optional[json.Json]:
        """
        Gets the sumRange property value. The sumRange property
        Returns: Optional[json.Json]
        """
        return self._sum_range
    
    @sum_range.setter
    def sum_range(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the sumRange property value. The sumRange property
        Args:
            value: Value to set for the sum_range property.
        """
        self._sum_range = value
    

