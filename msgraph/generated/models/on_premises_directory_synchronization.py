from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
    from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature

from .entity import Entity

@dataclass
class OnPremisesDirectorySynchronization(Entity, Parsable):
    # Consists of configurations that can be fine-tuned and impact the on-premises directory synchronization process for a tenant. Nullable.
    configuration: Optional[OnPremisesDirectorySynchronizationConfiguration] = None
    # The features property
    features: Optional[OnPremisesDirectorySynchronizationFeature] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesDirectorySynchronization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronization
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesDirectorySynchronization()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
        from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature

        from .entity import Entity
        from .on_premises_directory_synchronization_configuration import OnPremisesDirectorySynchronizationConfiguration
        from .on_premises_directory_synchronization_feature import OnPremisesDirectorySynchronizationFeature

        fields: dict[str, Callable[[Any], None]] = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(OnPremisesDirectorySynchronizationConfiguration)),
            "features": lambda n : setattr(self, 'features', n.get_object_value(OnPremisesDirectorySynchronizationFeature)),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("features", self.features)
    

