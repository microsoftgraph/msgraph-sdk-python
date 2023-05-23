from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_mapping_source_type, string_key_attribute_mapping_source_value_pair

class AttributeMappingSource(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new attributeMappingSource and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The expression property
        self._expression: Optional[str] = None
        # The name property
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The parameters property
        self._parameters: Optional[List[string_key_attribute_mapping_source_value_pair.StringKeyAttributeMappingSourceValuePair]] = None
        # The type property
        self._type: Optional[attribute_mapping_source_type.AttributeMappingSourceType] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeMappingSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeMappingSource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeMappingSource()
    
    @property
    def expression(self,) -> Optional[str]:
        """
        Gets the expression property value. The expression property
        Returns: Optional[str]
        """
        return self._expression
    
    @expression.setter
    def expression(self,value: Optional[str] = None) -> None:
        """
        Sets the expression property value. The expression property
        Args:
            value: Value to set for the expression property.
        """
        self._expression = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_mapping_source_type, string_key_attribute_mapping_source_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "expression": lambda n : setattr(self, 'expression', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(string_key_attribute_mapping_source_value_pair.StringKeyAttributeMappingSourceValuePair)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(attribute_mapping_source_type.AttributeMappingSourceType)),
        }
        return fields
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
    def parameters(self,) -> Optional[List[string_key_attribute_mapping_source_value_pair.StringKeyAttributeMappingSourceValuePair]]:
        """
        Gets the parameters property value. The parameters property
        Returns: Optional[List[string_key_attribute_mapping_source_value_pair.StringKeyAttributeMappingSourceValuePair]]
        """
        return self._parameters
    
    @parameters.setter
    def parameters(self,value: Optional[List[string_key_attribute_mapping_source_value_pair.StringKeyAttributeMappingSourceValuePair]] = None) -> None:
        """
        Sets the parameters property value. The parameters property
        Args:
            value: Value to set for the parameters property.
        """
        self._parameters = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("expression", self.expression)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[attribute_mapping_source_type.AttributeMappingSourceType]:
        """
        Gets the type property value. The type property
        Returns: Optional[attribute_mapping_source_type.AttributeMappingSourceType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[attribute_mapping_source_type.AttributeMappingSourceType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

