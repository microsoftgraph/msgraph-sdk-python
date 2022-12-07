from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method = lazy_import('msgraph.generated.models.authentication_method')
authentication_method_sign_in_state = lazy_import('msgraph.generated.models.authentication_method_sign_in_state')
authentication_phone_type = lazy_import('msgraph.generated.models.authentication_phone_type')

class PhoneAuthenticationMethod(authentication_method.AuthenticationMethod):
    def __init__(self,) -> None:
        """
        Instantiates a new PhoneAuthenticationMethod and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.phoneAuthenticationMethod"
        # The phone number to text or call for authentication. Phone numbers use the format +{country code} {number}x{extension}, with extension optional. For example, +1 5555551234 or +1 5555551234x123 are valid. Numbers are rejected when creating or updating if they do not match the required format.
        self._phone_number: Optional[str] = None
        # The type of this phone. Possible values are: mobile, alternateMobile, or office.
        self._phone_type: Optional[authentication_phone_type.AuthenticationPhoneType] = None
        # Whether a phone is ready to be used for SMS sign-in or not. Possible values are: notSupported, notAllowedByPolicy, notEnabled, phoneNumberNotUnique, ready, or notConfigured, unknownFutureValue.
        self._sms_sign_in_state: Optional[authentication_method_sign_in_state.AuthenticationMethodSignInState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PhoneAuthenticationMethod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PhoneAuthenticationMethod
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PhoneAuthenticationMethod()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "phone_number": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "phone_type": lambda n : setattr(self, 'phone_type', n.get_enum_value(authentication_phone_type.AuthenticationPhoneType)),
            "sms_sign_in_state": lambda n : setattr(self, 'sms_sign_in_state', n.get_enum_value(authentication_method_sign_in_state.AuthenticationMethodSignInState)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def phone_number(self,) -> Optional[str]:
        """
        Gets the phoneNumber property value. The phone number to text or call for authentication. Phone numbers use the format +{country code} {number}x{extension}, with extension optional. For example, +1 5555551234 or +1 5555551234x123 are valid. Numbers are rejected when creating or updating if they do not match the required format.
        Returns: Optional[str]
        """
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneNumber property value. The phone number to text or call for authentication. Phone numbers use the format +{country code} {number}x{extension}, with extension optional. For example, +1 5555551234 or +1 5555551234x123 are valid. Numbers are rejected when creating or updating if they do not match the required format.
        Args:
            value: Value to set for the phoneNumber property.
        """
        self._phone_number = value
    
    @property
    def phone_type(self,) -> Optional[authentication_phone_type.AuthenticationPhoneType]:
        """
        Gets the phoneType property value. The type of this phone. Possible values are: mobile, alternateMobile, or office.
        Returns: Optional[authentication_phone_type.AuthenticationPhoneType]
        """
        return self._phone_type
    
    @phone_type.setter
    def phone_type(self,value: Optional[authentication_phone_type.AuthenticationPhoneType] = None) -> None:
        """
        Sets the phoneType property value. The type of this phone. Possible values are: mobile, alternateMobile, or office.
        Args:
            value: Value to set for the phoneType property.
        """
        self._phone_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_enum_value("phoneType", self.phone_type)
        writer.write_enum_value("smsSignInState", self.sms_sign_in_state)
    
    @property
    def sms_sign_in_state(self,) -> Optional[authentication_method_sign_in_state.AuthenticationMethodSignInState]:
        """
        Gets the smsSignInState property value. Whether a phone is ready to be used for SMS sign-in or not. Possible values are: notSupported, notAllowedByPolicy, notEnabled, phoneNumberNotUnique, ready, or notConfigured, unknownFutureValue.
        Returns: Optional[authentication_method_sign_in_state.AuthenticationMethodSignInState]
        """
        return self._sms_sign_in_state
    
    @sms_sign_in_state.setter
    def sms_sign_in_state(self,value: Optional[authentication_method_sign_in_state.AuthenticationMethodSignInState] = None) -> None:
        """
        Sets the smsSignInState property value. Whether a phone is ready to be used for SMS sign-in or not. Possible values are: notSupported, notAllowedByPolicy, notEnabled, phoneNumberNotUnique, ready, or notConfigured, unknownFutureValue.
        Args:
            value: Value to set for the smsSignInState property.
        """
        self._sms_sign_in_state = value
    

