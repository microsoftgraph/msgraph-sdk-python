from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .snapshot_job_status import SnapshotJobStatus

from .entity import Entity

@dataclass
class ConfigurationSnapshotJob(Entity, Parsable):
    # The date and time when the snapshot job was completed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, ge, le) and $orderby.
    completed_date_time: Optional[datetime.datetime] = None
    # The createdBy property
    created_by: Optional[IdentitySet] = None
    # The date and time when the snapshot job was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Supports $filter (eq, ne, ge, le) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # User-friendly description of the snapshot given by the user. Supports $filter (eq, ne, startsWith) and $orderby.
    description: Optional[str] = None
    # User-friendly name provided by the user during snapshot creation. Supports $filter (eq, ne, startsWith) and $orderby.
    display_name: Optional[str] = None
    # Details of errors related to the reasons why the snapshot can't complete. Returned only on $select.
    error_details: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL at which the snapshot file resides. Returned only on $select.
    resource_location: Optional[str] = None
    # The names of all resources included in the request body by the user who created the snapshot. Fetched by the system. Returned only on $select.
    resources: Optional[list[str]] = None
    # The status property
    status: Optional[SnapshotJobStatus] = None
    # Globally unique identifier (GUID) of the tenant for which the snapshot is created. Supports $filter (eq, ne).
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationSnapshotJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationSnapshotJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationSnapshotJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .snapshot_job_status import SnapshotJobStatus

        from .entity import Entity
        from .identity_set import IdentitySet
        from .snapshot_job_status import SnapshotJobStatus

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "errorDetails": lambda n : setattr(self, 'error_details', n.get_collection_of_primitive_values(str)),
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_primitive_values(str)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SnapshotJobStatus)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_primitive_values("resources", self.resources)
        writer.write_enum_value("status", self.status)
    

