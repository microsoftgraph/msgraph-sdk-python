from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class Beta_InvPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The A property
    a: Optional[json.Json] = None
    # The alpha property
    alpha: Optional[json.Json] = None
    # The B property
    b: Optional[json.Json] = None
    # The beta property
    beta: Optional[json.Json] = None
    # The probability property
    probability: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Beta_InvPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Beta_InvPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Beta_InvPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "A": lambda n : setattr(self, 'a', n.get_object_value(json.Json)),
            "alpha": lambda n : setattr(self, 'alpha', n.get_object_value(json.Json)),
            "B": lambda n : setattr(self, 'b', n.get_object_value(json.Json)),
            "beta": lambda n : setattr(self, 'beta', n.get_object_value(json.Json)),
            "probability": lambda n : setattr(self, 'probability', n.get_object_value(json.Json)),
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
        writer.write_object_value("A", self.a)
        writer.write_object_value("alpha", self.alpha)
        writer.write_object_value("B", self.b)
        writer.write_object_value("beta", self.beta)
        writer.write_object_value("probability", self.probability)
        writer.write_additional_data_value(self.additional_data)
    

