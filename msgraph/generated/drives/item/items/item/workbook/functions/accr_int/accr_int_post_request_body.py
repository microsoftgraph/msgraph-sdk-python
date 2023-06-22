from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

@dataclass
class AccrIntPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The basis property
    basis: Optional[json.Json] = None
    # The calcMethod property
    calc_method: Optional[json.Json] = None
    # The firstInterest property
    first_interest: Optional[json.Json] = None
    # The frequency property
    frequency: Optional[json.Json] = None
    # The issue property
    issue: Optional[json.Json] = None
    # The par property
    par: Optional[json.Json] = None
    # The rate property
    rate: Optional[json.Json] = None
    # The settlement property
    settlement: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccrIntPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccrIntPostRequestBody
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccrIntPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "basis": lambda n : setattr(self, 'basis', n.get_object_value(json.Json)),
            "calcMethod": lambda n : setattr(self, 'calc_method', n.get_object_value(json.Json)),
            "firstInterest": lambda n : setattr(self, 'first_interest', n.get_object_value(json.Json)),
            "frequency": lambda n : setattr(self, 'frequency', n.get_object_value(json.Json)),
            "issue": lambda n : setattr(self, 'issue', n.get_object_value(json.Json)),
            "par": lambda n : setattr(self, 'par', n.get_object_value(json.Json)),
            "rate": lambda n : setattr(self, 'rate', n.get_object_value(json.Json)),
            "settlement": lambda n : setattr(self, 'settlement', n.get_object_value(json.Json)),
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
        writer.write_object_value("basis", self.basis)
        writer.write_object_value("calcMethod", self.calc_method)
        writer.write_object_value("firstInterest", self.first_interest)
        writer.write_object_value("frequency", self.frequency)
        writer.write_object_value("issue", self.issue)
        writer.write_object_value("par", self.par)
        writer.write_object_value("rate", self.rate)
        writer.write_object_value("settlement", self.settlement)
        writer.write_additional_data_value(self.additional_data)
    

