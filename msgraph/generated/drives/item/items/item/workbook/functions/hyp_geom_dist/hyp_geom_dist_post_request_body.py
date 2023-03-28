from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class HypGeom_DistPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new hypGeom_DistPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The cumulative property
        self._cumulative: Optional[json.Json] = None
        # The numberPop property
        self._number_pop: Optional[json.Json] = None
        # The numberSample property
        self._number_sample: Optional[json.Json] = None
        # The populationS property
        self._population_s: Optional[json.Json] = None
        # The sampleS property
        self._sample_s: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HypGeom_DistPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HypGeom_DistPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HypGeom_DistPostRequestBody()
    
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
            "numberPop": lambda n : setattr(self, 'number_pop', n.get_object_value(json.Json)),
            "numberSample": lambda n : setattr(self, 'number_sample', n.get_object_value(json.Json)),
            "populationS": lambda n : setattr(self, 'population_s', n.get_object_value(json.Json)),
            "sampleS": lambda n : setattr(self, 'sample_s', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def number_pop(self,) -> Optional[json.Json]:
        """
        Gets the numberPop property value. The numberPop property
        Returns: Optional[json.Json]
        """
        return self._number_pop
    
    @number_pop.setter
    def number_pop(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numberPop property value. The numberPop property
        Args:
            value: Value to set for the number_pop property.
        """
        self._number_pop = value
    
    @property
    def number_sample(self,) -> Optional[json.Json]:
        """
        Gets the numberSample property value. The numberSample property
        Returns: Optional[json.Json]
        """
        return self._number_sample
    
    @number_sample.setter
    def number_sample(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numberSample property value. The numberSample property
        Args:
            value: Value to set for the number_sample property.
        """
        self._number_sample = value
    
    @property
    def population_s(self,) -> Optional[json.Json]:
        """
        Gets the populationS property value. The populationS property
        Returns: Optional[json.Json]
        """
        return self._population_s
    
    @population_s.setter
    def population_s(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the populationS property value. The populationS property
        Args:
            value: Value to set for the population_s property.
        """
        self._population_s = value
    
    @property
    def sample_s(self,) -> Optional[json.Json]:
        """
        Gets the sampleS property value. The sampleS property
        Returns: Optional[json.Json]
        """
        return self._sample_s
    
    @sample_s.setter
    def sample_s(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the sampleS property value. The sampleS property
        Args:
            value: Value to set for the sample_s property.
        """
        self._sample_s = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("cumulative", self.cumulative)
        writer.write_object_value("numberPop", self.number_pop)
        writer.write_object_value("numberSample", self.number_sample)
        writer.write_object_value("populationS", self.population_s)
        writer.write_object_value("sampleS", self.sample_s)
        writer.write_additional_data_value(self.additional_data)
    

