from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_definition_metadata_entry, attribute_type, mutability, referenced_object, string_key_string_value_pair

@dataclass
class AttributeDefinition(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The anchor property
    anchor: Optional[bool] = None
    # The apiExpressions property
    api_expressions: Optional[List[string_key_string_value_pair.StringKeyStringValuePair]] = None
    # The caseExact property
    case_exact: Optional[bool] = None
    # The defaultValue property
    default_value: Optional[str] = None
    # The flowNullValues property
    flow_null_values: Optional[bool] = None
    # The metadata property
    metadata: Optional[List[attribute_definition_metadata_entry.AttributeDefinitionMetadataEntry]] = None
    # The multivalued property
    multivalued: Optional[bool] = None
    # The mutability property
    mutability: Optional[mutability.Mutability] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The referencedObjects property
    referenced_objects: Optional[List[referenced_object.ReferencedObject]] = None
    # The required property
    required: Optional[bool] = None
    # The type property
    type: Optional[attribute_type.AttributeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AttributeDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AttributeDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AttributeDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_definition_metadata_entry, attribute_type, mutability, referenced_object, string_key_string_value_pair

        fields: Dict[str, Callable[[Any], None]] = {
            "anchor": lambda n : setattr(self, 'anchor', n.get_bool_value()),
            "apiExpressions": lambda n : setattr(self, 'api_expressions', n.get_collection_of_object_values(string_key_string_value_pair.StringKeyStringValuePair)),
            "caseExact": lambda n : setattr(self, 'case_exact', n.get_bool_value()),
            "defaultValue": lambda n : setattr(self, 'default_value', n.get_str_value()),
            "flowNullValues": lambda n : setattr(self, 'flow_null_values', n.get_bool_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(attribute_definition_metadata_entry.AttributeDefinitionMetadataEntry)),
            "multivalued": lambda n : setattr(self, 'multivalued', n.get_bool_value()),
            "mutability": lambda n : setattr(self, 'mutability', n.get_enum_value(mutability.Mutability)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "referencedObjects": lambda n : setattr(self, 'referenced_objects', n.get_collection_of_object_values(referenced_object.ReferencedObject)),
            "required": lambda n : setattr(self, 'required', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(attribute_type.AttributeType)),
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
        writer.write_bool_value("anchor", self.anchor)
        writer.write_collection_of_object_values("apiExpressions", self.api_expressions)
        writer.write_bool_value("caseExact", self.case_exact)
        writer.write_str_value("defaultValue", self.default_value)
        writer.write_bool_value("flowNullValues", self.flow_null_values)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_bool_value("multivalued", self.multivalued)
        writer.write_enum_value("mutability", self.mutability)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("referencedObjects", self.referenced_objects)
        writer.write_bool_value("required", self.required)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

