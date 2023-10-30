from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_required_password_type import AndroidRequiredPasswordType
    from .device_compliance_policy import DeviceCompliancePolicy
    from .device_threat_protection_level import DeviceThreatProtectionLevel

from .device_compliance_policy import DeviceCompliancePolicy

@dataclass
class AndroidCompliancePolicy(DeviceCompliancePolicy):
    """
    This class contains compliance settings for Android.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidCompliancePolicy"
    # Require that devices have enabled device threat protection.
    device_threat_protection_enabled: Optional[bool] = None
    # Device threat protection levels for the Device Threat Protection API.
    device_threat_protection_required_security_level: Optional[DeviceThreatProtectionLevel] = None
    # Minimum Android security patch level.
    min_android_security_patch_level: Optional[str] = None
    # Maximum Android version.
    os_maximum_version: Optional[str] = None
    # Minimum Android version.
    os_minimum_version: Optional[str] = None
    # Number of days before the password expires. Valid values 1 to 365
    password_expiration_days: Optional[int] = None
    # Minimum password length. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before a password is required.
    password_minutes_of_inactivity_before_lock: Optional[int] = None
    # Number of previous passwords to block. Valid values 1 to 24
    password_previous_password_block_count: Optional[int] = None
    # Require a password to unlock device.
    password_required: Optional[bool] = None
    # Android required password type.
    password_required_type: Optional[AndroidRequiredPasswordType] = None
    # Devices must not be jailbroken or rooted.
    security_block_jailbroken_devices: Optional[bool] = None
    # Disable USB debugging on Android devices.
    security_disable_usb_debugging: Optional[bool] = None
    # Require that devices disallow installation of apps from unknown sources.
    security_prevent_install_apps_from_unknown_sources: Optional[bool] = None
    # Require the device to pass the Company Portal client app runtime integrity check.
    security_require_company_portal_app_integrity: Optional[bool] = None
    # Require Google Play Services to be installed and enabled on the device.
    security_require_google_play_services: Optional[bool] = None
    # Require the device to pass the SafetyNet basic integrity check.
    security_require_safety_net_attestation_basic_integrity: Optional[bool] = None
    # Require the device to pass the SafetyNet certified device check.
    security_require_safety_net_attestation_certified_device: Optional[bool] = None
    # Require the device to have up to date security providers. The device will require Google Play Services to be enabled and up to date.
    security_require_up_to_date_security_providers: Optional[bool] = None
    # Require the Android Verify apps feature is turned on.
    security_require_verify_apps: Optional[bool] = None
    # Require encryption on Android devices.
    storage_require_encryption: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidCompliancePolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidCompliancePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .android_required_password_type import AndroidRequiredPasswordType
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_threat_protection_level import DeviceThreatProtectionLevel

        from .android_required_password_type import AndroidRequiredPasswordType
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_threat_protection_level import DeviceThreatProtectionLevel

        fields: Dict[str, Callable[[Any], None]] = {
            "device_threat_protection_enabled": lambda n : setattr(self, 'device_threat_protection_enabled', n.get_bool_value()),
            "device_threat_protection_required_security_level": lambda n : setattr(self, 'device_threat_protection_required_security_level', n.get_enum_value(DeviceThreatProtectionLevel)),
            "min_android_security_patch_level": lambda n : setattr(self, 'min_android_security_patch_level', n.get_str_value()),
            "os_maximum_version": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "os_minimum_version": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_lock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidRequiredPasswordType)),
            "security_block_jailbroken_devices": lambda n : setattr(self, 'security_block_jailbroken_devices', n.get_bool_value()),
            "security_disable_usb_debugging": lambda n : setattr(self, 'security_disable_usb_debugging', n.get_bool_value()),
            "security_prevent_install_apps_from_unknown_sources": lambda n : setattr(self, 'security_prevent_install_apps_from_unknown_sources', n.get_bool_value()),
            "security_require_company_portal_app_integrity": lambda n : setattr(self, 'security_require_company_portal_app_integrity', n.get_bool_value()),
            "security_require_google_play_services": lambda n : setattr(self, 'security_require_google_play_services', n.get_bool_value()),
            "security_require_safety_net_attestation_basic_integrity": lambda n : setattr(self, 'security_require_safety_net_attestation_basic_integrity', n.get_bool_value()),
            "security_require_safety_net_attestation_certified_device": lambda n : setattr(self, 'security_require_safety_net_attestation_certified_device', n.get_bool_value()),
            "security_require_up_to_date_security_providers": lambda n : setattr(self, 'security_require_up_to_date_security_providers', n.get_bool_value()),
            "security_require_verify_apps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
            "storage_require_encryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("device_threat_protection_enabled", self.device_threat_protection_enabled)
        writer.write_enum_value("device_threat_protection_required_security_level", self.device_threat_protection_required_security_level)
        writer.write_str_value("min_android_security_patch_level", self.min_android_security_patch_level)
        writer.write_str_value("os_maximum_version", self.os_maximum_version)
        writer.write_str_value("os_minimum_version", self.os_minimum_version)
        writer.write_int_value("password_expiration_days", self.password_expiration_days)
        writer.write_int_value("password_minimum_length", self.password_minimum_length)
        writer.write_int_value("password_minutes_of_inactivity_before_lock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("password_previous_password_block_count", self.password_previous_password_block_count)
        writer.write_bool_value("password_required", self.password_required)
        writer.write_enum_value("password_required_type", self.password_required_type)
        writer.write_bool_value("security_block_jailbroken_devices", self.security_block_jailbroken_devices)
        writer.write_bool_value("security_disable_usb_debugging", self.security_disable_usb_debugging)
        writer.write_bool_value("security_prevent_install_apps_from_unknown_sources", self.security_prevent_install_apps_from_unknown_sources)
        writer.write_bool_value("security_require_company_portal_app_integrity", self.security_require_company_portal_app_integrity)
        writer.write_bool_value("security_require_google_play_services", self.security_require_google_play_services)
        writer.write_bool_value("security_require_safety_net_attestation_basic_integrity", self.security_require_safety_net_attestation_basic_integrity)
        writer.write_bool_value("security_require_safety_net_attestation_certified_device", self.security_require_safety_net_attestation_certified_device)
        writer.write_bool_value("security_require_up_to_date_security_providers", self.security_require_up_to_date_security_providers)
        writer.write_bool_value("security_require_verify_apps", self.security_require_verify_apps)
        writer.write_bool_value("storage_require_encryption", self.storage_require_encryption)
    

