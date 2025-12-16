from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_state import AuthenticationMethodState
    from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
    from .entity import Entity
    from .exclude_target import ExcludeTarget
    from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
    from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
    from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
    from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
    from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
    from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
    from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

from .entity import Entity

@dataclass
class AuthenticationMethodConfiguration(Entity, Parsable):
    # Groups of users that are excluded from a policy.
    exclude_targets: Optional[list[ExcludeTarget]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state of the policy. The possible values are: enabled, disabled.
    state: Optional[AuthenticationMethodState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethodConfiguration".casefold():
            from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration

            return EmailAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethodConfiguration".casefold():
            from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration

            return Fido2AuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration".casefold():
            from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration

            return MicrosoftAuthenticatorAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodConfiguration".casefold():
            from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration

            return SmsAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethodConfiguration".casefold():
            from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration

            return SoftwareOathAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration".casefold():
            from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration

            return TemporaryAccessPassAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.voiceAuthenticationMethodConfiguration".casefold():
            from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration

            return VoiceAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration".casefold():
            from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

            return X509CertificateAuthenticationMethodConfiguration()
        return AuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_state import AuthenticationMethodState
        from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
        from .entity import Entity
        from .exclude_target import ExcludeTarget
        from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
        from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
        from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
        from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
        from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
        from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
        from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

        from .authentication_method_state import AuthenticationMethodState
        from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
        from .entity import Entity
        from .exclude_target import ExcludeTarget
        from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
        from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
        from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
        from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
        from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
        from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
        from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "excludeTargets": lambda n : setattr(self, 'exclude_targets', n.get_collection_of_object_values(ExcludeTarget)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(AuthenticationMethodState)),
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
        writer.write_collection_of_object_values("excludeTargets", self.exclude_targets)
        writer.write_enum_value("state", self.state)
    

