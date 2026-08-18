from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .recovery_job_base import RecoveryJobBase
    from .snapshot import Snapshot

from ..entity import Entity

@dataclass
class Recovery(Entity, Parsable):
    # Collection of all recovery jobs (both preview and recovery) for the tenant.
    jobs: Optional[list[RecoveryJobBase]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Collection of backup snapshots available for the tenant.
    snapshots: Optional[list[Snapshot]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Recovery:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Recovery
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Recovery()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .recovery_job_base import RecoveryJobBase
        from .snapshot import Snapshot

        from ..entity import Entity
        from .recovery_job_base import RecoveryJobBase
        from .snapshot import Snapshot

        fields: dict[str, Callable[[Any], None]] = {
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(RecoveryJobBase)),
            "snapshots": lambda n : setattr(self, 'snapshots', n.get_collection_of_object_values(Snapshot)),
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
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_collection_of_object_values("snapshots", self.snapshots)
    

