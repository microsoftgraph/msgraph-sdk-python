from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_required_password_type = lazy_import('msgraph.generated.models.android_required_password_type')
device_compliance_policy = lazy_import('msgraph.generated.models.device_compliance_policy')
device_threat_protection_level = lazy_import('msgraph.generated.models.device_threat_protection_level')

class AndroidCompliancePolicy(device_compliance_policy.DeviceCompliancePolicy):
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidCompliancePolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidCompliancePolicy"
        # Require that devices have enabled device threat protection.
        self._device_threat_protection_enabled: Optional[bool] = None
        # Device threat protection levels for the Device Threat Protection API.
        self._device_threat_protection_required_security_level: Optional[device_threat_protection_level.DeviceThreatProtectionLevel] = None
        # Minimum Android security patch level.
        self._min_android_security_patch_level: Optional[str] = None
        # Maximum Android version.
        self._os_maximum_version: Optional[str] = None
        # Minimum Android version.
        self._os_minimum_version: Optional[str] = None
        # Number of days before the password expires. Valid values 1 to 365
        self._password_expiration_days: Optional[int] = None
        # Minimum password length. Valid values 4 to 16
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before a password is required.
        self._password_minutes_of_inactivity_before_lock: Optional[int] = None
        # Number of previous passwords to block. Valid values 1 to 24
        self._password_previous_password_block_count: Optional[int] = None
        # Require a password to unlock device.
        self._password_required: Optional[bool] = None
        # Android required password type.
        self._password_required_type: Optional[android_required_password_type.AndroidRequiredPasswordType] = None
        # Devices must not be jailbroken or rooted.
        self._security_block_jailbroken_devices: Optional[bool] = None
        # Disable USB debugging on Android devices.
        self._security_disable_usb_debugging: Optional[bool] = None
        # Require that devices disallow installation of apps from unknown sources.
        self._security_prevent_install_apps_from_unknown_sources: Optional[bool] = None
        # Require the device to pass the Company Portal client app runtime integrity check.
        self._security_require_company_portal_app_integrity: Optional[bool] = None
        # Require Google Play Services to be installed and enabled on the device.
        self._security_require_google_play_services: Optional[bool] = None
        # Require the device to pass the SafetyNet basic integrity check.
        self._security_require_safety_net_attestation_basic_integrity: Optional[bool] = None
        # Require the device to pass the SafetyNet certified device check.
        self._security_require_safety_net_attestation_certified_device: Optional[bool] = None
        # Require the device to have up to date security providers. The device will require Google Play Services to be enabled and up to date.
        self._security_require_up_to_date_security_providers: Optional[bool] = None
        # Require the Android Verify apps feature is turned on.
        self._security_require_verify_apps: Optional[bool] = None
        # Require encryption on Android devices.
        self._storage_require_encryption: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidCompliancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidCompliancePolicy()
    
    @property
    def device_threat_protection_enabled(self,) -> Optional[bool]:
        """
        Gets the deviceThreatProtectionEnabled property value. Require that devices have enabled device threat protection.
        Returns: Optional[bool]
        """
        return self._device_threat_protection_enabled
    
    @device_threat_protection_enabled.setter
    def device_threat_protection_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceThreatProtectionEnabled property value. Require that devices have enabled device threat protection.
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
            "min_android_security_patch_level": lambda n : setattr(self, 'min_android_security_patch_level', n.get_str_value()),
            "os_maximum_version": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "os_minimum_version": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_lock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(android_required_password_type.AndroidRequiredPasswordType)),
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
    
    @property
    def min_android_security_patch_level(self,) -> Optional[str]:
        """
        Gets the minAndroidSecurityPatchLevel property value. Minimum Android security patch level.
        Returns: Optional[str]
        """
        return self._min_android_security_patch_level
    
    @min_android_security_patch_level.setter
    def min_android_security_patch_level(self,value: Optional[str] = None) -> None:
        """
        Sets the minAndroidSecurityPatchLevel property value. Minimum Android security patch level.
        Args:
            value: Value to set for the minAndroidSecurityPatchLevel property.
        """
        self._min_android_security_patch_level = value
    
    @property
    def os_maximum_version(self,) -> Optional[str]:
        """
        Gets the osMaximumVersion property value. Maximum Android version.
        Returns: Optional[str]
        """
        return self._os_maximum_version
    
    @os_maximum_version.setter
    def os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumVersion property value. Maximum Android version.
        Args:
            value: Value to set for the osMaximumVersion property.
        """
        self._os_maximum_version = value
    
    @property
    def os_minimum_version(self,) -> Optional[str]:
        """
        Gets the osMinimumVersion property value. Minimum Android version.
        Returns: Optional[str]
        """
        return self._os_minimum_version
    
    @os_minimum_version.setter
    def os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumVersion property value. Minimum Android version.
        Args:
            value: Value to set for the osMinimumVersion property.
        """
        self._os_minimum_version = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Number of days before the password expires. Valid values 1 to 365
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Number of days before the password expires. Valid values 1 to 365
        Args:
            value: Value to set for the passwordExpirationDays property.
        """
        self._password_expiration_days = value
    
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
        Gets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block. Valid values 1 to 24
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block. Valid values 1 to 24
        Args:
            value: Value to set for the passwordPreviousPasswordBlockCount property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_required(self,) -> Optional[bool]:
        """
        Gets the passwordRequired property value. Require a password to unlock device.
        Returns: Optional[bool]
        """
        return self._password_required
    
    @password_required.setter
    def password_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequired property value. Require a password to unlock device.
        Args:
            value: Value to set for the passwordRequired property.
        """
        self._password_required = value
    
    @property
    def password_required_type(self,) -> Optional[android_required_password_type.AndroidRequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Android required password type.
        Returns: Optional[android_required_password_type.AndroidRequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[android_required_password_type.AndroidRequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Android required password type.
        Args:
            value: Value to set for the passwordRequiredType property.
        """
        self._password_required_type = value
    
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
    
    @property
    def security_disable_usb_debugging(self,) -> Optional[bool]:
        """
        Gets the securityDisableUsbDebugging property value. Disable USB debugging on Android devices.
        Returns: Optional[bool]
        """
        return self._security_disable_usb_debugging
    
    @security_disable_usb_debugging.setter
    def security_disable_usb_debugging(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityDisableUsbDebugging property value. Disable USB debugging on Android devices.
        Args:
            value: Value to set for the securityDisableUsbDebugging property.
        """
        self._security_disable_usb_debugging = value
    
    @property
    def security_prevent_install_apps_from_unknown_sources(self,) -> Optional[bool]:
        """
        Gets the securityPreventInstallAppsFromUnknownSources property value. Require that devices disallow installation of apps from unknown sources.
        Returns: Optional[bool]
        """
        return self._security_prevent_install_apps_from_unknown_sources
    
    @security_prevent_install_apps_from_unknown_sources.setter
    def security_prevent_install_apps_from_unknown_sources(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityPreventInstallAppsFromUnknownSources property value. Require that devices disallow installation of apps from unknown sources.
        Args:
            value: Value to set for the securityPreventInstallAppsFromUnknownSources property.
        """
        self._security_prevent_install_apps_from_unknown_sources = value
    
    @property
    def security_require_company_portal_app_integrity(self,) -> Optional[bool]:
        """
        Gets the securityRequireCompanyPortalAppIntegrity property value. Require the device to pass the Company Portal client app runtime integrity check.
        Returns: Optional[bool]
        """
        return self._security_require_company_portal_app_integrity
    
    @security_require_company_portal_app_integrity.setter
    def security_require_company_portal_app_integrity(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityRequireCompanyPortalAppIntegrity property value. Require the device to pass the Company Portal client app runtime integrity check.
        Args:
            value: Value to set for the securityRequireCompanyPortalAppIntegrity property.
        """
        self._security_require_company_portal_app_integrity = value
    
    @property
    def security_require_google_play_services(self,) -> Optional[bool]:
        """
        Gets the securityRequireGooglePlayServices property value. Require Google Play Services to be installed and enabled on the device.
        Returns: Optional[bool]
        """
        return self._security_require_google_play_services
    
    @security_require_google_play_services.setter
    def security_require_google_play_services(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityRequireGooglePlayServices property value. Require Google Play Services to be installed and enabled on the device.
        Args:
            value: Value to set for the securityRequireGooglePlayServices property.
        """
        self._security_require_google_play_services = value
    
    @property
    def security_require_safety_net_attestation_basic_integrity(self,) -> Optional[bool]:
        """
        Gets the securityRequireSafetyNetAttestationBasicIntegrity property value. Require the device to pass the SafetyNet basic integrity check.
        Returns: Optional[bool]
        """
        return self._security_require_safety_net_attestation_basic_integrity
    
    @security_require_safety_net_attestation_basic_integrity.setter
    def security_require_safety_net_attestation_basic_integrity(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityRequireSafetyNetAttestationBasicIntegrity property value. Require the device to pass the SafetyNet basic integrity check.
        Args:
            value: Value to set for the securityRequireSafetyNetAttestationBasicIntegrity property.
        """
        self._security_require_safety_net_attestation_basic_integrity = value
    
    @property
    def security_require_safety_net_attestation_certified_device(self,) -> Optional[bool]:
        """
        Gets the securityRequireSafetyNetAttestationCertifiedDevice property value. Require the device to pass the SafetyNet certified device check.
        Returns: Optional[bool]
        """
        return self._security_require_safety_net_attestation_certified_device
    
    @security_require_safety_net_attestation_certified_device.setter
    def security_require_safety_net_attestation_certified_device(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityRequireSafetyNetAttestationCertifiedDevice property value. Require the device to pass the SafetyNet certified device check.
        Args:
            value: Value to set for the securityRequireSafetyNetAttestationCertifiedDevice property.
        """
        self._security_require_safety_net_attestation_certified_device = value
    
    @property
    def security_require_up_to_date_security_providers(self,) -> Optional[bool]:
        """
        Gets the securityRequireUpToDateSecurityProviders property value. Require the device to have up to date security providers. The device will require Google Play Services to be enabled and up to date.
        Returns: Optional[bool]
        """
        return self._security_require_up_to_date_security_providers
    
    @security_require_up_to_date_security_providers.setter
    def security_require_up_to_date_security_providers(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityRequireUpToDateSecurityProviders property value. Require the device to have up to date security providers. The device will require Google Play Services to be enabled and up to date.
        Args:
            value: Value to set for the securityRequireUpToDateSecurityProviders property.
        """
        self._security_require_up_to_date_security_providers = value
    
    @property
    def security_require_verify_apps(self,) -> Optional[bool]:
        """
        Gets the securityRequireVerifyApps property value. Require the Android Verify apps feature is turned on.
        Returns: Optional[bool]
        """
        return self._security_require_verify_apps
    
    @security_require_verify_apps.setter
    def security_require_verify_apps(self,value: Optional[bool] = None) -> None:
        """
        Sets the securityRequireVerifyApps property value. Require the Android Verify apps feature is turned on.
        Args:
            value: Value to set for the securityRequireVerifyApps property.
        """
        self._security_require_verify_apps = value
    
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
    
    @property
    def storage_require_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireEncryption property value. Require encryption on Android devices.
        Returns: Optional[bool]
        """
        return self._storage_require_encryption
    
    @storage_require_encryption.setter
    def storage_require_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireEncryption property value. Require encryption on Android devices.
        Args:
            value: Value to set for the storageRequireEncryption property.
        """
        self._storage_require_encryption = value
    

