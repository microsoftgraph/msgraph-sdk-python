from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_compliance_policy = lazy_import('msgraph.generated.models.device_compliance_policy')
device_threat_protection_level = lazy_import('msgraph.generated.models.device_threat_protection_level')
required_password_type = lazy_import('msgraph.generated.models.required_password_type')

class IosCompliancePolicy(device_compliance_policy.DeviceCompliancePolicy):
    def __init__(self,) -> None:
        """
        Instantiates a new IosCompliancePolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosCompliancePolicy"
        # Require that devices have enabled device threat protection .
        self._device_threat_protection_enabled: Optional[bool] = None
        # Device threat protection levels for the Device Threat Protection API.
        self._device_threat_protection_required_security_level: Optional[device_threat_protection_level.DeviceThreatProtectionLevel] = None
        # Indicates whether or not to require a managed email profile.
        self._managed_email_profile_required: Optional[bool] = None
        # Maximum IOS version.
        self._os_maximum_version: Optional[str] = None
        # Minimum IOS version.
        self._os_minimum_version: Optional[str] = None
        # Indicates whether or not to block simple passcodes.
        self._passcode_block_simple: Optional[bool] = None
        # Number of days before the passcode expires. Valid values 1 to 65535
        self._passcode_expiration_days: Optional[int] = None
        # The number of character sets required in the password.
        self._passcode_minimum_character_set_count: Optional[int] = None
        # Minimum length of passcode. Valid values 4 to 14
        self._passcode_minimum_length: Optional[int] = None
        # Minutes of inactivity before a passcode is required.
        self._passcode_minutes_of_inactivity_before_lock: Optional[int] = None
        # Number of previous passcodes to block. Valid values 1 to 24
        self._passcode_previous_passcode_block_count: Optional[int] = None
        # Indicates whether or not to require a passcode.
        self._passcode_required: Optional[bool] = None
        # Possible values of required passwords.
        self._passcode_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # Devices must not be jailbroken or rooted.
        self._security_block_jailbroken_devices: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosCompliancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosCompliancePolicy()
    
    @property
    def device_threat_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the deviceThreatProtectionEnabled property value. Require that devices have enabled device threat protection .
        Returns: Optional[bool]
        """
        return self._device_threat_protection_enabled
    
    @device_threat_protection_enabled.setter
    def device_threat_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceThreatProtectionEnabled property value. Require that devices have enabled device threat protection .
        Args:
            value: Value to set for the deviceThreatProtectionEnabled property.
        """
        self._device_threat_protection_enabled = value
    
    @property
    def device_threat_protection_required_security_level(self,) -> Optional[device_threat_protection_level.DeviceThreatProtectionLevel]:
        """
        Gets the deviceThreatProtectionRequiredSecurityLevel property value. Device threat protection levels for the Device Threat Protection API.
        Returns: Optional[device_threat_protection_level.DeviceThreatProtectionLevel]
        """
        return self._device_threat_protection_required_security_level
    
    @device_threat_protection_required_security_level.setter
    def device_threat_protection_required_security_level(self,value: Optional[device_threat_protection_level.DeviceThreatProtectionLevel] = None) -> None:
        """
        Sets the deviceThreatProtectionRequiredSecurityLevel property value. Device threat protection levels for the Device Threat Protection API.
        Args:
            value: Value to set for the deviceThreatProtectionRequiredSecurityLevel property.
        """
        self._device_threat_protection_required_security_level = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_threat_protection_enabled": lambda n : setattr(self, 'device_threat_protection_enabled', n.get_bool_value()),
            "device_threat_protection_required_security_level": lambda n : setattr(self, 'device_threat_protection_required_security_level', n.get_enum_value(device_threat_protection_level.DeviceThreatProtectionLevel)),
            "managed_email_profile_required": lambda n : setattr(self, 'managed_email_profile_required', n.get_bool_value()),
            "os_maximum_version": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "os_minimum_version": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passcode_block_simple": lambda n : setattr(self, 'passcode_block_simple', n.get_bool_value()),
            "passcode_expiration_days": lambda n : setattr(self, 'passcode_expiration_days', n.get_int_value()),
            "passcode_minimum_character_set_count": lambda n : setattr(self, 'passcode_minimum_character_set_count', n.get_int_value()),
            "passcode_minimum_length": lambda n : setattr(self, 'passcode_minimum_length', n.get_int_value()),
            "passcode_minutes_of_inactivity_before_lock": lambda n : setattr(self, 'passcode_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passcode_previous_passcode_block_count": lambda n : setattr(self, 'passcode_previous_passcode_block_count', n.get_int_value()),
            "passcode_required": lambda n : setattr(self, 'passcode_required', n.get_bool_value()),
            "passcode_required_type": lambda n : setattr(self, 'passcode_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "security_block_jailbroken_devices": lambda n : setattr(self, 'security_block_jailbroken_devices', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_email_profile_required(self,) -> Optional[bool]:
        """
        Gets the managedEmailProfileRequired property value. Indicates whether or not to require a managed email profile.
        Returns: Optional[bool]
        """
        return self._managed_email_profile_required
    
    @managed_email_profile_required.setter
    def managed_email_profile_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the managedEmailProfileRequired property value. Indicates whether or not to require a managed email profile.
        Args:
            value: Value to set for the managedEmailProfileRequired property.
        """
        self._managed_email_profile_required = value
    
    @property
    def os_maximum_version(self,) -> Optional[str]:
        """
        Gets the osMaximumVersion property value. Maximum IOS version.
        Returns: Optional[str]
        """
        return self._os_maximum_version
    
    @os_maximum_version.setter
    def os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumVersion property value. Maximum IOS version.
        Args:
            value: Value to set for the osMaximumVersion property.
        """
        self._os_maximum_version = value
    
    @property
    def os_minimum_version(self,) -> Optional[str]:
        """
        Gets the osMinimumVersion property value. Minimum IOS version.
        Returns: Optional[str]
        """
        return self._os_minimum_version
    
    @os_minimum_version.setter
    def os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumVersion property value. Minimum IOS version.
        Args:
            value: Value to set for the osMinimumVersion property.
        """
        self._os_minimum_version = value
    
    @property
    def passcode_block_simple(self,) -> Optional[bool]:
        """
        Gets the passcodeBlockSimple property value. Indicates whether or not to block simple passcodes.
        Returns: Optional[bool]
        """
        return self._passcode_block_simple
    
    @passcode_block_simple.setter
    def passcode_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeBlockSimple property value. Indicates whether or not to block simple passcodes.
        Args:
            value: Value to set for the passcodeBlockSimple property.
        """
        self._passcode_block_simple = value
    
    @property
    def passcode_expiration_days(self,) -> Optional[int]:
        """
        Gets the passcodeExpirationDays property value. Number of days before the passcode expires. Valid values 1 to 65535
        Returns: Optional[int]
        """
        return self._passcode_expiration_days
    
    @passcode_expiration_days.setter
    def passcode_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeExpirationDays property value. Number of days before the passcode expires. Valid values 1 to 65535
        Args:
            value: Value to set for the passcodeExpirationDays property.
        """
        self._passcode_expiration_days = value
    
    @property
    def passcode_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passcodeMinimumCharacterSetCount property value. The number of character sets required in the password.
        Returns: Optional[int]
        """
        return self._passcode_minimum_character_set_count
    
    @passcode_minimum_character_set_count.setter
    def passcode_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinimumCharacterSetCount property value. The number of character sets required in the password.
        Args:
            value: Value to set for the passcodeMinimumCharacterSetCount property.
        """
        self._passcode_minimum_character_set_count = value
    
    @property
    def passcode_minimum_length(self,) -> Optional[int]:
        """
        Gets the passcodeMinimumLength property value. Minimum length of passcode. Valid values 4 to 14
        Returns: Optional[int]
        """
        return self._passcode_minimum_length
    
    @passcode_minimum_length.setter
    def passcode_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinimumLength property value. Minimum length of passcode. Valid values 4 to 14
        Args:
            value: Value to set for the passcodeMinimumLength property.
        """
        self._passcode_minimum_length = value
    
    @property
    def passcode_minutes_of_inactivity_before_lock(self,) -> Optional[int]:
        """
        Gets the passcodeMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a passcode is required.
        Returns: Optional[int]
        """
        return self._passcode_minutes_of_inactivity_before_lock
    
    @passcode_minutes_of_inactivity_before_lock.setter
    def passcode_minutes_of_inactivity_before_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodeMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a passcode is required.
        Args:
            value: Value to set for the passcodeMinutesOfInactivityBeforeLock property.
        """
        self._passcode_minutes_of_inactivity_before_lock = value
    
    @property
    def passcode_previous_passcode_block_count(self,) -> Optional[int]:
        """
        Gets the passcodePreviousPasscodeBlockCount property value. Number of previous passcodes to block. Valid values 1 to 24
        Returns: Optional[int]
        """
        return self._passcode_previous_passcode_block_count
    
    @passcode_previous_passcode_block_count.setter
    def passcode_previous_passcode_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passcodePreviousPasscodeBlockCount property value. Number of previous passcodes to block. Valid values 1 to 24
        Args:
            value: Value to set for the passcodePreviousPasscodeBlockCount property.
        """
        self._passcode_previous_passcode_block_count = value
    
    @property
    def passcode_required(self,) -> Optional[bool]:
        """
        Gets the passcodeRequired property value. Indicates whether or not to require a passcode.
        Returns: Optional[bool]
        """
        return self._passcode_required
    
    @passcode_required.setter
    def passcode_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passcodeRequired property value. Indicates whether or not to require a passcode.
        Args:
            value: Value to set for the passcodeRequired property.
        """
        self._passcode_required = value
    
    @property
    def passcode_required_type(self,) -> Optional[required_password_type.RequiredPasswordType]:
        """
        Gets the passcodeRequiredType property value. Possible values of required passwords.
        Returns: Optional[required_password_type.RequiredPasswordType]
        """
        return self._passcode_required_type
    
    @passcode_required_type.setter
    def passcode_required_type(self,value: Optional[required_password_type.RequiredPasswordType] = None) -> None:
        """
        Sets the passcodeRequiredType property value. Possible values of required passwords.
        Args:
            value: Value to set for the passcodeRequiredType property.
        """
        self._passcode_required_type = value
    
    @property
    def security_block_jailbroken_devices(self,) -> Optional[bool]:
        """
        Gets the securityBlockJailbrokenDevices property value. Devices must not be jailbroken or rooted.
        Returns: Optional[bool]
        """
        return self._security_block_jailbroken_devices
    
    @security_block_jailbroken_devices.setter
    def security_block_jailbroken_devices(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityBlockJailbrokenDevices property value. Devices must not be jailbroken or rooted.
        Args:
            value: Value to set for the securityBlockJailbrokenDevices property.
        """
        self._security_block_jailbroken_devices = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    

