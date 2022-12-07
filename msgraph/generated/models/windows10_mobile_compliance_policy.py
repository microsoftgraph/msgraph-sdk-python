from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_compliance_policy = lazy_import('msgraph.generated.models.device_compliance_policy')
required_password_type = lazy_import('msgraph.generated.models.required_password_type')

class Windows10MobileCompliancePolicy(device_compliance_policy.DeviceCompliancePolicy):
    @property
    def bit_locker_enabled(self,) -> Optional[bool]:
        """
        Gets the bitLockerEnabled property value. Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        Returns: Optional[bool]
        """
        return self._bit_locker_enabled
    
    @bit_locker_enabled.setter
    def bit_locker_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerEnabled property value. Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        Args:
            value: Value to set for the bitLockerEnabled property.
        """
        self._bit_locker_enabled = value
    
    @property
    def code_integrity_enabled(self,) -> Optional[bool]:
        """
        Gets the codeIntegrityEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Returns: Optional[bool]
        """
        return self._code_integrity_enabled
    
    @code_integrity_enabled.setter
    def code_integrity_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the codeIntegrityEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Args:
            value: Value to set for the codeIntegrityEnabled property.
        """
        self._code_integrity_enabled = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10MobileCompliancePolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10MobileCompliancePolicy"
        # Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        self._bit_locker_enabled: Optional[bool] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation.
        self._code_integrity_enabled: Optional[bool] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        self._early_launch_anti_malware_driver_enabled: Optional[bool] = None
        # Maximum Windows Phone version.
        self._os_maximum_version: Optional[str] = None
        # Minimum Windows Phone version.
        self._os_minimum_version: Optional[str] = None
        # Whether or not to block syncing the calendar.
        self._password_block_simple: Optional[bool] = None
        # Number of days before password expiration. Valid values 1 to 255
        self._password_expiration_days: Optional[int] = None
        # The number of character sets required in the password.
        self._password_minimum_character_set_count: Optional[int] = None
        # Minimum password length. Valid values 4 to 16
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before a password is required.
        self._password_minutes_of_inactivity_before_lock: Optional[int] = None
        # The number of previous passwords to prevent re-use of.
        self._password_previous_password_block_count: Optional[int] = None
        # Require a password to unlock Windows Phone device.
        self._password_required: Optional[bool] = None
        # Possible values of required passwords.
        self._password_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # Require a password to unlock an idle device.
        self._password_require_to_unlock_from_idle: Optional[bool] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        self._secure_boot_enabled: Optional[bool] = None
        # Require encryption on windows devices.
        self._storage_require_encryption: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10MobileCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10MobileCompliancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10MobileCompliancePolicy()
    
    @property
    def early_launch_anti_malware_driver_enabled(self,) -> Optional[bool]:
        """
        Gets the earlyLaunchAntiMalwareDriverEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        Returns: Optional[bool]
        """
        return self._early_launch_anti_malware_driver_enabled
    
    @early_launch_anti_malware_driver_enabled.setter
    def early_launch_anti_malware_driver_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the earlyLaunchAntiMalwareDriverEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        Args:
            value: Value to set for the earlyLaunchAntiMalwareDriverEnabled property.
        """
        self._early_launch_anti_malware_driver_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bit_locker_enabled": lambda n : setattr(self, 'bit_locker_enabled', n.get_bool_value()),
            "code_integrity_enabled": lambda n : setattr(self, 'code_integrity_enabled', n.get_bool_value()),
            "early_launch_anti_malware_driver_enabled": lambda n : setattr(self, 'early_launch_anti_malware_driver_enabled', n.get_bool_value()),
            "os_maximum_version": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "os_minimum_version": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "password_block_simple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_character_set_count": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_lock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "password_require_to_unlock_from_idle": lambda n : setattr(self, 'password_require_to_unlock_from_idle', n.get_bool_value()),
            "secure_boot_enabled": lambda n : setattr(self, 'secure_boot_enabled', n.get_bool_value()),
            "storage_require_encryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def os_maximum_version(self,) -> Optional[str]:
        """
        Gets the osMaximumVersion property value. Maximum Windows Phone version.
        Returns: Optional[str]
        """
        return self._os_maximum_version
    
    @os_maximum_version.setter
    def os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumVersion property value. Maximum Windows Phone version.
        Args:
            value: Value to set for the osMaximumVersion property.
        """
        self._os_maximum_version = value
    
    @property
    def os_minimum_version(self,) -> Optional[str]:
        """
        Gets the osMinimumVersion property value. Minimum Windows Phone version.
        Returns: Optional[str]
        """
        return self._os_minimum_version
    
    @os_minimum_version.setter
    def os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumVersion property value. Minimum Windows Phone version.
        Args:
            value: Value to set for the osMinimumVersion property.
        """
        self._os_minimum_version = value
    
    @property
    def password_block_simple(self,) -> Optional[bool]:
        """
        Gets the passwordBlockSimple property value. Whether or not to block syncing the calendar.
        Returns: Optional[bool]
        """
        return self._password_block_simple
    
    @password_block_simple.setter
    def password_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockSimple property value. Whether or not to block syncing the calendar.
        Args:
            value: Value to set for the passwordBlockSimple property.
        """
        self._password_block_simple = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Number of days before password expiration. Valid values 1 to 255
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Number of days before password expiration. Valid values 1 to 255
        Args:
            value: Value to set for the passwordExpirationDays property.
        """
        self._password_expiration_days = value
    
    @property
    def password_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Returns: Optional[int]
        """
        return self._password_minimum_character_set_count
    
    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Args:
            value: Value to set for the passwordMinimumCharacterSetCount property.
        """
        self._password_minimum_character_set_count = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Minimum password length. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Minimum password length. Valid values 4 to 16
        Args:
            value: Value to set for the passwordMinimumLength property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_lock(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a password is required.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_lock
    
    @password_minutes_of_inactivity_before_lock.setter
    def password_minutes_of_inactivity_before_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a password is required.
        Args:
            value: Value to set for the passwordMinutesOfInactivityBeforeLock property.
        """
        self._password_minutes_of_inactivity_before_lock = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent re-use of.
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent re-use of.
        Args:
            value: Value to set for the passwordPreviousPasswordBlockCount property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_required(self,) -> Optional[bool]:
        """
        Gets the passwordRequired property value. Require a password to unlock Windows Phone device.
        Returns: Optional[bool]
        """
        return self._password_required
    
    @password_required.setter
    def password_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequired property value. Require a password to unlock Windows Phone device.
        Args:
            value: Value to set for the passwordRequired property.
        """
        self._password_required = value
    
    @property
    def password_required_type(self,) -> Optional[required_password_type.RequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Possible values of required passwords.
        Returns: Optional[required_password_type.RequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[required_password_type.RequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Possible values of required passwords.
        Args:
            value: Value to set for the passwordRequiredType property.
        """
        self._password_required_type = value
    
    @property
    def password_require_to_unlock_from_idle(self,) -> Optional[bool]:
        """
        Gets the passwordRequireToUnlockFromIdle property value. Require a password to unlock an idle device.
        Returns: Optional[bool]
        """
        return self._password_require_to_unlock_from_idle
    
    @password_require_to_unlock_from_idle.setter
    def password_require_to_unlock_from_idle(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequireToUnlockFromIdle property value. Require a password to unlock an idle device.
        Args:
            value: Value to set for the passwordRequireToUnlockFromIdle property.
        """
        self._password_require_to_unlock_from_idle = value
    
    @property
    def secure_boot_enabled(self,) -> Optional[bool]:
        """
        Gets the secureBootEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        Returns: Optional[bool]
        """
        return self._secure_boot_enabled
    
    @secure_boot_enabled.setter
    def secure_boot_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the secureBootEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        Args:
            value: Value to set for the secureBootEnabled property.
        """
        self._secure_boot_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("passwordRequireToUnlockFromIdle", self.password_require_to_unlock_from_idle)
        writer.write_bool_value("secureBootEnabled", self.secure_boot_enabled)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
    
    @property
    def storage_require_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireEncryption property value. Require encryption on windows devices.
        Returns: Optional[bool]
        """
        return self._storage_require_encryption
    
    @storage_require_encryption.setter
    def storage_require_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireEncryption property value. Require encryption on windows devices.
        Args:
            value: Value to set for the storageRequireEncryption property.
        """
        self._storage_require_encryption = value
    

