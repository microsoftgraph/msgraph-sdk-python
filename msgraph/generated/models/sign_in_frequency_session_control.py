from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_session_control import ConditionalAccessSessionControl
    from .signin_frequency_type import SigninFrequencyType
    from .sign_in_frequency_authentication_type import SignInFrequencyAuthenticationType
    from .sign_in_frequency_interval import SignInFrequencyInterval

from .conditional_access_session_control import ConditionalAccessSessionControl

@dataclass
class SignInFrequencySessionControl(ConditionalAccessSessionControl, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.signInFrequencySessionControl"
    # The possible values are primaryAndSecondaryAuthentication, secondaryAuthentication, unknownFutureValue. This property isn't required when using frequencyInterval with the value of timeBased.
    authentication_type: Optional[SignInFrequencyAuthenticationType] = None
    # The possible values are timeBased, everyTime, unknownFutureValue. Sign-in frequency of everyTime is available for risky users, risky sign-ins, and Intune device enrollment. For more information, see Require reauthentication every time.
    frequency_interval: Optional[SignInFrequencyInterval] = None
    # The possible values are: days, hours.
    type: Optional[SigninFrequencyType] = None
    # The number of days or hours.
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignInFrequencySessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignInFrequencySessionControl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignInFrequencySessionControl()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_session_control import ConditionalAccessSessionControl
        from .signin_frequency_type import SigninFrequencyType
        from .sign_in_frequency_authentication_type import SignInFrequencyAuthenticationType
        from .sign_in_frequency_interval import SignInFrequencyInterval

        from .conditional_access_session_control import ConditionalAccessSessionControl
        from .signin_frequency_type import SigninFrequencyType
        from .sign_in_frequency_authentication_type import SignInFrequencyAuthenticationType
        from .sign_in_frequency_interval import SignInFrequencyInterval

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationType": lambda n : setattr(self, 'authentication_type', n.get_enum_value(SignInFrequencyAuthenticationType)),
            "frequencyInterval": lambda n : setattr(self, 'frequency_interval', n.get_enum_value(SignInFrequencyInterval)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(SigninFrequencyType)),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        writer.write_enum_value("authenticationType", self.authentication_type)
        writer.write_enum_value("frequencyInterval", self.frequency_interval)
        writer.write_enum_value("type", self.type)
        writer.write_int_value("value", self.value)
    

