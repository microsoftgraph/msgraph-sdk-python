from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class CumPrincPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The endPeriod property
    end_period: Optional[json.Json] = None
    # The nper property
    nper: Optional[json.Json] = None
    # The pv property
    pv: Optional[json.Json] = None
    # The rate property
    rate: Optional[json.Json] = None
    # The startPeriod property
    start_period: Optional[json.Json] = None
    # The type property
    type: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CumPrincPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CumPrincPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CumPrincPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "endPeriod": lambda n : setattr(self, 'end_period', n.get_object_value(json.Json)),
            "nper": lambda n : setattr(self, 'nper', n.get_object_value(json.Json)),
            "pv": lambda n : setattr(self, 'pv', n.get_object_value(json.Json)),
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(json.Json)),
            "startPeriod": lambda n : setattr(self, 'start_period', n.get_object_value(json.Json)),
            "type": lambda n : setattr(self, 'type', n.get_object_value(json.Json)),
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
        writer.write_object_value("endPeriod", self.end_period)
        writer.write_object_value("nper", self.nper)
        writer.write_object_value("pv", self.pv)
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("startPeriod", self.start_period)
        writer.write_object_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

