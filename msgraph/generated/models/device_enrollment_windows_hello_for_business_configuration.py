from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration
    from .enablement import Enablement
    from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage

from .device_enrollment_configuration import DeviceEnrollmentConfiguration

@dataclass
class DeviceEnrollmentWindowsHelloForBusinessConfiguration(DeviceEnrollmentConfiguration, Parsable):
    """
    Windows Hello for Business settings lets users access their devices using a gesture, such as biometric authentication, or a PIN. Configure settings for enrolled Windows 10, Windows 10 Mobile and later.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration"
    # Possible values of a property
    enhanced_biometrics_state: Optional[Enablement] = None
    # Controls the period of time (in days) that a PIN can be used before the system requires the user to change it. This must be set between 0 and 730, inclusive. If set to 0, the user's PIN will never expire
    pin_expiration_in_days: Optional[int] = None
    # Windows Hello for Business pin usage options
    pin_lowercase_characters_usage: Optional[WindowsHelloForBusinessPinUsage] = None
    # Controls the maximum number of characters allowed for the Windows Hello for Business PIN. This value must be between 4 and 127, inclusive. This value must be greater than or equal to the value set for the minimum PIN.
    pin_maximum_length: Optional[int] = None
    # Controls the minimum number of characters required for the Windows Hello for Business PIN.  This value must be between 4 and 127, inclusive, and less than or equal to the value set for the maximum PIN.
    pin_minimum_length: Optional[int] = None
    # Controls the ability to prevent users from using past PINs. This must be set between 0 and 50, inclusive, and the current PIN of the user is included in that count. If set to 0, previous PINs are not stored. PIN history is not preserved through a PIN reset.
    pin_previous_block_count: Optional[int] = None
    # Windows Hello for Business pin usage options
    pin_special_characters_usage: Optional[WindowsHelloForBusinessPinUsage] = None
    # Windows Hello for Business pin usage options
    pin_uppercase_characters_usage: Optional[WindowsHelloForBusinessPinUsage] = None
    # Controls the use of Remote Windows Hello for Business. Remote Windows Hello for Business provides the ability for a portable, registered device to be usable as a companion for desktop authentication. The desktop must be Azure AD joined and the companion device must have a Windows Hello for Business PIN.
    remote_passport_enabled: Optional[bool] = None
    # Controls whether to require a Trusted Platform Module (TPM) for provisioning Windows Hello for Business. A TPM provides an additional security benefit in that data stored on it cannot be used on other devices. If set to False, all devices can provision Windows Hello for Business even if there is not a usable TPM.
    security_device_required: Optional[bool] = None
    # Possible values of a property
    state: Optional[Enablement] = None
    # Controls the use of biometric gestures, such as face and fingerprint, as an alternative to the Windows Hello for Business PIN.  If set to False, biometric gestures are not allowed. Users must still configure a PIN as a backup in case of failures.
    unlock_with_biometrics_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceEnrollmentWindowsHelloForBusinessConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentWindowsHelloForBusinessConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceEnrollmentWindowsHelloForBusinessConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .enablement import Enablement
        from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage

        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .enablement import Enablement
        from .windows_hello_for_business_pin_usage import WindowsHelloForBusinessPinUsage

        fields: dict[str, Callable[[Any], None]] = {
            "enhancedBiometricsState": lambda n : setattr(self, 'enhanced_biometrics_state', n.get_enum_value(Enablement)),
            "pinExpirationInDays": lambda n : setattr(self, 'pin_expiration_in_days', n.get_int_value()),
            "pinLowercaseCharactersUsage": lambda n : setattr(self, 'pin_lowercase_characters_usage', n.get_enum_value(WindowsHelloForBusinessPinUsage)),
            "pinMaximumLength": lambda n : setattr(self, 'pin_maximum_length', n.get_int_value()),
            "pinMinimumLength": lambda n : setattr(self, 'pin_minimum_length', n.get_int_value()),
            "pinPreviousBlockCount": lambda n : setattr(self, 'pin_previous_block_count', n.get_int_value()),
            "pinSpecialCharactersUsage": lambda n : setattr(self, 'pin_special_characters_usage', n.get_enum_value(WindowsHelloForBusinessPinUsage)),
            "pinUppercaseCharactersUsage": lambda n : setattr(self, 'pin_uppercase_characters_usage', n.get_enum_value(WindowsHelloForBusinessPinUsage)),
            "remotePassportEnabled": lambda n : setattr(self, 'remote_passport_enabled', n.get_bool_value()),
            "securityDeviceRequired": lambda n : setattr(self, 'security_device_required', n.get_bool_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(Enablement)),
            "unlockWithBiometricsEnabled": lambda n : setattr(self, 'unlock_with_biometrics_enabled', n.get_bool_value()),
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
        writer.write_enum_value("enhancedBiometricsState", self.enhanced_biometrics_state)
        writer.write_int_value("pinExpirationInDays", self.pin_expiration_in_days)
        writer.write_enum_value("pinLowercaseCharactersUsage", self.pin_lowercase_characters_usage)
        writer.write_int_value("pinMaximumLength", self.pin_maximum_length)
        writer.write_int_value("pinMinimumLength", self.pin_minimum_length)
        writer.write_int_value("pinPreviousBlockCount", self.pin_previous_block_count)
        writer.write_enum_value("pinSpecialCharactersUsage", self.pin_special_characters_usage)
        writer.write_enum_value("pinUppercaseCharactersUsage", self.pin_uppercase_characters_usage)
        writer.write_bool_value("remotePassportEnabled", self.remote_passport_enabled)
        writer.write_bool_value("securityDeviceRequired", self.security_device_required)
        writer.write_enum_value("state", self.state)
        writer.write_bool_value("unlockWithBiometricsEnabled", self.unlock_with_biometrics_enabled)
    

