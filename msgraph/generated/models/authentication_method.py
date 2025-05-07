from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_authentication_method import EmailAuthenticationMethod
    from .entity import Entity
    from .fido2_authentication_method import Fido2AuthenticationMethod
    from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
    from .password_authentication_method import PasswordAuthenticationMethod
    from .phone_authentication_method import PhoneAuthenticationMethod
    from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
    from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
    from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
    from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

from .entity import Entity

@dataclass
class AuthenticationMethod(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethod".casefold():
            from .email_authentication_method import EmailAuthenticationMethod

            return EmailAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethod".casefold():
            from .fido2_authentication_method import Fido2AuthenticationMethod

            return Fido2AuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod".casefold():
            from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod

            return MicrosoftAuthenticatorAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.passwordAuthenticationMethod".casefold():
            from .password_authentication_method import PasswordAuthenticationMethod

            return PasswordAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.phoneAuthenticationMethod".casefold():
            from .phone_authentication_method import PhoneAuthenticationMethod

            return PhoneAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.platformCredentialAuthenticationMethod".casefold():
            from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod

            return PlatformCredentialAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethod".casefold():
            from .software_oath_authentication_method import SoftwareOathAuthenticationMethod

            return SoftwareOathAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethod".casefold():
            from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod

            return TemporaryAccessPassAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod".casefold():
            from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

            return WindowsHelloForBusinessAuthenticationMethod()
        return AuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_authentication_method import EmailAuthenticationMethod
        from .entity import Entity
        from .fido2_authentication_method import Fido2AuthenticationMethod
        from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
        from .password_authentication_method import PasswordAuthenticationMethod
        from .phone_authentication_method import PhoneAuthenticationMethod
        from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
        from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
        from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
        from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

        from .email_authentication_method import EmailAuthenticationMethod
        from .entity import Entity
        from .fido2_authentication_method import Fido2AuthenticationMethod
        from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
        from .password_authentication_method import PasswordAuthenticationMethod
        from .phone_authentication_method import PhoneAuthenticationMethod
        from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
        from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
        from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
        from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

        fields: dict[str, Callable[[Any], None]] = {
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
    

