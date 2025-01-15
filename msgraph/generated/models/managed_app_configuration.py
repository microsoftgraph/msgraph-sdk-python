from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .key_value_pair import KeyValuePair
    from .managed_app_policy import ManagedAppPolicy
    from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

from .managed_app_policy import ManagedAppPolicy

@dataclass
class ManagedAppConfiguration(ManagedAppPolicy, Parsable):
    """
    Configuration used to deliver a set of custom settings as-is to apps for users to whom the configuration is scoped
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.managedAppConfiguration"
    # A set of string key and string value pairs to be sent to apps for users to whom the configuration is scoped, unalterned by this service
    custom_settings: Optional[list[KeyValuePair]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfiguration".casefold():
            from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

            return TargetedManagedAppConfiguration()
        return ManagedAppConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .key_value_pair import KeyValuePair
        from .managed_app_policy import ManagedAppPolicy
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

        from .key_value_pair import KeyValuePair
        from .managed_app_policy import ManagedAppPolicy
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "customSettings": lambda n : setattr(self, 'custom_settings', n.get_collection_of_object_values(KeyValuePair)),
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
        writer.write_collection_of_object_values("customSettings", self.custom_settings)
    

