from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_configuration = lazy_import('msgraph.generated.models.authentication_method_configuration')
authentication_method_target = lazy_import('msgraph.generated.models.authentication_method_target')
x509_certificate_authentication_mode_configuration = lazy_import('msgraph.generated.models.x509_certificate_authentication_mode_configuration')
x509_certificate_user_binding = lazy_import('msgraph.generated.models.x509_certificate_user_binding')

class X509CertificateAuthenticationMethodConfiguration(authentication_method_configuration.AuthenticationMethodConfiguration):
    @property
    def authentication_mode_configuration(self,) -> Optional[x509_certificate_authentication_mode_configuration.X509CertificateAuthenticationModeConfiguration]:
        """
        Gets the authenticationModeConfiguration property value. Defines strong authentication configurations. This configuration includes the default authentication mode and the different rules for strong authentication bindings.
        Returns: Optional[x509_certificate_authentication_mode_configuration.X509CertificateAuthenticationModeConfiguration]
        """
        return self._authentication_mode_configuration
    
    @authentication_mode_configuration.setter
    def authentication_mode_configuration(self,value: Optional[x509_certificate_authentication_mode_configuration.X509CertificateAuthenticationModeConfiguration] = None) -> None:
        """
        Sets the authenticationModeConfiguration property value. Defines strong authentication configurations. This configuration includes the default authentication mode and the different rules for strong authentication bindings.
        Args:
            value: Value to set for the authenticationModeConfiguration property.
        """
        self._authentication_mode_configuration = value
    
    @property
    def certificate_user_bindings(self,) -> Optional[List[x509_certificate_user_binding.X509CertificateUserBinding]]:
        """
        Gets the certificateUserBindings property value. Defines fields in the X.509 certificate that map to attributes of the Azure AD user object in order to bind the certificate to the user. The priority of the object determines the order in which the binding is carried out. The first binding that matches will be used and the rest ignored.
        Returns: Optional[List[x509_certificate_user_binding.X509CertificateUserBinding]]
        """
        return self._certificate_user_bindings
    
    @certificate_user_bindings.setter
    def certificate_user_bindings(self,value: Optional[List[x509_certificate_user_binding.X509CertificateUserBinding]] = None) -> None:
        """
        Sets the certificateUserBindings property value. Defines fields in the X.509 certificate that map to attributes of the Azure AD user object in order to bind the certificate to the user. The priority of the object determines the order in which the binding is carried out. The first binding that matches will be used and the rest ignored.
        Args:
            value: Value to set for the certificateUserBindings property.
        """
        self._certificate_user_bindings = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new X509CertificateAuthenticationMethodConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration"
        # Defines strong authentication configurations. This configuration includes the default authentication mode and the different rules for strong authentication bindings.
        self._authentication_mode_configuration: Optional[x509_certificate_authentication_mode_configuration.X509CertificateAuthenticationModeConfiguration] = None
        # Defines fields in the X.509 certificate that map to attributes of the Azure AD user object in order to bind the certificate to the user. The priority of the object determines the order in which the binding is carried out. The first binding that matches will be used and the rest ignored.
        self._certificate_user_bindings: Optional[List[x509_certificate_user_binding.X509CertificateUserBinding]] = None
        # A collection of users or groups who are enabled to use the authentication method.
        self._include_targets: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None
    
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
        fields = {
            "authentication_mode_configuration": lambda n : setattr(self, 'authentication_mode_configuration', n.get_object_value(x509_certificate_authentication_mode_configuration.X509CertificateAuthenticationModeConfiguration)),
            "certificate_user_bindings": lambda n : setattr(self, 'certificate_user_bindings', n.get_collection_of_object_values(x509_certificate_user_binding.X509CertificateUserBinding)),
            "include_targets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_method_target.AuthenticationMethodTarget)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_targets(self,) -> Optional[List[authentication_method_target.AuthenticationMethodTarget]]:
        """
        Gets the includeTargets property value. A collection of users or groups who are enabled to use the authentication method.
        Returns: Optional[List[authentication_method_target.AuthenticationMethodTarget]]
        """
        return self._include_targets
    
    @include_targets.setter
    def include_targets(self,value: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None) -> None:
        """
        Sets the includeTargets property value. A collection of users or groups who are enabled to use the authentication method.
        Args:
            value: Value to set for the includeTargets property.
        """
        self._include_targets = value
    
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
    

