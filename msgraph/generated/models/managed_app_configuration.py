from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import key_value_pair, managed_app_policy, targeted_managed_app_configuration

from . import managed_app_policy

@dataclass
class ManagedAppConfiguration(managed_app_policy.ManagedAppPolicy):
    odata_type = "#microsoft.graph.managedAppConfiguration"
    # A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service
    custom_settings: Optional[List[key_value_pair.KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfiguration".casefold():
            from . import targeted_managed_app_configuration

            return targeted_managed_app_configuration.TargetedManagedAppConfiguration()
        return ManagedAppConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import key_value_pair, managed_app_policy, targeted_managed_app_configuration

        from . import key_value_pair, managed_app_policy, targeted_managed_app_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "customSettings": lambda n : setattr(self, 'custom_settings', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("customSettings", self.custom_settings)
    

