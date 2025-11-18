from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .web_application_firewall_provider import WebApplicationFirewallProvider

from .web_application_firewall_provider import WebApplicationFirewallProvider

@dataclass
class AkamaiWebApplicationFirewallProvider(WebApplicationFirewallProvider, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.akamaiWebApplicationFirewallProvider"
    # Akamai API access token used to authenticate to the Akamai account. Contact your Akamai Customer Success Manager for assistance with your accessToken.
    access_token: Optional[str] = None
    # Akamai API client secret used in conjunction with the client token and access token for authentication. Contact your Akamai Customer Success Manager for assistance with this information.
    client_secret: Optional[str] = None
    # Akamai API client token used for authentication to the Akamai account. Contact your Akamai Customer Success Manager for assistance with this information.
    client_token: Optional[str] = None
    # Prefix used to identify the host or domain in Akamai configuration operations. This value may be required for certain API calls or configuration scenarios.
    host_prefix: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AkamaiWebApplicationFirewallProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AkamaiWebApplicationFirewallProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AkamaiWebApplicationFirewallProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .web_application_firewall_provider import WebApplicationFirewallProvider

        from .web_application_firewall_provider import WebApplicationFirewallProvider

        fields: dict[str, Callable[[Any], None]] = {
            "accessToken": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "clientSecret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "clientToken": lambda n : setattr(self, 'client_token', n.get_str_value()),
            "hostPrefix": lambda n : setattr(self, 'host_prefix', n.get_str_value()),
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
        writer.write_str_value("accessToken", self.access_token)
        writer.write_str_value("clientSecret", self.client_secret)
        writer.write_str_value("clientToken", self.client_token)
        writer.write_str_value("hostPrefix", self.host_prefix)
    

