from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_required_password_type import AndroidRequiredPasswordType
    from .app_list_item import AppListItem
    from .app_list_type import AppListType
    from .device_configuration import DeviceConfiguration
    from .web_browser_cookie_settings import WebBrowserCookieSettings

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidGeneralDeviceConfiguration(DeviceConfiguration, Parsable):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the androidGeneralDeviceConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.androidGeneralDeviceConfiguration"
    # Indicates whether or not to block clipboard sharing to copy and paste between applications.
    apps_block_clipboard_sharing: Optional[bool] = None
    # Indicates whether or not to block copy and paste within applications.
    apps_block_copy_paste: Optional[bool] = None
    # Indicates whether or not to block the YouTube app.
    apps_block_you_tube: Optional[bool] = None
    # List of apps to be hidden on the KNOX device. This collection can contain a maximum of 500 elements.
    apps_hide_list: Optional[list[AppListItem]] = None
    # List of apps which can be installed on the KNOX device. This collection can contain a maximum of 500 elements.
    apps_install_allow_list: Optional[list[AppListItem]] = None
    # List of apps which are blocked from being launched on the KNOX device. This collection can contain a maximum of 500 elements.
    apps_launch_block_list: Optional[list[AppListItem]] = None
    # Indicates whether or not to block Bluetooth.
    bluetooth_blocked: Optional[bool] = None
    # Indicates whether or not to block the use of the camera.
    camera_blocked: Optional[bool] = None
    # Indicates whether or not to block data roaming.
    cellular_block_data_roaming: Optional[bool] = None
    # Indicates whether or not to block SMS/MMS messaging.
    cellular_block_messaging: Optional[bool] = None
    # Indicates whether or not to block voice roaming.
    cellular_block_voice_roaming: Optional[bool] = None
    # Indicates whether or not to block syncing Wi-Fi tethering.
    cellular_block_wi_fi_tethering: Optional[bool] = None
    # Possible values of the compliance app list.
    compliant_app_list_type: Optional[AppListType] = None
    # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
    compliant_apps_list: Optional[list[AppListItem]] = None
    # Indicates whether or not to allow device sharing mode.
    device_sharing_allowed: Optional[bool] = None
    # Indicates whether or not to block diagnostic data submission.
    diagnostic_data_block_submission: Optional[bool] = None
    # Indicates whether or not to block user performing a factory reset.
    factory_reset_blocked: Optional[bool] = None
    # Indicates whether or not to block Google account auto sync.
    google_account_block_auto_sync: Optional[bool] = None
    # Indicates whether or not to block the Google Play store.
    google_play_store_blocked: Optional[bool] = None
    # A list of apps that will be allowed to run when the device is in Kiosk Mode. This collection can contain a maximum of 500 elements.
    kiosk_mode_apps: Optional[list[AppListItem]] = None
    # Indicates whether or not to block the screen sleep button while in Kiosk Mode.
    kiosk_mode_block_sleep_button: Optional[bool] = None
    # Indicates whether or not to block the volume buttons while in Kiosk Mode.
    kiosk_mode_block_volume_buttons: Optional[bool] = None
    # Indicates whether or not to block location services.
    location_services_blocked: Optional[bool] = None
    # Indicates whether or not to block Near-Field Communication.
    nfc_blocked: Optional[bool] = None
    # Indicates whether or not to block fingerprint unlock.
    password_block_fingerprint_unlock: Optional[bool] = None
    # Indicates whether or not to block Smart Lock and other trust agents.
    password_block_trust_agents: Optional[bool] = None
    # Number of days before the password expires. Valid values 1 to 365
    password_expiration_days: Optional[int] = None
    # Minimum length of passwords. Valid values 4 to 16
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before the screen times out.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Number of previous passwords to block. Valid values 0 to 24
    password_previous_password_block_count: Optional[int] = None
    # Indicates whether or not to require a password.
    password_required: Optional[bool] = None
    # Android required password type.
    password_required_type: Optional[AndroidRequiredPasswordType] = None
    # Number of sign in failures allowed before factory reset. Valid values 1 to 16
    password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    # Indicates whether or not to block powering off the device.
    power_off_blocked: Optional[bool] = None
    # Indicates whether or not to block screenshots.
    screen_capture_blocked: Optional[bool] = None
    # Require the Android Verify apps feature is turned on.
    security_require_verify_apps: Optional[bool] = None
    # Indicates whether or not to block Google Backup.
    storage_block_google_backup: Optional[bool] = None
    # Indicates whether or not to block removable storage usage.
    storage_block_removable_storage: Optional[bool] = None
    # Indicates whether or not to require device encryption.
    storage_require_device_encryption: Optional[bool] = None
    # Indicates whether or not to require removable storage encryption.
    storage_require_removable_storage_encryption: Optional[bool] = None
    # Indicates whether or not to block the use of the Voice Assistant.
    voice_assistant_blocked: Optional[bool] = None
    # Indicates whether or not to block voice dialing.
    voice_dialing_blocked: Optional[bool] = None
    # Indicates whether or not to block the web browser's auto fill feature.
    web_browser_block_autofill: Optional[bool] = None
    # Indicates whether or not to block JavaScript within the web browser.
    web_browser_block_java_script: Optional[bool] = None
    # Indicates whether or not to block popups within the web browser.
    web_browser_block_popups: Optional[bool] = None
    # Indicates whether or not to block the web browser.
    web_browser_blocked: Optional[bool] = None
    # Web Browser Cookie Settings.
    web_browser_cookie_settings: Optional[WebBrowserCookieSettings] = None
    # Indicates whether or not to block syncing Wi-Fi.
    wi_fi_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AndroidGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AndroidGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_required_password_type import AndroidRequiredPasswordType
        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .web_browser_cookie_settings import WebBrowserCookieSettings

        from .android_required_password_type import AndroidRequiredPasswordType
        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .web_browser_cookie_settings import WebBrowserCookieSettings

        fields: dict[str, Callable[[Any], None]] = {
            "appsBlockClipboardSharing": lambda n : setattr(self, 'apps_block_clipboard_sharing', n.get_bool_value()),
            "appsBlockCopyPaste": lambda n : setattr(self, 'apps_block_copy_paste', n.get_bool_value()),
            "appsBlockYouTube": lambda n : setattr(self, 'apps_block_you_tube', n.get_bool_value()),
            "appsHideList": lambda n : setattr(self, 'apps_hide_list', n.get_collection_of_object_values(AppListItem)),
            "appsInstallAllowList": lambda n : setattr(self, 'apps_install_allow_list', n.get_collection_of_object_values(AppListItem)),
            "appsLaunchBlockList": lambda n : setattr(self, 'apps_launch_block_list', n.get_collection_of_object_values(AppListItem)),
            "bluetoothBlocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "cameraBlocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellularBlockDataRoaming": lambda n : setattr(self, 'cellular_block_data_roaming', n.get_bool_value()),
            "cellularBlockMessaging": lambda n : setattr(self, 'cellular_block_messaging', n.get_bool_value()),
            "cellularBlockVoiceRoaming": lambda n : setattr(self, 'cellular_block_voice_roaming', n.get_bool_value()),
            "cellularBlockWiFiTethering": lambda n : setattr(self, 'cellular_block_wi_fi_tethering', n.get_bool_value()),
            "compliantAppListType": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(AppListType)),
            "compliantAppsList": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(AppListItem)),
            "deviceSharingAllowed": lambda n : setattr(self, 'device_sharing_allowed', n.get_bool_value()),
            "diagnosticDataBlockSubmission": lambda n : setattr(self, 'diagnostic_data_block_submission', n.get_bool_value()),
            "factoryResetBlocked": lambda n : setattr(self, 'factory_reset_blocked', n.get_bool_value()),
            "googleAccountBlockAutoSync": lambda n : setattr(self, 'google_account_block_auto_sync', n.get_bool_value()),
            "googlePlayStoreBlocked": lambda n : setattr(self, 'google_play_store_blocked', n.get_bool_value()),
            "kioskModeApps": lambda n : setattr(self, 'kiosk_mode_apps', n.get_collection_of_object_values(AppListItem)),
            "kioskModeBlockSleepButton": lambda n : setattr(self, 'kiosk_mode_block_sleep_button', n.get_bool_value()),
            "kioskModeBlockVolumeButtons": lambda n : setattr(self, 'kiosk_mode_block_volume_buttons', n.get_bool_value()),
            "locationServicesBlocked": lambda n : setattr(self, 'location_services_blocked', n.get_bool_value()),
            "nfcBlocked": lambda n : setattr(self, 'nfc_blocked', n.get_bool_value()),
            "passwordBlockFingerprintUnlock": lambda n : setattr(self, 'password_block_fingerprint_unlock', n.get_bool_value()),
            "passwordBlockTrustAgents": lambda n : setattr(self, 'password_block_trust_agents', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeScreenTimeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidRequiredPasswordType)),
            "passwordSignInFailureCountBeforeFactoryReset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "powerOffBlocked": lambda n : setattr(self, 'power_off_blocked', n.get_bool_value()),
            "screenCaptureBlocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "securityRequireVerifyApps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
            "storageBlockGoogleBackup": lambda n : setattr(self, 'storage_block_google_backup', n.get_bool_value()),
            "storageBlockRemovableStorage": lambda n : setattr(self, 'storage_block_removable_storage', n.get_bool_value()),
            "storageRequireDeviceEncryption": lambda n : setattr(self, 'storage_require_device_encryption', n.get_bool_value()),
            "storageRequireRemovableStorageEncryption": lambda n : setattr(self, 'storage_require_removable_storage_encryption', n.get_bool_value()),
            "voiceAssistantBlocked": lambda n : setattr(self, 'voice_assistant_blocked', n.get_bool_value()),
            "voiceDialingBlocked": lambda n : setattr(self, 'voice_dialing_blocked', n.get_bool_value()),
            "webBrowserBlockAutofill": lambda n : setattr(self, 'web_browser_block_autofill', n.get_bool_value()),
            "webBrowserBlockJavaScript": lambda n : setattr(self, 'web_browser_block_java_script', n.get_bool_value()),
            "webBrowserBlockPopups": lambda n : setattr(self, 'web_browser_block_popups', n.get_bool_value()),
            "webBrowserBlocked": lambda n : setattr(self, 'web_browser_blocked', n.get_bool_value()),
            "webBrowserCookieSettings": lambda n : setattr(self, 'web_browser_cookie_settings', n.get_enum_value(WebBrowserCookieSettings)),
            "wiFiBlocked": lambda n : setattr(self, 'wi_fi_blocked', n.get_bool_value()),
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
        writer.write_bool_value("appsBlockClipboardSharing", self.apps_block_clipboard_sharing)
        writer.write_bool_value("appsBlockCopyPaste", self.apps_block_copy_paste)
        writer.write_bool_value("appsBlockYouTube", self.apps_block_you_tube)
        writer.write_collection_of_object_values("appsHideList", self.apps_hide_list)
        writer.write_collection_of_object_values("appsInstallAllowList", self.apps_install_allow_list)
        writer.write_collection_of_object_values("appsLaunchBlockList", self.apps_launch_block_list)
        writer.write_bool_value("bluetoothBlocked", self.bluetooth_blocked)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("cellularBlockDataRoaming", self.cellular_block_data_roaming)
        writer.write_bool_value("cellularBlockMessaging", self.cellular_block_messaging)
        writer.write_bool_value("cellularBlockVoiceRoaming", self.cellular_block_voice_roaming)
        writer.write_bool_value("cellularBlockWiFiTethering", self.cellular_block_wi_fi_tethering)
        writer.write_enum_value("compliantAppListType", self.compliant_app_list_type)
        writer.write_collection_of_object_values("compliantAppsList", self.compliant_apps_list)
        writer.write_bool_value("deviceSharingAllowed", self.device_sharing_allowed)
        writer.write_bool_value("diagnosticDataBlockSubmission", self.diagnostic_data_block_submission)
        writer.write_bool_value("factoryResetBlocked", self.factory_reset_blocked)
        writer.write_bool_value("googleAccountBlockAutoSync", self.google_account_block_auto_sync)
        writer.write_bool_value("googlePlayStoreBlocked", self.google_play_store_blocked)
        writer.write_collection_of_object_values("kioskModeApps", self.kiosk_mode_apps)
        writer.write_bool_value("kioskModeBlockSleepButton", self.kiosk_mode_block_sleep_button)
        writer.write_bool_value("kioskModeBlockVolumeButtons", self.kiosk_mode_block_volume_buttons)
        writer.write_bool_value("locationServicesBlocked", self.location_services_blocked)
        writer.write_bool_value("nfcBlocked", self.nfc_blocked)
        writer.write_bool_value("passwordBlockFingerprintUnlock", self.password_block_fingerprint_unlock)
        writer.write_bool_value("passwordBlockTrustAgents", self.password_block_trust_agents)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("powerOffBlocked", self.power_off_blocked)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("securityRequireVerifyApps", self.security_require_verify_apps)
        writer.write_bool_value("storageBlockGoogleBackup", self.storage_block_google_backup)
        writer.write_bool_value("storageBlockRemovableStorage", self.storage_block_removable_storage)
        writer.write_bool_value("storageRequireDeviceEncryption", self.storage_require_device_encryption)
        writer.write_bool_value("storageRequireRemovableStorageEncryption", self.storage_require_removable_storage_encryption)
        writer.write_bool_value("voiceAssistantBlocked", self.voice_assistant_blocked)
        writer.write_bool_value("voiceDialingBlocked", self.voice_dialing_blocked)
        writer.write_bool_value("webBrowserBlockAutofill", self.web_browser_block_autofill)
        writer.write_bool_value("webBrowserBlockJavaScript", self.web_browser_block_java_script)
        writer.write_bool_value("webBrowserBlockPopups", self.web_browser_block_popups)
        writer.write_bool_value("webBrowserBlocked", self.web_browser_blocked)
        writer.write_enum_value("webBrowserCookieSettings", self.web_browser_cookie_settings)
        writer.write_bool_value("wiFiBlocked", self.wi_fi_blocked)
    

