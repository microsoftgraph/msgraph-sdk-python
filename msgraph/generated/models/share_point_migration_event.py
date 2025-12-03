from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .share_point_migration_finish_manifest_file_upload_event import SharePointMigrationFinishManifestFileUploadEvent
    from .share_point_migration_job_cancelled_event import SharePointMigrationJobCancelledEvent
    from .share_point_migration_job_deleted_event import SharePointMigrationJobDeletedEvent
    from .share_point_migration_job_error_event import SharePointMigrationJobErrorEvent
    from .share_point_migration_job_postponed_event import SharePointMigrationJobPostponedEvent
    from .share_point_migration_job_progress_event import SharePointMigrationJobProgressEvent
    from .share_point_migration_job_queued_event import SharePointMigrationJobQueuedEvent
    from .share_point_migration_job_start_event import SharePointMigrationJobStartEvent

from .entity import Entity

@dataclass
class SharePointMigrationEvent(Entity, Parsable):
    # The correlation ID of a migration job. Read-only.
    correlation_id: Optional[str] = None
    # The date and time when the job status changes. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    event_date_time: Optional[datetime.datetime] = None
    # The unique identifier of a migration job. Read-only.
    job_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationFinishManifestFileUploadEvent".casefold():
            from .share_point_migration_finish_manifest_file_upload_event import SharePointMigrationFinishManifestFileUploadEvent

            return SharePointMigrationFinishManifestFileUploadEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobCancelledEvent".casefold():
            from .share_point_migration_job_cancelled_event import SharePointMigrationJobCancelledEvent

            return SharePointMigrationJobCancelledEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobDeletedEvent".casefold():
            from .share_point_migration_job_deleted_event import SharePointMigrationJobDeletedEvent

            return SharePointMigrationJobDeletedEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobErrorEvent".casefold():
            from .share_point_migration_job_error_event import SharePointMigrationJobErrorEvent

            return SharePointMigrationJobErrorEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobPostponedEvent".casefold():
            from .share_point_migration_job_postponed_event import SharePointMigrationJobPostponedEvent

            return SharePointMigrationJobPostponedEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobProgressEvent".casefold():
            from .share_point_migration_job_progress_event import SharePointMigrationJobProgressEvent

            return SharePointMigrationJobProgressEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobQueuedEvent".casefold():
            from .share_point_migration_job_queued_event import SharePointMigrationJobQueuedEvent

            return SharePointMigrationJobQueuedEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobStartEvent".casefold():
            from .share_point_migration_job_start_event import SharePointMigrationJobStartEvent

            return SharePointMigrationJobStartEvent()
        return SharePointMigrationEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .share_point_migration_finish_manifest_file_upload_event import SharePointMigrationFinishManifestFileUploadEvent
        from .share_point_migration_job_cancelled_event import SharePointMigrationJobCancelledEvent
        from .share_point_migration_job_deleted_event import SharePointMigrationJobDeletedEvent
        from .share_point_migration_job_error_event import SharePointMigrationJobErrorEvent
        from .share_point_migration_job_postponed_event import SharePointMigrationJobPostponedEvent
        from .share_point_migration_job_progress_event import SharePointMigrationJobProgressEvent
        from .share_point_migration_job_queued_event import SharePointMigrationJobQueuedEvent
        from .share_point_migration_job_start_event import SharePointMigrationJobStartEvent

        from .entity import Entity
        from .share_point_migration_finish_manifest_file_upload_event import SharePointMigrationFinishManifestFileUploadEvent
        from .share_point_migration_job_cancelled_event import SharePointMigrationJobCancelledEvent
        from .share_point_migration_job_deleted_event import SharePointMigrationJobDeletedEvent
        from .share_point_migration_job_error_event import SharePointMigrationJobErrorEvent
        from .share_point_migration_job_postponed_event import SharePointMigrationJobPostponedEvent
        from .share_point_migration_job_progress_event import SharePointMigrationJobProgressEvent
        from .share_point_migration_job_queued_event import SharePointMigrationJobQueuedEvent
        from .share_point_migration_job_start_event import SharePointMigrationJobStartEvent

        fields: dict[str, Callable[[Any], None]] = {
            "correlationId": lambda n : setattr(self, 'correlation_id', n.get_str_value()),
            "eventDateTime": lambda n : setattr(self, 'event_date_time', n.get_datetime_value()),
            "jobId": lambda n : setattr(self, 'job_id', n.get_str_value()),
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
        writer.write_str_value("correlationId", self.correlation_id)
        writer.write_datetime_value("eventDateTime", self.event_date_time)
        writer.write_str_value("jobId", self.job_id)
    

