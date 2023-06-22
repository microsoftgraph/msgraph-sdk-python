from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_authentication_method, entity, fido2_authentication_method, microsoft_authenticator_authentication_method, password_authentication_method, phone_authentication_method, software_oath_authentication_method, temporary_access_pass_authentication_method, windows_hello_for_business_authentication_method

from . import entity

@dataclass
class AuthenticationMethod(entity.Entity):
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethod
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethod".casefold():
            from . import email_authentication_method

            return email_authentication_method.EmailAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethod".casefold():
            from . import fido2_authentication_method

            return fido2_authentication_method.Fido2AuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod".casefold():
            from . import microsoft_authenticator_authentication_method

            return microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.passwordAuthenticationMethod".casefold():
            from . import password_authentication_method

            return password_authentication_method.PasswordAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.phoneAuthenticationMethod".casefold():
            from . import phone_authentication_method

            return phone_authentication_method.PhoneAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethod".casefold():
            from . import software_oath_authentication_method

            return software_oath_authentication_method.SoftwareOathAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethod".casefold():
            from . import temporary_access_pass_authentication_method

            return temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod".casefold():
            from . import windows_hello_for_business_authentication_method

            return windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod()
        return AuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_authentication_method, entity, fido2_authentication_method, microsoft_authenticator_authentication_method, password_authentication_method, phone_authentication_method, software_oath_authentication_method, temporary_access_pass_authentication_method, windows_hello_for_business_authentication_method

        from . import email_authentication_method, entity, fido2_authentication_method, microsoft_authenticator_authentication_method, password_authentication_method, phone_authentication_method, software_oath_authentication_method, temporary_access_pass_authentication_method, windows_hello_for_business_authentication_method

        fields: Dict[str, Callable[[Any], None]] = {
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
    

