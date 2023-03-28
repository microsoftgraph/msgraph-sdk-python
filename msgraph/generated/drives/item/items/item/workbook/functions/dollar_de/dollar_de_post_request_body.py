from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class DollarDePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new dollarDePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The fraction property
        self._fraction: Optional[json.Json] = None
        # The fractionalDollar property
        self._fractional_dollar: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DollarDePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DollarDePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DollarDePostRequestBody()
    
    @property
    def fraction(self,) -> Optional[json.Json]:
        """
        Gets the fraction property value. The fraction property
        Returns: Optional[json.Json]
        """
        return self._fraction
    
    @fraction.setter
    def fraction(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the fraction property value. The fraction property
        Args:
            value: Value to set for the fraction property.
        """
        self._fraction = value
    
    @property
    def fractional_dollar(self,) -> Optional[json.Json]:
        """
        Gets the fractionalDollar property value. The fractionalDollar property
        Returns: Optional[json.Json]
        """
        return self._fractional_dollar
    
    @fractional_dollar.setter
    def fractional_dollar(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the fractionalDollar property value. The fractionalDollar property
        Args:
            value: Value to set for the fractional_dollar property.
        """
        self._fractional_dollar = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "fraction": lambda n : setattr(self, 'fraction', n.get_object_value(json.Json)),
            "fractionalDollar": lambda n : setattr(self, 'fractional_dollar', n.get_object_value(json.Json)),
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
        writer.write_object_value("fraction", self.fraction)
        writer.write_object_value("fractionalDollar", self.fractional_dollar)
        writer.write_additional_data_value(self.additional_data)
    

