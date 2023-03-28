from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class NegBinom_DistPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new negBinom_DistPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cumulative property
        self._cumulative: Optional[json.Json] = None
        # The numberF property
        self._number_f: Optional[json.Json] = None
        # The numberS property
        self._number_s: Optional[json.Json] = None
        # The probabilityS property
        self._probability_s: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> NegBinom_DistPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: NegBinom_DistPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return NegBinom_DistPostRequestBody()
    
    @property
    def cumulative(self,) -> Optional[json.Json]:
        """
        Gets the cumulative property value. The cumulative property
        Returns: Optional[json.Json]
        """
        return self._cumulative
    
    @cumulative.setter
    def cumulative(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the cumulative property value. The cumulative property
        Args:
            value: Value to set for the cumulative property.
        """
        self._cumulative = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "cumulative": lambda n : setattr(self, 'cumulative', n.get_object_value(json.Json)),
            "numberF": lambda n : setattr(self, 'number_f', n.get_object_value(json.Json)),
            "numberS": lambda n : setattr(self, 'number_s', n.get_object_value(json.Json)),
            "probabilityS": lambda n : setattr(self, 'probability_s', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def number_f(self,) -> Optional[json.Json]:
        """
        Gets the numberF property value. The numberF property
        Returns: Optional[json.Json]
        """
        return self._number_f
    
    @number_f.setter
    def number_f(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numberF property value. The numberF property
        Args:
            value: Value to set for the number_f property.
        """
        self._number_f = value
    
    @property
    def number_s(self,) -> Optional[json.Json]:
        """
        Gets the numberS property value. The numberS property
        Returns: Optional[json.Json]
        """
        return self._number_s
    
    @number_s.setter
    def number_s(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numberS property value. The numberS property
        Args:
            value: Value to set for the number_s property.
        """
        self._number_s = value
    
    @property
    def probability_s(self,) -> Optional[json.Json]:
        """
        Gets the probabilityS property value. The probabilityS property
        Returns: Optional[json.Json]
        """
        return self._probability_s
    
    @probability_s.setter
    def probability_s(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the probabilityS property value. The probabilityS property
        Args:
            value: Value to set for the probability_s property.
        """
        self._probability_s = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("cumulative", self.cumulative)
        writer.write_object_value("numberF", self.number_f)
        writer.write_object_value("numberS", self.number_s)
        writer.write_object_value("probabilityS", self.probability_s)
        writer.write_additional_data_value(self.additional_data)
    

