from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .recovery_job_base import RecoveryJobBase

from .recovery_job_base import RecoveryJobBase

@dataclass
class RecoveryJob(RecoveryJobBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.entraRecoveryServices.recoveryJob"
    # The count of changes (including both objects and links) that failed to apply during recovery.
    total_failed_changes: Optional[int] = None
    # The count of directory object links (relationships) that were successfully modified during recovery. This value may be less than totalChangedLinksCalculated if some link changes failed.
    total_links_modified: Optional[int] = None
    # The count of directory objects that were successfully modified during recovery. This value may be less than totalChangedObjectsCalculated if some object changes failed.
    total_objects_modified: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RecoveryJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RecoveryJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RecoveryJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .recovery_job_base import RecoveryJobBase

        from .recovery_job_base import RecoveryJobBase

        fields: dict[str, Callable[[Any], None]] = {
            "totalFailedChanges": lambda n : setattr(self, 'total_failed_changes', n.get_int_value()),
            "totalLinksModified": lambda n : setattr(self, 'total_links_modified', n.get_int_value()),
            "totalObjectsModified": lambda n : setattr(self, 'total_objects_modified', n.get_int_value()),
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
        writer.write_int_value("totalFailedChanges", self.total_failed_changes)
        writer.write_int_value("totalLinksModified", self.total_links_modified)
        writer.write_int_value("totalObjectsModified", self.total_objects_modified)
    

