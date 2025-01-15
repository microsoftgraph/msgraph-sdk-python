from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .container_filter import ContainerFilter
    from .group_filter import GroupFilter
    from .object_mapping import ObjectMapping
    from .string_key_string_value_pair import StringKeyStringValuePair

@dataclass
class SynchronizationRule(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The containerFilter property
    container_filter: Optional[ContainerFilter] = None
    # true if the synchronization rule can be customized; false if this rule is read-only and shouldn't be changed.
    editable: Optional[bool] = None
    # The groupFilter property
    group_filter: Optional[GroupFilter] = None
    # Synchronization rule identifier. Must be one of the identifiers recognized by the synchronization engine. Supported rule identifiers can be found in the synchronization template returned by the API.
    id: Optional[str] = None
    # Additional extension properties. Unless instructed explicitly by the support team, metadata values shouldn't be changed.
    metadata: Optional[list[StringKeyStringValuePair]] = None
    # Human-readable name of the synchronization rule. Not nullable.
    name: Optional[str] = None
    # Collection of object mappings supported by the rule. Tells the synchronization engine which objects should be synchronized.
    object_mappings: Optional[list[ObjectMapping]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Priority relative to other rules in the synchronizationSchema. Rules with the lowest priority number will be processed first.
    priority: Optional[int] = None
    # Name of the source directory. Must match one of the directory definitions in synchronizationSchema.
    source_directory_name: Optional[str] = None
    # Name of the target directory. Must match one of the directory definitions in synchronizationSchema.
    target_directory_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationRule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationRule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationRule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .container_filter import ContainerFilter
        from .group_filter import GroupFilter
        from .object_mapping import ObjectMapping
        from .string_key_string_value_pair import StringKeyStringValuePair

        from .container_filter import ContainerFilter
        from .group_filter import GroupFilter
        from .object_mapping import ObjectMapping
        from .string_key_string_value_pair import StringKeyStringValuePair

        fields: dict[str, Callable[[Any], None]] = {
            "containerFilter": lambda n : setattr(self, 'container_filter', n.get_object_value(ContainerFilter)),
            "editable": lambda n : setattr(self, 'editable', n.get_bool_value()),
            "groupFilter": lambda n : setattr(self, 'group_filter', n.get_object_value(GroupFilter)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(StringKeyStringValuePair)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objectMappings": lambda n : setattr(self, 'object_mappings', n.get_collection_of_object_values(ObjectMapping)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "sourceDirectoryName": lambda n : setattr(self, 'source_directory_name', n.get_str_value()),
            "targetDirectoryName": lambda n : setattr(self, 'target_directory_name', n.get_str_value()),
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
        writer.write_object_value("containerFilter", self.container_filter)
        writer.write_bool_value("editable", self.editable)
        writer.write_object_value("groupFilter", self.group_filter)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("objectMappings", self.object_mappings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("sourceDirectoryName", self.source_directory_name)
        writer.write_str_value("targetDirectoryName", self.target_directory_name)
        writer.write_additional_data_value(self.additional_data)
    

