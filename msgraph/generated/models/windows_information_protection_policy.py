from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_information_protection = lazy_import('msgraph.generated.models.windows_information_protection')
windows_information_protection_pin_character_requirements = lazy_import('msgraph.generated.models.windows_information_protection_pin_character_requirements')

class WindowsInformationProtectionPolicy(windows_information_protection.WindowsInformationProtection):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsInformationProtectionPolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsInformationProtectionPolicy"
        # Offline interval before app data is wiped (days)
        self._days_without_contact_before_unenroll: Optional[int] = None
        # Enrollment url for the MDM
        self._mdm_enrollment_url: Optional[str] = None
        # Specifies the maximum amount of time (in minutes) allowed after the device is idle that will cause the device to become PIN or password locked.   Range is an integer X where 0 <= X <= 999.
        self._minutes_of_inactivity_before_device_lock: Optional[int] = None
        # Integer value that specifies the number of past PINs that can be associated to a user account that can't be reused. The largest number you can configure for this policy setting is 50. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then storage of previous PINs is not required. This node was added in Windows 10, version 1511. Default is 0.
        self._number_of_past_pins_remembered: Optional[int] = None
        # The number of authentication failures allowed before the device will be wiped. A value of 0 disables device wipe functionality. Range is an integer X where 4 <= X <= 16 for desktop and 0 <= X <= 999 for mobile devices.
        self._password_maximum_attempt_count: Optional[int] = None
        # Integer value specifies the period of time (in days) that a PIN can be used before the system requires the user to change it. The largest number you can configure for this policy setting is 730. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then the user's PIN will never expire. This node was added in Windows 10, version 1511. Default is 0.
        self._pin_expiration_days: Optional[int] = None
        # Pin Character Requirements
        self._pin_lowercase_letters: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements] = None
        # Integer value that sets the minimum number of characters required for the PIN. Default value is 4. The lowest number you can configure for this policy setting is 4. The largest number you can configure must be less than the number configured in the Maximum PIN length policy setting or the number 127, whichever is the lowest.
        self._pin_minimum_length: Optional[int] = None
        # Pin Character Requirements
        self._pin_special_characters: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements] = None
        # Pin Character Requirements
        self._pin_uppercase_letters: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements] = None
        # New property in RS2, pending documentation
        self._revoke_on_mdm_handoff_disabled: Optional[bool] = None
        # Boolean value that sets Windows Hello for Business as a method for signing into Windows.
        self._windows_hello_for_business_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionPolicy()
    
    @property
    def days_without_contact_before_unenroll(self,) -> Optional[int]:
        """
        Gets the daysWithoutContactBeforeUnenroll property value. Offline interval before app data is wiped (days)
        Returns: Optional[int]
        """
        return self._days_without_contact_before_unenroll
    
    @days_without_contact_before_unenroll.setter
    def days_without_contact_before_unenroll(self,value: Optional[int] = None) -> None:
        """
        Sets the daysWithoutContactBeforeUnenroll property value. Offline interval before app data is wiped (days)
        Args:
            value: Value to set for the daysWithoutContactBeforeUnenroll property.
        """
        self._days_without_contact_before_unenroll = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "days_without_contact_before_unenroll": lambda n : setattr(self, 'days_without_contact_before_unenroll', n.get_int_value()),
            "mdm_enrollment_url": lambda n : setattr(self, 'mdm_enrollment_url', n.get_str_value()),
            "minutes_of_inactivity_before_device_lock": lambda n : setattr(self, 'minutes_of_inactivity_before_device_lock', n.get_int_value()),
            "number_of_past_pins_remembered": lambda n : setattr(self, 'number_of_past_pins_remembered', n.get_int_value()),
            "password_maximum_attempt_count": lambda n : setattr(self, 'password_maximum_attempt_count', n.get_int_value()),
            "pin_expiration_days": lambda n : setattr(self, 'pin_expiration_days', n.get_int_value()),
            "pin_lowercase_letters": lambda n : setattr(self, 'pin_lowercase_letters', n.get_enum_value(windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements)),
            "pin_minimum_length": lambda n : setattr(self, 'pin_minimum_length', n.get_int_value()),
            "pin_special_characters": lambda n : setattr(self, 'pin_special_characters', n.get_enum_value(windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements)),
            "pin_uppercase_letters": lambda n : setattr(self, 'pin_uppercase_letters', n.get_enum_value(windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements)),
            "revoke_on_mdm_handoff_disabled": lambda n : setattr(self, 'revoke_on_mdm_handoff_disabled', n.get_bool_value()),
            "windows_hello_for_business_blocked": lambda n : setattr(self, 'windows_hello_for_business_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mdm_enrollment_url(self,) -> Optional[str]:
        """
        Gets the mdmEnrollmentUrl property value. Enrollment url for the MDM
        Returns: Optional[str]
        """
        return self._mdm_enrollment_url
    
    @mdm_enrollment_url.setter
    def mdm_enrollment_url(self,value: Optional[str] = None) -> None:
        """
        Sets the mdmEnrollmentUrl property value. Enrollment url for the MDM
        Args:
            value: Value to set for the mdmEnrollmentUrl property.
        """
        self._mdm_enrollment_url = value
    
    @property
    def minutes_of_inactivity_before_device_lock(self,) -> Optional[int]:
        """
        Gets the minutesOfInactivityBeforeDeviceLock property value. Specifies the maximum amount of time (in minutes) allowed after the device is idle that will cause the device to become PIN or password locked.   Range is an integer X where 0 <= X <= 999.
        Returns: Optional[int]
        """
        return self._minutes_of_inactivity_before_device_lock
    
    @minutes_of_inactivity_before_device_lock.setter
    def minutes_of_inactivity_before_device_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the minutesOfInactivityBeforeDeviceLock property value. Specifies the maximum amount of time (in minutes) allowed after the device is idle that will cause the device to become PIN or password locked.   Range is an integer X where 0 <= X <= 999.
        Args:
            value: Value to set for the minutesOfInactivityBeforeDeviceLock property.
        """
        self._minutes_of_inactivity_before_device_lock = value
    
    @property
    def number_of_past_pins_remembered(self,) -> Optional[int]:
        """
        Gets the numberOfPastPinsRemembered property value. Integer value that specifies the number of past PINs that can be associated to a user account that can't be reused. The largest number you can configure for this policy setting is 50. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then storage of previous PINs is not required. This node was added in Windows 10, version 1511. Default is 0.
        Returns: Optional[int]
        """
        return self._number_of_past_pins_remembered
    
    @number_of_past_pins_remembered.setter
    def number_of_past_pins_remembered(self,value: Optional[int] = None) -> None:
        """
        Sets the numberOfPastPinsRemembered property value. Integer value that specifies the number of past PINs that can be associated to a user account that can't be reused. The largest number you can configure for this policy setting is 50. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then storage of previous PINs is not required. This node was added in Windows 10, version 1511. Default is 0.
        Args:
            value: Value to set for the numberOfPastPinsRemembered property.
        """
        self._number_of_past_pins_remembered = value
    
    @property
    def password_maximum_attempt_count(self,) -> Optional[int]:
        """
        Gets the passwordMaximumAttemptCount property value. The number of authentication failures allowed before the device will be wiped. A value of 0 disables device wipe functionality. Range is an integer X where 4 <= X <= 16 for desktop and 0 <= X <= 999 for mobile devices.
        Returns: Optional[int]
        """
        return self._password_maximum_attempt_count
    
    @password_maximum_attempt_count.setter
    def password_maximum_attempt_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMaximumAttemptCount property value. The number of authentication failures allowed before the device will be wiped. A value of 0 disables device wipe functionality. Range is an integer X where 4 <= X <= 16 for desktop and 0 <= X <= 999 for mobile devices.
        Args:
            value: Value to set for the passwordMaximumAttemptCount property.
        """
        self._password_maximum_attempt_count = value
    
    @property
    def pin_expiration_days(self,) -> Optional[int]:
        """
        Gets the pinExpirationDays property value. Integer value specifies the period of time (in days) that a PIN can be used before the system requires the user to change it. The largest number you can configure for this policy setting is 730. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then the user's PIN will never expire. This node was added in Windows 10, version 1511. Default is 0.
        Returns: Optional[int]
        """
        return self._pin_expiration_days
    
    @pin_expiration_days.setter
    def pin_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the pinExpirationDays property value. Integer value specifies the period of time (in days) that a PIN can be used before the system requires the user to change it. The largest number you can configure for this policy setting is 730. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then the user's PIN will never expire. This node was added in Windows 10, version 1511. Default is 0.
        Args:
            value: Value to set for the pinExpirationDays property.
        """
        self._pin_expiration_days = value
    
    @property
    def pin_lowercase_letters(self,) -> Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements]:
        """
        Gets the pinLowercaseLetters property value. Pin Character Requirements
        Returns: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements]
        """
        return self._pin_lowercase_letters
    
    @pin_lowercase_letters.setter
    def pin_lowercase_letters(self,value: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements] = None) -> None:
        """
        Sets the pinLowercaseLetters property value. Pin Character Requirements
        Args:
            value: Value to set for the pinLowercaseLetters property.
        """
        self._pin_lowercase_letters = value
    
    @property
    def pin_minimum_length(self,) -> Optional[int]:
        """
        Gets the pinMinimumLength property value. Integer value that sets the minimum number of characters required for the PIN. Default value is 4. The lowest number you can configure for this policy setting is 4. The largest number you can configure must be less than the number configured in the Maximum PIN length policy setting or the number 127, whichever is the lowest.
        Returns: Optional[int]
        """
        return self._pin_minimum_length
    
    @pin_minimum_length.setter
    def pin_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the pinMinimumLength property value. Integer value that sets the minimum number of characters required for the PIN. Default value is 4. The lowest number you can configure for this policy setting is 4. The largest number you can configure must be less than the number configured in the Maximum PIN length policy setting or the number 127, whichever is the lowest.
        Args:
            value: Value to set for the pinMinimumLength property.
        """
        self._pin_minimum_length = value
    
    @property
    def pin_special_characters(self,) -> Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements]:
        """
        Gets the pinSpecialCharacters property value. Pin Character Requirements
        Returns: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements]
        """
        return self._pin_special_characters
    
    @pin_special_characters.setter
    def pin_special_characters(self,value: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements] = None) -> None:
        """
        Sets the pinSpecialCharacters property value. Pin Character Requirements
        Args:
            value: Value to set for the pinSpecialCharacters property.
        """
        self._pin_special_characters = value
    
    @property
    def pin_uppercase_letters(self,) -> Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements]:
        """
        Gets the pinUppercaseLetters property value. Pin Character Requirements
        Returns: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements]
        """
        return self._pin_uppercase_letters
    
    @pin_uppercase_letters.setter
    def pin_uppercase_letters(self,value: Optional[windows_information_protection_pin_character_requirements.WindowsInformationProtectionPinCharacterRequirements] = None) -> None:
        """
        Sets the pinUppercaseLetters property value. Pin Character Requirements
        Args:
            value: Value to set for the pinUppercaseLetters property.
        """
        self._pin_uppercase_letters = value
    
    @property
    def revoke_on_mdm_handoff_disabled(self,) -> Optional[bool]:
        """
        Gets the revokeOnMdmHandoffDisabled property value. New property in RS2, pending documentation
        Returns: Optional[bool]
        """
        return self._revoke_on_mdm_handoff_disabled
    
    @revoke_on_mdm_handoff_disabled.setter
    def revoke_on_mdm_handoff_disabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the revokeOnMdmHandoffDisabled property value. New property in RS2, pending documentation
        Args:
            value: Value to set for the revokeOnMdmHandoffDisabled property.
        """
        self._revoke_on_mdm_handoff_disabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("daysWithoutContactBeforeUnenroll", self.days_without_contact_before_unenroll)
        writer.write_str_value("mdmEnrollmentUrl", self.mdm_enrollment_url)
        writer.write_int_value("minutesOfInactivityBeforeDeviceLock", self.minutes_of_inactivity_before_device_lock)
        writer.write_int_value("numberOfPastPinsRemembered", self.number_of_past_pins_remembered)
        writer.write_int_value("passwordMaximumAttemptCount", self.password_maximum_attempt_count)
        writer.write_int_value("pinExpirationDays", self.pin_expiration_days)
        writer.write_enum_value("pinLowercaseLetters", self.pin_lowercase_letters)
        writer.write_int_value("pinMinimumLength", self.pin_minimum_length)
        writer.write_enum_value("pinSpecialCharacters", self.pin_special_characters)
        writer.write_enum_value("pinUppercaseLetters", self.pin_uppercase_letters)
        writer.write_bool_value("revokeOnMdmHandoffDisabled", self.revoke_on_mdm_handoff_disabled)
        writer.write_bool_value("windowsHelloForBusinessBlocked", self.windows_hello_for_business_blocked)
    
    @property
    def windows_hello_for_business_blocked(self,) -> Optional[bool]:
        """
        Gets the windowsHelloForBusinessBlocked property value. Boolean value that sets Windows Hello for Business as a method for signing into Windows.
        Returns: Optional[bool]
        """
        return self._windows_hello_for_business_blocked
    
    @windows_hello_for_business_blocked.setter
    def windows_hello_for_business_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsHelloForBusinessBlocked property value. Boolean value that sets Windows Hello for Business as a method for signing into Windows.
        Args:
            value: Value to set for the windowsHelloForBusinessBlocked property.
        """
        self._windows_hello_for_business_blocked = value
    

