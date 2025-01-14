from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase

from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase

@dataclass
class Pkcs12Certificate(ApiAuthenticationConfigurationBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.pkcs12Certificate"
    # The password for the pfx file. Required. If no password is used, you must still provide a value of ''.
    password: Optional[str] = None
    # Represents the pfx content that is sent. The value should be a base-64 encoded version of the actual certificate content. Required.
    pkcs12_value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Pkcs12Certificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Pkcs12Certificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Pkcs12Certificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase

        from .api_authentication_configuration_base import ApiAuthenticationConfigurationBase

        fields: dict[str, Callable[[Any], None]] = {
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "pkcs12Value": lambda n : setattr(self, 'pkcs12_value', n.get_str_value()),
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
        writer.write_str_value("password", self.password)
        writer.write_str_value("pkcs12Value", self.pkcs12_value)
    

