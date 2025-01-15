from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_policy import DeviceCompliancePolicy
    from .required_password_type import RequiredPasswordType

from .device_compliance_policy import DeviceCompliancePolicy

@dataclass
class Windows10MobileCompliancePolicy(DeviceCompliancePolicy, Parsable):
    """
    This class contains compliance settings for Windows 10 Mobile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windows10MobileCompliancePolicy"
    # Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
    bit_locker_enabled: Optional[bool] = None
    # Require devices to be reported as healthy by Windows Device Health Attestation.
    code_integrity_enabled: Optional[bool] = None
    # Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
    early_launch_anti_malware_driver_enabled: Optional[bool] = None
    # Maximum Windows Phone version.
    os_maximum_version: Optional[str] = None
    # Minimum Windows Phone version.
    os_minimum_version: Optional[str] = None
    # Whether or not to block syncing the calendar.
    password_block_simple: Optional[bool] = None
    # Number of days before password expiration. Valid values 1 to 255
    password_expiration_days: Optional[int] = None
    # The number of character sets required in the password.
    password_minimum_character_set_count: Optional[int] = None
    # Minimum password length. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before a password is required.
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # The number of previous passwords to prevent re-use of.
    password_previous_password_block_count: Optional[int] = None
    # Require a password to unlock an idle device.
    password_require_to_unlock_from_idle: Optional[bool] = None
    # Require a password to unlock Windows Phone device.
    password_required: Optional[bool] = None
    # Possible values of required passwords.
    password_required_type: Optional[RequiredPasswordType] = None
    # Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
    secure_boot_enabled: Optional[bool] = None
    # Require encryption on windows devices.
    storage_require_encryption: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Windows10MobileCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Windows10MobileCompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Windows10MobileCompliancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_policy import DeviceCompliancePolicy
        from .required_password_type import RequiredPasswordType

        from .device_compliance_policy import DeviceCompliancePolicy
        from .required_password_type import RequiredPasswordType

        fields: dict[str, Callable[[Any], None]] = {
            "bitLockerEnabled": lambda n : setattr(self, 'bit_locker_enabled', n.get_bool_value()),
            "codeIntegrityEnabled": lambda n : setattr(self, 'code_integrity_enabled', n.get_bool_value()),
            "earlyLaunchAntiMalwareDriverEnabled": lambda n : setattr(self, 'early_launch_anti_malware_driver_enabled', n.get_bool_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequireToUnlockFromIdle": lambda n : setattr(self, 'password_require_to_unlock_from_idle', n.get_bool_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(RequiredPasswordType)),
            "secureBootEnabled": lambda n : setattr(self, 'secure_boot_enabled', n.get_bool_value()),
            "storageRequireEncryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
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
        writer.write_bool_value("bitLockerEnabled", self.bit_locker_enabled)
        writer.write_bool_value("codeIntegrityEnabled", self.code_integrity_enabled)
        writer.write_bool_value("earlyLaunchAntiMalwareDriverEnabled", self.early_launch_anti_malware_driver_enabled)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequireToUnlockFromIdle", self.password_require_to_unlock_from_idle)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("secureBootEnabled", self.secure_boot_enabled)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
    

