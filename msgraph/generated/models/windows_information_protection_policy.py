from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .windows_information_protection import WindowsInformationProtection
    from .windows_information_protection_pin_character_requirements import WindowsInformationProtectionPinCharacterRequirements

from .windows_information_protection import WindowsInformationProtection

@dataclass
class WindowsInformationProtectionPolicy(WindowsInformationProtection, Parsable):
    """
    Policy for Windows information protection without MDM
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsInformationProtectionPolicy"
    # Offline interval before app data is wiped (days) . Valid values 0 to 999
    days_without_contact_before_unenroll: Optional[int] = None
    # Enrollment url for the MDM
    mdm_enrollment_url: Optional[str] = None
    # Specifies the maximum amount of time (in minutes) allowed after the device is idle that will cause the device to become PIN or password locked.   Range is an integer X where 0 <= X <= 999. Valid values 0 to 999
    minutes_of_inactivity_before_device_lock: Optional[int] = None
    # Integer value that specifies the number of past PINs that can be associated to a user account that can't be reused. The largest number you can configure for this policy setting is 50. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then storage of previous PINs is not required. This node was added in Windows 10, version 1511. Default is 0. Valid values 0 to 50
    number_of_past_pins_remembered: Optional[int] = None
    # The number of authentication failures allowed before the device will be wiped. A value of 0 disables device wipe functionality. Range is an integer X where 4 <= X <= 16 for desktop and 0 <= X <= 999 for mobile devices. Valid values 0 to 999
    password_maximum_attempt_count: Optional[int] = None
    # Integer value specifies the period of time (in days) that a PIN can be used before the system requires the user to change it. The largest number you can configure for this policy setting is 730. The lowest number you can configure for this policy setting is 0. If this policy is set to 0, then the user's PIN will never expire. This node was added in Windows 10, version 1511. Default is 0. Valid values 0 to 730
    pin_expiration_days: Optional[int] = None
    # Pin Character Requirements
    pin_lowercase_letters: Optional[WindowsInformationProtectionPinCharacterRequirements] = None
    # Integer value that sets the minimum number of characters required for the PIN. Default value is 4. The lowest number you can configure for this policy setting is 4. The largest number you can configure must be less than the number configured in the Maximum PIN length policy setting or the number 127, whichever is the lowest. Valid values 0 to 127
    pin_minimum_length: Optional[int] = None
    # Pin Character Requirements
    pin_special_characters: Optional[WindowsInformationProtectionPinCharacterRequirements] = None
    # Pin Character Requirements
    pin_uppercase_letters: Optional[WindowsInformationProtectionPinCharacterRequirements] = None
    # New property in RS2, pending documentation
    revoke_on_mdm_handoff_disabled: Optional[bool] = None
    # Boolean value that sets Windows Hello for Business as a method for signing into Windows.
    windows_hello_for_business_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsInformationProtectionPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsInformationProtectionPolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .windows_information_protection import WindowsInformationProtection
        from .windows_information_protection_pin_character_requirements import WindowsInformationProtectionPinCharacterRequirements

        from .windows_information_protection import WindowsInformationProtection
        from .windows_information_protection_pin_character_requirements import WindowsInformationProtectionPinCharacterRequirements

        fields: dict[str, Callable[[Any], None]] = {
            "daysWithoutContactBeforeUnenroll": lambda n : setattr(self, 'days_without_contact_before_unenroll', n.get_int_value()),
            "mdmEnrollmentUrl": lambda n : setattr(self, 'mdm_enrollment_url', n.get_str_value()),
            "minutesOfInactivityBeforeDeviceLock": lambda n : setattr(self, 'minutes_of_inactivity_before_device_lock', n.get_int_value()),
            "numberOfPastPinsRemembered": lambda n : setattr(self, 'number_of_past_pins_remembered', n.get_int_value()),
            "passwordMaximumAttemptCount": lambda n : setattr(self, 'password_maximum_attempt_count', n.get_int_value()),
            "pinExpirationDays": lambda n : setattr(self, 'pin_expiration_days', n.get_int_value()),
            "pinLowercaseLetters": lambda n : setattr(self, 'pin_lowercase_letters', n.get_enum_value(WindowsInformationProtectionPinCharacterRequirements)),
            "pinMinimumLength": lambda n : setattr(self, 'pin_minimum_length', n.get_int_value()),
            "pinSpecialCharacters": lambda n : setattr(self, 'pin_special_characters', n.get_enum_value(WindowsInformationProtectionPinCharacterRequirements)),
            "pinUppercaseLetters": lambda n : setattr(self, 'pin_uppercase_letters', n.get_enum_value(WindowsInformationProtectionPinCharacterRequirements)),
            "revokeOnMdmHandoffDisabled": lambda n : setattr(self, 'revoke_on_mdm_handoff_disabled', n.get_bool_value()),
            "windowsHelloForBusinessBlocked": lambda n : setattr(self, 'windows_hello_for_business_blocked', n.get_bool_value()),
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
    

