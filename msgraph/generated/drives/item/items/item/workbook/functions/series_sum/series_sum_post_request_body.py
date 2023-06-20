from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class SeriesSumPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The coefficients property
    coefficients: Optional[json.Json] = None
    # The m property
    m: Optional[json.Json] = None
    # The n property
    n: Optional[json.Json] = None
    # The x property
    x: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SeriesSumPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SeriesSumPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SeriesSumPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "coefficients": lambda n : setattr(self, 'coefficients', n.get_object_value(json.Json)),
            "m": lambda n : setattr(self, 'm', n.get_object_value(json.Json)),
            "n": lambda n : setattr(self, 'n', n.get_object_value(json.Json)),
            "x": lambda n : setattr(self, 'x', n.get_object_value(json.Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("coefficients", self.coefficients)
        writer.write_object_value("m", self.m)
        writer.write_object_value("n", self.n)
        writer.write_object_value("x", self.x)
        writer.write_additional_data_value(self.additional_data)
    

