from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .application_risk_factor_certificate_info import ApplicationRiskFactorCertificateInfo
    from .password_policy import PasswordPolicy
    from .rest_encryption_type import RestEncryptionType
    from .ssl_version import SslVersion

@dataclass
class ApplicationRiskFactorSecurityInfo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The certificate property
    certificate: Optional[ApplicationRiskFactorCertificateInfo] = None
    # Specifies the domain or hostname evaluated during the security assessment.
    domain_to_check: Optional[str] = None
    # Indicates whether the application maintains an audit trail for administrative actions.
    has_admin_audit_trail: Optional[bool] = None
    # Indicates whether the application allows anonymous or unauthenticated usage.
    has_anonymous_usage: Optional[bool] = None
    # Indicates whether the application logs access or modification of customer data for audit purposes.
    has_data_audit_trail: Optional[bool] = None
    # Indicates whether the application classifies and labels data based on sensitivity levels.
    has_data_classification: Optional[bool] = None
    # Indicates whether data at rest and in transit are encrypted using approved algorithms.
    has_data_encrypted: Optional[bool] = None
    # Indicates whether HTTPS or equivalent secure transport is enforced for all communication channels.
    has_enforce_transport_enc: Optional[bool] = None
    # Indicates whether access to the application can be restricted based on IP address or network range.
    has_ip_restriction: Optional[bool] = None
    # Indicates whether the application supports or enforces multi-factor authentication (MFA).
    has_m_f_a: Optional[bool] = None
    # Indicates whether the application undergoes periodic penetration testing or external security reviews.
    has_pen_test: Optional[bool] = None
    # Indicates whether the application supports password-saving functionality, which may pose a security risk.
    has_remember_password: Optional[bool] = None
    # Indicates whether the application supports SAML-based single sign-on (SSO).
    has_saml_support: Optional[bool] = None
    # Indicates whether user activity is logged for security or compliance monitoring.
    has_user_audit_logs: Optional[bool] = None
    # Indicates whether users can upload or store personal or organizational data within the application.
    has_user_data_upload: Optional[bool] = None
    # Indicates whether the application supports role-based access control (RBAC).
    has_user_roles_support: Optional[bool] = None
    # Indicates whether the certificate’s common name matches the application’s verified domain.
    has_valid_cert_name: Optional[bool] = None
    # Lists the HTTP security headers detected for the application (for example, HSTS, X-Frame-Options, or CSP).
    https_security_headers: Optional[list[str]] = None
    # Indicates whether the application’s certificate is signed by a trusted certificate authority (CA).
    is_cert_trusted: Optional[bool] = None
    # Indicates whether the application is vulnerable to the DROWN (Decrypting RSA with Obsolete and Weakened eNcryption) attack.
    is_drown_vulnerable: Optional[bool] = None
    # Indicates whether the application’s SSL implementation is protected from the Heartbleed vulnerability.
    is_heartbleed_proof: Optional[bool] = None
    # Specifies the date of the last publicly reported data breach or security incident related to the application, if known.
    last_breach_date: Optional[datetime.date] = None
    # The latestValidSSL property
    latest_valid_s_s_l: Optional[SslVersion] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The passwordPolicy property
    password_policy: Optional[PasswordPolicy] = None
    # The restEncryptionType property
    rest_encryption_type: Optional[RestEncryptionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApplicationRiskFactorSecurityInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApplicationRiskFactorSecurityInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApplicationRiskFactorSecurityInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .application_risk_factor_certificate_info import ApplicationRiskFactorCertificateInfo
        from .password_policy import PasswordPolicy
        from .rest_encryption_type import RestEncryptionType
        from .ssl_version import SslVersion

        from .application_risk_factor_certificate_info import ApplicationRiskFactorCertificateInfo
        from .password_policy import PasswordPolicy
        from .rest_encryption_type import RestEncryptionType
        from .ssl_version import SslVersion

        fields: dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_object_value(ApplicationRiskFactorCertificateInfo)),
            "domainToCheck": lambda n : setattr(self, 'domain_to_check', n.get_str_value()),
            "hasAdminAuditTrail": lambda n : setattr(self, 'has_admin_audit_trail', n.get_bool_value()),
            "hasAnonymousUsage": lambda n : setattr(self, 'has_anonymous_usage', n.get_bool_value()),
            "hasDataAuditTrail": lambda n : setattr(self, 'has_data_audit_trail', n.get_bool_value()),
            "hasDataClassification": lambda n : setattr(self, 'has_data_classification', n.get_bool_value()),
            "hasDataEncrypted": lambda n : setattr(self, 'has_data_encrypted', n.get_bool_value()),
            "hasEnforceTransportEnc": lambda n : setattr(self, 'has_enforce_transport_enc', n.get_bool_value()),
            "hasIpRestriction": lambda n : setattr(self, 'has_ip_restriction', n.get_bool_value()),
            "hasMFA": lambda n : setattr(self, 'has_m_f_a', n.get_bool_value()),
            "hasPenTest": lambda n : setattr(self, 'has_pen_test', n.get_bool_value()),
            "hasRememberPassword": lambda n : setattr(self, 'has_remember_password', n.get_bool_value()),
            "hasSamlSupport": lambda n : setattr(self, 'has_saml_support', n.get_bool_value()),
            "hasUserAuditLogs": lambda n : setattr(self, 'has_user_audit_logs', n.get_bool_value()),
            "hasUserDataUpload": lambda n : setattr(self, 'has_user_data_upload', n.get_bool_value()),
            "hasUserRolesSupport": lambda n : setattr(self, 'has_user_roles_support', n.get_bool_value()),
            "hasValidCertName": lambda n : setattr(self, 'has_valid_cert_name', n.get_bool_value()),
            "httpsSecurityHeaders": lambda n : setattr(self, 'https_security_headers', n.get_collection_of_primitive_values(str)),
            "isCertTrusted": lambda n : setattr(self, 'is_cert_trusted', n.get_bool_value()),
            "isDrownVulnerable": lambda n : setattr(self, 'is_drown_vulnerable', n.get_bool_value()),
            "isHeartbleedProof": lambda n : setattr(self, 'is_heartbleed_proof', n.get_bool_value()),
            "lastBreachDate": lambda n : setattr(self, 'last_breach_date', n.get_date_value()),
            "latestValidSSL": lambda n : setattr(self, 'latest_valid_s_s_l', n.get_enum_value(SslVersion)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passwordPolicy": lambda n : setattr(self, 'password_policy', n.get_collection_of_enum_values(PasswordPolicy)),
            "restEncryptionType": lambda n : setattr(self, 'rest_encryption_type', n.get_enum_value(RestEncryptionType)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("certificate", self.certificate)
        writer.write_str_value("domainToCheck", self.domain_to_check)
        writer.write_bool_value("hasAdminAuditTrail", self.has_admin_audit_trail)
        writer.write_bool_value("hasAnonymousUsage", self.has_anonymous_usage)
        writer.write_bool_value("hasDataAuditTrail", self.has_data_audit_trail)
        writer.write_bool_value("hasDataClassification", self.has_data_classification)
        writer.write_bool_value("hasDataEncrypted", self.has_data_encrypted)
        writer.write_bool_value("hasEnforceTransportEnc", self.has_enforce_transport_enc)
        writer.write_bool_value("hasIpRestriction", self.has_ip_restriction)
        writer.write_bool_value("hasMFA", self.has_m_f_a)
        writer.write_bool_value("hasPenTest", self.has_pen_test)
        writer.write_bool_value("hasRememberPassword", self.has_remember_password)
        writer.write_bool_value("hasSamlSupport", self.has_saml_support)
        writer.write_bool_value("hasUserAuditLogs", self.has_user_audit_logs)
        writer.write_bool_value("hasUserDataUpload", self.has_user_data_upload)
        writer.write_bool_value("hasUserRolesSupport", self.has_user_roles_support)
        writer.write_bool_value("hasValidCertName", self.has_valid_cert_name)
        writer.write_collection_of_primitive_values("httpsSecurityHeaders", self.https_security_headers)
        writer.write_bool_value("isCertTrusted", self.is_cert_trusted)
        writer.write_bool_value("isDrownVulnerable", self.is_drown_vulnerable)
        writer.write_bool_value("isHeartbleedProof", self.is_heartbleed_proof)
        writer.write_date_value("lastBreachDate", self.last_breach_date)
        writer.write_enum_value("latestValidSSL", self.latest_valid_s_s_l)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("passwordPolicy", self.password_policy)
        writer.write_enum_value("restEncryptionType", self.rest_encryption_type)
        writer.write_additional_data_value(self.additional_data)
    

