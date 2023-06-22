from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_state, email_authentication_method_configuration, entity, exclude_target, fido2_authentication_method_configuration, microsoft_authenticator_authentication_method_configuration, sms_authentication_method_configuration, software_oath_authentication_method_configuration, temporary_access_pass_authentication_method_configuration, voice_authentication_method_configuration, x509_certificate_authentication_method_configuration

from . import entity

@dataclass
class AuthenticationMethodConfiguration(entity.Entity):
    # Groups of users that are excluded from a policy.
    exclude_targets: Optional[List[exclude_target.ExcludeTarget]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of the policy. Possible values are: enabled, disabled.
    state: Optional[authentication_method_state.AuthenticationMethodState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethodConfiguration".casefold():
            from . import email_authentication_method_configuration

            return email_authentication_method_configuration.EmailAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethodConfiguration".casefold():
            from . import fido2_authentication_method_configuration

            return fido2_authentication_method_configuration.Fido2AuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration".casefold():
            from . import microsoft_authenticator_authentication_method_configuration

            return microsoft_authenticator_authentication_method_configuration.MicrosoftAuthenticatorAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodConfiguration".casefold():
            from . import sms_authentication_method_configuration

            return sms_authentication_method_configuration.SmsAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethodConfiguration".casefold():
            from . import software_oath_authentication_method_configuration

            return software_oath_authentication_method_configuration.SoftwareOathAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration".casefold():
            from . import temporary_access_pass_authentication_method_configuration

            return temporary_access_pass_authentication_method_configuration.TemporaryAccessPassAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.voiceAuthenticationMethodConfiguration".casefold():
            from . import voice_authentication_method_configuration

            return voice_authentication_method_configuration.VoiceAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration".casefold():
            from . import x509_certificate_authentication_method_configuration

            return x509_certificate_authentication_method_configuration.X509CertificateAuthenticationMethodConfiguration()
        return AuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_state, email_authentication_method_configuration, entity, exclude_target, fido2_authentication_method_configuration, microsoft_authenticator_authentication_method_configuration, sms_authentication_method_configuration, software_oath_authentication_method_configuration, temporary_access_pass_authentication_method_configuration, voice_authentication_method_configuration, x509_certificate_authentication_method_configuration

        from . import authentication_method_state, email_authentication_method_configuration, entity, exclude_target, fido2_authentication_method_configuration, microsoft_authenticator_authentication_method_configuration, sms_authentication_method_configuration, software_oath_authentication_method_configuration, temporary_access_pass_authentication_method_configuration, voice_authentication_method_configuration, x509_certificate_authentication_method_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "excludeTargets": lambda n : setattr(self, 'exclude_targets', n.get_collection_of_object_values(exclude_target.ExcludeTarget)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(authentication_method_state.AuthenticationMethodState)),
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
        writer.write_collection_of_object_values("excludeTargets", self.exclude_targets)
        writer.write_enum_value("state", self.state)
    

