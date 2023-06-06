from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_mapping, filter, object_flow_types, object_mapping_metadata_entry

@dataclass
class ObjectMapping(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The attributeMappings property
    attribute_mappings: Optional[List[attribute_mapping.AttributeMapping]] = None
    # The enabled property
    enabled: Optional[bool] = None
    # The flowTypes property
    flow_types: Optional[object_flow_types.ObjectFlowTypes] = None
    # The metadata property
    metadata: Optional[List[object_mapping_metadata_entry.ObjectMappingMetadataEntry]] = None
    # The name property
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scope property
    scope: Optional[filter.Filter] = None
    # The sourceObjectName property
    source_object_name: Optional[str] = None
    # The targetObjectName property
    target_object_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ObjectMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ObjectMapping
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ObjectMapping()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_mapping, filter, object_flow_types, object_mapping_metadata_entry

        fields: Dict[str, Callable[[Any], None]] = {
            "attributeMappings": lambda n : setattr(self, 'attribute_mappings', n.get_collection_of_object_values(attribute_mapping.AttributeMapping)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "flowTypes": lambda n : setattr(self, 'flow_types', n.get_enum_value(object_flow_types.ObjectFlowTypes)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(object_mapping_metadata_entry.ObjectMappingMetadataEntry)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(filter.Filter)),
            "sourceObjectName": lambda n : setattr(self, 'source_object_name', n.get_str_value()),
            "targetObjectName": lambda n : setattr(self, 'target_object_name', n.get_str_value()),
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
        writer.write_collection_of_object_values("attributeMappings", self.attribute_mappings)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_enum_value("flowTypes", self.flow_types)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("scope", self.scope)
        writer.write_str_value("sourceObjectName", self.source_object_name)
        writer.write_str_value("targetObjectName", self.target_object_name)
        writer.write_additional_data_value(self.additional_data)
    

