from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class DollarFrPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new dollarFrPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The decimalDollar property
        self._decimal_dollar: Optional[json.Json] = None
        # The fraction property
        self._fraction: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DollarFrPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DollarFrPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DollarFrPostRequestBody()
    
    @property
    def decimal_dollar(self,) -> Optional[json.Json]:
        """
        Gets the decimalDollar property value. The decimalDollar property
        Returns: Optional[json.Json]
        """
        return self._decimal_dollar
    
    @decimal_dollar.setter
    def decimal_dollar(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the decimalDollar property value. The decimalDollar property
        Args:
            value: Value to set for the decimal_dollar property.
        """
        self._decimal_dollar = value
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "decimalDollar": lambda n : setattr(self, 'decimal_dollar', n.get_object_value(json.Json)),
            "fraction": lambda n : setattr(self, 'fraction', n.get_object_value(json.Json)),
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
        writer.write_object_value("decimalDollar", self.decimal_dollar)
        writer.write_object_value("fraction", self.fraction)
        writer.write_additional_data_value(self.additional_data)
    

