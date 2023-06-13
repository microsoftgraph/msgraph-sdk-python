from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import filter_operand

@dataclass
class FilterClause(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The operatorName property
    operator_name: Optional[str] = None
    # The sourceOperandName property
    source_operand_name: Optional[str] = None
    # The targetOperand property
    target_operand: Optional[filter_operand.FilterOperand] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilterClause:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FilterClause
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FilterClause()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import filter_operand

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operatorName": lambda n : setattr(self, 'operator_name', n.get_str_value()),
            "sourceOperandName": lambda n : setattr(self, 'source_operand_name', n.get_str_value()),
            "targetOperand": lambda n : setattr(self, 'target_operand', n.get_object_value(filter_operand.FilterOperand)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("operatorName", self.operator_name)
        writer.write_str_value("sourceOperandName", self.source_operand_name)
        writer.write_object_value("targetOperand", self.target_operand)
        writer.write_additional_data_value(self.additional_data)
    

