from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource import AccessPackageResource
    from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

from .access_package_resource import AccessPackageResource

@dataclass
class CustomDataProvidedResource(AccessPackageResource, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.customDataProvidedResource"
    # The endpoint configuration of the logic app that is triggered when the access review for this resource goes into an initializing state.
    notification_endpoint_configuration: Optional[CustomExtensionEndpointConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomDataProvidedResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomDataProvidedResource
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomDataProvidedResource()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource import AccessPackageResource
        from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

        from .access_package_resource import AccessPackageResource
        from .custom_extension_endpoint_configuration import CustomExtensionEndpointConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "notificationEndpointConfiguration": lambda n : setattr(self, 'notification_endpoint_configuration', n.get_object_value(CustomExtensionEndpointConfiguration)),
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
        writer.write_object_value("notificationEndpointConfiguration", self.notification_endpoint_configuration)
    

