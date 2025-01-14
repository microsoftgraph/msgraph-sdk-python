from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

@dataclass
class AzureAdTokenAuthentication(CustomExtensionAuthenticationConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.azureAdTokenAuthentication"
    # The appID of the Microsoft Entra application to use to authenticate an app with a custom extension.
    resource_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AzureAdTokenAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AzureAdTokenAuthentication
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AzureAdTokenAuthentication()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

        from .custom_extension_authentication_configuration import CustomExtensionAuthenticationConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
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
        writer.write_str_value("resourceId", self.resource_id)
    

