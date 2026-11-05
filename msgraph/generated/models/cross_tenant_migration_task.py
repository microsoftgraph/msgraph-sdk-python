from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_migration_service_status_details import CrossTenantMigrationServiceStatusDetails
    from .entity import Entity

from .entity import Entity

@dataclass
class CrossTenantMigrationTask(Entity, Parsable):
    # Most recent status of this migration task.
    current_status: Optional[list[CrossTenantMigrationServiceStatusDetails]] = None
    # Date and time when the task was last updated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of migration task. Currently, only Users is supported.
    task_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantMigrationTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantMigrationTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantMigrationTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_migration_service_status_details import CrossTenantMigrationServiceStatusDetails
        from .entity import Entity

        from .cross_tenant_migration_service_status_details import CrossTenantMigrationServiceStatusDetails
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "currentStatus": lambda n : setattr(self, 'current_status', n.get_collection_of_object_values(CrossTenantMigrationServiceStatusDetails)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "taskType": lambda n : setattr(self, 'task_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("currentStatus", self.current_status)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("taskType", self.task_type)
    

