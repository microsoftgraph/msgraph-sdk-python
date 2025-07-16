from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_definition import DirectoryDefinition
    from .entity import Entity
    from .synchronization_rule import SynchronizationRule

from .entity import Entity

@dataclass
class SynchronizationSchema(Entity, Parsable):
    # Contains the collection of directories and all of their objects.
    directories: Optional[list[DirectoryDefinition]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of synchronization rules configured for the synchronizationJob or synchronizationTemplate.
    synchronization_rules: Optional[list[SynchronizationRule]] = None
    # The version of the schema, updated automatically with every schema change.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationSchema
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationSchema()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_definition import DirectoryDefinition
        from .entity import Entity
        from .synchronization_rule import SynchronizationRule

        from .directory_definition import DirectoryDefinition
        from .entity import Entity
        from .synchronization_rule import SynchronizationRule

        fields: dict[str, Callable[[Any], None]] = {
            "directories": lambda n : setattr(self, 'directories', n.get_collection_of_object_values(DirectoryDefinition)),
            "synchronizationRules": lambda n : setattr(self, 'synchronization_rules', n.get_collection_of_object_values(SynchronizationRule)),
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
        writer.write_collection_of_object_values("directories", self.directories)
        writer.write_collection_of_object_values("synchronizationRules", self.synchronization_rules)
        writer.write_str_value("version", self.version)
    

