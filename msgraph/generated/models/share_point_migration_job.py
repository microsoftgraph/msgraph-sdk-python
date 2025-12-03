from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .share_point_migration_container_info import SharePointMigrationContainerInfo
    from .share_point_migration_event import SharePointMigrationEvent

from .entity import Entity

@dataclass
class SharePointMigrationJob(Entity, Parsable):
    # The containerInfo property
    container_info: Optional[SharePointMigrationContainerInfo] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of migration events that reflects the job status changes.
    progress_events: Optional[list[SharePointMigrationEvent]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointMigrationJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .share_point_migration_container_info import SharePointMigrationContainerInfo
        from .share_point_migration_event import SharePointMigrationEvent

        from .entity import Entity
        from .share_point_migration_container_info import SharePointMigrationContainerInfo
        from .share_point_migration_event import SharePointMigrationEvent

        fields: dict[str, Callable[[Any], None]] = {
            "containerInfo": lambda n : setattr(self, 'container_info', n.get_object_value(SharePointMigrationContainerInfo)),
            "progressEvents": lambda n : setattr(self, 'progress_events', n.get_collection_of_object_values(SharePointMigrationEvent)),
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
        writer.write_object_value("containerInfo", self.container_info)
        writer.write_collection_of_object_values("progressEvents", self.progress_events)
    

