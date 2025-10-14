from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_required_password_type import AndroidRequiredPasswordType
    from .device_compliance_policy import DeviceCompliancePolicy
    from .device_threat_protection_level import DeviceThreatProtectionLevel

from .device_compliance_policy import DeviceCompliancePolicy

@dataclass
class AndroidWorkProfileCompliancePolicy(DeviceCompliancePolicy, Parsable):
    """
    This class contains compliance settings for Android Work Profile.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidWorkProfileCompliancePolicy"
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
    # Indicates the device should not be rooted. When TRUE, if the device is detected as rooted it will be reported non-compliant. When FALSE, the device is not reported as non-compliant regardless of device rooted state. Default is FALSE.
    security_block_jailbroken_devices: Optional[bool] = None
    # Disable USB debugging on Android devices.
    security_disable_usb_debugging: Optional[bool] = None
    # Require that devices disallow installation of apps from unknown sources.
    security_prevent_install_apps_from_unknown_sources: Optional[bool] = None
    # Require the device to pass the Company Portal client app runtime integrity check.
    security_require_company_portal_app_integrity: Optional[bool] = None
    # Require Google Play Services to be installed and enabled on the device.
    security_require_google_play_services: Optional[bool] = None
    # Require the device to pass the Play Integrity basic integrity check.
    security_require_safety_net_attestation_basic_integrity: Optional[bool] = None
    # Require the device to pass the Play Integrity device integrity check.
    security_require_safety_net_attestation_certified_device: Optional[bool] = None
    # Require the device to have up to date security providers. The device will require Google Play Services to be enabled and up to date.
    security_require_up_to_date_security_providers: Optional[bool] = None
    # Require the Android Verify apps feature is turned on.
    security_require_verify_apps: Optional[bool] = None
    # Require encryption on Android devices.
    storage_require_encryption: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidWorkProfileCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidWorkProfileCompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidWorkProfileCompliancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_required_password_type import AndroidRequiredPasswordType
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_threat_protection_level import DeviceThreatProtectionLevel

        from .android_required_password_type import AndroidRequiredPasswordType
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_threat_protection_level import DeviceThreatProtectionLevel

        fields: dict[str, Callable[[Any], None]] = {
            "deviceThreatProtectionEnabled": lambda n : setattr(self, 'device_threat_protection_enabled', n.get_bool_value()),
            "deviceThreatProtectionRequiredSecurityLevel": lambda n : setattr(self, 'device_threat_protection_required_security_level', n.get_enum_value(DeviceThreatProtectionLevel)),
            "minAndroidSecurityPatchLevel": lambda n : setattr(self, 'min_android_security_patch_level', n.get_str_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidRequiredPasswordType)),
            "securityBlockJailbrokenDevices": lambda n : setattr(self, 'security_block_jailbroken_devices', n.get_bool_value()),
            "securityDisableUsbDebugging": lambda n : setattr(self, 'security_disable_usb_debugging', n.get_bool_value()),
            "securityPreventInstallAppsFromUnknownSources": lambda n : setattr(self, 'security_prevent_install_apps_from_unknown_sources', n.get_bool_value()),
            "securityRequireCompanyPortalAppIntegrity": lambda n : setattr(self, 'security_require_company_portal_app_integrity', n.get_bool_value()),
            "securityRequireGooglePlayServices": lambda n : setattr(self, 'security_require_google_play_services', n.get_bool_value()),
            "securityRequireSafetyNetAttestationBasicIntegrity": lambda n : setattr(self, 'security_require_safety_net_attestation_basic_integrity', n.get_bool_value()),
            "securityRequireSafetyNetAttestationCertifiedDevice": lambda n : setattr(self, 'security_require_safety_net_attestation_certified_device', n.get_bool_value()),
            "securityRequireUpToDateSecurityProviders": lambda n : setattr(self, 'security_require_up_to_date_security_providers', n.get_bool_value()),
            "securityRequireVerifyApps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
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
        writer.write_bool_value("deviceThreatProtectionEnabled", self.device_threat_protection_enabled)
        writer.write_enum_value("deviceThreatProtectionRequiredSecurityLevel", self.device_threat_protection_required_security_level)
        writer.write_str_value("minAndroidSecurityPatchLevel", self.min_android_security_patch_level)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("securityBlockJailbrokenDevices", self.security_block_jailbroken_devices)
        writer.write_bool_value("securityDisableUsbDebugging", self.security_disable_usb_debugging)
        writer.write_bool_value("securityPreventInstallAppsFromUnknownSources", self.security_prevent_install_apps_from_unknown_sources)
        writer.write_bool_value("securityRequireCompanyPortalAppIntegrity", self.security_require_company_portal_app_integrity)
        writer.write_bool_value("securityRequireGooglePlayServices", self.security_require_google_play_services)
        writer.write_bool_value("securityRequireSafetyNetAttestationBasicIntegrity", self.security_require_safety_net_attestation_basic_integrity)
        writer.write_bool_value("securityRequireSafetyNetAttestationCertifiedDevice", self.security_require_safety_net_attestation_certified_device)
        writer.write_bool_value("securityRequireUpToDateSecurityProviders", self.security_require_up_to_date_security_providers)
        writer.write_bool_value("securityRequireVerifyApps", self.security_require_verify_apps)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
    

