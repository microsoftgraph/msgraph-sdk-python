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
class MacOSCompliancePolicy(DeviceCompliancePolicy, Parsable):
    """
    This class contains compliance settings for Mac OS.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.macOSCompliancePolicy"
    # Require that devices have enabled device threat protection.
    device_threat_protection_enabled: Optional[bool] = None
    # Device threat protection levels for the Device Threat Protection API.
    device_threat_protection_required_security_level: Optional[DeviceThreatProtectionLevel] = None
    # Corresponds to the 'Block all incoming connections' option.
    firewall_block_all_incoming: Optional[bool] = None
    # Corresponds to 'Enable stealth mode.'
    firewall_enable_stealth_mode: Optional[bool] = None
    # Whether the firewall should be enabled or not.
    firewall_enabled: Optional[bool] = None
    # Maximum MacOS version.
    os_maximum_version: Optional[str] = None
    # Minimum MacOS version.
    os_minimum_version: Optional[str] = None
    # Indicates whether or not to block simple passwords.
    password_block_simple: Optional[bool] = None
    # Number of days before the password expires. Valid values 1 to 65535
    password_expiration_days: Optional[int] = None
    # The number of character sets required in the password.
    password_minimum_character_set_count: Optional[int] = None
    # Minimum length of password. Valid values 4 to 14
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before a password is required.
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # Number of previous passwords to block. Valid values 1 to 24
    password_previous_password_block_count: Optional[int] = None
    # Whether or not to require a password.
    password_required: Optional[bool] = None
    # Possible values of required passwords.
    password_required_type: Optional[RequiredPasswordType] = None
    # Require encryption on Mac OS devices.
    storage_require_encryption: Optional[bool] = None
    # Require that devices have enabled system integrity protection.
    system_integrity_protection_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MacOSCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MacOSCompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MacOSCompliancePolicy()
    
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
            "firewallBlockAllIncoming": lambda n : setattr(self, 'firewall_block_all_incoming', n.get_bool_value()),
            "firewallEnableStealthMode": lambda n : setattr(self, 'firewall_enable_stealth_mode', n.get_bool_value()),
            "firewallEnabled": lambda n : setattr(self, 'firewall_enabled', n.get_bool_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(RequiredPasswordType)),
            "storageRequireEncryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
            "systemIntegrityProtectionEnabled": lambda n : setattr(self, 'system_integrity_protection_enabled', n.get_bool_value()),
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
        writer.write_bool_value("firewallBlockAllIncoming", self.firewall_block_all_incoming)
        writer.write_bool_value("firewallEnableStealthMode", self.firewall_enable_stealth_mode)
        writer.write_bool_value("firewallEnabled", self.firewall_enabled)
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
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
        writer.write_bool_value("systemIntegrityProtectionEnabled", self.system_integrity_protection_enabled)
    

