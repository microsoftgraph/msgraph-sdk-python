from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

android_required_password_type = lazy_import('msgraph.generated.models.android_required_password_type')
app_list_item = lazy_import('msgraph.generated.models.app_list_item')
app_list_type = lazy_import('msgraph.generated.models.app_list_type')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
web_browser_cookie_settings = lazy_import('msgraph.generated.models.web_browser_cookie_settings')

class AndroidGeneralDeviceConfiguration(device_configuration.DeviceConfiguration):
    @property
    def apps_block_clipboard_sharing(self,) -> Optional[bool]:
        """
        Gets the appsBlockClipboardSharing property value. Indicates whether or not to block clipboard sharing to copy and paste between applications.
        Returns: Optional[bool]
        """
        return self._apps_block_clipboard_sharing
    
    @apps_block_clipboard_sharing.setter
    def apps_block_clipboard_sharing(self,value: Optional[bool] = None) -> None:
        """
        Sets the appsBlockClipboardSharing property value. Indicates whether or not to block clipboard sharing to copy and paste between applications.
        Args:
            value: Value to set for the appsBlockClipboardSharing property.
        """
        self._apps_block_clipboard_sharing = value
    
    @property
    def apps_block_copy_paste(self,) -> Optional[bool]:
        """
        Gets the appsBlockCopyPaste property value. Indicates whether or not to block copy and paste within applications.
        Returns: Optional[bool]
        """
        return self._apps_block_copy_paste
    
    @apps_block_copy_paste.setter
    def apps_block_copy_paste(self,value: Optional[bool] = None) -> None:
        """
        Sets the appsBlockCopyPaste property value. Indicates whether or not to block copy and paste within applications.
        Args:
            value: Value to set for the appsBlockCopyPaste property.
        """
        self._apps_block_copy_paste = value
    
    @property
    def apps_block_you_tube(self,) -> Optional[bool]:
        """
        Gets the appsBlockYouTube property value. Indicates whether or not to block the YouTube app.
        Returns: Optional[bool]
        """
        return self._apps_block_you_tube
    
    @apps_block_you_tube.setter
    def apps_block_you_tube(self,value: Optional[bool] = None) -> None:
        """
        Sets the appsBlockYouTube property value. Indicates whether or not to block the YouTube app.
        Args:
            value: Value to set for the appsBlockYouTube property.
        """
        self._apps_block_you_tube = value
    
    @property
    def apps_hide_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the appsHideList property value. List of apps to be hidden on the KNOX device. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._apps_hide_list
    
    @apps_hide_list.setter
    def apps_hide_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the appsHideList property value. List of apps to be hidden on the KNOX device. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the appsHideList property.
        """
        self._apps_hide_list = value
    
    @property
    def apps_install_allow_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the appsInstallAllowList property value. List of apps which can be installed on the KNOX device. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._apps_install_allow_list
    
    @apps_install_allow_list.setter
    def apps_install_allow_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the appsInstallAllowList property value. List of apps which can be installed on the KNOX device. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the appsInstallAllowList property.
        """
        self._apps_install_allow_list = value
    
    @property
    def apps_launch_block_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the appsLaunchBlockList property value. List of apps which are blocked from being launched on the KNOX device. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._apps_launch_block_list
    
    @apps_launch_block_list.setter
    def apps_launch_block_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the appsLaunchBlockList property value. List of apps which are blocked from being launched on the KNOX device. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the appsLaunchBlockList property.
        """
        self._apps_launch_block_list = value
    
    @property
    def bluetooth_blocked(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlocked property value. Indicates whether or not to block Bluetooth.
        Returns: Optional[bool]
        """
        return self._bluetooth_blocked
    
    @bluetooth_blocked.setter
    def bluetooth_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlocked property value. Indicates whether or not to block Bluetooth.
        Args:
            value: Value to set for the bluetoothBlocked property.
        """
        self._bluetooth_blocked = value
    
    @property
    def camera_blocked(self,) -> Optional[bool]:
        """
        Gets the cameraBlocked property value. Indicates whether or not to block the use of the camera.
        Returns: Optional[bool]
        """
        return self._camera_blocked
    
    @camera_blocked.setter
    def camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cameraBlocked property value. Indicates whether or not to block the use of the camera.
        Args:
            value: Value to set for the cameraBlocked property.
        """
        self._camera_blocked = value
    
    @property
    def cellular_block_data_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockDataRoaming property value. Indicates whether or not to block data roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_data_roaming
    
    @cellular_block_data_roaming.setter
    def cellular_block_data_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockDataRoaming property value. Indicates whether or not to block data roaming.
        Args:
            value: Value to set for the cellularBlockDataRoaming property.
        """
        self._cellular_block_data_roaming = value
    
    @property
    def cellular_block_messaging(self,) -> Optional[bool]:
        """
        Gets the cellularBlockMessaging property value. Indicates whether or not to block SMS/MMS messaging.
        Returns: Optional[bool]
        """
        return self._cellular_block_messaging
    
    @cellular_block_messaging.setter
    def cellular_block_messaging(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockMessaging property value. Indicates whether or not to block SMS/MMS messaging.
        Args:
            value: Value to set for the cellularBlockMessaging property.
        """
        self._cellular_block_messaging = value
    
    @property
    def cellular_block_voice_roaming(self,) -> Optional[bool]:
        """
        Gets the cellularBlockVoiceRoaming property value. Indicates whether or not to block voice roaming.
        Returns: Optional[bool]
        """
        return self._cellular_block_voice_roaming
    
    @cellular_block_voice_roaming.setter
    def cellular_block_voice_roaming(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockVoiceRoaming property value. Indicates whether or not to block voice roaming.
        Args:
            value: Value to set for the cellularBlockVoiceRoaming property.
        """
        self._cellular_block_voice_roaming = value
    
    @property
    def cellular_block_wi_fi_tethering(self,) -> Optional[bool]:
        """
        Gets the cellularBlockWiFiTethering property value. Indicates whether or not to block syncing Wi-Fi tethering.
        Returns: Optional[bool]
        """
        return self._cellular_block_wi_fi_tethering
    
    @cellular_block_wi_fi_tethering.setter
    def cellular_block_wi_fi_tethering(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockWiFiTethering property value. Indicates whether or not to block syncing Wi-Fi tethering.
        Args:
            value: Value to set for the cellularBlockWiFiTethering property.
        """
        self._cellular_block_wi_fi_tethering = value
    
    @property
    def compliant_app_list_type(self,) -> Optional[app_list_type.AppListType]:
        """
        Gets the compliantAppListType property value. Possible values of the compliance app list.
        Returns: Optional[app_list_type.AppListType]
        """
        return self._compliant_app_list_type
    
    @compliant_app_list_type.setter
    def compliant_app_list_type(self,value: Optional[app_list_type.AppListType] = None) -> None:
        """
        Sets the compliantAppListType property value. Possible values of the compliance app list.
        Args:
            value: Value to set for the compliantAppListType property.
        """
        self._compliant_app_list_type = value
    
    @property
    def compliant_apps_list(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the compliantAppsList property value. List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._compliant_apps_list
    
    @compliant_apps_list.setter
    def compliant_apps_list(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the compliantAppsList property value. List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        Args:
            value: Value to set for the compliantAppsList property.
        """
        self._compliant_apps_list = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AndroidGeneralDeviceConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.androidGeneralDeviceConfiguration"
        # Indicates whether or not to block clipboard sharing to copy and paste between applications.
        self._apps_block_clipboard_sharing: Optional[bool] = None
        # Indicates whether or not to block copy and paste within applications.
        self._apps_block_copy_paste: Optional[bool] = None
        # Indicates whether or not to block the YouTube app.
        self._apps_block_you_tube: Optional[bool] = None
        # List of apps to be hidden on the KNOX device. This collection can contain a maximum of 500 elements.
        self._apps_hide_list: Optional[List[app_list_item.AppListItem]] = None
        # List of apps which can be installed on the KNOX device. This collection can contain a maximum of 500 elements.
        self._apps_install_allow_list: Optional[List[app_list_item.AppListItem]] = None
        # List of apps which are blocked from being launched on the KNOX device. This collection can contain a maximum of 500 elements.
        self._apps_launch_block_list: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to block Bluetooth.
        self._bluetooth_blocked: Optional[bool] = None
        # Indicates whether or not to block the use of the camera.
        self._camera_blocked: Optional[bool] = None
        # Indicates whether or not to block data roaming.
        self._cellular_block_data_roaming: Optional[bool] = None
        # Indicates whether or not to block SMS/MMS messaging.
        self._cellular_block_messaging: Optional[bool] = None
        # Indicates whether or not to block voice roaming.
        self._cellular_block_voice_roaming: Optional[bool] = None
        # Indicates whether or not to block syncing Wi-Fi tethering.
        self._cellular_block_wi_fi_tethering: Optional[bool] = None
        # Possible values of the compliance app list.
        self._compliant_app_list_type: Optional[app_list_type.AppListType] = None
        # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        self._compliant_apps_list: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to allow device sharing mode.
        self._device_sharing_allowed: Optional[bool] = None
        # Indicates whether or not to block diagnostic data submission.
        self._diagnostic_data_block_submission: Optional[bool] = None
        # Indicates whether or not to block user performing a factory reset.
        self._factory_reset_blocked: Optional[bool] = None
        # Indicates whether or not to block Google account auto sync.
        self._google_account_block_auto_sync: Optional[bool] = None
        # Indicates whether or not to block the Google Play store.
        self._google_play_store_blocked: Optional[bool] = None
        # A list of apps that will be allowed to run when the device is in Kiosk Mode. This collection can contain a maximum of 500 elements.
        self._kiosk_mode_apps: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to block the screen sleep button while in Kiosk Mode.
        self._kiosk_mode_block_sleep_button: Optional[bool] = None
        # Indicates whether or not to block the volume buttons while in Kiosk Mode.
        self._kiosk_mode_block_volume_buttons: Optional[bool] = None
        # Indicates whether or not to block location services.
        self._location_services_blocked: Optional[bool] = None
        # Indicates whether or not to block Near-Field Communication.
        self._nfc_blocked: Optional[bool] = None
        # Indicates whether or not to block fingerprint unlock.
        self._password_block_fingerprint_unlock: Optional[bool] = None
        # Indicates whether or not to block Smart Lock and other trust agents.
        self._password_block_trust_agents: Optional[bool] = None
        # Number of days before the password expires. Valid values 1 to 365
        self._password_expiration_days: Optional[int] = None
        # Minimum length of passwords. Valid values 4 to 16
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before the screen times out.
        self._password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # Number of previous passwords to block. Valid values 0 to 24
        self._password_previous_password_block_count: Optional[int] = None
        # Indicates whether or not to require a password.
        self._password_required: Optional[bool] = None
        # Android required password type.
        self._password_required_type: Optional[android_required_password_type.AndroidRequiredPasswordType] = None
        # Number of sign in failures allowed before factory reset. Valid values 1 to 16
        self._password_sign_in_failure_count_before_factory_reset: Optional[int] = None
        # Indicates whether or not to block powering off the device.
        self._power_off_blocked: Optional[bool] = None
        # Indicates whether or not to block screenshots.
        self._screen_capture_blocked: Optional[bool] = None
        # Require the Android Verify apps feature is turned on.
        self._security_require_verify_apps: Optional[bool] = None
        # Indicates whether or not to block Google Backup.
        self._storage_block_google_backup: Optional[bool] = None
        # Indicates whether or not to block removable storage usage.
        self._storage_block_removable_storage: Optional[bool] = None
        # Indicates whether or not to require device encryption.
        self._storage_require_device_encryption: Optional[bool] = None
        # Indicates whether or not to require removable storage encryption.
        self._storage_require_removable_storage_encryption: Optional[bool] = None
        # Indicates whether or not to block the use of the Voice Assistant.
        self._voice_assistant_blocked: Optional[bool] = None
        # Indicates whether or not to block voice dialing.
        self._voice_dialing_blocked: Optional[bool] = None
        # Indicates whether or not to block the web browser's auto fill feature.
        self._web_browser_block_autofill: Optional[bool] = None
        # Indicates whether or not to block the web browser.
        self._web_browser_blocked: Optional[bool] = None
        # Indicates whether or not to block JavaScript within the web browser.
        self._web_browser_block_java_script: Optional[bool] = None
        # Indicates whether or not to block popups within the web browser.
        self._web_browser_block_popups: Optional[bool] = None
        # Web Browser Cookie Settings.
        self._web_browser_cookie_settings: Optional[web_browser_cookie_settings.WebBrowserCookieSettings] = None
        # Indicates whether or not to block syncing Wi-Fi.
        self._wi_fi_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AndroidGeneralDeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AndroidGeneralDeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AndroidGeneralDeviceConfiguration()
    
    @property
    def device_sharing_allowed(self,) -> Optional[bool]:
        """
        Gets the deviceSharingAllowed property value. Indicates whether or not to allow device sharing mode.
        Returns: Optional[bool]
        """
        return self._device_sharing_allowed
    
    @device_sharing_allowed.setter
    def device_sharing_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceSharingAllowed property value. Indicates whether or not to allow device sharing mode.
        Args:
            value: Value to set for the deviceSharingAllowed property.
        """
        self._device_sharing_allowed = value
    
    @property
    def diagnostic_data_block_submission(self,) -> Optional[bool]:
        """
        Gets the diagnosticDataBlockSubmission property value. Indicates whether or not to block diagnostic data submission.
        Returns: Optional[bool]
        """
        return self._diagnostic_data_block_submission
    
    @diagnostic_data_block_submission.setter
    def diagnostic_data_block_submission(self,value: Optional[bool] = None) -> None:
        """
        Sets the diagnosticDataBlockSubmission property value. Indicates whether or not to block diagnostic data submission.
        Args:
            value: Value to set for the diagnosticDataBlockSubmission property.
        """
        self._diagnostic_data_block_submission = value
    
    @property
    def factory_reset_blocked(self,) -> Optional[bool]:
        """
        Gets the factoryResetBlocked property value. Indicates whether or not to block user performing a factory reset.
        Returns: Optional[bool]
        """
        return self._factory_reset_blocked
    
    @factory_reset_blocked.setter
    def factory_reset_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the factoryResetBlocked property value. Indicates whether or not to block user performing a factory reset.
        Args:
            value: Value to set for the factoryResetBlocked property.
        """
        self._factory_reset_blocked = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apps_block_clipboard_sharing": lambda n : setattr(self, 'apps_block_clipboard_sharing', n.get_bool_value()),
            "apps_block_copy_paste": lambda n : setattr(self, 'apps_block_copy_paste', n.get_bool_value()),
            "apps_block_you_tube": lambda n : setattr(self, 'apps_block_you_tube', n.get_bool_value()),
            "apps_hide_list": lambda n : setattr(self, 'apps_hide_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "apps_install_allow_list": lambda n : setattr(self, 'apps_install_allow_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "apps_launch_block_list": lambda n : setattr(self, 'apps_launch_block_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "bluetooth_blocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "camera_blocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellular_block_data_roaming": lambda n : setattr(self, 'cellular_block_data_roaming', n.get_bool_value()),
            "cellular_block_messaging": lambda n : setattr(self, 'cellular_block_messaging', n.get_bool_value()),
            "cellular_block_voice_roaming": lambda n : setattr(self, 'cellular_block_voice_roaming', n.get_bool_value()),
            "cellular_block_wi_fi_tethering": lambda n : setattr(self, 'cellular_block_wi_fi_tethering', n.get_bool_value()),
            "compliant_app_list_type": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(app_list_type.AppListType)),
            "compliant_apps_list": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "device_sharing_allowed": lambda n : setattr(self, 'device_sharing_allowed', n.get_bool_value()),
            "diagnostic_data_block_submission": lambda n : setattr(self, 'diagnostic_data_block_submission', n.get_bool_value()),
            "factory_reset_blocked": lambda n : setattr(self, 'factory_reset_blocked', n.get_bool_value()),
            "google_account_block_auto_sync": lambda n : setattr(self, 'google_account_block_auto_sync', n.get_bool_value()),
            "google_play_store_blocked": lambda n : setattr(self, 'google_play_store_blocked', n.get_bool_value()),
            "kiosk_mode_apps": lambda n : setattr(self, 'kiosk_mode_apps', n.get_collection_of_object_values(app_list_item.AppListItem)),
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
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(android_required_password_type.AndroidRequiredPasswordType)),
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
            "web_browser_blocked": lambda n : setattr(self, 'web_browser_blocked', n.get_bool_value()),
            "web_browser_block_java_script": lambda n : setattr(self, 'web_browser_block_java_script', n.get_bool_value()),
            "web_browser_block_popups": lambda n : setattr(self, 'web_browser_block_popups', n.get_bool_value()),
            "web_browser_cookie_settings": lambda n : setattr(self, 'web_browser_cookie_settings', n.get_enum_value(web_browser_cookie_settings.WebBrowserCookieSettings)),
            "wi_fi_blocked": lambda n : setattr(self, 'wi_fi_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def google_account_block_auto_sync(self,) -> Optional[bool]:
        """
        Gets the googleAccountBlockAutoSync property value. Indicates whether or not to block Google account auto sync.
        Returns: Optional[bool]
        """
        return self._google_account_block_auto_sync
    
    @google_account_block_auto_sync.setter
    def google_account_block_auto_sync(self,value: Optional[bool] = None) -> None:
        """
        Sets the googleAccountBlockAutoSync property value. Indicates whether or not to block Google account auto sync.
        Args:
            value: Value to set for the googleAccountBlockAutoSync property.
        """
        self._google_account_block_auto_sync = value
    
    @property
    def google_play_store_blocked(self,) -> Optional[bool]:
        """
        Gets the googlePlayStoreBlocked property value. Indicates whether or not to block the Google Play store.
        Returns: Optional[bool]
        """
        return self._google_play_store_blocked
    
    @google_play_store_blocked.setter
    def google_play_store_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the googlePlayStoreBlocked property value. Indicates whether or not to block the Google Play store.
        Args:
            value: Value to set for the googlePlayStoreBlocked property.
        """
        self._google_play_store_blocked = value
    
    @property
    def kiosk_mode_apps(self,) -> Optional[List[app_list_item.AppListItem]]:
        """
        Gets the kioskModeApps property value. A list of apps that will be allowed to run when the device is in Kiosk Mode. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[app_list_item.AppListItem]]
        """
        return self._kiosk_mode_apps
    
    @kiosk_mode_apps.setter
    def kiosk_mode_apps(self,value: Optional[List[app_list_item.AppListItem]] = None) -> None:
        """
        Sets the kioskModeApps property value. A list of apps that will be allowed to run when the device is in Kiosk Mode. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the kioskModeApps property.
        """
        self._kiosk_mode_apps = value
    
    @property
    def kiosk_mode_block_sleep_button(self,) -> Optional[bool]:
        """
        Gets the kioskModeBlockSleepButton property value. Indicates whether or not to block the screen sleep button while in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_block_sleep_button
    
    @kiosk_mode_block_sleep_button.setter
    def kiosk_mode_block_sleep_button(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBlockSleepButton property value. Indicates whether or not to block the screen sleep button while in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeBlockSleepButton property.
        """
        self._kiosk_mode_block_sleep_button = value
    
    @property
    def kiosk_mode_block_volume_buttons(self,) -> Optional[bool]:
        """
        Gets the kioskModeBlockVolumeButtons property value. Indicates whether or not to block the volume buttons while in Kiosk Mode.
        Returns: Optional[bool]
        """
        return self._kiosk_mode_block_volume_buttons
    
    @kiosk_mode_block_volume_buttons.setter
    def kiosk_mode_block_volume_buttons(self,value: Optional[bool] = None) -> None:
        """
        Sets the kioskModeBlockVolumeButtons property value. Indicates whether or not to block the volume buttons while in Kiosk Mode.
        Args:
            value: Value to set for the kioskModeBlockVolumeButtons property.
        """
        self._kiosk_mode_block_volume_buttons = value
    
    @property
    def location_services_blocked(self,) -> Optional[bool]:
        """
        Gets the locationServicesBlocked property value. Indicates whether or not to block location services.
        Returns: Optional[bool]
        """
        return self._location_services_blocked
    
    @location_services_blocked.setter
    def location_services_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the locationServicesBlocked property value. Indicates whether or not to block location services.
        Args:
            value: Value to set for the locationServicesBlocked property.
        """
        self._location_services_blocked = value
    
    @property
    def nfc_blocked(self,) -> Optional[bool]:
        """
        Gets the nfcBlocked property value. Indicates whether or not to block Near-Field Communication.
        Returns: Optional[bool]
        """
        return self._nfc_blocked
    
    @nfc_blocked.setter
    def nfc_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the nfcBlocked property value. Indicates whether or not to block Near-Field Communication.
        Args:
            value: Value to set for the nfcBlocked property.
        """
        self._nfc_blocked = value
    
    @property
    def password_block_fingerprint_unlock(self,) -> Optional[bool]:
        """
        Gets the passwordBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock.
        Returns: Optional[bool]
        """
        return self._password_block_fingerprint_unlock
    
    @password_block_fingerprint_unlock.setter
    def password_block_fingerprint_unlock(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockFingerprintUnlock property value. Indicates whether or not to block fingerprint unlock.
        Args:
            value: Value to set for the passwordBlockFingerprintUnlock property.
        """
        self._password_block_fingerprint_unlock = value
    
    @property
    def password_block_trust_agents(self,) -> Optional[bool]:
        """
        Gets the passwordBlockTrustAgents property value. Indicates whether or not to block Smart Lock and other trust agents.
        Returns: Optional[bool]
        """
        return self._password_block_trust_agents
    
    @password_block_trust_agents.setter
    def password_block_trust_agents(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockTrustAgents property value. Indicates whether or not to block Smart Lock and other trust agents.
        Args:
            value: Value to set for the passwordBlockTrustAgents property.
        """
        self._password_block_trust_agents = value
    
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
        Gets the passwordMinimumLength property value. Minimum length of passwords. Valid values 4 to 16
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Minimum length of passwords. Valid values 4 to 16
        Args:
            value: Value to set for the passwordMinimumLength property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_screen_timeout
    
    @password_minutes_of_inactivity_before_screen_timeout.setter
    def password_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before the screen times out.
        Args:
            value: Value to set for the passwordMinutesOfInactivityBeforeScreenTimeout property.
        """
        self._password_minutes_of_inactivity_before_screen_timeout = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block. Valid values 0 to 24
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. Number of previous passwords to block. Valid values 0 to 24
        Args:
            value: Value to set for the passwordPreviousPasswordBlockCount property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_required(self,) -> Optional[bool]:
        """
        Gets the passwordRequired property value. Indicates whether or not to require a password.
        Returns: Optional[bool]
        """
        return self._password_required
    
    @password_required.setter
    def password_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequired property value. Indicates whether or not to require a password.
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
    def password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the passwordSignInFailureCountBeforeFactoryReset property value. Number of sign in failures allowed before factory reset. Valid values 1 to 16
        Returns: Optional[int]
        """
        return self._password_sign_in_failure_count_before_factory_reset
    
    @password_sign_in_failure_count_before_factory_reset.setter
    def password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordSignInFailureCountBeforeFactoryReset property value. Number of sign in failures allowed before factory reset. Valid values 1 to 16
        Args:
            value: Value to set for the passwordSignInFailureCountBeforeFactoryReset property.
        """
        self._password_sign_in_failure_count_before_factory_reset = value
    
    @property
    def power_off_blocked(self,) -> Optional[bool]:
        """
        Gets the powerOffBlocked property value. Indicates whether or not to block powering off the device.
        Returns: Optional[bool]
        """
        return self._power_off_blocked
    
    @power_off_blocked.setter
    def power_off_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the powerOffBlocked property value. Indicates whether or not to block powering off the device.
        Args:
            value: Value to set for the powerOffBlocked property.
        """
        self._power_off_blocked = value
    
    @property
    def screen_capture_blocked(self,) -> Optional[bool]:
        """
        Gets the screenCaptureBlocked property value. Indicates whether or not to block screenshots.
        Returns: Optional[bool]
        """
        return self._screen_capture_blocked
    
    @screen_capture_blocked.setter
    def screen_capture_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the screenCaptureBlocked property value. Indicates whether or not to block screenshots.
        Args:
            value: Value to set for the screenCaptureBlocked property.
        """
        self._screen_capture_blocked = value
    
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
        writer.write_bool_value("webBrowserBlocked", self.web_browser_blocked)
        writer.write_bool_value("webBrowserBlockJavaScript", self.web_browser_block_java_script)
        writer.write_bool_value("webBrowserBlockPopups", self.web_browser_block_popups)
        writer.write_enum_value("webBrowserCookieSettings", self.web_browser_cookie_settings)
        writer.write_bool_value("wiFiBlocked", self.wi_fi_blocked)
    
    @property
    def storage_block_google_backup(self,) -> Optional[bool]:
        """
        Gets the storageBlockGoogleBackup property value. Indicates whether or not to block Google Backup.
        Returns: Optional[bool]
        """
        return self._storage_block_google_backup
    
    @storage_block_google_backup.setter
    def storage_block_google_backup(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageBlockGoogleBackup property value. Indicates whether or not to block Google Backup.
        Args:
            value: Value to set for the storageBlockGoogleBackup property.
        """
        self._storage_block_google_backup = value
    
    @property
    def storage_block_removable_storage(self,) -> Optional[bool]:
        """
        Gets the storageBlockRemovableStorage property value. Indicates whether or not to block removable storage usage.
        Returns: Optional[bool]
        """
        return self._storage_block_removable_storage
    
    @storage_block_removable_storage.setter
    def storage_block_removable_storage(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageBlockRemovableStorage property value. Indicates whether or not to block removable storage usage.
        Args:
            value: Value to set for the storageBlockRemovableStorage property.
        """
        self._storage_block_removable_storage = value
    
    @property
    def storage_require_device_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireDeviceEncryption property value. Indicates whether or not to require device encryption.
        Returns: Optional[bool]
        """
        return self._storage_require_device_encryption
    
    @storage_require_device_encryption.setter
    def storage_require_device_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireDeviceEncryption property value. Indicates whether or not to require device encryption.
        Args:
            value: Value to set for the storageRequireDeviceEncryption property.
        """
        self._storage_require_device_encryption = value
    
    @property
    def storage_require_removable_storage_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireRemovableStorageEncryption property value. Indicates whether or not to require removable storage encryption.
        Returns: Optional[bool]
        """
        return self._storage_require_removable_storage_encryption
    
    @storage_require_removable_storage_encryption.setter
    def storage_require_removable_storage_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireRemovableStorageEncryption property value. Indicates whether or not to require removable storage encryption.
        Args:
            value: Value to set for the storageRequireRemovableStorageEncryption property.
        """
        self._storage_require_removable_storage_encryption = value
    
    @property
    def voice_assistant_blocked(self,) -> Optional[bool]:
        """
        Gets the voiceAssistantBlocked property value. Indicates whether or not to block the use of the Voice Assistant.
        Returns: Optional[bool]
        """
        return self._voice_assistant_blocked
    
    @voice_assistant_blocked.setter
    def voice_assistant_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the voiceAssistantBlocked property value. Indicates whether or not to block the use of the Voice Assistant.
        Args:
            value: Value to set for the voiceAssistantBlocked property.
        """
        self._voice_assistant_blocked = value
    
    @property
    def voice_dialing_blocked(self,) -> Optional[bool]:
        """
        Gets the voiceDialingBlocked property value. Indicates whether or not to block voice dialing.
        Returns: Optional[bool]
        """
        return self._voice_dialing_blocked
    
    @voice_dialing_blocked.setter
    def voice_dialing_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the voiceDialingBlocked property value. Indicates whether or not to block voice dialing.
        Args:
            value: Value to set for the voiceDialingBlocked property.
        """
        self._voice_dialing_blocked = value
    
    @property
    def web_browser_block_autofill(self,) -> Optional[bool]:
        """
        Gets the webBrowserBlockAutofill property value. Indicates whether or not to block the web browser's auto fill feature.
        Returns: Optional[bool]
        """
        return self._web_browser_block_autofill
    
    @web_browser_block_autofill.setter
    def web_browser_block_autofill(self,value: Optional[bool] = None) -> None:
        """
        Sets the webBrowserBlockAutofill property value. Indicates whether or not to block the web browser's auto fill feature.
        Args:
            value: Value to set for the webBrowserBlockAutofill property.
        """
        self._web_browser_block_autofill = value
    
    @property
    def web_browser_blocked(self,) -> Optional[bool]:
        """
        Gets the webBrowserBlocked property value. Indicates whether or not to block the web browser.
        Returns: Optional[bool]
        """
        return self._web_browser_blocked
    
    @web_browser_blocked.setter
    def web_browser_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the webBrowserBlocked property value. Indicates whether or not to block the web browser.
        Args:
            value: Value to set for the webBrowserBlocked property.
        """
        self._web_browser_blocked = value
    
    @property
    def web_browser_block_java_script(self,) -> Optional[bool]:
        """
        Gets the webBrowserBlockJavaScript property value. Indicates whether or not to block JavaScript within the web browser.
        Returns: Optional[bool]
        """
        return self._web_browser_block_java_script
    
    @web_browser_block_java_script.setter
    def web_browser_block_java_script(self,value: Optional[bool] = None) -> None:
        """
        Sets the webBrowserBlockJavaScript property value. Indicates whether or not to block JavaScript within the web browser.
        Args:
            value: Value to set for the webBrowserBlockJavaScript property.
        """
        self._web_browser_block_java_script = value
    
    @property
    def web_browser_block_popups(self,) -> Optional[bool]:
        """
        Gets the webBrowserBlockPopups property value. Indicates whether or not to block popups within the web browser.
        Returns: Optional[bool]
        """
        return self._web_browser_block_popups
    
    @web_browser_block_popups.setter
    def web_browser_block_popups(self,value: Optional[bool] = None) -> None:
        """
        Sets the webBrowserBlockPopups property value. Indicates whether or not to block popups within the web browser.
        Args:
            value: Value to set for the webBrowserBlockPopups property.
        """
        self._web_browser_block_popups = value
    
    @property
    def web_browser_cookie_settings(self,) -> Optional[web_browser_cookie_settings.WebBrowserCookieSettings]:
        """
        Gets the webBrowserCookieSettings property value. Web Browser Cookie Settings.
        Returns: Optional[web_browser_cookie_settings.WebBrowserCookieSettings]
        """
        return self._web_browser_cookie_settings
    
    @web_browser_cookie_settings.setter
    def web_browser_cookie_settings(self,value: Optional[web_browser_cookie_settings.WebBrowserCookieSettings] = None) -> None:
        """
        Sets the webBrowserCookieSettings property value. Web Browser Cookie Settings.
        Args:
            value: Value to set for the webBrowserCookieSettings property.
        """
        self._web_browser_cookie_settings = value
    
    @property
    def wi_fi_blocked(self,) -> Optional[bool]:
        """
        Gets the wiFiBlocked property value. Indicates whether or not to block syncing Wi-Fi.
        Returns: Optional[bool]
        """
        return self._wi_fi_blocked
    
    @wi_fi_blocked.setter
    def wi_fi_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the wiFiBlocked property value. Indicates whether or not to block syncing Wi-Fi.
        Args:
            value: Value to set for the wiFiBlocked property.
        """
        self._wi_fi_blocked = value
    

