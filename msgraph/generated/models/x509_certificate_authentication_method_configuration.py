from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_configuration, authentication_method_target, x509_certificate_authentication_mode_configuration, x509_certificate_user_binding

from . import authentication_method_configuration

@dataclass
class X509CertificateAuthenticationMethodConfiguration(authentication_method_configuration.AuthenticationMethodConfiguration):
    odata_type = "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration"
    # Defines strong authentication configurations. This configuration includes the default authentication mode and the different rules for strong authentication bindings.
    authentication_mode_configuration: Optional[x509_certificate_authentication_mode_configuration.X509CertificateAuthenticationModeConfiguration] = None
    # Defines fields in the X.509 certificate that map to attributes of the Azure AD user object in order to bind the certificate to the user. The priority of the object determines the order in which the binding is carried out. The first binding that matches will be used and the rest ignored.
    certificate_user_bindings: Optional[List[x509_certificate_user_binding.X509CertificateUserBinding]] = None
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> X509CertificateAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: X509CertificateAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return X509CertificateAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_configuration, authentication_method_target, x509_certificate_authentication_mode_configuration, x509_certificate_user_binding

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationModeConfiguration": lambda n : setattr(self, 'authentication_mode_configuration', n.get_object_value(x509_certificate_authentication_mode_configuration.X509CertificateAuthenticationModeConfiguration)),
            "certificateUserBindings": lambda n : setattr(self, 'certificate_user_bindings', n.get_collection_of_object_values(x509_certificate_user_binding.X509CertificateUserBinding)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_method_target.AuthenticationMethodTarget)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("authenticationModeConfiguration", self.authentication_mode_configuration)
        writer.write_collection_of_object_values("certificateUserBindings", self.certificate_user_bindings)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
    

