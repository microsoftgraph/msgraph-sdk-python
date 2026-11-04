from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cross_tenant_migration_job_status import CrossTenantMigrationJobStatus
    from .cross_tenant_migration_job_type import CrossTenantMigrationJobType
    from .cross_tenant_migration_task import CrossTenantMigrationTask
    from .entity import Entity
    from .exchange_online_cross_tenant_migration_settings import ExchangeOnlineCrossTenantMigrationSettings

from .entity import Entity

@dataclass
class CrossTenantMigrationJob(Entity, Parsable):
    # Date and time after which the migration should be performed. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z.
    complete_after_date_time: Optional[datetime.datetime] = None
    # User principal name (UPN) of the user who created the job. Read-only.
    created_by: Optional[str] = None
    # When the job was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Display name of the job. Must be unique per tenant.
    display_name: Optional[str] = None
    # Settings to use for migration of Exchange workload. Nullable.
    exchange_settings: Optional[ExchangeOnlineCrossTenantMigrationSettings] = None
    # The jobType property
    job_type: Optional[CrossTenantMigrationJobType] = None
    # When this migration job was last updated. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2024, is 2024-01-01T00:00:00Z. Read-only.
    last_updated_date_time: Optional[datetime.datetime] = None
    # Status message of the migration job. Nullable. Read-only.
    message: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of resource being migrated. Only Users is currently supported.
    resource_type: Optional[str] = None
    # IDs (GUID) of the resources that are migrated with the migration job.
    resources: Optional[list[str]] = None
    # ID (GUID) of the source tenant for the content migration.
    source_tenant_id: Optional[str] = None
    # The status property
    status: Optional[CrossTenantMigrationJobStatus] = None
    # ID of the target tenant for the content migration. Read-only.
    target_tenant_id: Optional[str] = None
    # Details and status of the users migrated in this migration job.
    users: Optional[list[CrossTenantMigrationTask]] = None
    # Workloads to migrate. Supported workloads are Teams, Exchange, and ODSP (OneDrive/SharePoint).
    workloads: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CrossTenantMigrationJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantMigrationJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantMigrationJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cross_tenant_migration_job_status import CrossTenantMigrationJobStatus
        from .cross_tenant_migration_job_type import CrossTenantMigrationJobType
        from .cross_tenant_migration_task import CrossTenantMigrationTask
        from .entity import Entity
        from .exchange_online_cross_tenant_migration_settings import ExchangeOnlineCrossTenantMigrationSettings

        from .cross_tenant_migration_job_status import CrossTenantMigrationJobStatus
        from .cross_tenant_migration_job_type import CrossTenantMigrationJobType
        from .cross_tenant_migration_task import CrossTenantMigrationTask
        from .entity import Entity
        from .exchange_online_cross_tenant_migration_settings import ExchangeOnlineCrossTenantMigrationSettings

        fields: dict[str, Callable[[Any], None]] = {
            "completeAfterDateTime": lambda n : setattr(self, 'complete_after_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "exchangeSettings": lambda n : setattr(self, 'exchange_settings', n.get_object_value(ExchangeOnlineCrossTenantMigrationSettings)),
            "jobType": lambda n : setattr(self, 'job_type', n.get_enum_value(CrossTenantMigrationJobType)),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_str_value()),
            "resources": lambda n : setattr(self, 'resources', n.get_collection_of_primitive_values(str)),
            "sourceTenantId": lambda n : setattr(self, 'source_tenant_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CrossTenantMigrationJobStatus)),
            "targetTenantId": lambda n : setattr(self, 'target_tenant_id', n.get_str_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(CrossTenantMigrationTask)),
            "workloads": lambda n : setattr(self, 'workloads', n.get_collection_of_primitive_values(str)),
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
        writer.write_datetime_value("completeAfterDateTime", self.complete_after_date_time)
        writer.write_str_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("exchangeSettings", self.exchange_settings)
        writer.write_enum_value("jobType", self.job_type)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_str_value("message", self.message)
        writer.write_str_value("resourceType", self.resource_type)
        writer.write_collection_of_primitive_values("resources", self.resources)
        writer.write_str_value("sourceTenantId", self.source_tenant_id)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("targetTenantId", self.target_tenant_id)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_collection_of_primitive_values("workloads", self.workloads)
    

