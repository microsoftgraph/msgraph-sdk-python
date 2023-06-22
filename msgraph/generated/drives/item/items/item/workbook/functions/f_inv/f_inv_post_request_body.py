from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class F_InvPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The degFreedom1 property
    deg_freedom1: Optional[json.Json] = None
    # The degFreedom2 property
    deg_freedom2: Optional[json.Json] = None
    # The probability property
    probability: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> F_InvPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: F_InvPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return F_InvPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "degFreedom1": lambda n : setattr(self, 'deg_freedom1', n.get_object_value(json.Json)),
            "degFreedom2": lambda n : setattr(self, 'deg_freedom2', n.get_object_value(json.Json)),
            "probability": lambda n : setattr(self, 'probability', n.get_object_value(json.Json)),
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
        writer.write_object_value("degFreedom1", self.deg_freedom1)
        writer.write_object_value("degFreedom2", self.deg_freedom2)
        writer.write_object_value("probability", self.probability)
        writer.write_additional_data_value(self.additional_data)
    

