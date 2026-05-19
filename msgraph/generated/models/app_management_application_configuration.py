from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_management_configuration import AppManagementConfiguration
    from .identifier_uri_configuration import IdentifierUriConfiguration

from .app_management_configuration import AppManagementConfiguration

@dataclass
class AppManagementApplicationConfiguration(AppManagementConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.appManagementApplicationConfiguration"
    # Configuration object for restrictions on identifierUris property for an application.
    identifier_uris: Optional[IdentifierUriConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppManagementApplicationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppManagementApplicationConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppManagementApplicationConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_management_configuration import AppManagementConfiguration
        from .identifier_uri_configuration import IdentifierUriConfiguration

        from .app_management_configuration import AppManagementConfiguration
        from .identifier_uri_configuration import IdentifierUriConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "identifierUris": lambda n : setattr(self, 'identifier_uris', n.get_object_value(IdentifierUriConfiguration)),
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
        writer.write_object_value("identifierUris", self.identifier_uris)
    

