from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_protocol import AuthenticationProtocol
    from .identity_provider_base import IdentityProviderBase
    from .internal_domain_federation import InternalDomainFederation
    from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation

from .identity_provider_base import IdentityProviderBase

@dataclass
class SamlOrWsFedProvider(IdentityProviderBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.samlOrWsFedProvider"
    # Issuer URI of the federation server.
    issuer_uri: Optional[str] = None
    # URI of the metadata exchange endpoint used for authentication from rich client applications.
    metadata_exchange_uri: Optional[str] = None
    # URI that web-based clients are directed to when signing in to Microsoft Entra services.
    passive_sign_in_uri: Optional[str] = None
    # Preferred authentication protocol. The possible values are: wsFed, saml, unknownFutureValue.
    preferred_authentication_protocol: Optional[AuthenticationProtocol] = None
    # Current certificate used to sign tokens passed to the Microsoft identity platform. The certificate is formatted as a Base64 encoded string of the public portion of the federated IdP's token signing certificate and must be compatible with the X509Certificate2 class.   This property is used in the following scenarios:  if a rollover is required outside of the autorollover update a new federation service is being set up  if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.   Microsoft Entra ID updates certificates via an autorollover process in which it attempts to retrieve a new certificate from the federation service metadata, 30 days before expiry of the current certificate. If a new certificate isn't available, Microsoft Entra ID monitors the metadata daily and will update the federation settings for the domain when a new certificate is available.
    signing_certificate: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SamlOrWsFedProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SamlOrWsFedProvider
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalDomainFederation".casefold():
            from .internal_domain_federation import InternalDomainFederation

            return InternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedExternalDomainFederation".casefold():
            from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation

            return SamlOrWsFedExternalDomainFederation()
        return SamlOrWsFedProvider()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_protocol import AuthenticationProtocol
        from .identity_provider_base import IdentityProviderBase
        from .internal_domain_federation import InternalDomainFederation
        from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation

        from .authentication_protocol import AuthenticationProtocol
        from .identity_provider_base import IdentityProviderBase
        from .internal_domain_federation import InternalDomainFederation
        from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation

        fields: dict[str, Callable[[Any], None]] = {
            "issuerUri": lambda n : setattr(self, 'issuer_uri', n.get_str_value()),
            "metadataExchangeUri": lambda n : setattr(self, 'metadata_exchange_uri', n.get_str_value()),
            "passiveSignInUri": lambda n : setattr(self, 'passive_sign_in_uri', n.get_str_value()),
            "preferredAuthenticationProtocol": lambda n : setattr(self, 'preferred_authentication_protocol', n.get_enum_value(AuthenticationProtocol)),
            "signingCertificate": lambda n : setattr(self, 'signing_certificate', n.get_str_value()),
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
        writer.write_str_value("issuerUri", self.issuer_uri)
        writer.write_str_value("metadataExchangeUri", self.metadata_exchange_uri)
        writer.write_str_value("passiveSignInUri", self.passive_sign_in_uri)
        writer.write_enum_value("preferredAuthenticationProtocol", self.preferred_authentication_protocol)
        writer.write_str_value("signingCertificate", self.signing_certificate)
    

