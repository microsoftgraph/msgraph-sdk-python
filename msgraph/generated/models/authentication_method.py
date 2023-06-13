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
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.emailAuthenticationMethod":
                from . import email_authentication_method

                return email_authentication_method.EmailAuthenticationMethod()
            if mapping_value == "#microsoft.graph.fido2AuthenticationMethod":
                from . import fido2_authentication_method

                return fido2_authentication_method.Fido2AuthenticationMethod()
            if mapping_value == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod":
                from . import microsoft_authenticator_authentication_method

                return microsoft_authenticator_authentication_method.MicrosoftAuthenticatorAuthenticationMethod()
            if mapping_value == "#microsoft.graph.passwordAuthenticationMethod":
                from . import password_authentication_method

                return password_authentication_method.PasswordAuthenticationMethod()
            if mapping_value == "#microsoft.graph.phoneAuthenticationMethod":
                from . import phone_authentication_method

                return phone_authentication_method.PhoneAuthenticationMethod()
            if mapping_value == "#microsoft.graph.softwareOathAuthenticationMethod":
                from . import software_oath_authentication_method

                return software_oath_authentication_method.SoftwareOathAuthenticationMethod()
            if mapping_value == "#microsoft.graph.temporaryAccessPassAuthenticationMethod":
                from . import temporary_access_pass_authentication_method

                return temporary_access_pass_authentication_method.TemporaryAccessPassAuthenticationMethod()
            if mapping_value == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod":
                from . import windows_hello_for_business_authentication_method

                return windows_hello_for_business_authentication_method.WindowsHelloForBusinessAuthenticationMethod()
        return AuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
    

