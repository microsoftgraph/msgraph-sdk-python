from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

conditional_access_session_control = lazy_import('msgraph.generated.models.conditional_access_session_control')
sign_in_frequency_authentication_type = lazy_import('msgraph.generated.models.sign_in_frequency_authentication_type')
sign_in_frequency_interval = lazy_import('msgraph.generated.models.sign_in_frequency_interval')
signin_frequency_type = lazy_import('msgraph.generated.models.signin_frequency_type')

class SignInFrequencySessionControl(conditional_access_session_control.ConditionalAccessSessionControl):
    @property
    def authentication_type(self,) -> Optional[sign_in_frequency_authentication_type.SignInFrequencyAuthenticationType]:
        """
        Gets the authenticationType property value. The possible values are primaryAndSecondaryAuthentication, secondaryAuthentication, unknownFutureValue.
        Returns: Optional[sign_in_frequency_authentication_type.SignInFrequencyAuthenticationType]
        """
        return self._authentication_type
    
    @authentication_type.setter
    def authentication_type(self,value: Optional[sign_in_frequency_authentication_type.SignInFrequencyAuthenticationType] = None) -> None:
        """
        Sets the authenticationType property value. The possible values are primaryAndSecondaryAuthentication, secondaryAuthentication, unknownFutureValue.
        Args:
            value: Value to set for the authenticationType property.
        """
        self._authentication_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new SignInFrequencySessionControl and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.signInFrequencySessionControl"
        # The possible values are primaryAndSecondaryAuthentication, secondaryAuthentication, unknownFutureValue.
        self._authentication_type: Optional[sign_in_frequency_authentication_type.SignInFrequencyAuthenticationType] = None
        # The possible values are timeBased, everyTime, unknownFutureValue.
        self._frequency_interval: Optional[sign_in_frequency_interval.SignInFrequencyInterval] = None
        # Possible values are: days, hours.
        self._type: Optional[signin_frequency_type.SigninFrequencyType] = None
        # The number of days or hours.
        self._value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SignInFrequencySessionControl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SignInFrequencySessionControl
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SignInFrequencySessionControl()
    
    @property
    def frequency_interval(self,) -> Optional[sign_in_frequency_interval.SignInFrequencyInterval]:
        """
        Gets the frequencyInterval property value. The possible values are timeBased, everyTime, unknownFutureValue.
        Returns: Optional[sign_in_frequency_interval.SignInFrequencyInterval]
        """
        return self._frequency_interval
    
    @frequency_interval.setter
    def frequency_interval(self,value: Optional[sign_in_frequency_interval.SignInFrequencyInterval] = None) -> None:
        """
        Sets the frequencyInterval property value. The possible values are timeBased, everyTime, unknownFutureValue.
        Args:
            value: Value to set for the frequencyInterval property.
        """
        self._frequency_interval = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_type": lambda n : setattr(self, 'authentication_type', n.get_enum_value(sign_in_frequency_authentication_type.SignInFrequencyAuthenticationType)),
            "frequency_interval": lambda n : setattr(self, 'frequency_interval', n.get_enum_value(sign_in_frequency_interval.SignInFrequencyInterval)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(signin_frequency_type.SigninFrequencyType)),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        writer.write_enum_value("authenticationType", self.authentication_type)
        writer.write_enum_value("frequencyInterval", self.frequency_interval)
        writer.write_enum_value("type", self.type)
        writer.write_int_value("value", self.value)
    
    @property
    def type(self,) -> Optional[signin_frequency_type.SigninFrequencyType]:
        """
        Gets the type property value. Possible values are: days, hours.
        Returns: Optional[signin_frequency_type.SigninFrequencyType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[signin_frequency_type.SigninFrequencyType] = None) -> None:
        """
        Sets the type property value. Possible values are: days, hours.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def value(self,) -> Optional[int]:
        """
        Gets the value property value. The number of days or hours.
        Returns: Optional[int]
        """
        return self._value
    
    @value.setter
    def value(self,value: Optional[int] = None) -> None:
        """
        Sets the value property value. The number of days or hours.
        Args:
            value: Value to set for the value property.
        """
        self._value = value
    

