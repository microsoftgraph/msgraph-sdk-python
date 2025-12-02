from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .share_point_migration_event import SharePointMigrationEvent

from .share_point_migration_event import SharePointMigrationEvent

@dataclass
class SharePointMigrationJobProgressEvent(SharePointMigrationEvent, Parsable):
    # The number of bytes processed. Read-only.
    bytes_processed: Optional[int] = None
    # The number of bytes processed with version history excluded. Read-only.
    bytes_processed_only_current_version: Optional[int] = None
    # CPU duration in milliseconds. Read-only.
    cpu_duration_ms: Optional[int] = None
    # The number of files processed. Read-only.
    files_processed: Optional[int] = None
    # The number of files processed with version history excluded. Read-only.
    files_processed_only_current_version: Optional[int] = None
    # True if the job status is End. False if the job is In progress. Read-only.
    is_completed: Optional[bool] = None
    # The unique identifier of the last object processed. Read-only.
    last_processed_object_id: Optional[str] = None
    # The number of objects processed. Read-only.
    objects_processed: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # SQL duration in milliseconds. Read-only.
    sql_duration_ms: Optional[int] = None
    # SQL query count. Read-only.
    sql_query_count: Optional[int] = None
    # Total duration time in milliseconds. Read-only.
    total_duration_ms: Optional[int] = None
    # Total errors. Read-only.
    total_errors: Optional[int] = None
    # Total bytes to be processed. Read-only.
    total_expected_bytes: Optional[int] = None
    # The number of objects to process. Read-only.
    total_expected_objects: Optional[int] = None
    # The current retry count of the job. Read-only.
    total_retry_count: Optional[int] = None
    # Total warnings. Read-only.
    total_warnings: Optional[int] = None
    # Waiting time due to SQL throttling, in milliseconds. Read-only.
    wait_time_on_sql_throttling_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationJobProgressEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationJobProgressEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointMigrationJobProgressEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .share_point_migration_event import SharePointMigrationEvent

        from .share_point_migration_event import SharePointMigrationEvent

        fields: dict[str, Callable[[Any], None]] = {
            "bytesProcessed": lambda n : setattr(self, 'bytes_processed', n.get_int_value()),
            "bytesProcessedOnlyCurrentVersion": lambda n : setattr(self, 'bytes_processed_only_current_version', n.get_int_value()),
            "cpuDurationMs": lambda n : setattr(self, 'cpu_duration_ms', n.get_int_value()),
            "filesProcessed": lambda n : setattr(self, 'files_processed', n.get_int_value()),
            "filesProcessedOnlyCurrentVersion": lambda n : setattr(self, 'files_processed_only_current_version', n.get_int_value()),
            "isCompleted": lambda n : setattr(self, 'is_completed', n.get_bool_value()),
            "lastProcessedObjectId": lambda n : setattr(self, 'last_processed_object_id', n.get_str_value()),
            "objectsProcessed": lambda n : setattr(self, 'objects_processed', n.get_int_value()),
            "sqlDurationMs": lambda n : setattr(self, 'sql_duration_ms', n.get_int_value()),
            "sqlQueryCount": lambda n : setattr(self, 'sql_query_count', n.get_int_value()),
            "totalDurationMs": lambda n : setattr(self, 'total_duration_ms', n.get_int_value()),
            "totalErrors": lambda n : setattr(self, 'total_errors', n.get_int_value()),
            "totalExpectedBytes": lambda n : setattr(self, 'total_expected_bytes', n.get_int_value()),
            "totalExpectedObjects": lambda n : setattr(self, 'total_expected_objects', n.get_int_value()),
            "totalRetryCount": lambda n : setattr(self, 'total_retry_count', n.get_int_value()),
            "totalWarnings": lambda n : setattr(self, 'total_warnings', n.get_int_value()),
            "waitTimeOnSqlThrottlingMs": lambda n : setattr(self, 'wait_time_on_sql_throttling_ms', n.get_int_value()),
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
        writer.write_int_value("bytesProcessed", self.bytes_processed)
        writer.write_int_value("bytesProcessedOnlyCurrentVersion", self.bytes_processed_only_current_version)
        writer.write_int_value("cpuDurationMs", self.cpu_duration_ms)
        writer.write_int_value("filesProcessed", self.files_processed)
        writer.write_int_value("filesProcessedOnlyCurrentVersion", self.files_processed_only_current_version)
        writer.write_bool_value("isCompleted", self.is_completed)
        writer.write_str_value("lastProcessedObjectId", self.last_processed_object_id)
        writer.write_int_value("objectsProcessed", self.objects_processed)
        writer.write_int_value("sqlDurationMs", self.sql_duration_ms)
        writer.write_int_value("sqlQueryCount", self.sql_query_count)
        writer.write_int_value("totalDurationMs", self.total_duration_ms)
        writer.write_int_value("totalErrors", self.total_errors)
        writer.write_int_value("totalExpectedBytes", self.total_expected_bytes)
        writer.write_int_value("totalExpectedObjects", self.total_expected_objects)
        writer.write_int_value("totalRetryCount", self.total_retry_count)
        writer.write_int_value("totalWarnings", self.total_warnings)
        writer.write_int_value("waitTimeOnSqlThrottlingMs", self.wait_time_on_sql_throttling_ms)
    

