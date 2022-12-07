from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

federated_idp_mfa_behavior = lazy_import('msgraph.generated.models.federated_idp_mfa_behavior')
prompt_login_behavior = lazy_import('msgraph.generated.models.prompt_login_behavior')
saml_or_ws_fed_provider = lazy_import('msgraph.generated.models.saml_or_ws_fed_provider')
signing_certificate_update_status = lazy_import('msgraph.generated.models.signing_certificate_update_status')

class InternalDomainFederation(saml_or_ws_fed_provider.SamlOrWsFedProvider):
    @property
    def active_sign_in_uri(self,) -> Optional[str]:
        """
        Gets the activeSignInUri property value. URL of the endpoint used by active clients when authenticating with federated domains set up for single sign-on in Azure Active Directory (Azure AD). Corresponds to the ActiveLogOnUri property of the Set-MsolDomainFederationSettings MSOnline v1 PowerShell cmdlet.
        Returns: Optional[str]
        """
        return self._active_sign_in_uri
    
    @active_sign_in_uri.setter
    def active_sign_in_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the activeSignInUri property value. URL of the endpoint used by active clients when authenticating with federated domains set up for single sign-on in Azure Active Directory (Azure AD). Corresponds to the ActiveLogOnUri property of the Set-MsolDomainFederationSettings MSOnline v1 PowerShell cmdlet.
        Args:
            value: Value to set for the activeSignInUri property.
        """
        self._active_sign_in_uri = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new InternalDomainFederation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.internalDomainFederation"
        # URL of the endpoint used by active clients when authenticating with federated domains set up for single sign-on in Azure Active Directory (Azure AD). Corresponds to the ActiveLogOnUri property of the Set-MsolDomainFederationSettings MSOnline v1 PowerShell cmdlet.
        self._active_sign_in_uri: Optional[str] = None
        # Determines whether Azure AD accepts the MFA performed by the federated IdP when a federated user accesses an application that is governed by a conditional access policy that requires MFA. The possible values are: acceptIfMfaDoneByFederatedIdp, enforceMfaByFederatedIdp, rejectMfaByFederatedIdp, unknownFutureValue. For more information, see federatedIdpMfaBehavior values.
        self._federated_idp_mfa_behavior: Optional[federated_idp_mfa_behavior.FederatedIdpMfaBehavior] = None
        # If true, when SAML authentication requests are sent to the federated SAML IdP, Azure AD will sign those requests using the OrgID signing key. If false (default), the SAML authentication requests sent to the federated IdP are not signed.
        self._is_signed_authentication_request_required: Optional[bool] = None
        # Fallback token signing certificate that is used to sign tokens when the primary signing certificate expires. Formatted as Base64 encoded strings of the public portion of the federated IdP's token signing certificate. Needs to be compatible with the X509Certificate2 class. Much like the signingCertificate, the nextSigningCertificate property is used if a rollover is required outside of the auto-rollover update, a new federation service is being set up, or if the new token signing certificate is not present in the federation properties after the federation service certificate has been updated.
        self._next_signing_certificate: Optional[str] = None
        # Sets the preferred behavior for the sign-in prompt. The possible values are: translateToFreshPasswordAuthentication, nativeSupport, disabled, unknownFutureValue.
        self._prompt_login_behavior: Optional[prompt_login_behavior.PromptLoginBehavior] = None
        # Provides status and timestamp of the last update of the signing certificate.
        self._signing_certificate_update_status: Optional[signing_certificate_update_status.SigningCertificateUpdateStatus] = None
        # URI that clients are redirected to when they sign out of Azure AD services. Corresponds to the LogOffUri property of the Set-MsolDomainFederationSettings MSOnline v1 PowerShell cmdlet.
        self._sign_out_uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InternalDomainFederation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InternalDomainFederation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InternalDomainFederation()
    
    @property
    def federated_idp_mfa_behavior(self,) -> Optional[federated_idp_mfa_behavior.FederatedIdpMfaBehavior]:
        """
        Gets the federatedIdpMfaBehavior property value. Determines whether Azure AD accepts the MFA performed by the federated IdP when a federated user accesses an application that is governed by a conditional access policy that requires MFA. The possible values are: acceptIfMfaDoneByFederatedIdp, enforceMfaByFederatedIdp, rejectMfaByFederatedIdp, unknownFutureValue. For more information, see federatedIdpMfaBehavior values.
        Returns: Optional[federated_idp_mfa_behavior.FederatedIdpMfaBehavior]
        """
        return self._federated_idp_mfa_behavior
    
    @federated_idp_mfa_behavior.setter
    def federated_idp_mfa_behavior(self,value: Optional[federated_idp_mfa_behavior.FederatedIdpMfaBehavior] = None) -> None:
        """
        Sets the federatedIdpMfaBehavior property value. Determines whether Azure AD accepts the MFA performed by the federated IdP when a federated user accesses an application that is governed by a conditional access policy that requires MFA. The possible values are: acceptIfMfaDoneByFederatedIdp, enforceMfaByFederatedIdp, rejectMfaByFederatedIdp, unknownFutureValue. For more information, see federatedIdpMfaBehavior values.
        Args:
            value: Value to set for the federatedIdpMfaBehavior property.
        """
        self._federated_idp_mfa_behavior = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_sign_in_uri": lambda n : setattr(self, 'active_sign_in_uri', n.get_str_value()),
            "federated_idp_mfa_behavior": lambda n : setattr(self, 'federated_idp_mfa_behavior', n.get_enum_value(federated_idp_mfa_behavior.FederatedIdpMfaBehavior)),
            "is_signed_authentication_request_required": lambda n : setattr(self, 'is_signed_authentication_request_required', n.get_bool_value()),
            "next_signing_certificate": lambda n : setattr(self, 'next_signing_certificate', n.get_str_value()),
            "prompt_login_behavior": lambda n : setattr(self, 'prompt_login_behavior', n.get_enum_value(prompt_login_behavior.PromptLoginBehavior)),
            "signing_certificate_update_status": lambda n : setattr(self, 'signing_certificate_update_status', n.get_object_value(signing_certificate_update_status.SigningCertificateUpdateStatus)),
            "sign_out_uri": lambda n : setattr(self, 'sign_out_uri', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_signed_authentication_request_required(self,) -> Optional[bool]:
        """
        Gets the isSignedAuthenticationRequestRequired property value. If true, when SAML authentication requests are sent to the federated SAML IdP, Azure AD will sign those requests using the OrgID signing key. If false (default), the SAML authentication requests sent to the federated IdP are not signed.
        Returns: Optional[bool]
        """
        return self._is_signed_authentication_request_required
    
    @is_signed_authentication_request_required.setter
    def is_signed_authentication_request_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSignedAuthenticationRequestRequired property value. If true, when SAML authentication requests are sent to the federated SAML IdP, Azure AD will sign those requests using the OrgID signing key. If false (default), the SAML authentication requests sent to the federated IdP are not signed.
        Args:
            value: Value to set for the isSignedAuthenticationRequestRequired property.
        """
        self._is_signed_authentication_request_required = value
    
    @property
    def next_signing_certificate(self,) -> Optional[str]:
        """
        Gets the nextSigningCertificate property value. Fallback token signing certificate that is used to sign tokens when the primary signing certificate expires. Formatted as Base64 encoded strings of the public portion of the federated IdP's token signing certificate. Needs to be compatible with the X509Certificate2 class. Much like the signingCertificate, the nextSigningCertificate property is used if a rollover is required outside of the auto-rollover update, a new federation service is being set up, or if the new token signing certificate is not present in the federation properties after the federation service certificate has been updated.
        Returns: Optional[str]
        """
        return self._next_signing_certificate
    
    @next_signing_certificate.setter
    def next_signing_certificate(self,value: Optional[str] = None) -> None:
        """
        Sets the nextSigningCertificate property value. Fallback token signing certificate that is used to sign tokens when the primary signing certificate expires. Formatted as Base64 encoded strings of the public portion of the federated IdP's token signing certificate. Needs to be compatible with the X509Certificate2 class. Much like the signingCertificate, the nextSigningCertificate property is used if a rollover is required outside of the auto-rollover update, a new federation service is being set up, or if the new token signing certificate is not present in the federation properties after the federation service certificate has been updated.
        Args:
            value: Value to set for the nextSigningCertificate property.
        """
        self._next_signing_certificate = value
    
    @property
    def prompt_login_behavior(self,) -> Optional[prompt_login_behavior.PromptLoginBehavior]:
        """
        Gets the promptLoginBehavior property value. Sets the preferred behavior for the sign-in prompt. The possible values are: translateToFreshPasswordAuthentication, nativeSupport, disabled, unknownFutureValue.
        Returns: Optional[prompt_login_behavior.PromptLoginBehavior]
        """
        return self._prompt_login_behavior
    
    @prompt_login_behavior.setter
    def prompt_login_behavior(self,value: Optional[prompt_login_behavior.PromptLoginBehavior] = None) -> None:
        """
        Sets the promptLoginBehavior property value. Sets the preferred behavior for the sign-in prompt. The possible values are: translateToFreshPasswordAuthentication, nativeSupport, disabled, unknownFutureValue.
        Args:
            value: Value to set for the promptLoginBehavior property.
        """
        self._prompt_login_behavior = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("activeSignInUri", self.active_sign_in_uri)
        writer.write_enum_value("federatedIdpMfaBehavior", self.federated_idp_mfa_behavior)
        writer.write_bool_value("isSignedAuthenticationRequestRequired", self.is_signed_authentication_request_required)
        writer.write_str_value("nextSigningCertificate", self.next_signing_certificate)
        writer.write_enum_value("promptLoginBehavior", self.prompt_login_behavior)
        writer.write_object_value("signingCertificateUpdateStatus", self.signing_certificate_update_status)
        writer.write_str_value("signOutUri", self.sign_out_uri)
    
    @property
    def signing_certificate_update_status(self,) -> Optional[signing_certificate_update_status.SigningCertificateUpdateStatus]:
        """
        Gets the signingCertificateUpdateStatus property value. Provides status and timestamp of the last update of the signing certificate.
        Returns: Optional[signing_certificate_update_status.SigningCertificateUpdateStatus]
        """
        return self._signing_certificate_update_status
    
    @signing_certificate_update_status.setter
    def signing_certificate_update_status(self,value: Optional[signing_certificate_update_status.SigningCertificateUpdateStatus] = None) -> None:
        """
        Sets the signingCertificateUpdateStatus property value. Provides status and timestamp of the last update of the signing certificate.
        Args:
            value: Value to set for the signingCertificateUpdateStatus property.
        """
        self._signing_certificate_update_status = value
    
    @property
    def sign_out_uri(self,) -> Optional[str]:
        """
        Gets the signOutUri property value. URI that clients are redirected to when they sign out of Azure AD services. Corresponds to the LogOffUri property of the Set-MsolDomainFederationSettings MSOnline v1 PowerShell cmdlet.
        Returns: Optional[str]
        """
        return self._sign_out_uri
    
    @sign_out_uri.setter
    def sign_out_uri(self,value: Optional[str] = None) -> None:
        """
        Sets the signOutUri property value. URI that clients are redirected to when they sign out of Azure AD services. Corresponds to the LogOffUri property of the Set-MsolDomainFederationSettings MSOnline v1 PowerShell cmdlet.
        Args:
            value: Value to set for the signOutUri property.
        """
        self._sign_out_uri = value
    

