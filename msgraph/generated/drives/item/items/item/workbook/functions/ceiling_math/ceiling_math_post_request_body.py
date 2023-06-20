from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class Ceiling_MathPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The mode property
    mode: Optional[json.Json] = None
    # The number property
    number: Optional[json.Json] = None
    # The significance property
    significance: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Ceiling_MathPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Ceiling_MathPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Ceiling_MathPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "mode": lambda n : setattr(self, 'mode', n.get_object_value(json.Json)),
            "number": lambda n : setattr(self, 'number', n.get_object_value(json.Json)),
            "significance": lambda n : setattr(self, 'significance', n.get_object_value(json.Json)),
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
        writer.write_object_value("mode", self.mode)
        writer.write_object_value("number", self.number)
        writer.write_object_value("significance", self.significance)
        writer.write_additional_data_value(self.additional_data)
    

