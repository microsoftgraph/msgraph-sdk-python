from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_type, entity, scope_operator_multi_valued_comparison_type, scope_operator_type

from . import entity

@dataclass
class FilterOperatorSchema(entity.Entity):
    # The arity property
    arity: Optional[scope_operator_type.ScopeOperatorType] = None
    # The multivaluedComparisonType property
    multivalued_comparison_type: Optional[scope_operator_multi_valued_comparison_type.ScopeOperatorMultiValuedComparisonType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The supportedAttributeTypes property
    supported_attribute_types: Optional[List[attribute_type.AttributeType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilterOperatorSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FilterOperatorSchema
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FilterOperatorSchema()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_type, entity, scope_operator_multi_valued_comparison_type, scope_operator_type

        from . import attribute_type, entity, scope_operator_multi_valued_comparison_type, scope_operator_type

        fields: Dict[str, Callable[[Any], None]] = {
            "arity": lambda n : setattr(self, 'arity', n.get_enum_value(scope_operator_type.ScopeOperatorType)),
            "multivaluedComparisonType": lambda n : setattr(self, 'multivalued_comparison_type', n.get_enum_value(scope_operator_multi_valued_comparison_type.ScopeOperatorMultiValuedComparisonType)),
            "supportedAttributeTypes": lambda n : setattr(self, 'supported_attribute_types', n.get_collection_of_enum_values(attribute_type.AttributeType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("arity", self.arity)
        writer.write_enum_value("multivaluedComparisonType", self.multivalued_comparison_type)
        writer.write_collection_of_enum_values("supportedAttributeTypes", self.supported_attribute_types)
    

