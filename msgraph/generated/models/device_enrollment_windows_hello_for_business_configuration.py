from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_enrollment_configuration = lazy_import('msgraph.generated.models.device_enrollment_configuration')
enablement = lazy_import('msgraph.generated.models.enablement')
windows_hello_for_business_pin_usage = lazy_import('msgraph.generated.models.windows_hello_for_business_pin_usage')

class DeviceEnrollmentWindowsHelloForBusinessConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceEnrollmentWindowsHelloForBusinessConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration"
        # Possible values of a property
        self._enhanced_biometrics_state: Optional[enablement.Enablement] = None
        # Controls the period of time (in days) that a PIN can be used before the system requires the user to change it. This must be set between 0 and 730, inclusive. If set to 0, the user's PIN will never expire
        self._pin_expiration_in_days: Optional[int] = None
        # Windows Hello for Business pin usage options
        self._pin_lowercase_characters_usage: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage] = None
        # Controls the maximum number of characters allowed for the Windows Hello for Business PIN. This value must be between 4 and 127, inclusive. This value must be greater than or equal to the value set for the minimum PIN.
        self._pin_maximum_length: Optional[int] = None
        # Controls the minimum number of characters required for the Windows Hello for Business PIN.  This value must be between 4 and 127, inclusive, and less than or equal to the value set for the maximum PIN.
        self._pin_minimum_length: Optional[int] = None
        # Controls the ability to prevent users from using past PINs. This must be set between 0 and 50, inclusive, and the current PIN of the user is included in that count. If set to 0, previous PINs are not stored. PIN history is not preserved through a PIN reset.
        self._pin_previous_block_count: Optional[int] = None
        # Windows Hello for Business pin usage options
        self._pin_special_characters_usage: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage] = None
        # Windows Hello for Business pin usage options
        self._pin_uppercase_characters_usage: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage] = None
        # Controls the use of Remote Windows Hello for Business. Remote Windows Hello for Business provides the ability for a portable, registered device to be usable as a companion for desktop authentication. The desktop must be Azure AD joined and the companion device must have a Windows Hello for Business PIN.
        self._remote_passport_enabled: Optional[bool] = None
        # Controls whether to require a Trusted Platform Module (TPM) for provisioning Windows Hello for Business. A TPM provides an additional security benefit in that data stored on it cannot be used on other devices. If set to False, all devices can provision Windows Hello for Business even if there is not a usable TPM.
        self._security_device_required: Optional[bool] = None
        # Possible values of a property
        self._state: Optional[enablement.Enablement] = None
        # Controls the use of biometric gestures, such as face and fingerprint, as an alternative to the Windows Hello for Business PIN.  If set to False, biometric gestures are not allowed. Users must still configure a PIN as a backup in case of failures.
        self._unlock_with_biometrics_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentWindowsHelloForBusinessConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentWindowsHelloForBusinessConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEnrollmentWindowsHelloForBusinessConfiguration()
    
    @property
    def enhanced_biometrics_state(self,) -> Optional[enablement.Enablement]:
        """
        Gets the enhancedBiometricsState property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._enhanced_biometrics_state
    
    @enhanced_biometrics_state.setter
    def enhanced_biometrics_state(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the enhancedBiometricsState property value. Possible values of a property
        Args:
            value: Value to set for the enhancedBiometricsState property.
        """
        self._enhanced_biometrics_state = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enhanced_biometrics_state": lambda n : setattr(self, 'enhanced_biometrics_state', n.get_enum_value(enablement.Enablement)),
            "pin_expiration_in_days": lambda n : setattr(self, 'pin_expiration_in_days', n.get_int_value()),
            "pin_lowercase_characters_usage": lambda n : setattr(self, 'pin_lowercase_characters_usage', n.get_enum_value(windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage)),
            "pin_maximum_length": lambda n : setattr(self, 'pin_maximum_length', n.get_int_value()),
            "pin_minimum_length": lambda n : setattr(self, 'pin_minimum_length', n.get_int_value()),
            "pin_previous_block_count": lambda n : setattr(self, 'pin_previous_block_count', n.get_int_value()),
            "pin_special_characters_usage": lambda n : setattr(self, 'pin_special_characters_usage', n.get_enum_value(windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage)),
            "pin_uppercase_characters_usage": lambda n : setattr(self, 'pin_uppercase_characters_usage', n.get_enum_value(windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage)),
            "remote_passport_enabled": lambda n : setattr(self, 'remote_passport_enabled', n.get_bool_value()),
            "security_device_required": lambda n : setattr(self, 'security_device_required', n.get_bool_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(enablement.Enablement)),
            "unlock_with_biometrics_enabled": lambda n : setattr(self, 'unlock_with_biometrics_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def pin_expiration_in_days(self,) -> Optional[int]:
        """
        Gets the pinExpirationInDays property value. Controls the period of time (in days) that a PIN can be used before the system requires the user to change it. This must be set between 0 and 730, inclusive. If set to 0, the user's PIN will never expire
        Returns: Optional[int]
        """
        return self._pin_expiration_in_days
    
    @pin_expiration_in_days.setter
    def pin_expiration_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the pinExpirationInDays property value. Controls the period of time (in days) that a PIN can be used before the system requires the user to change it. This must be set between 0 and 730, inclusive. If set to 0, the user's PIN will never expire
        Args:
            value: Value to set for the pinExpirationInDays property.
        """
        self._pin_expiration_in_days = value
    
    @property
    def pin_lowercase_characters_usage(self,) -> Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage]:
        """
        Gets the pinLowercaseCharactersUsage property value. Windows Hello for Business pin usage options
        Returns: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage]
        """
        return self._pin_lowercase_characters_usage
    
    @pin_lowercase_characters_usage.setter
    def pin_lowercase_characters_usage(self,value: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage] = None) -> None:
        """
        Sets the pinLowercaseCharactersUsage property value. Windows Hello for Business pin usage options
        Args:
            value: Value to set for the pinLowercaseCharactersUsage property.
        """
        self._pin_lowercase_characters_usage = value
    
    @property
    def pin_maximum_length(self,) -> Optional[int]:
        """
        Gets the pinMaximumLength property value. Controls the maximum number of characters allowed for the Windows Hello for Business PIN. This value must be between 4 and 127, inclusive. This value must be greater than or equal to the value set for the minimum PIN.
        Returns: Optional[int]
        """
        return self._pin_maximum_length
    
    @pin_maximum_length.setter
    def pin_maximum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the pinMaximumLength property value. Controls the maximum number of characters allowed for the Windows Hello for Business PIN. This value must be between 4 and 127, inclusive. This value must be greater than or equal to the value set for the minimum PIN.
        Args:
            value: Value to set for the pinMaximumLength property.
        """
        self._pin_maximum_length = value
    
    @property
    def pin_minimum_length(self,) -> Optional[int]:
        """
        Gets the pinMinimumLength property value. Controls the minimum number of characters required for the Windows Hello for Business PIN.  This value must be between 4 and 127, inclusive, and less than or equal to the value set for the maximum PIN.
        Returns: Optional[int]
        """
        return self._pin_minimum_length
    
    @pin_minimum_length.setter
    def pin_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the pinMinimumLength property value. Controls the minimum number of characters required for the Windows Hello for Business PIN.  This value must be between 4 and 127, inclusive, and less than or equal to the value set for the maximum PIN.
        Args:
            value: Value to set for the pinMinimumLength property.
        """
        self._pin_minimum_length = value
    
    @property
    def pin_previous_block_count(self,) -> Optional[int]:
        """
        Gets the pinPreviousBlockCount property value. Controls the ability to prevent users from using past PINs. This must be set between 0 and 50, inclusive, and the current PIN of the user is included in that count. If set to 0, previous PINs are not stored. PIN history is not preserved through a PIN reset.
        Returns: Optional[int]
        """
        return self._pin_previous_block_count
    
    @pin_previous_block_count.setter
    def pin_previous_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the pinPreviousBlockCount property value. Controls the ability to prevent users from using past PINs. This must be set between 0 and 50, inclusive, and the current PIN of the user is included in that count. If set to 0, previous PINs are not stored. PIN history is not preserved through a PIN reset.
        Args:
            value: Value to set for the pinPreviousBlockCount property.
        """
        self._pin_previous_block_count = value
    
    @property
    def pin_special_characters_usage(self,) -> Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage]:
        """
        Gets the pinSpecialCharactersUsage property value. Windows Hello for Business pin usage options
        Returns: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage]
        """
        return self._pin_special_characters_usage
    
    @pin_special_characters_usage.setter
    def pin_special_characters_usage(self,value: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage] = None) -> None:
        """
        Sets the pinSpecialCharactersUsage property value. Windows Hello for Business pin usage options
        Args:
            value: Value to set for the pinSpecialCharactersUsage property.
        """
        self._pin_special_characters_usage = value
    
    @property
    def pin_uppercase_characters_usage(self,) -> Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage]:
        """
        Gets the pinUppercaseCharactersUsage property value. Windows Hello for Business pin usage options
        Returns: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage]
        """
        return self._pin_uppercase_characters_usage
    
    @pin_uppercase_characters_usage.setter
    def pin_uppercase_characters_usage(self,value: Optional[windows_hello_for_business_pin_usage.WindowsHelloForBusinessPinUsage] = None) -> None:
        """
        Sets the pinUppercaseCharactersUsage property value. Windows Hello for Business pin usage options
        Args:
            value: Value to set for the pinUppercaseCharactersUsage property.
        """
        self._pin_uppercase_characters_usage = value
    
    @property
    def remote_passport_enabled(self,) -> Optional[bool]:
        """
        Gets the remotePassportEnabled property value. Controls the use of Remote Windows Hello for Business. Remote Windows Hello for Business provides the ability for a portable, registered device to be usable as a companion for desktop authentication. The desktop must be Azure AD joined and the companion device must have a Windows Hello for Business PIN.
        Returns: Optional[bool]
        """
        return self._remote_passport_enabled
    
    @remote_passport_enabled.setter
    def remote_passport_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the remotePassportEnabled property value. Controls the use of Remote Windows Hello for Business. Remote Windows Hello for Business provides the ability for a portable, registered device to be usable as a companion for desktop authentication. The desktop must be Azure AD joined and the companion device must have a Windows Hello for Business PIN.
        Args:
            value: Value to set for the remotePassportEnabled property.
        """
        self._remote_passport_enabled = value
    
    @property
    def security_device_required(self,) -> Optional[bool]:
        """
        Gets the securityDeviceRequired property value. Controls whether to require a Trusted Platform Module (TPM) for provisioning Windows Hello for Business. A TPM provides an additional security benefit in that data stored on it cannot be used on other devices. If set to False, all devices can provision Windows Hello for Business even if there is not a usable TPM.
        Returns: Optional[bool]
        """
        return self._security_device_required
    
    @security_device_required.setter
    def security_device_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityDeviceRequired property value. Controls whether to require a Trusted Platform Module (TPM) for provisioning Windows Hello for Business. A TPM provides an additional security benefit in that data stored on it cannot be used on other devices. If set to False, all devices can provision Windows Hello for Business even if there is not a usable TPM.
        Args:
            value: Value to set for the securityDeviceRequired property.
        """
        self._security_device_required = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def state(self,) -> Optional[enablement.Enablement]:
        """
        Gets the state property value. Possible values of a property
        Returns: Optional[enablement.Enablement]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[enablement.Enablement] = None) -> None:
        """
        Sets the state property value. Possible values of a property
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def unlock_with_biometrics_enabled(self,) -> Optional[bool]:
        """
        Gets the unlockWithBiometricsEnabled property value. Controls the use of biometric gestures, such as face and fingerprint, as an alternative to the Windows Hello for Business PIN.  If set to False, biometric gestures are not allowed. Users must still configure a PIN as a backup in case of failures.
        Returns: Optional[bool]
        """
        return self._unlock_with_biometrics_enabled
    
    @unlock_with_biometrics_enabled.setter
    def unlock_with_biometrics_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the unlockWithBiometricsEnabled property value. Controls the use of biometric gestures, such as face and fingerprint, as an alternative to the Windows Hello for Business PIN.  If set to False, biometric gestures are not allowed. Users must still configure a PIN as a backup in case of failures.
        Args:
            value: Value to set for the unlockWithBiometricsEnabled property.
        """
        self._unlock_with_biometrics_enabled = value
    

