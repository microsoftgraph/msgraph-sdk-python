from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_list_item = lazy_import('msgraph.generated.models.app_list_item')
app_list_type = lazy_import('msgraph.generated.models.app_list_type')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
required_password_type = lazy_import('msgraph.generated.models.required_password_type')

class WindowsPhone81GeneralConfiguration(device_configuration.DeviceConfiguration):
    @property
    def apply_only_to_windows_phone81(self,) -> Optional[bool]:
        """
        Gets the applyOnlyToWindowsPhone81 property value. Value indicating whether this policy only applies to Windows Phone 8.1. This property is read-only.
        Returns: Optional[bool]
        """
        return self._apply_only_to_windows_phone81
    
    @apply_only_to_windows_phone81.setter
    def apply_only_to_windows_phone81(self,value: Optional[bool] = None) -> None:
        """
        Sets the applyOnlyToWindowsPhone81 property value. Value indicating whether this policy only applies to Windows Phone 8.1. This property is read-only.
        Args:
            value: Value to set for the applyOnlyToWindowsPhone81 property.
        """
        self._apply_only_to_windows_phone81 = value
    
    @property
    def apps_block_copy_paste(self,) -> Optional[bool]:
        """
        Gets the appsBlockCopyPaste property value. Indicates whether or not to block copy paste.
        Returns: Optional[bool]
        """
        return self._apps_block_copy_paste
    
    @apps_block_copy_paste.setter
    def apps_block_copy_paste(self,value: Optional[bool] = None) -> None:
        """
        Sets the appsBlockCopyPaste property value. Indicates whether or not to block copy paste.
        Args:
            value: Value to set for the appsBlockCopyPaste property.
        """
        self._apps_block_copy_paste = value
    
    @property
    def bluetooth_blocked(self,) -> Optional[bool]:
        """
        Gets the bluetoothBlocked property value. Indicates whether or not to block bluetooth.
        Returns: Optional[bool]
        """
        return self._bluetooth_blocked
    
    @bluetooth_blocked.setter
    def bluetooth_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the bluetoothBlocked property value. Indicates whether or not to block bluetooth.
        Args:
            value: Value to set for the bluetoothBlocked property.
        """
        self._bluetooth_blocked = value
    
    @property
    def camera_blocked(self,) -> Optional[bool]:
        """
        Gets the cameraBlocked property value. Indicates whether or not to block camera.
        Returns: Optional[bool]
        """
        return self._camera_blocked
    
    @camera_blocked.setter
    def camera_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the cameraBlocked property value. Indicates whether or not to block camera.
        Args:
            value: Value to set for the cameraBlocked property.
        """
        self._camera_blocked = value
    
    @property
    def cellular_block_wifi_tethering(self,) -> Optional[bool]:
        """
        Gets the cellularBlockWifiTethering property value. Indicates whether or not to block Wi-Fi tethering. Has no impact if Wi-Fi is blocked.
        Returns: Optional[bool]
        """
        return self._cellular_block_wifi_tethering
    
    @cellular_block_wifi_tethering.setter
    def cellular_block_wifi_tethering(self,value: Optional[bool] = None) -> None:
        """
        Sets the cellularBlockWifiTethering property value. Indicates whether or not to block Wi-Fi tethering. Has no impact if Wi-Fi is blocked.
        Args:
            value: Value to set for the cellularBlockWifiTethering property.
        """
        self._cellular_block_wifi_tethering = value
    
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
        Instantiates a new WindowsPhone81GeneralConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsPhone81GeneralConfiguration"
        # Value indicating whether this policy only applies to Windows Phone 8.1. This property is read-only.
        self._apply_only_to_windows_phone81: Optional[bool] = None
        # Indicates whether or not to block copy paste.
        self._apps_block_copy_paste: Optional[bool] = None
        # Indicates whether or not to block bluetooth.
        self._bluetooth_blocked: Optional[bool] = None
        # Indicates whether or not to block camera.
        self._camera_blocked: Optional[bool] = None
        # Indicates whether or not to block Wi-Fi tethering. Has no impact if Wi-Fi is blocked.
        self._cellular_block_wifi_tethering: Optional[bool] = None
        # Possible values of the compliance app list.
        self._compliant_app_list_type: Optional[app_list_type.AppListType] = None
        # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
        self._compliant_apps_list: Optional[List[app_list_item.AppListItem]] = None
        # Indicates whether or not to block diagnostic data submission.
        self._diagnostic_data_block_submission: Optional[bool] = None
        # Indicates whether or not to block custom email accounts.
        self._email_block_adding_accounts: Optional[bool] = None
        # Indicates whether or not to block location services.
        self._location_services_blocked: Optional[bool] = None
        # Indicates whether or not to block using a Microsoft Account.
        self._microsoft_account_blocked: Optional[bool] = None
        # Indicates whether or not to block Near-Field Communication.
        self._nfc_blocked: Optional[bool] = None
        # Indicates whether or not to block syncing the calendar.
        self._password_block_simple: Optional[bool] = None
        # Number of days before the password expires.
        self._password_expiration_days: Optional[int] = None
        # Number of character sets a password must contain.
        self._password_minimum_character_set_count: Optional[int] = None
        # Minimum length of passwords.
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before screen timeout.
        self._password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
        # Number of previous passwords to block. Valid values 0 to 24
        self._password_previous_password_block_count: Optional[int] = None
        # Indicates whether or not to require a password.
        self._password_required: Optional[bool] = None
        # Possible values of required passwords.
        self._password_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # Number of sign in failures allowed before factory reset.
        self._password_sign_in_failure_count_before_factory_reset: Optional[int] = None
        # Indicates whether or not to block screenshots.
        self._screen_capture_blocked: Optional[bool] = None
        # Indicates whether or not to block removable storage.
        self._storage_block_removable_storage: Optional[bool] = None
        # Indicates whether or not to require encryption.
        self._storage_require_encryption: Optional[bool] = None
        # Indicates whether or not to block the web browser.
        self._web_browser_blocked: Optional[bool] = None
        # Indicates whether or not to block automatically connecting to Wi-Fi hotspots. Has no impact if Wi-Fi is blocked.
        self._wifi_block_automatic_connect_hotspots: Optional[bool] = None
        # Indicates whether or not to block Wi-Fi.
        self._wifi_blocked: Optional[bool] = None
        # Indicates whether or not to block Wi-Fi hotspot reporting. Has no impact if Wi-Fi is blocked.
        self._wifi_block_hotspot_reporting: Optional[bool] = None
        # Indicates whether or not to block the Windows Store.
        self._windows_store_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81GeneralConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81GeneralConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsPhone81GeneralConfiguration()
    
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
    def email_block_adding_accounts(self,) -> Optional[bool]:
        """
        Gets the emailBlockAddingAccounts property value. Indicates whether or not to block custom email accounts.
        Returns: Optional[bool]
        """
        return self._email_block_adding_accounts
    
    @email_block_adding_accounts.setter
    def email_block_adding_accounts(self,value: Optional[bool] = None) -> None:
        """
        Sets the emailBlockAddingAccounts property value. Indicates whether or not to block custom email accounts.
        Args:
            value: Value to set for the emailBlockAddingAccounts property.
        """
        self._email_block_adding_accounts = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apply_only_to_windows_phone81": lambda n : setattr(self, 'apply_only_to_windows_phone81', n.get_bool_value()),
            "apps_block_copy_paste": lambda n : setattr(self, 'apps_block_copy_paste', n.get_bool_value()),
            "bluetooth_blocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "camera_blocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellular_block_wifi_tethering": lambda n : setattr(self, 'cellular_block_wifi_tethering', n.get_bool_value()),
            "compliant_app_list_type": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(app_list_type.AppListType)),
            "compliant_apps_list": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(app_list_item.AppListItem)),
            "diagnostic_data_block_submission": lambda n : setattr(self, 'diagnostic_data_block_submission', n.get_bool_value()),
            "email_block_adding_accounts": lambda n : setattr(self, 'email_block_adding_accounts', n.get_bool_value()),
            "location_services_blocked": lambda n : setattr(self, 'location_services_blocked', n.get_bool_value()),
            "microsoft_account_blocked": lambda n : setattr(self, 'microsoft_account_blocked', n.get_bool_value()),
            "nfc_blocked": lambda n : setattr(self, 'nfc_blocked', n.get_bool_value()),
            "password_block_simple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "password_expiration_days": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "password_minimum_character_set_count": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "password_minimum_length": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "password_minutes_of_inactivity_before_screen_timeout": lambda n : setattr(self, 'password_minutes_of_inactivity_before_screen_timeout', n.get_int_value()),
            "password_previous_password_block_count": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "password_required": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "storage_block_removable_storage": lambda n : setattr(self, 'storage_block_removable_storage', n.get_bool_value()),
            "storage_require_encryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
            "web_browser_blocked": lambda n : setattr(self, 'web_browser_blocked', n.get_bool_value()),
            "wifi_block_automatic_connect_hotspots": lambda n : setattr(self, 'wifi_block_automatic_connect_hotspots', n.get_bool_value()),
            "wifi_blocked": lambda n : setattr(self, 'wifi_blocked', n.get_bool_value()),
            "wifi_block_hotspot_reporting": lambda n : setattr(self, 'wifi_block_hotspot_reporting', n.get_bool_value()),
            "windows_store_blocked": lambda n : setattr(self, 'windows_store_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    def microsoft_account_blocked(self,) -> Optional[bool]:
        """
        Gets the microsoftAccountBlocked property value. Indicates whether or not to block using a Microsoft Account.
        Returns: Optional[bool]
        """
        return self._microsoft_account_blocked
    
    @microsoft_account_blocked.setter
    def microsoft_account_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the microsoftAccountBlocked property value. Indicates whether or not to block using a Microsoft Account.
        Args:
            value: Value to set for the microsoftAccountBlocked property.
        """
        self._microsoft_account_blocked = value
    
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
    def password_block_simple(self,) -> Optional[bool]:
        """
        Gets the passwordBlockSimple property value. Indicates whether or not to block syncing the calendar.
        Returns: Optional[bool]
        """
        return self._password_block_simple
    
    @password_block_simple.setter
    def password_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockSimple property value. Indicates whether or not to block syncing the calendar.
        Args:
            value: Value to set for the passwordBlockSimple property.
        """
        self._password_block_simple = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. Number of days before the password expires.
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. Number of days before the password expires.
        Args:
            value: Value to set for the passwordExpirationDays property.
        """
        self._password_expiration_days = value
    
    @property
    def password_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passwordMinimumCharacterSetCount property value. Number of character sets a password must contain.
        Returns: Optional[int]
        """
        return self._password_minimum_character_set_count
    
    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumCharacterSetCount property value. Number of character sets a password must contain.
        Args:
            value: Value to set for the passwordMinimumCharacterSetCount property.
        """
        self._password_minimum_character_set_count = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. Minimum length of passwords.
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. Minimum length of passwords.
        Args:
            value: Value to set for the passwordMinimumLength property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_screen_timeout(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before screen timeout.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_screen_timeout
    
    @password_minutes_of_inactivity_before_screen_timeout.setter
    def password_minutes_of_inactivity_before_screen_timeout(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeScreenTimeout property value. Minutes of inactivity before screen timeout.
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
    def password_sign_in_failure_count_before_factory_reset(self,) -> Optional[int]:
        """
        Gets the passwordSignInFailureCountBeforeFactoryReset property value. Number of sign in failures allowed before factory reset.
        Returns: Optional[int]
        """
        return self._password_sign_in_failure_count_before_factory_reset
    
    @password_sign_in_failure_count_before_factory_reset.setter
    def password_sign_in_failure_count_before_factory_reset(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordSignInFailureCountBeforeFactoryReset property value. Number of sign in failures allowed before factory reset.
        Args:
            value: Value to set for the passwordSignInFailureCountBeforeFactoryReset property.
        """
        self._password_sign_in_failure_count_before_factory_reset = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("appsBlockCopyPaste", self.apps_block_copy_paste)
        writer.write_bool_value("bluetoothBlocked", self.bluetooth_blocked)
        writer.write_bool_value("cameraBlocked", self.camera_blocked)
        writer.write_bool_value("cellularBlockWifiTethering", self.cellular_block_wifi_tethering)
        writer.write_enum_value("compliantAppListType", self.compliant_app_list_type)
        writer.write_collection_of_object_values("compliantAppsList", self.compliant_apps_list)
        writer.write_bool_value("diagnosticDataBlockSubmission", self.diagnostic_data_block_submission)
        writer.write_bool_value("emailBlockAddingAccounts", self.email_block_adding_accounts)
        writer.write_bool_value("locationServicesBlocked", self.location_services_blocked)
        writer.write_bool_value("microsoftAccountBlocked", self.microsoft_account_blocked)
        writer.write_bool_value("nfcBlocked", self.nfc_blocked)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeScreenTimeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_int_value("passwordSignInFailureCountBeforeFactoryReset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("screenCaptureBlocked", self.screen_capture_blocked)
        writer.write_bool_value("storageBlockRemovableStorage", self.storage_block_removable_storage)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
        writer.write_bool_value("webBrowserBlocked", self.web_browser_blocked)
        writer.write_bool_value("wifiBlockAutomaticConnectHotspots", self.wifi_block_automatic_connect_hotspots)
        writer.write_bool_value("wifiBlocked", self.wifi_blocked)
        writer.write_bool_value("wifiBlockHotspotReporting", self.wifi_block_hotspot_reporting)
        writer.write_bool_value("windowsStoreBlocked", self.windows_store_blocked)
    
    @property
    def storage_block_removable_storage(self,) -> Optional[bool]:
        """
        Gets the storageBlockRemovableStorage property value. Indicates whether or not to block removable storage.
        Returns: Optional[bool]
        """
        return self._storage_block_removable_storage
    
    @storage_block_removable_storage.setter
    def storage_block_removable_storage(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageBlockRemovableStorage property value. Indicates whether or not to block removable storage.
        Args:
            value: Value to set for the storageBlockRemovableStorage property.
        """
        self._storage_block_removable_storage = value
    
    @property
    def storage_require_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireEncryption property value. Indicates whether or not to require encryption.
        Returns: Optional[bool]
        """
        return self._storage_require_encryption
    
    @storage_require_encryption.setter
    def storage_require_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireEncryption property value. Indicates whether or not to require encryption.
        Args:
            value: Value to set for the storageRequireEncryption property.
        """
        self._storage_require_encryption = value
    
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
    def wifi_block_automatic_connect_hotspots(self,) -> Optional[bool]:
        """
        Gets the wifiBlockAutomaticConnectHotspots property value. Indicates whether or not to block automatically connecting to Wi-Fi hotspots. Has no impact if Wi-Fi is blocked.
        Returns: Optional[bool]
        """
        return self._wifi_block_automatic_connect_hotspots
    
    @wifi_block_automatic_connect_hotspots.setter
    def wifi_block_automatic_connect_hotspots(self,value: Optional[bool] = None) -> None:
        """
        Sets the wifiBlockAutomaticConnectHotspots property value. Indicates whether or not to block automatically connecting to Wi-Fi hotspots. Has no impact if Wi-Fi is blocked.
        Args:
            value: Value to set for the wifiBlockAutomaticConnectHotspots property.
        """
        self._wifi_block_automatic_connect_hotspots = value
    
    @property
    def wifi_blocked(self,) -> Optional[bool]:
        """
        Gets the wifiBlocked property value. Indicates whether or not to block Wi-Fi.
        Returns: Optional[bool]
        """
        return self._wifi_blocked
    
    @wifi_blocked.setter
    def wifi_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the wifiBlocked property value. Indicates whether or not to block Wi-Fi.
        Args:
            value: Value to set for the wifiBlocked property.
        """
        self._wifi_blocked = value
    
    @property
    def wifi_block_hotspot_reporting(self,) -> Optional[bool]:
        """
        Gets the wifiBlockHotspotReporting property value. Indicates whether or not to block Wi-Fi hotspot reporting. Has no impact if Wi-Fi is blocked.
        Returns: Optional[bool]
        """
        return self._wifi_block_hotspot_reporting
    
    @wifi_block_hotspot_reporting.setter
    def wifi_block_hotspot_reporting(self,value: Optional[bool] = None) -> None:
        """
        Sets the wifiBlockHotspotReporting property value. Indicates whether or not to block Wi-Fi hotspot reporting. Has no impact if Wi-Fi is blocked.
        Args:
            value: Value to set for the wifiBlockHotspotReporting property.
        """
        self._wifi_block_hotspot_reporting = value
    
    @property
    def windows_store_blocked(self,) -> Optional[bool]:
        """
        Gets the windowsStoreBlocked property value. Indicates whether or not to block the Windows Store.
        Returns: Optional[bool]
        """
        return self._windows_store_blocked
    
    @windows_store_blocked.setter
    def windows_store_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the windowsStoreBlocked property value. Indicates whether or not to block the Windows Store.
        Args:
            value: Value to set for the windowsStoreBlocked property.
        """
        self._windows_store_blocked = value
    

