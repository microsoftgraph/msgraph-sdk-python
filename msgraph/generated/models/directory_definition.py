from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_definition_discoverabilities import DirectoryDefinitionDiscoverabilities
    from .entity import Entity
    from .object_definition import ObjectDefinition

from .entity import Entity

@dataclass
class DirectoryDefinition(Entity, Parsable):
    # The discoverabilities property
    discoverabilities: Optional[DirectoryDefinitionDiscoverabilities] = None
    # Represents the discovery date and time using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    discovery_date_time: Optional[datetime.datetime] = None
    # Name of the directory. Must be unique within the synchronization schema. Not nullable.
    name: Optional[str] = None
    # Collection of objects supported by the directory.
    objects: Optional[list[ObjectDefinition]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Whether this object is read-only.
    read_only: Optional[bool] = None
    # Read only value that indicates version discovered. null if discovery hasn't yet occurred.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DirectoryDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DirectoryDefinition()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_definition_discoverabilities import DirectoryDefinitionDiscoverabilities
        from .entity import Entity
        from .object_definition import ObjectDefinition

        from .directory_definition_discoverabilities import DirectoryDefinitionDiscoverabilities
        from .entity import Entity
        from .object_definition import ObjectDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "discoverabilities": lambda n : setattr(self, 'discoverabilities', n.get_collection_of_enum_values(DirectoryDefinitionDiscoverabilities)),
            "discoveryDateTime": lambda n : setattr(self, 'discovery_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objects": lambda n : setattr(self, 'objects', n.get_collection_of_object_values(ObjectDefinition)),
            "readOnly": lambda n : setattr(self, 'read_only', n.get_bool_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("discoverabilities", self.discoverabilities)
        writer.write_datetime_value("discoveryDateTime", self.discovery_date_time)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("objects", self.objects)
        writer.write_bool_value("readOnly", self.read_only)
        writer.write_str_value("version", self.version)
    

