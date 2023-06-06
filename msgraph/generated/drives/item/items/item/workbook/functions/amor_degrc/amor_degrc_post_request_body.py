from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class AmorDegrcPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The basis property
    basis: Optional[json.Json] = None
    # The cost property
    cost: Optional[json.Json] = None
    # The datePurchased property
    date_purchased: Optional[json.Json] = None
    # The firstPeriod property
    first_period: Optional[json.Json] = None
    # The period property
    period: Optional[json.Json] = None
    # The rate property
    rate: Optional[json.Json] = None
    # The salvage property
    salvage: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AmorDegrcPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AmorDegrcPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AmorDegrcPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "basis": lambda n : setattr(self, 'basis', n.get_object_value(json.Json)),
            "cost": lambda n : setattr(self, 'cost', n.get_object_value(json.Json)),
            "datePurchased": lambda n : setattr(self, 'date_purchased', n.get_object_value(json.Json)),
            "firstPeriod": lambda n : setattr(self, 'first_period', n.get_object_value(json.Json)),
            "period": lambda n : setattr(self, 'period', n.get_object_value(json.Json)),
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(json.Json)),
            "salvage": lambda n : setattr(self, 'salvage', n.get_object_value(json.Json)),
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
        writer.write_object_value("basis", self.basis)
        writer.write_object_value("cost", self.cost)
        writer.write_object_value("datePurchased", self.date_purchased)
        writer.write_object_value("firstPeriod", self.first_period)
        writer.write_object_value("period", self.period)
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("salvage", self.salvage)
        writer.write_additional_data_value(self.additional_data)
    

