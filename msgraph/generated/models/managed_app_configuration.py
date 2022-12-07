from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
managed_app_policy = lazy_import('msgraph.generated.models.managed_app_policy')

class ManagedAppConfiguration(managed_app_policy.ManagedAppPolicy):
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedAppConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.managedAppConfiguration"
        # A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service
        self._custom_settings: Optional[List[key_value_pair.KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppConfiguration()
    
    @property
    def custom_settings(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the customSettings property value. A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._custom_settings
    
    @custom_settings.setter
    def custom_settings(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the customSettings property value. A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service
        Args:
            value: Value to set for the customSettings property.
        """
        self._custom_settings = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "custom_settings": lambda n : setattr(self, 'custom_settings', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
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
        writer.write_collection_of_object_values("customSettings", self.custom_settings)
    

