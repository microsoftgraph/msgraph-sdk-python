from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attribute_mapping import AttributeMapping
    from .filter import Filter
    from .object_flow_types import ObjectFlowTypes
    from .object_mapping_metadata_entry import ObjectMappingMetadataEntry

@dataclass
class ObjectMapping(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Attribute mappings define which attributes to map from the source object into the target object and how they should flow. A number of functions are available to support the transformation of the original source values.
    attribute_mappings: Optional[list[AttributeMapping]] = None
    # When true, this object mapping will be processed during synchronization. When false, this object mapping will be skipped.
    enabled: Optional[bool] = None
    # The flowTypes property
    flow_types: Optional[ObjectFlowTypes] = None
    # Additional extension properties. Unless mentioned explicitly, metadata values should not be changed.
    metadata: Optional[list[ObjectMappingMetadataEntry]] = None
    # Human-friendly name of the object mapping.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines a filter to be used when deciding whether a given object should be provisioned. For example, you might want to only provision users that are located in the US.
    scope: Optional[Filter] = None
    # Name of the object in the source directory. Must match the object name from the source directory definition.
    source_object_name: Optional[str] = None
    # Name of the object in target directory. Must match the object name from the target directory definition.
    target_object_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ObjectMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ObjectMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ObjectMapping()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attribute_mapping import AttributeMapping
        from .filter import Filter
        from .object_flow_types import ObjectFlowTypes
        from .object_mapping_metadata_entry import ObjectMappingMetadataEntry

        from .attribute_mapping import AttributeMapping
        from .filter import Filter
        from .object_flow_types import ObjectFlowTypes
        from .object_mapping_metadata_entry import ObjectMappingMetadataEntry

        fields: dict[str, Callable[[Any], None]] = {
            "attributeMappings": lambda n : setattr(self, 'attribute_mappings', n.get_collection_of_object_values(AttributeMapping)),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "flowTypes": lambda n : setattr(self, 'flow_types', n.get_collection_of_enum_values(ObjectFlowTypes)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(ObjectMappingMetadataEntry)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(Filter)),
            "sourceObjectName": lambda n : setattr(self, 'source_object_name', n.get_str_value()),
            "targetObjectName": lambda n : setattr(self, 'target_object_name', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
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
    

