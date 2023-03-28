from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class SeriesSumPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new seriesSumPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The coefficients property
        self._coefficients: Optional[json.Json] = None
        # The m property
        self._m: Optional[json.Json] = None
        # The n property
        self._n: Optional[json.Json] = None
        # The x property
        self._x: Optional[json.Json] = None
    
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
    def coefficients(self,) -> Optional[json.Json]:
        """
        Gets the coefficients property value. The coefficients property
        Returns: Optional[json.Json]
        """
        return self._coefficients
    
    @coefficients.setter
    def coefficients(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the coefficients property value. The coefficients property
        Args:
            value: Value to set for the coefficients property.
        """
        self._coefficients = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SeriesSumPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SeriesSumPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SeriesSumPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "coefficients": lambda n : setattr(self, 'coefficients', n.get_object_value(json.Json)),
            "m": lambda n : setattr(self, 'm', n.get_object_value(json.Json)),
            "n": lambda n : setattr(self, 'n', n.get_object_value(json.Json)),
            "x": lambda n : setattr(self, 'x', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def m(self,) -> Optional[json.Json]:
        """
        Gets the m property value. The m property
        Returns: Optional[json.Json]
        """
        return self._m
    
    @m.setter
    def m(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the m property value. The m property
        Args:
            value: Value to set for the m property.
        """
        self._m = value
    
    @property
    def n(self,) -> Optional[json.Json]:
        """
        Gets the n property value. The n property
        Returns: Optional[json.Json]
        """
        return self._n
    
    @n.setter
    def n(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the n property value. The n property
        Args:
            value: Value to set for the n property.
        """
        self._n = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("coefficients", self.coefficients)
        writer.write_object_value("m", self.m)
        writer.write_object_value("n", self.n)
        writer.write_object_value("x", self.x)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def x(self,) -> Optional[json.Json]:
        """
        Gets the x property value. The x property
        Returns: Optional[json.Json]
        """
        return self._x
    
    @x.setter
    def x(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the x property value. The x property
        Args:
            value: Value to set for the x property.
        """
        self._x = value
    

