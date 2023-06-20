from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_protocol, identity_provider_base, internal_domain_federation, saml_or_ws_fed_external_domain_federation

from . import identity_provider_base

@dataclass
class SamlOrWsFedProvider(identity_provider_base.IdentityProviderBase):
    odata_type = "#microsoft.graph.samlOrWsFedProvider"
    # Issuer URI of the federation server.
    issuer_uri: Optional[str] = None
    # URI of the metadata exchange endpoint used for authentication from rich client applications.
    metadata_exchange_uri: Optional[str] = None
    # URI that web-based clients are directed to when signing in to Azure Active Directory (Azure AD) services.
    passive_sign_in_uri: Optional[str] = None
    # Preferred authentication protocol. The possible values are: wsFed, saml, unknownFutureValue.
    preferred_authentication_protocol: Optional[authentication_protocol.AuthenticationProtocol] = None
    # Current certificate used to sign tokens passed to the Microsoft identity platform. The certificate is formatted as a Base64 encoded string of the public portion of the federated IdP's token signing certificate and must be compatible with the X509Certificate2 class.   This property is used in the following scenarios:  if a rollover is required outside of the autorollover update a new federation service is being set up  if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.   Azure AD updates certificates via an autorollover process in which it attempts to retrieve a new certificate from the federation service metadata, 30 days before expiry of the current certificate. If a new certificate isn't available, Azure AD monitors the metadata daily and will update the federation settings for the domain when a new certificate is available.
    signing_certificate: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SamlOrWsFedProvider:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SamlOrWsFedProvider
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalDomainFederation".casefold():
            from . import internal_domain_federation

            return internal_domain_federation.InternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedExternalDomainFederation".casefold():
            from . import saml_or_ws_fed_external_domain_federation

            return saml_or_ws_fed_external_domain_federation.SamlOrWsFedExternalDomainFederation()
        return SamlOrWsFedProvider()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_protocol, identity_provider_base, internal_domain_federation, saml_or_ws_fed_external_domain_federation

        from . import authentication_protocol, identity_provider_base, internal_domain_federation, saml_or_ws_fed_external_domain_federation

        fields: Dict[str, Callable[[Any], None]] = {
            "issuerUri": lambda n : setattr(self, 'issuer_uri', n.get_str_value()),
            "metadataExchangeUri": lambda n : setattr(self, 'metadata_exchange_uri', n.get_str_value()),
            "passiveSignInUri": lambda n : setattr(self, 'passive_sign_in_uri', n.get_str_value()),
            "preferredAuthenticationProtocol": lambda n : setattr(self, 'preferred_authentication_protocol', n.get_enum_value(authentication_protocol.AuthenticationProtocol)),
            "signingCertificate": lambda n : setattr(self, 'signing_certificate', n.get_str_value()),
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
        writer.write_str_value("issuerUri", self.issuer_uri)
        writer.write_str_value("metadataExchangeUri", self.metadata_exchange_uri)
        writer.write_str_value("passiveSignInUri", self.passive_sign_in_uri)
        writer.write_enum_value("preferredAuthenticationProtocol", self.preferred_authentication_protocol)
        writer.write_str_value("signingCertificate", self.signing_certificate)
    

