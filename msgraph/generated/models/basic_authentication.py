from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import api_authentication_configuration_base

from . import api_authentication_configuration_base

@dataclass
class BasicAuthentication(api_authentication_configuration_base.ApiAuthenticationConfigurationBase):
    odata_type = "#microsoft.graph.basicAuthentication"
    # The password. It is not returned in the responses.
    password: Optional[str] = None
    # The username.
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BasicAuthentication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BasicAuthentication
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return BasicAuthentication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import api_authentication_configuration_base

        from . import api_authentication_configuration_base

        fields: Dict[str, Callable[[Any], None]] = {
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
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
        writer.write_str_value("password", self.password)
        writer.write_str_value("username", self.username)
    

