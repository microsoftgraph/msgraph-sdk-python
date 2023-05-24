from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, key_value_pair, synchronization_schedule, synchronization_schema, synchronization_status

from . import entity

class SynchronizationJob(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationJob and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The schedule property
        self._schedule: Optional[synchronization_schedule.SynchronizationSchedule] = None
        # The schema property
        self._schema: Optional[synchronization_schema.SynchronizationSchema] = None
        # The status property
        self._status: Optional[synchronization_status.SynchronizationStatus] = None
        # The synchronizationJobSettings property
        self._synchronization_job_settings: Optional[List[key_value_pair.KeyValuePair]] = None
        # The templateId property
        self._template_id: Optional[str] = None
    
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
    
    @property
    def schedule(self,) -> Optional[synchronization_schedule.SynchronizationSchedule]:
        """
        Gets the schedule property value. The schedule property
        Returns: Optional[synchronization_schedule.SynchronizationSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[synchronization_schedule.SynchronizationSchedule] = None) -> None:
        """
        Sets the schedule property value. The schedule property
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    @property
    def schema(self,) -> Optional[synchronization_schema.SynchronizationSchema]:
        """
        Gets the schema property value. The schema property
        Returns: Optional[synchronization_schema.SynchronizationSchema]
        """
        return self._schema
    
    @schema.setter
    def schema(self,value: Optional[synchronization_schema.SynchronizationSchema] = None) -> None:
        """
        Sets the schema property value. The schema property
        Args:
            value: Value to set for the schema property.
        """
        self._schema = value
    
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
    
    @property
    def status(self,) -> Optional[synchronization_status.SynchronizationStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[synchronization_status.SynchronizationStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[synchronization_status.SynchronizationStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def synchronization_job_settings(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the synchronizationJobSettings property value. The synchronizationJobSettings property
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._synchronization_job_settings
    
    @synchronization_job_settings.setter
    def synchronization_job_settings(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the synchronizationJobSettings property value. The synchronizationJobSettings property
        Args:
            value: Value to set for the synchronization_job_settings property.
        """
        self._synchronization_job_settings = value
    
    @property
    def template_id(self,) -> Optional[str]:
        """
        Gets the templateId property value. The templateId property
        Returns: Optional[str]
        """
        return self._template_id
    
    @template_id.setter
    def template_id(self,value: Optional[str] = None) -> None:
        """
        Sets the templateId property value. The templateId property
        Args:
            value: Value to set for the template_id property.
        """
        self._template_id = value
    

