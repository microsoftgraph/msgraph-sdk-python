from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class IfPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The logicalTest property
    logical_test: Optional[json.Json] = None
    # The valueIfFalse property
    value_if_false: Optional[json.Json] = None
    # The valueIfTrue property
    value_if_true: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IfPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IfPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IfPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "logicalTest": lambda n : setattr(self, 'logical_test', n.get_object_value(json.Json)),
            "valueIfFalse": lambda n : setattr(self, 'value_if_false', n.get_object_value(json.Json)),
            "valueIfTrue": lambda n : setattr(self, 'value_if_true', n.get_object_value(json.Json)),
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
        writer.write_object_value("logicalTest", self.logical_test)
        writer.write_object_value("valueIfFalse", self.value_if_false)
        writer.write_object_value("valueIfTrue", self.value_if_true)
        writer.write_additional_data_value(self.additional_data)
    

