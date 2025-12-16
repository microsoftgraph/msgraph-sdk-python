from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method import AuthenticationMethod
    from .authentication_method_sign_in_state import AuthenticationMethodSignInState
    from .authentication_phone_type import AuthenticationPhoneType

from .authentication_method import AuthenticationMethod

@dataclass
class PhoneAuthenticationMethod(AuthenticationMethod, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.phoneAuthenticationMethod"
    # The phone number to text or call for authentication. Phone numbers use the format +{country code} {number}x{extension}, with extension optional. For example, +1 5555551234 or +1 5555551234x123 are valid. Numbers are rejected when creating or updating if they don't match the required format.
    phone_number: Optional[str] = None
    # The type of this phone. The possible values are: mobile, alternateMobile, or office.
    phone_type: Optional[AuthenticationPhoneType] = None
    # Whether a phone is ready to be used for SMS sign-in or not. The possible values are: notSupported, notAllowedByPolicy, notEnabled, phoneNumberNotUnique, ready, or notConfigured, unknownFutureValue.
    sms_sign_in_state: Optional[AuthenticationMethodSignInState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PhoneAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PhoneAuthenticationMethod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PhoneAuthenticationMethod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method import AuthenticationMethod
        from .authentication_method_sign_in_state import AuthenticationMethodSignInState
        from .authentication_phone_type import AuthenticationPhoneType

        from .authentication_method import AuthenticationMethod
        from .authentication_method_sign_in_state import AuthenticationMethodSignInState
        from .authentication_phone_type import AuthenticationPhoneType

        fields: dict[str, Callable[[Any], None]] = {
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phoneType": lambda n : setattr(self, 'phone_type', n.get_enum_value(AuthenticationPhoneType)),
            "smsSignInState": lambda n : setattr(self, 'sms_sign_in_state', n.get_enum_value(AuthenticationMethodSignInState)),
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
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_enum_value("phoneType", self.phone_type)
        writer.write_enum_value("smsSignInState", self.sms_sign_in_state)
    

