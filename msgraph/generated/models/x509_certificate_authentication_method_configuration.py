from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_target import AuthenticationMethodTarget
    from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
    from .x509_certificate_c_r_l_validation_configuration import X509CertificateCRLValidationConfiguration
    from .x509_certificate_user_binding import X509CertificateUserBinding

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class X509CertificateAuthenticationMethodConfiguration(AuthenticationMethodConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration"
    # Defines strong authentication configurations. This configuration includes the default authentication mode and the different rules for strong authentication bindings.
    authentication_mode_configuration: Optional[X509CertificateAuthenticationModeConfiguration] = None
    # Defines fields in the X.509 certificate that map to attributes of the Microsoft Entra user object in order to bind the certificate to the user. The priority of the object determines the order in which the binding is carried out. The first binding that matches will be used and the rest ignored.
    certificate_user_bindings: Optional[list[X509CertificateUserBinding]] = None
    # The crlValidationConfiguration property
    crl_validation_configuration: Optional[X509CertificateCRLValidationConfiguration] = None
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[list[AuthenticationMethodTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> X509CertificateAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return X509CertificateAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
        from .x509_certificate_c_r_l_validation_configuration import X509CertificateCRLValidationConfiguration
        from .x509_certificate_user_binding import X509CertificateUserBinding

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .x509_certificate_authentication_mode_configuration import X509CertificateAuthenticationModeConfiguration
        from .x509_certificate_c_r_l_validation_configuration import X509CertificateCRLValidationConfiguration
        from .x509_certificate_user_binding import X509CertificateUserBinding

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationModeConfiguration": lambda n : setattr(self, 'authentication_mode_configuration', n.get_object_value(X509CertificateAuthenticationModeConfiguration)),
            "certificateUserBindings": lambda n : setattr(self, 'certificate_user_bindings', n.get_collection_of_object_values(X509CertificateUserBinding)),
            "crlValidationConfiguration": lambda n : setattr(self, 'crl_validation_configuration', n.get_object_value(X509CertificateCRLValidationConfiguration)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodTarget)),
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
        writer.write_object_value("authenticationModeConfiguration", self.authentication_mode_configuration)
        writer.write_collection_of_object_values("certificateUserBindings", self.certificate_user_bindings)
        writer.write_object_value("crlValidationConfiguration", self.crl_validation_configuration)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
    

