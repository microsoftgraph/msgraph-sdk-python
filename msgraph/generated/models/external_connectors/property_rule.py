from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import rule_operation
    from .. import binary_operator

class PropertyRule(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new propertyRule and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The operation property
        self._operation: Optional[rule_operation.RuleOperation] = None
        # The property from the externalItem schema. Required.
        self._property_: Optional[str] = None
        # A collection with one or many strings. The specified string(s) will be matched with the specified property using the specified operation. Required.
        self._values: Optional[List[str]] = None
        # The valuesJoinedBy property
        self._values_joined_by: Optional[binary_operator.BinaryOperator] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PropertyRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PropertyRule
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PropertyRule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def operation(self,) -> Optional[rule_operation.RuleOperation]:
        """
        Gets the operation property value. The operation property
        Returns: Optional[rule_operation.RuleOperation]
        """
        return self._operation
    
    @operation.setter
    def operation(self,value: Optional[rule_operation.RuleOperation] = None) -> None:
        """
        Sets the operation property value. The operation property
        Args:
            value: Value to set for the operation property.
        """
        self._operation = value
    
    @property
    def property_(self,) -> Optional[str]:
        """
        Gets the property property value. The property from the externalItem schema. Required.
        Returns: Optional[str]
        """
        return self._property_
    
    @property_.setter
    def property_(self,value: Optional[str] = None) -> None:
        """
        Sets the property property value. The property from the externalItem schema. Required.
        Args:
            value: Value to set for the property_ property.
        """
        self._property_ = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("operation", self.operation)
        writer.write_str_value("property", self.property_)
        writer.write_collection_of_primitive_values("values", self.values)
        writer.write_enum_value("valuesJoinedBy", self.values_joined_by)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def values(self,) -> Optional[List[str]]:
        """
        Gets the values property value. A collection with one or many strings. The specified string(s) will be matched with the specified property using the specified operation. Required.
        Returns: Optional[List[str]]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the values property value. A collection with one or many strings. The specified string(s) will be matched with the specified property using the specified operation. Required.
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    
    @property
    def values_joined_by(self,) -> Optional[binary_operator.BinaryOperator]:
        """
        Gets the valuesJoinedBy property value. The valuesJoinedBy property
        Returns: Optional[binary_operator.BinaryOperator]
        """
        return self._values_joined_by
    
    @values_joined_by.setter
    def values_joined_by(self,value: Optional[binary_operator.BinaryOperator] = None) -> None:
        """
        Sets the valuesJoinedBy property value. The valuesJoinedBy property
        Args:
            value: Value to set for the values_joined_by property.
        """
        self._values_joined_by = value
    

