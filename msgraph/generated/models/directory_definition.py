from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_definition_discoverabilities, entity, object_definition

from . import entity

@dataclass
class DirectoryDefinition(entity.Entity):
    # The discoverabilities property
    discoverabilities: Optional[directory_definition_discoverabilities.DirectoryDefinitionDiscoverabilities] = None
    # The discoveryDateTime property
    discovery_date_time: Optional[datetime] = None
    # The name property
    name: Optional[str] = None
    # The objects property
    objects: Optional[List[object_definition.ObjectDefinition]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The readOnly property
    read_only: Optional[bool] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DirectoryDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DirectoryDefinition
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DirectoryDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_definition_discoverabilities, entity, object_definition

        from . import directory_definition_discoverabilities, entity, object_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "discoverabilities": lambda n : setattr(self, 'discoverabilities', n.get_enum_value(directory_definition_discoverabilities.DirectoryDefinitionDiscoverabilities)),
            "discoveryDateTime": lambda n : setattr(self, 'discovery_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objects": lambda n : setattr(self, 'objects', n.get_collection_of_object_values(object_definition.ObjectDefinition)),
            "readOnly": lambda n : setattr(self, 'read_only', n.get_bool_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_enum_value("discoverabilities", self.discoverabilities)
        writer.write_datetime_value("discoveryDateTime", self.discovery_date_time)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("objects", self.objects)
        writer.write_bool_value("readOnly", self.read_only)
        writer.write_str_value("version", self.version)
    

