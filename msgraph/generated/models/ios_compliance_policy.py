from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_policy import DeviceCompliancePolicy
    from .device_threat_protection_level import DeviceThreatProtectionLevel
    from .required_password_type import RequiredPasswordType

from .device_compliance_policy import DeviceCompliancePolicy

@dataclass
class IosCompliancePolicy(DeviceCompliancePolicy, Parsable):
    """
    This class contains compliance settings for IOS.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosCompliancePolicy"
    # Require that devices have enabled device threat protection .
    device_threat_protection_enabled: Optional[bool] = None
    # Device threat protection levels for the Device Threat Protection API.
    device_threat_protection_required_security_level: Optional[DeviceThreatProtectionLevel] = None
    # Indicates whether or not to require a managed email profile.
    managed_email_profile_required: Optional[bool] = None
    # Maximum IOS version.
    os_maximum_version: Optional[str] = None
    # Minimum IOS version.
    os_minimum_version: Optional[str] = None
    # Indicates whether or not to block simple passcodes.
    passcode_block_simple: Optional[bool] = None
    # Number of days before the passcode expires. Valid values 1 to 65535
    passcode_expiration_days: Optional[int] = None
    # The number of character sets required in the password.
    passcode_minimum_character_set_count: Optional[int] = None
    # Minimum length of passcode. Valid values 4 to 14
    passcode_minimum_length: Optional[int] = None
    # Minutes of inactivity before a passcode is required.
    passcode_minutes_of_inactivity_before_lock: Optional[int] = None
    # Number of previous passcodes to block. Valid values 1 to 24
    passcode_previous_passcode_block_count: Optional[int] = None
    # Indicates whether or not to require a passcode.
    passcode_required: Optional[bool] = None
    # Possible values of required passwords.
    passcode_required_type: Optional[RequiredPasswordType] = None
    # Indicates the device should not be jailbroken. When TRUE, if the device is detected as jailbroken it will be reported non-compliant. When FALSE, the device is not reported as non-compliant regardless of device jailbroken state. Default is FALSE.
    security_block_jailbroken_devices: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IosCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosCompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IosCompliancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_threat_protection_level import DeviceThreatProtectionLevel
        from .required_password_type import RequiredPasswordType

        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_threat_protection_level import DeviceThreatProtectionLevel
        from .required_password_type import RequiredPasswordType

        fields: dict[str, Callable[[Any], None]] = {
            "deviceThreatProtectionEnabled": lambda n : setattr(self, 'device_threat_protection_enabled', n.get_bool_value()),
            "deviceThreatProtectionRequiredSecurityLevel": lambda n : setattr(self, 'device_threat_protection_required_security_level', n.get_enum_value(DeviceThreatProtectionLevel)),
            "managedEmailProfileRequired": lambda n : setattr(self, 'managed_email_profile_required', n.get_bool_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passcodeBlockSimple": lambda n : setattr(self, 'passcode_block_simple', n.get_bool_value()),
            "passcodeExpirationDays": lambda n : setattr(self, 'passcode_expiration_days', n.get_int_value()),
            "passcodeMinimumCharacterSetCount": lambda n : setattr(self, 'passcode_minimum_character_set_count', n.get_int_value()),
            "passcodeMinimumLength": lambda n : setattr(self, 'passcode_minimum_length', n.get_int_value()),
            "passcodeMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'passcode_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passcodePreviousPasscodeBlockCount": lambda n : setattr(self, 'passcode_previous_passcode_block_count', n.get_int_value()),
            "passcodeRequired": lambda n : setattr(self, 'passcode_required', n.get_bool_value()),
            "passcodeRequiredType": lambda n : setattr(self, 'passcode_required_type', n.get_enum_value(RequiredPasswordType)),
            "securityBlockJailbrokenDevices": lambda n : setattr(self, 'security_block_jailbroken_devices', n.get_bool_value()),
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
        writer.write_bool_value("deviceThreatProtectionEnabled", self.device_threat_protection_enabled)
        writer.write_enum_value("deviceThreatProtectionRequiredSecurityLevel", self.device_threat_protection_required_security_level)
        writer.write_bool_value("managedEmailProfileRequired", self.managed_email_profile_required)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_bool_value("passcodeBlockSimple", self.passcode_block_simple)
        writer.write_int_value("passcodeExpirationDays", self.passcode_expiration_days)
        writer.write_int_value("passcodeMinimumCharacterSetCount", self.passcode_minimum_character_set_count)
        writer.write_int_value("passcodeMinimumLength", self.passcode_minimum_length)
        writer.write_int_value("passcodeMinutesOfInactivityBeforeLock", self.passcode_minutes_of_inactivity_before_lock)
        writer.write_int_value("passcodePreviousPasscodeBlockCount", self.passcode_previous_passcode_block_count)
        writer.write_bool_value("passcodeRequired", self.passcode_required)
        writer.write_enum_value("passcodeRequiredType", self.passcode_required_type)
        writer.write_bool_value("securityBlockJailbrokenDevices", self.security_block_jailbroken_devices)
    

