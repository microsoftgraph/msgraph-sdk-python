from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_type, entity, scope_operator_multi_valued_comparison_type, scope_operator_type

from . import entity

class FilterOperatorSchema(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new FilterOperatorSchema and sets the default values.
        """
        super().__init__()
        # The arity property
        self._arity: Optional[scope_operator_type.ScopeOperatorType] = None
        # The multivaluedComparisonType property
        self._multivalued_comparison_type: Optional[scope_operator_multi_valued_comparison_type.ScopeOperatorMultiValuedComparisonType] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The supportedAttributeTypes property
        self._supported_attribute_types: Optional[List[attribute_type.AttributeType]] = None
    
    @property
    def arity(self,) -> Optional[scope_operator_type.ScopeOperatorType]:
        """
        Gets the arity property value. The arity property
        Returns: Optional[scope_operator_type.ScopeOperatorType]
        """
        return self._arity
    
    @arity.setter
    def arity(self,value: Optional[scope_operator_type.ScopeOperatorType] = None) -> None:
        """
        Sets the arity property value. The arity property
        Args:
            value: Value to set for the arity property.
        """
        self._arity = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FilterOperatorSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FilterOperatorSchema
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FilterOperatorSchema()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_type, entity, scope_operator_multi_valued_comparison_type, scope_operator_type

        fields: Dict[str, Callable[[Any], None]] = {
            "arity": lambda n : setattr(self, 'arity', n.get_enum_value(scope_operator_type.ScopeOperatorType)),
            "multivaluedComparisonType": lambda n : setattr(self, 'multivalued_comparison_type', n.get_enum_value(scope_operator_multi_valued_comparison_type.ScopeOperatorMultiValuedComparisonType)),
            "supportedAttributeTypes": lambda n : setattr(self, 'supported_attribute_types', n.get_collection_of_enum_values(attribute_type.AttributeType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def multivalued_comparison_type(self,) -> Optional[scope_operator_multi_valued_comparison_type.ScopeOperatorMultiValuedComparisonType]:
        """
        Gets the multivaluedComparisonType property value. The multivaluedComparisonType property
        Returns: Optional[scope_operator_multi_valued_comparison_type.ScopeOperatorMultiValuedComparisonType]
        """
        return self._multivalued_comparison_type
    
    @multivalued_comparison_type.setter
    def multivalued_comparison_type(self,value: Optional[scope_operator_multi_valued_comparison_type.ScopeOperatorMultiValuedComparisonType] = None) -> None:
        """
        Sets the multivaluedComparisonType property value. The multivaluedComparisonType property
        Args:
            value: Value to set for the multivalued_comparison_type property.
        """
        self._multivalued_comparison_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("arity", self.arity)
        writer.write_enum_value("multivaluedComparisonType", self.multivalued_comparison_type)
        writer.write_enum_value("supportedAttributeTypes", self.supported_attribute_types)
    
    @property
    def supported_attribute_types(self,) -> Optional[List[attribute_type.AttributeType]]:
        """
        Gets the supportedAttributeTypes property value. The supportedAttributeTypes property
        Returns: Optional[List[attribute_type.AttributeType]]
        """
        return self._supported_attribute_types
    
    @supported_attribute_types.setter
    def supported_attribute_types(self,value: Optional[List[attribute_type.AttributeType]] = None) -> None:
        """
        Sets the supportedAttributeTypes property value. The supportedAttributeTypes property
        Args:
            value: Value to set for the supported_attribute_types property.
        """
        self._supported_attribute_types = value
    

