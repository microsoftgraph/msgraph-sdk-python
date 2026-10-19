from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_callout_extension import CustomCalloutExtension
    from .custom_callout_extension_type import CustomCalloutExtensionType
    from .custom_extension_resource_type import CustomExtensionResourceType

from .custom_callout_extension import CustomCalloutExtension

@dataclass
class RoleManagementCustomCalloutExtension(CustomCalloutExtension, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.roleManagementCustomCalloutExtension"
    # The customAttributes property
    custom_attributes: Optional[list[str]] = None
    # The resourceType property
    resource_type: Optional[CustomExtensionResourceType] = None
    # The type property
    type: Optional[CustomCalloutExtensionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoleManagementCustomCalloutExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoleManagementCustomCalloutExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoleManagementCustomCalloutExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_callout_extension import CustomCalloutExtension
        from .custom_callout_extension_type import CustomCalloutExtensionType
        from .custom_extension_resource_type import CustomExtensionResourceType

        from .custom_callout_extension import CustomCalloutExtension
        from .custom_callout_extension_type import CustomCalloutExtensionType
        from .custom_extension_resource_type import CustomExtensionResourceType

        fields: dict[str, Callable[[Any], None]] = {
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_primitive_values(str)),
            "resourceType": lambda n : setattr(self, 'resource_type', n.get_enum_value(CustomExtensionResourceType)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CustomCalloutExtensionType)),
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
        writer.write_collection_of_primitive_values("customAttributes", self.custom_attributes)
        writer.write_enum_value("resourceType", self.resource_type)
        writer.write_enum_value("type", self.type)
    

