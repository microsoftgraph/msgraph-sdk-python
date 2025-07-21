from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .synchronization_job import SynchronizationJob
    from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
    from .synchronization_template import SynchronizationTemplate

from .entity import Entity

@dataclass
class Synchronization(Entity, Parsable):
    # Performs synchronization by periodically running in the background, polling for changes in one directory, and pushing them to another directory.
    jobs: Optional[list[SynchronizationJob]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a collection of credentials to access provisioned cloud applications.
    secrets: Optional[list[SynchronizationSecretKeyStringValuePair]] = None
    # Preconfigured synchronization settings for a particular application.
    templates: Optional[list[SynchronizationTemplate]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Synchronization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Synchronization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Synchronization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .synchronization_job import SynchronizationJob
        from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
        from .synchronization_template import SynchronizationTemplate

        from .entity import Entity
        from .synchronization_job import SynchronizationJob
        from .synchronization_secret_key_string_value_pair import SynchronizationSecretKeyStringValuePair
        from .synchronization_template import SynchronizationTemplate

        fields: dict[str, Callable[[Any], None]] = {
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(SynchronizationJob)),
            "secrets": lambda n : setattr(self, 'secrets', n.get_collection_of_object_values(SynchronizationSecretKeyStringValuePair)),
            "templates": lambda n : setattr(self, 'templates', n.get_collection_of_object_values(SynchronizationTemplate)),
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
        writer.write_collection_of_object_values("secrets", self.secrets)
        writer.write_collection_of_object_values("templates", self.templates)
    

