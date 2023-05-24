from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import entity, synchronization_metadata_entry, synchronization_schema

from . import entity

class SynchronizationTemplate(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationTemplate and sets the default values.
        """
        super().__init__()
        # The applicationId property
        self._application_id: Optional[UUID] = None
        # The default property
        self._default: Optional[bool] = None
        # The description property
        self._description: Optional[str] = None
        # The discoverable property
        self._discoverable: Optional[bool] = None
        # The factoryTag property
        self._factory_tag: Optional[str] = None
        # The metadata property
        self._metadata: Optional[List[synchronization_metadata_entry.SynchronizationMetadataEntry]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The schema property
        self._schema: Optional[synchronization_schema.SynchronizationSchema] = None
    
    @property
    def application_id(self,) -> Optional[UUID]:
        """
        Gets the applicationId property value. The applicationId property
        Returns: Optional[UUID]
        """
        return self._application_id
    
    @application_id.setter
    def application_id(self,value: Optional[UUID] = None) -> None:
        """
        Sets the applicationId property value. The applicationId property
        Args:
            value: Value to set for the application_id property.
        """
        self._application_id = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationTemplate
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationTemplate()
    
    @property
    def default(self,) -> Optional[bool]:
        """
        Gets the default property value. The default property
        Returns: Optional[bool]
        """
        return self._default
    
    @default.setter
    def default(self,value: Optional[bool] = None) -> None:
        """
        Sets the default property value. The default property
        Args:
            value: Value to set for the default property.
        """
        self._default = value
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def discoverable(self,) -> Optional[bool]:
        """
        Gets the discoverable property value. The discoverable property
        Returns: Optional[bool]
        """
        return self._discoverable
    
    @discoverable.setter
    def discoverable(self,value: Optional[bool] = None) -> None:
        """
        Sets the discoverable property value. The discoverable property
        Args:
            value: Value to set for the discoverable property.
        """
        self._discoverable = value
    
    @property
    def factory_tag(self,) -> Optional[str]:
        """
        Gets the factoryTag property value. The factoryTag property
        Returns: Optional[str]
        """
        return self._factory_tag
    
    @factory_tag.setter
    def factory_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the factoryTag property value. The factoryTag property
        Args:
            value: Value to set for the factory_tag property.
        """
        self._factory_tag = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
    
    @property
    def metadata(self,) -> Optional[List[synchronization_metadata_entry.SynchronizationMetadataEntry]]:
        """
        Gets the metadata property value. The metadata property
        Returns: Optional[List[synchronization_metadata_entry.SynchronizationMetadataEntry]]
        """
        return self._metadata
    
    @metadata.setter
    def metadata(self,value: Optional[List[synchronization_metadata_entry.SynchronizationMetadataEntry]] = None) -> None:
        """
        Sets the metadata property value. The metadata property
        Args:
            value: Value to set for the metadata property.
        """
        self._metadata = value
    
    @property
    def schema(self,) -> Optional[synchronization_schema.SynchronizationSchema]:
        """
        Gets the schema property value. The schema property
        Returns: Optional[synchronization_schema.SynchronizationSchema]
        """
        return self._schema
    
    @schema.setter
    def schema(self,value: Optional[synchronization_schema.SynchronizationSchema] = None) -> None:
        """
        Sets the schema property value. The schema property
        Args:
            value: Value to set for the schema property.
        """
        self._schema = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_uuid_value("applicationId", self.application_id)
        writer.write_bool_value("default", self.default)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("discoverable", self.discoverable)
        writer.write_str_value("factoryTag", self.factory_tag)
        writer.write_collection_of_object_values("metadata", self.metadata)
        writer.write_object_value("schema", self.schema)
    

