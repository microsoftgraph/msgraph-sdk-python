from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_type import AttributeType
    from .entity import Entity
    from .scope_operator_multi_valued_comparison_type import ScopeOperatorMultiValuedComparisonType
    from .scope_operator_type import ScopeOperatorType

from .entity import Entity

@dataclass
class FilterOperatorSchema(Entity, Parsable):
    # The arity property
    arity: Optional[ScopeOperatorType] = None
    # The multivaluedComparisonType property
    multivalued_comparison_type: Optional[ScopeOperatorMultiValuedComparisonType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Attribute types supported by the operator. The possible values are: Boolean, Binary, Reference, Integer, String.
    supported_attribute_types: Optional[list[AttributeType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilterOperatorSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilterOperatorSchema
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilterOperatorSchema()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_type import AttributeType
        from .entity import Entity
        from .scope_operator_multi_valued_comparison_type import ScopeOperatorMultiValuedComparisonType
        from .scope_operator_type import ScopeOperatorType

        from .attribute_type import AttributeType
        from .entity import Entity
        from .scope_operator_multi_valued_comparison_type import ScopeOperatorMultiValuedComparisonType
        from .scope_operator_type import ScopeOperatorType

        fields: dict[str, Callable[[Any], None]] = {
            "arity": lambda n : setattr(self, 'arity', n.get_enum_value(ScopeOperatorType)),
            "multivaluedComparisonType": lambda n : setattr(self, 'multivalued_comparison_type', n.get_enum_value(ScopeOperatorMultiValuedComparisonType)),
            "supportedAttributeTypes": lambda n : setattr(self, 'supported_attribute_types', n.get_collection_of_enum_values(AttributeType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("arity", self.arity)
        writer.write_enum_value("multivaluedComparisonType", self.multivalued_comparison_type)
        writer.write_collection_of_enum_values("supportedAttributeTypes", self.supported_attribute_types)
    

