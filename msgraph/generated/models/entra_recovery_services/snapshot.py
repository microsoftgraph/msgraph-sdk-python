from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .recovery_job import RecoveryJob
    from .recovery_preview_job import RecoveryPreviewJob

from ..entity import Entity

@dataclass
class Snapshot(Entity, Parsable):
    # The date and time when the snapshot was created.
    created_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of recovery jobs created for this snapshot.
    recovery_jobs: Optional[list[RecoveryJob]] = None
    # Collection of preview jobs created for this snapshot.
    recovery_preview_jobs: Optional[list[RecoveryPreviewJob]] = None
    # The total number of changed objects identified in this snapshot.
    total_changed_objects: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Snapshot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Snapshot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Snapshot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .recovery_job import RecoveryJob
        from .recovery_preview_job import RecoveryPreviewJob

        from ..entity import Entity
        from .recovery_job import RecoveryJob
        from .recovery_preview_job import RecoveryPreviewJob

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "recoveryJobs": lambda n : setattr(self, 'recovery_jobs', n.get_collection_of_object_values(RecoveryJob)),
            "recoveryPreviewJobs": lambda n : setattr(self, 'recovery_preview_jobs', n.get_collection_of_object_values(RecoveryPreviewJob)),
            "totalChangedObjects": lambda n : setattr(self, 'total_changed_objects', n.get_int_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("recoveryJobs", self.recovery_jobs)
        writer.write_collection_of_object_values("recoveryPreviewJobs", self.recovery_preview_jobs)
        writer.write_int_value("totalChangedObjects", self.total_changed_objects)
    

