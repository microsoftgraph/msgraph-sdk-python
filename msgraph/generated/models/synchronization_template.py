from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, synchronization_metadata_entry, synchronization_schema

from . import entity

@dataclass
class SynchronizationTemplate(entity.Entity):
    # The applicationId property
    application_id: Optional[UUID] = None
    # The default property
    default: Optional[bool] = None
    # The description property
    description: Optional[str] = None
    # The discoverable property
    discoverable: Optional[bool] = None
    # The factoryTag property
    factory_tag: Optional[str] = None
    # The metadata property
    metadata: Optional[List[synchronization_metadata_entry.SynchronizationMetadataEntry]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The schema property
    schema: Optional[synchronization_schema.SynchronizationSchema] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationTemplate
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, synchronization_metadata_entry, synchronization_schema

        from . import entity, synchronization_metadata_entry, synchronization_schema

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationId": lambda n : setattr(self, 'application_id', n.get_uuid_value()),
            "default": lambda n : setattr(self, 'default', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "discoverable": lambda n : setattr(self, 'discoverable', n.get_bool_value()),
            "factoryTag": lambda n : setattr(self, 'factory_tag', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_collection_of_object_values(synchronization_metadata_entry.SynchronizationMetadataEntry)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(synchronization_schema.SynchronizationSchema)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_uuid_value("applicationId", self.application_id)
        writer.write_bool_value("default", self.default)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("discoverable", self.discoverable)
        writer.write_str_value("factoryTag", self.factory_tag)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_object_value("schema", self.schema)
    

