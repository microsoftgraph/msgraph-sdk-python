from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .web_application_firewall_provider import WebApplicationFirewallProvider

from .web_application_firewall_provider import WebApplicationFirewallProvider

@dataclass
class CloudFlareWebApplicationFirewallProvider(WebApplicationFirewallProvider, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.cloudFlareWebApplicationFirewallProvider"
    # Cloudflare API token or credential used by Microsoft services to authenticate to the Cloudflare account. Contact your Cloudflare Customer Success Manager for assistance with your apitoken.
    api_token: Optional[str] = None
    # Default Cloudflare Zone ID associated with this provider configuration. This ID identifies the DNS zone in Cloudflare that is commonly used for verification and configuration operations for the provider.
    zone_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudFlareWebApplicationFirewallProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudFlareWebApplicationFirewallProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudFlareWebApplicationFirewallProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .web_application_firewall_provider import WebApplicationFirewallProvider

        from .web_application_firewall_provider import WebApplicationFirewallProvider

        fields: dict[str, Callable[[Any], None]] = {
            "apiToken": lambda n : setattr(self, 'api_token', n.get_str_value()),
            "zoneId": lambda n : setattr(self, 'zone_id', n.get_str_value()),
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
        writer.write_str_value("apiToken", self.api_token)
        writer.write_str_value("zoneId", self.zone_id)
    

