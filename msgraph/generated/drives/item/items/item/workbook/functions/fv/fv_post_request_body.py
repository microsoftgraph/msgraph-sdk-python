from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class FvPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The nper property
    nper: Optional[json.Json] = None
    # The pmt property
    pmt: Optional[json.Json] = None
    # The pv property
    pv: Optional[json.Json] = None
    # The rate property
    rate: Optional[json.Json] = None
    # The type property
    type: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FvPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FvPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FvPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "nper": lambda n : setattr(self, 'nper', n.get_object_value(json.Json)),
            "pmt": lambda n : setattr(self, 'pmt', n.get_object_value(json.Json)),
            "pv": lambda n : setattr(self, 'pv', n.get_object_value(json.Json)),
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(json.Json)),
            "type": lambda n : setattr(self, 'type', n.get_object_value(json.Json)),
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
        writer.write_object_value("nper", self.nper)
        writer.write_object_value("pmt", self.pmt)
        writer.write_object_value("pv", self.pv)
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

