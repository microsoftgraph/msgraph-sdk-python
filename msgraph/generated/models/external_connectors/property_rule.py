from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import rule_operation
    from .. import binary_operator

@dataclass
class PropertyRule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # The operation property
    operation: Optional[rule_operation.RuleOperation] = None
    # The property from the externalItem schema. Required.
    property_: Optional[str] = None
    # A collection with one or many strings. The specified string(s) will be matched with the specified property using the specified operation. Required.
    values: Optional[List[str]] = None
    # The valuesJoinedBy property
    values_joined_by: Optional[binary_operator.BinaryOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PropertyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PropertyRule
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PropertyRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import rule_operation
        from .. import binary_operator

        from . import rule_operation
        from .. import binary_operator

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operation": lambda n : setattr(self, 'operation', n.get_enum_value(rule_operation.RuleOperation)),
            "property": lambda n : setattr(self, 'property_', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_collection_of_primitive_values(str)),
            "valuesJoinedBy": lambda n : setattr(self, 'values_joined_by', n.get_enum_value(binary_operator.BinaryOperator)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operation", self.operation)
        writer.write_str_value("property", self.property_)
        writer.write_collection_of_primitive_values("values", self.values)
        writer.write_enum_value("valuesJoinedBy", self.values_joined_by)
        writer.write_additional_data_value(self.additional_data)
    

