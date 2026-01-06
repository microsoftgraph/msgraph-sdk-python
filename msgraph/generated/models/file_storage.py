from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .file_storage_container import FileStorageContainer
    from .file_storage_container_type import FileStorageContainerType
    from .file_storage_container_type_registration import FileStorageContainerTypeRegistration

from .entity import Entity

@dataclass
class FileStorage(Entity, Parsable):
    # The collection of fileStorageContainerTypeRegistration resources.
    container_type_registrations: Optional[list[FileStorageContainerTypeRegistration]] = None
    # The collection of fileStorageContainerType resources.
    container_types: Optional[list[FileStorageContainerType]] = None
    # The collection of active fileStorageContainer resources.
    containers: Optional[list[FileStorageContainer]] = None
    # The collection of deleted fileStorageContainer resources.
    deleted_containers: Optional[list[FileStorageContainer]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileStorage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileStorage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileStorage()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .file_storage_container import FileStorageContainer
        from .file_storage_container_type import FileStorageContainerType
        from .file_storage_container_type_registration import FileStorageContainerTypeRegistration

        from .entity import Entity
        from .file_storage_container import FileStorageContainer
        from .file_storage_container_type import FileStorageContainerType
        from .file_storage_container_type_registration import FileStorageContainerTypeRegistration

        fields: dict[str, Callable[[Any], None]] = {
            "containerTypeRegistrations": lambda n : setattr(self, 'container_type_registrations', n.get_collection_of_object_values(FileStorageContainerTypeRegistration)),
            "containerTypes": lambda n : setattr(self, 'container_types', n.get_collection_of_object_values(FileStorageContainerType)),
            "containers": lambda n : setattr(self, 'containers', n.get_collection_of_object_values(FileStorageContainer)),
            "deletedContainers": lambda n : setattr(self, 'deleted_containers', n.get_collection_of_object_values(FileStorageContainer)),
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
        writer.write_collection_of_object_values("containerTypeRegistrations", self.container_type_registrations)
        writer.write_collection_of_object_values("containerTypes", self.container_types)
        writer.write_collection_of_object_values("containers", self.containers)
        writer.write_collection_of_object_values("deletedContainers", self.deleted_containers)
    

