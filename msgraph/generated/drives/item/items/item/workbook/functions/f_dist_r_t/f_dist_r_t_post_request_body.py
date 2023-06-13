from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class F_Dist_RTPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The degFreedom1 property
    deg_freedom1: Optional[json.Json] = None
    # The degFreedom2 property
    deg_freedom2: Optional[json.Json] = None
    # The x property
    x: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> F_Dist_RTPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: F_Dist_RTPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return F_Dist_RTPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "degFreedom1": lambda n : setattr(self, 'deg_freedom1', n.get_object_value(json.Json)),
            "degFreedom2": lambda n : setattr(self, 'deg_freedom2', n.get_object_value(json.Json)),
            "x": lambda n : setattr(self, 'x', n.get_object_value(json.Json)),
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
        writer.write_object_value("degFreedom1", self.deg_freedom1)
        writer.write_object_value("degFreedom2", self.deg_freedom2)
        writer.write_object_value("x", self.x)
        writer.write_additional_data_value(self.additional_data)
    

