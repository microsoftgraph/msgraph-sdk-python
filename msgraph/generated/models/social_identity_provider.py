from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_provider_base import IdentityProviderBase

from .identity_provider_base import IdentityProviderBase

@dataclass
class SocialIdentityProvider(IdentityProviderBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.socialIdentityProvider"
    # The identifier for the client application obtained when registering the application with the identity provider. Required.
    client_id: Optional[str] = None
    # The client secret for the application that is obtained when the application is registered with the identity provider. This is write-only. A read operation returns . Required.
    client_secret: Optional[str] = None
    # For a B2B scenario, possible values: Google, Facebook. For a B2C scenario, possible values: Microsoft, Google, Amazon, LinkedIn, Facebook, GitHub, Twitter, Weibo, QQ, WeChat. Required.
    identity_provider_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SocialIdentityProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SocialIdentityProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SocialIdentityProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_provider_base import IdentityProviderBase

        from .identity_provider_base import IdentityProviderBase

        fields: dict[str, Callable[[Any], None]] = {
            "clientId": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "identityProviderType": lambda n : setattr(self, 'identity_provider_type', n.get_str_value()),
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
        writer.write_str_value("clientId", self.client_id)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("identityProviderType", self.identity_provider_type)
    

