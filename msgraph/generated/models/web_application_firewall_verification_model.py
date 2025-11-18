from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .web_application_firewall_provider import WebApplicationFirewallProvider
    from .web_application_firewall_provider_type import WebApplicationFirewallProviderType
    from .web_application_firewall_verification_result import WebApplicationFirewallVerificationResult
    from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

from .entity import Entity

@dataclass
class WebApplicationFirewallVerificationModel(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Reference to a provider resource associated with this verification model. Represents a WAF provider that can be used to verify or manage the host.
    provider: Optional[WebApplicationFirewallProvider] = None
    # The providerType property
    provider_type: Optional[WebApplicationFirewallProviderType] = None
    # An object describing the outcome of the verification operation, including status, errors or warnings
    verification_result: Optional[WebApplicationFirewallVerificationResult] = None
    # Details of DNS configuration
    verified_details: Optional[WebApplicationFirewallVerifiedDetails] = None
    # The host (domain or subdomain) that was verified as part of this verification operation.
    verified_host: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebApplicationFirewallVerificationModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebApplicationFirewallVerificationModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebApplicationFirewallVerificationModel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .web_application_firewall_provider import WebApplicationFirewallProvider
        from .web_application_firewall_provider_type import WebApplicationFirewallProviderType
        from .web_application_firewall_verification_result import WebApplicationFirewallVerificationResult
        from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

        from .entity import Entity
        from .web_application_firewall_provider import WebApplicationFirewallProvider
        from .web_application_firewall_provider_type import WebApplicationFirewallProviderType
        from .web_application_firewall_verification_result import WebApplicationFirewallVerificationResult
        from .web_application_firewall_verified_details import WebApplicationFirewallVerifiedDetails

        fields: dict[str, Callable[[Any], None]] = {
            "provider": lambda n : setattr(self, 'provider', n.get_object_value(WebApplicationFirewallProvider)),
            "providerType": lambda n : setattr(self, 'provider_type', n.get_enum_value(WebApplicationFirewallProviderType)),
            "verificationResult": lambda n : setattr(self, 'verification_result', n.get_object_value(WebApplicationFirewallVerificationResult)),
            "verifiedDetails": lambda n : setattr(self, 'verified_details', n.get_object_value(WebApplicationFirewallVerifiedDetails)),
            "verifiedHost": lambda n : setattr(self, 'verified_host', n.get_str_value()),
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
        writer.write_object_value("provider", self.provider)
        writer.write_enum_value("providerType", self.provider_type)
        writer.write_object_value("verificationResult", self.verification_result)
        writer.write_object_value("verifiedDetails", self.verified_details)
        writer.write_str_value("verifiedHost", self.verified_host)
    

