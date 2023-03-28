from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class Binom_Dist_RangePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new binom_Dist_RangePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The numberS property
        self._number_s: Optional[json.Json] = None
        # The numberS2 property
        self._number_s2: Optional[json.Json] = None
        # The probabilityS property
        self._probability_s: Optional[json.Json] = None
        # The trials property
        self._trials: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Binom_Dist_RangePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Binom_Dist_RangePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Binom_Dist_RangePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "numberS": lambda n : setattr(self, 'number_s', n.get_object_value(json.Json)),
            "numberS2": lambda n : setattr(self, 'number_s2', n.get_object_value(json.Json)),
            "probabilityS": lambda n : setattr(self, 'probability_s', n.get_object_value(json.Json)),
            "trials": lambda n : setattr(self, 'trials', n.get_object_value(json.Json)),
        }
        return fields
    
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
    def number_s2(self,) -> Optional[json.Json]:
        """
        Gets the numberS2 property value. The numberS2 property
        Returns: Optional[json.Json]
        """
        return self._number_s2
    
    @number_s2.setter
    def number_s2(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numberS2 property value. The numberS2 property
        Args:
            value: Value to set for the number_s2 property.
        """
        self._number_s2 = value
    
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
        writer.write_object_value("numberS", self.number_s)
        writer.write_object_value("numberS2", self.number_s2)
        writer.write_object_value("probabilityS", self.probability_s)
        writer.write_object_value("trials", self.trials)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def trials(self,) -> Optional[json.Json]:
        """
        Gets the trials property value. The trials property
        Returns: Optional[json.Json]
        """
        return self._trials
    
    @trials.setter
    def trials(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the trials property value. The trials property
        Args:
            value: Value to set for the trials property.
        """
        self._trials = value
    

