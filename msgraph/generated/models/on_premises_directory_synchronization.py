from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
on_premises_directory_synchronization_configuration = lazy_import('msgraph.generated.models.on_premises_directory_synchronization_configuration')
on_premises_directory_synchronization_feature = lazy_import('msgraph.generated.models.on_premises_directory_synchronization_feature')

class OnPremisesDirectorySynchronization(entity.Entity):
    @property
    def configuration(self,) -> Optional[on_premises_directory_synchronization_configuration.OnPremisesDirectorySynchronizationConfiguration]:
        """
        Gets the configuration property value. Consists of configurations that can be fine-tuned and impact the on-premises directory synchronization process for a tenant.
        Returns: Optional[on_premises_directory_synchronization_configuration.OnPremisesDirectorySynchronizationConfiguration]
        """
        return self._configuration
    
    @configuration.setter
    def configuration(self,value: Optional[on_premises_directory_synchronization_configuration.OnPremisesDirectorySynchronizationConfiguration] = None) -> None:
        """
        Sets the configuration property value. Consists of configurations that can be fine-tuned and impact the on-premises directory synchronization process for a tenant.
        Args:
            value: Value to set for the configuration property.
        """
        self._configuration = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesDirectorySynchronization and sets the default values.
        """
        super().__init__()
        # Consists of configurations that can be fine-tuned and impact the on-premises directory synchronization process for a tenant.
        self._configuration: Optional[on_premises_directory_synchronization_configuration.OnPremisesDirectorySynchronizationConfiguration] = None
        # The features property
        self._features: Optional[on_premises_directory_synchronization_feature.OnPremisesDirectorySynchronizationFeature] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesDirectorySynchronization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesDirectorySynchronization()
    
    @property
    def features(self,) -> Optional[on_premises_directory_synchronization_feature.OnPremisesDirectorySynchronizationFeature]:
        """
        Gets the features property value. The features property
        Returns: Optional[on_premises_directory_synchronization_feature.OnPremisesDirectorySynchronizationFeature]
        """
        return self._features
    
    @features.setter
    def features(self,value: Optional[on_premises_directory_synchronization_feature.OnPremisesDirectorySynchronizationFeature] = None) -> None:
        """
        Sets the features property value. The features property
        Args:
            value: Value to set for the features property.
        """
        self._features = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration": lambda n : setattr(self, 'configuration', n.get_object_value(on_premises_directory_synchronization_configuration.OnPremisesDirectorySynchronizationConfiguration)),
            "features": lambda n : setattr(self, 'features', n.get_object_value(on_premises_directory_synchronization_feature.OnPremisesDirectorySynchronizationFeature)),
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
        writer.write_object_value("configuration", self.configuration)
        writer.write_object_value("features", self.features)
    

