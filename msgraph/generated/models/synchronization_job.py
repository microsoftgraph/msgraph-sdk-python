from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, key_value_pair, synchronization_schedule, synchronization_schema, synchronization_status

from . import entity

@dataclass
class SynchronizationJob(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    # The schedule property
    schedule: Optional[synchronization_schedule.SynchronizationSchedule] = None
    # The schema property
    schema: Optional[synchronization_schema.SynchronizationSchema] = None
    # The status property
    status: Optional[synchronization_status.SynchronizationStatus] = None
    # The synchronizationJobSettings property
    synchronization_job_settings: Optional[List[key_value_pair.KeyValuePair]] = None
    # The templateId property
    template_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationJob
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationJob()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, key_value_pair, synchronization_schedule, synchronization_schema, synchronization_status

        fields: Dict[str, Callable[[Any], None]] = {
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(synchronization_schedule.SynchronizationSchedule)),
            "schema": lambda n : setattr(self, 'schema', n.get_object_value(synchronization_schema.SynchronizationSchema)),
            "status": lambda n : setattr(self, 'status', n.get_object_value(synchronization_status.SynchronizationStatus)),
            "synchronizationJobSettings": lambda n : setattr(self, 'synchronization_job_settings', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "templateId": lambda n : setattr(self, 'template_id', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("schedule", self.schedule)
        writer.write_object_value("schema", self.schema)
        writer.write_object_value("status", self.status)
        writer.write_collection_of_object_values("synchronizationJobSettings", self.synchronization_job_settings)
        writer.write_str_value("templateId", self.template_id)
    

