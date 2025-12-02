from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .share_point_migration_event import SharePointMigrationEvent

from .share_point_migration_event import SharePointMigrationEvent

@dataclass
class SharePointMigrationJobPostponedEvent(SharePointMigrationEvent, Parsable):
    # The number of migration jobs in the queue of the current database. Read-only.
    jobs_in_queue: Optional[int] = None
    # The date and time that indicate when this job is picked up next. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    next_pickup_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The reason for the postponement. Read-only.
    reason: Optional[str] = None
    # The current retry count of the job. Read-only.
    total_retry_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationJobPostponedEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationJobPostponedEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointMigrationJobPostponedEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .share_point_migration_event import SharePointMigrationEvent

        from .share_point_migration_event import SharePointMigrationEvent

        fields: dict[str, Callable[[Any], None]] = {
            "jobsInQueue": lambda n : setattr(self, 'jobs_in_queue', n.get_int_value()),
            "nextPickupDateTime": lambda n : setattr(self, 'next_pickup_date_time', n.get_datetime_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "totalRetryCount": lambda n : setattr(self, 'total_retry_count', n.get_int_value()),
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
        writer.write_int_value("jobsInQueue", self.jobs_in_queue)
        writer.write_datetime_value("nextPickupDateTime", self.next_pickup_date_time)
        writer.write_str_value("reason", self.reason)
        writer.write_int_value("totalRetryCount", self.total_retry_count)
    

