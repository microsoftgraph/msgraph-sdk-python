from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .federated_idp_mfa_behavior import FederatedIdpMfaBehavior
    from .prompt_login_behavior import PromptLoginBehavior
    from .saml_or_ws_fed_provider import SamlOrWsFedProvider
    from .signing_certificate_update_status import SigningCertificateUpdateStatus

from .saml_or_ws_fed_provider import SamlOrWsFedProvider

@dataclass
class InternalDomainFederation(SamlOrWsFedProvider, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.internalDomainFederation"
    # URL of the endpoint used by active clients when authenticating with federated domains set up for single sign-on in Microsoft Entra ID. Corresponds to the ActiveLogOnUri property of the Set-EntraDomainFederationSettings PowerShell cmdlet.
    active_sign_in_uri: Optional[str] = None
    # Determines whether Microsoft Entra ID accepts the MFA performed by the federated IdP when a federated user accesses an application that is governed by a conditional access policy that requires MFA. The possible values are: acceptIfMfaDoneByFederatedIdp, enforceMfaByFederatedIdp, rejectMfaByFederatedIdp, unknownFutureValue. For more information, see federatedIdpMfaBehavior values.
    federated_idp_mfa_behavior: Optional[FederatedIdpMfaBehavior] = None
    # If true, when SAML authentication requests are sent to the federated SAML IdP, Microsoft Entra ID will sign those requests using the OrgID signing key. If false (default), the SAML authentication requests sent to the federated IdP aren't signed.
    is_signed_authentication_request_required: Optional[bool] = None
    # Fallback token signing certificate that can also be used to sign tokens, for example when the primary signing certificate expires. Formatted as Base64 encoded strings of the public portion of the federated IdP's token signing certificate. Needs to be compatible with the X509Certificate2 class. Much like the signingCertificate, the nextSigningCertificate property is used if a rollover is required outside of the auto-rollover update, a new federation service is being set up, or if the new token signing certificate isn't present in the federation properties after the federation service certificate has been updated.
    next_signing_certificate: Optional[str] = None
    # The passwordResetUri property
    password_reset_uri: Optional[str] = None
    # Sets the preferred behavior for the sign-in prompt. The possible values are: translateToFreshPasswordAuthentication, nativeSupport, disabled, unknownFutureValue.
    prompt_login_behavior: Optional[PromptLoginBehavior] = None
    # URI that clients are redirected to when they sign out of Microsoft Entra services. Corresponds to the LogOffUri property of the Set-EntraDomainFederationSettings PowerShell cmdlet.
    sign_out_uri: Optional[str] = None
    # Provides status and timestamp of the last update of the signing certificate.
    signing_certificate_update_status: Optional[SigningCertificateUpdateStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InternalDomainFederation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InternalDomainFederation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InternalDomainFederation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .federated_idp_mfa_behavior import FederatedIdpMfaBehavior
        from .prompt_login_behavior import PromptLoginBehavior
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .signing_certificate_update_status import SigningCertificateUpdateStatus

        from .federated_idp_mfa_behavior import FederatedIdpMfaBehavior
        from .prompt_login_behavior import PromptLoginBehavior
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .signing_certificate_update_status import SigningCertificateUpdateStatus

        fields: dict[str, Callable[[Any], None]] = {
            "activeSignInUri": lambda n : setattr(self, 'active_sign_in_uri', n.get_str_value()),
            "federatedIdpMfaBehavior": lambda n : setattr(self, 'federated_idp_mfa_behavior', n.get_enum_value(FederatedIdpMfaBehavior)),
            "isSignedAuthenticationRequestRequired": lambda n : setattr(self, 'is_signed_authentication_request_required', n.get_bool_value()),
            "nextSigningCertificate": lambda n : setattr(self, 'next_signing_certificate', n.get_str_value()),
            "passwordResetUri": lambda n : setattr(self, 'password_reset_uri', n.get_str_value()),
            "promptLoginBehavior": lambda n : setattr(self, 'prompt_login_behavior', n.get_enum_value(PromptLoginBehavior)),
            "signOutUri": lambda n : setattr(self, 'sign_out_uri', n.get_str_value()),
            "signingCertificateUpdateStatus": lambda n : setattr(self, 'signing_certificate_update_status', n.get_object_value(SigningCertificateUpdateStatus)),
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
        writer.write_str_value("activeSignInUri", self.active_sign_in_uri)
        writer.write_enum_value("federatedIdpMfaBehavior", self.federated_idp_mfa_behavior)
        writer.write_bool_value("isSignedAuthenticationRequestRequired", self.is_signed_authentication_request_required)
        writer.write_str_value("nextSigningCertificate", self.next_signing_certificate)
        writer.write_str_value("passwordResetUri", self.password_reset_uri)
        writer.write_enum_value("promptLoginBehavior", self.prompt_login_behavior)
        writer.write_str_value("signOutUri", self.sign_out_uri)
        writer.write_object_value("signingCertificateUpdateStatus", self.signing_certificate_update_status)
    

