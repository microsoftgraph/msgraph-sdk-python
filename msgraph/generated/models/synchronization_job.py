from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bulk_upload import BulkUpload
    from .entity import Entity
    from .key_value_pair import KeyValuePair
    from .synchronization_schedule import SynchronizationSchedule
    from .synchronization_schema import SynchronizationSchema
    from .synchronization_status import SynchronizationStatus

from .entity import Entity

@dataclass
class SynchronizationJob(Entity, Parsable):
    # The bulk upload operation for the job.
    bulk_upload: Optional[BulkUpload] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Schedule used to run the job. Read-only.
    schedule: Optional[SynchronizationSchedule] = None
    # The synchronization schema configured for the job.
    schema: Optional[SynchronizationSchema] = None
    # Status of the job, which includes when the job was last run, current job state, and errors.
    status: Optional[SynchronizationStatus] = None
    # Settings associated with the job. Some settings are inherited from the template.
    synchronization_job_settings: Optional[list[KeyValuePair]] = None
    # Identifier of the synchronization template this job is based on.
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SynchronizationJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SynchronizationJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .bulk_upload import BulkUpload
        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .synchronization_schedule import SynchronizationSchedule
        from .synchronization_schema import SynchronizationSchema
        from .synchronization_status import SynchronizationStatus

        from .bulk_upload import BulkUpload
        from .entity import Entity
        from .key_value_pair import KeyValuePair
        from .synchronization_schedule import SynchronizationSchedule
        from .synchronization_schema import SynchronizationSchema
        from .synchronization_status import SynchronizationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "bulkUpload": lambda n : setattr(self, 'bulk_upload', n.get_object_value(BulkUpload)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(SynchronizationSchedule)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(SynchronizationSchema)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(SynchronizationStatus)),
            "synchronizationJobSettings": lambda n : setattr(self, 'synchronization_job_settings', n.get_collection_of_object_values(KeyValuePair)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
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
        writer.write_object_value("bulkUpload", self.bulk_upload)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("schema", self.schema)
        writer.write_object_value("status", self.status)
        writer.write_collection_of_object_values("synchronizationJobSettings", self.synchronization_job_settings)
        writer.write_str_value("templateId", self.template_id)
    

