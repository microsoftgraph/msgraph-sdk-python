from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.json import Json

@dataclass
class HypGeom_DistPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The cumulative property
    cumulative: Optional[Json] = None
    # The numberPop property
    number_pop: Optional[Json] = None
    # The numberSample property
    number_sample: Optional[Json] = None
    # The populationS property
    population_s: Optional[Json] = None
    # The sampleS property
    sample_s: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HypGeom_DistPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HypGeom_DistPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return HypGeom_DistPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models.json import Json

        from ........models.json import Json

        fields: Dict[str, Callable[[Any], None]] = {
            "cumulative": lambda n : setattr(self, 'cumulative', n.get_object_value(Json)),
            "numberPop": lambda n : setattr(self, 'number_pop', n.get_object_value(Json)),
            "numberSample": lambda n : setattr(self, 'number_sample', n.get_object_value(Json)),
            "populationS": lambda n : setattr(self, 'population_s', n.get_object_value(Json)),
            "sampleS": lambda n : setattr(self, 'sample_s', n.get_object_value(Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("cumulative", self.cumulative)
        writer.write_object_value("numberPop", self.number_pop)
        writer.write_object_value("numberSample", self.number_sample)
        writer.write_object_value("populationS", self.population_s)
        writer.write_object_value("sampleS", self.sample_s)
        writer.write_additional_data_value(self.additional_data)
    

