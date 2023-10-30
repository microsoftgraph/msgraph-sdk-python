from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_required_password_type import AndroidRequiredPasswordType
    from .app_list_item import AppListItem
    from .app_list_type import AppListType
    from .device_configuration import DeviceConfiguration
    from .web_browser_cookie_settings import WebBrowserCookieSettings

from .device_configuration import DeviceConfiguration

@dataclass
class AndroidGeneralDeviceConfiguration(DeviceConfiguration):
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
    apps_hide_list: Optional[List[AppListItem]] = None
    # List of apps which can be installed on the KNOX device. This collection can contain a maximum of 500 elements.
    apps_install_allow_list: Optional[List[AppListItem]] = None
    # List of apps which are blocked from being launched on the KNOX device. This collection can contain a maximum of 500 elements.
    apps_launch_block_list: Optional[List[AppListItem]] = None
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
    compliant_apps_list: Optional[List[AppListItem]] = None
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
    kiosk_mode_apps: Optional[List[AppListItem]] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AndroidGeneralDeviceConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AndroidGeneralDeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
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

        fields: Dict[str, Callable[[Any], None]] = {
            "apps_block_clipboard_sharing": lambda n : setattr(self, 'apps_block_clipboard_sharing', n.get_bool_value()),
            "apps_block_copy_paste": lambda n : setattr(self, 'apps_block_copy_paste', n.get_bool_value()),
            "apps_block_you_tube": lambda n : setattr(self, 'apps_block_you_tube', n.get_bool_value()),
            "apps_hide_list": lambda n : setattr(self, 'apps_hide_list', n.get_collection_of_object_values(AppListItem)),
            "apps_install_allow_list": lambda n : setattr(self, 'apps_install_allow_list', n.get_collection_of_object_values(AppListItem)),
            "apps_launch_block_list": lambda n : setattr(self, 'apps_launch_block_list', n.get_collection_of_object_values(AppListItem)),
            "bluetooth_blocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "camera_blocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellular_block_data_roaming": lambda n : setattr(self, 'cellular_block_data_roaming', n.get_bool_value()),
            "cellular_block_messaging": lambda n : setattr(self, 'cellular_block_messaging', n.get_bool_value()),
            "cellular_block_voice_roaming": lambda n : setattr(self, 'cellular_block_voice_roaming', n.get_bool_value()),
            "cellular_block_wi_fi_tethering": lambda n : setattr(self, 'cellular_block_wi_fi_tethering', n.get_bool_value()),
            "compliant_app_list_type": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(AppListType)),
            "compliant_apps_list": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(AppListItem)),
            "device_sharing_allowed": lambda n : setattr(self, 'device_sharing_allowed', n.get_bool_value()),
            "diagnostic_data_block_submission": lambda n : setattr(self, 'diagnostic_data_block_submission', n.get_bool_value()),
            "factory_reset_blocked": lambda n : setattr(self, 'factory_reset_blocked', n.get_bool_value()),
            "google_account_block_auto_sync": lambda n : setattr(self, 'google_account_block_auto_sync', n.get_bool_value()),
            "google_play_store_blocked": lambda n : setattr(self, 'google_play_store_blocked', n.get_bool_value()),
            "kiosk_mode_apps": lambda n : setattr(self, 'kiosk_mode_apps', n.get_collection_of_object_values(AppListItem)),
            "kiosk_mode_block_sleep_button": lambda n : setattr(self, 'kiosk_mode_block_sleep_button', n.get_bool_value()),
            "kiosk_mode_block_volume_buttons": lambda n : setattr(self, 'kiosk_mode_block_volume_buttons', n.get_bool_value()),
            "location_services_blocked": lambda n : setattr(self, 'location_services_blocked', n.get_bool_value()),
            "nfc_blocked": lambda n : setattr(self, 'nfc_blocked', n.get_bool_value()),
            "password_block_fingerprint_unlock": lambda n : setattr(self, 'password_block_fingerprint_unlock', n.get_bool_value()),
            "password_block_trust_agents": lambda n : setattr(self, 'password_block_trust_agents', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(AndroidRequiredPasswordType)),
            "password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "power_off_blocked": lambda n : setattr(self, 'power_off_blocked', n.get_bool_value()),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "security_require_verify_apps": lambda n : setattr(self, 'security_require_verify_apps', n.get_bool_value()),
            "storage_block_google_backup": lambda n : setattr(self, 'storage_block_google_backup', n.get_bool_value()),
            "storage_block_removable_storage": lambda n : setattr(self, 'storage_block_removable_storage', n.get_bool_value()),
            "storage_require_device_encryption": lambda n : setattr(self, 'storage_require_device_encryption', n.get_bool_value()),
            "storage_require_removable_storage_encryption": lambda n : setattr(self, 'storage_require_removable_storage_encryption', n.get_bool_value()),
            "voice_assistant_blocked": lambda n : setattr(self, 'voice_assistant_blocked', n.get_bool_value()),
            "voice_dialing_blocked": lambda n : setattr(self, 'voice_dialing_blocked', n.get_bool_value()),
            "web_browser_block_autofill": lambda n : setattr(self, 'web_browser_block_autofill', n.get_bool_value()),
            "web_browser_block_java_script": lambda n : setattr(self, 'web_browser_block_java_script', n.get_bool_value()),
            "web_browser_block_popups": lambda n : setattr(self, 'web_browser_block_popups', n.get_bool_value()),
            "web_browser_blocked": lambda n : setattr(self, 'web_browser_blocked', n.get_bool_value()),
            "web_browser_cookie_settings": lambda n : setattr(self, 'web_browser_cookie_settings', n.get_enum_value(WebBrowserCookieSettings)),
            "wi_fi_blocked": lambda n : setattr(self, 'wi_fi_blocked', n.get_bool_value()),
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
        writer.write_bool_value("apps_block_clipboard_sharing", self.apps_block_clipboard_sharing)
        writer.write_bool_value("apps_block_copy_paste", self.apps_block_copy_paste)
        writer.write_bool_value("apps_block_you_tube", self.apps_block_you_tube)
        writer.write_collection_of_object_values("apps_hide_list", self.apps_hide_list)
        writer.write_collection_of_object_values("apps_install_allow_list", self.apps_install_allow_list)
        writer.write_collection_of_object_values("apps_launch_block_list", self.apps_launch_block_list)
        writer.write_bool_value("bluetooth_blocked", self.bluetooth_blocked)
        writer.write_bool_value("camera_blocked", self.camera_blocked)
        writer.write_bool_value("cellular_block_data_roaming", self.cellular_block_data_roaming)
        writer.write_bool_value("cellular_block_messaging", self.cellular_block_messaging)
        writer.write_bool_value("cellular_block_voice_roaming", self.cellular_block_voice_roaming)
        writer.write_bool_value("cellular_block_wi_fi_tethering", self.cellular_block_wi_fi_tethering)
        writer.write_enum_value("compliant_app_list_type", self.compliant_app_list_type)
        writer.write_collection_of_object_values("compliant_apps_list", self.compliant_apps_list)
        writer.write_bool_value("device_sharing_allowed", self.device_sharing_allowed)
        writer.write_bool_value("diagnostic_data_block_submission", self.diagnostic_data_block_submission)
        writer.write_bool_value("factory_reset_blocked", self.factory_reset_blocked)
        writer.write_bool_value("google_account_block_auto_sync", self.google_account_block_auto_sync)
        writer.write_bool_value("google_play_store_blocked", self.google_play_store_blocked)
        writer.write_collection_of_object_values("kiosk_mode_apps", self.kiosk_mode_apps)
        writer.write_bool_value("kiosk_mode_block_sleep_button", self.kiosk_mode_block_sleep_button)
        writer.write_bool_value("kiosk_mode_block_volume_buttons", self.kiosk_mode_block_volume_buttons)
        writer.write_bool_value("location_services_blocked", self.location_services_blocked)
        writer.write_bool_value("nfc_blocked", self.nfc_blocked)
        writer.write_bool_value("password_block_fingerprint_unlock", self.password_block_fingerprint_unlock)
        writer.write_bool_value("password_block_trust_agents", self.password_block_trust_agents)
        writer.write_int_value("password_expiration_days", self.password_expiration_days)
        writer.write_int_value("password_minimum_length", self.password_minimum_length)
        writer.write_int_value("password_minutes_of_inactivity_before_screen_timeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("password_previous_password_block_count", self.password_previous_password_block_count)
        writer.write_bool_value("password_required", self.password_required)
        writer.write_enum_value("password_required_type", self.password_required_type)
        writer.write_int_value("password_sign_in_failure_count_before_factory_reset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("power_off_blocked", self.power_off_blocked)
        writer.write_bool_value("screen_capture_blocked", self.screen_capture_blocked)
        writer.write_bool_value("security_require_verify_apps", self.security_require_verify_apps)
        writer.write_bool_value("storage_block_google_backup", self.storage_block_google_backup)
        writer.write_bool_value("storage_block_removable_storage", self.storage_block_removable_storage)
        writer.write_bool_value("storage_require_device_encryption", self.storage_require_device_encryption)
        writer.write_bool_value("storage_require_removable_storage_encryption", self.storage_require_removable_storage_encryption)
        writer.write_bool_value("voice_assistant_blocked", self.voice_assistant_blocked)
        writer.write_bool_value("voice_dialing_blocked", self.voice_dialing_blocked)
        writer.write_bool_value("web_browser_block_autofill", self.web_browser_block_autofill)
        writer.write_bool_value("web_browser_block_java_script", self.web_browser_block_java_script)
        writer.write_bool_value("web_browser_block_popups", self.web_browser_block_popups)
        writer.write_bool_value("web_browser_blocked", self.web_browser_blocked)
        writer.write_enum_value("web_browser_cookie_settings", self.web_browser_cookie_settings)
        writer.write_bool_value("wi_fi_blocked", self.wi_fi_blocked)
    

