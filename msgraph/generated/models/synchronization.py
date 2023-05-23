from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, synchronization_job, synchronization_secret_key_string_value_pair, synchronization_template

from . import entity

class Synchronization(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronization and sets the default values.
        """
        super().__init__()
        # The jobs property
        self._jobs: Optional[List[synchronization_job.SynchronizationJob]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The secrets property
        self._secrets: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]] = None
        # The templates property
        self._templates: Optional[List[synchronization_template.SynchronizationTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Synchronization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Synchronization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Synchronization()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, synchronization_job, synchronization_secret_key_string_value_pair, synchronization_template

        fields: Dict[str, Callable[[Any], None]] = {
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(synchronization_job.SynchronizationJob)),
            "secrets": lambda n : setattr(self, 'secrets', n.get_collection_of_object_values(synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(synchronization_template.SynchronizationTemplate)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def jobs(self,) -> Optional[List[synchronization_job.SynchronizationJob]]:
        """
        Gets the jobs property value. The jobs property
        Returns: Optional[List[synchronization_job.SynchronizationJob]]
        """
        return self._jobs
    
    @jobs.setter
    def jobs(self,value: Optional[List[synchronization_job.SynchronizationJob]] = None) -> None:
        """
        Sets the jobs property value. The jobs property
        Args:
            value: Value to set for the jobs property.
        """
        self._jobs = value
    
    @property
    def secrets(self,) -> Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]]:
        """
        Gets the secrets property value. The secrets property
        Returns: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]]
        """
        return self._secrets
    
    @secrets.setter
    def secrets(self,value: Optional[List[synchronization_secret_key_string_value_pair.SynchronizationSecretKeyStringValuePair]] = None) -> None:
        """
        Sets the secrets property value. The secrets property
        Args:
            value: Value to set for the secrets property.
        """
        self._secrets = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_collection_of_object_values("secrets", self.secrets)
        writer.write_collection_of_object_values("templates", self.templates)
    
    @property
    def templates(self,) -> Optional[List[synchronization_template.SynchronizationTemplate]]:
        """
        Gets the templates property value. The templates property
        Returns: Optional[List[synchronization_template.SynchronizationTemplate]]
        """
        return self._templates
    
    @templates.setter
    def templates(self,value: Optional[List[synchronization_template.SynchronizationTemplate]] = None) -> None:
        """
        Sets the templates property value. The templates property
        Args:
            value: Value to set for the templates property.
        """
        self._templates = value
    

