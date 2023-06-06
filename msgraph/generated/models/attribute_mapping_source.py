from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_mapping_source_type, string_key_attribute_mapping_source_value_pair

@dataclass
class AttributeMappingSource(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The expression property
    expression: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parameters property
    parameters: Optional[List[string_key_attribute_mapping_source_value_pair.StringKeyAttributeMappingSourceValuePair]] = None
    # The type property
    type: Optional[attribute_mapping_source_type.AttributeMappingSourceType] = None
    
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
    

