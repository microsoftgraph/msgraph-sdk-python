from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_definition import AttributeDefinition
    from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

@dataclass
class ObjectDefinition(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The attributes property
    attributes: Optional[List[AttributeDefinition]] = None
    # The metadata property
    metadata: Optional[List[ObjectDefinitionMetadataEntry]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The supportedApis property
    supported_apis: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ObjectDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObjectDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ObjectDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_definition import AttributeDefinition
        from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

        from .attribute_definition import AttributeDefinition
        from .object_definition_metadata_entry import ObjectDefinitionMetadataEntry

        fields: Dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_collection_of_object_values(AttributeDefinition)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(ObjectDefinitionMetadataEntry)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "supportedApis": lambda n : setattr(self, 'supported_apis', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_object_values("attributes", self.attributes)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_primitive_values("supportedApis", self.supported_apis)
        writer.write_additional_data_value(self.additional_data)
    

