from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .file_storage_container import FileStorageContainer

from .entity import Entity

@dataclass
class FileStorage(Entity):
    # The containers property
    containers: Optional[List[FileStorageContainer]] = None
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .file_storage_container import FileStorageContainer

        from .entity import Entity
        from .file_storage_container import FileStorageContainer

        fields: Dict[str, Callable[[Any], None]] = {
            "containers": lambda n : setattr(self, 'containers', n.get_collection_of_object_values(FileStorageContainer)),
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
        writer.write_collection_of_object_values("containers", self.containers)
    

