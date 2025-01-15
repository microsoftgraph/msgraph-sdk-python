from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
    from .custom_callout_extension import CustomCalloutExtension
    from .entity import Entity

from .entity import Entity

@dataclass
class CustomExtensionStageSetting(Entity, Parsable):
    # Indicates the custom workflow extension that will be executed at this stage. Nullable. Supports $expand.
    custom_extension: Optional[CustomCalloutExtension] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The stage property
    stage: Optional[AccessPackageCustomExtensionStage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomExtensionStageSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomExtensionStageSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomExtensionStageSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
        from .custom_callout_extension import CustomCalloutExtension
        from .entity import Entity

        from .access_package_custom_extension_stage import AccessPackageCustomExtensionStage
        from .custom_callout_extension import CustomCalloutExtension
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "customExtension": lambda n : setattr(self, 'custom_extension', n.get_object_value(CustomCalloutExtension)),
            "stage": lambda n : setattr(self, 'stage', n.get_enum_value(AccessPackageCustomExtensionStage)),
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
        writer.write_object_value("customExtension", self.custom_extension)
        writer.write_enum_value("stage", self.stage)
    

