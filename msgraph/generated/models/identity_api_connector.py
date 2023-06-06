from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import api_authentication_configuration_base, entity

from . import entity

@dataclass
class IdentityApiConnector(entity.Entity):
    # The object which describes the authentication configuration details for calling the API. Basic and PKCS 12 client certificate are supported.
    authentication_configuration: Optional[api_authentication_configuration_base.ApiAuthenticationConfigurationBase] = None
    # The name of the API connector.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL of the API endpoint to call.
    target_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityApiConnector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IdentityApiConnector
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IdentityApiConnector()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import api_authentication_configuration_base, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationConfiguration": lambda n : setattr(self, 'authentication_configuration', n.get_object_value(api_authentication_configuration_base.ApiAuthenticationConfigurationBase)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "targetUrl": lambda n : setattr(self, 'target_url', n.get_str_value()),
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
        writer.write_object_value("authenticationConfiguration", self.authentication_configuration)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("targetUrl", self.target_url)
    

