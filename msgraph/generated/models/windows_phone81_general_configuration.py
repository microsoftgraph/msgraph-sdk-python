from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_list_item import AppListItem
    from .app_list_type import AppListType
    from .device_configuration import DeviceConfiguration
    from .required_password_type import RequiredPasswordType

from .device_configuration import DeviceConfiguration

@dataclass
class WindowsPhone81GeneralConfiguration(DeviceConfiguration):
    """
    This topic provides descriptions of the declared methods, properties and relationships exposed by the windowsPhone81GeneralConfiguration resource.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsPhone81GeneralConfiguration"
    # Value indicating whether this policy only applies to Windows Phone 8.1. This property is read-only.
    apply_only_to_windows_phone81: Optional[bool] = None
    # Indicates whether or not to block copy paste.
    apps_block_copy_paste: Optional[bool] = None
    # Indicates whether or not to block bluetooth.
    bluetooth_blocked: Optional[bool] = None
    # Indicates whether or not to block camera.
    camera_blocked: Optional[bool] = None
    # Indicates whether or not to block Wi-Fi tethering. Has no impact if Wi-Fi is blocked.
    cellular_block_wifi_tethering: Optional[bool] = None
    # Possible values of the compliance app list.
    compliant_app_list_type: Optional[AppListType] = None
    # List of apps in the compliance (either allow list or block list, controlled by CompliantAppListType). This collection can contain a maximum of 10000 elements.
    compliant_apps_list: Optional[List[AppListItem]] = None
    # Indicates whether or not to block diagnostic data submission.
    diagnostic_data_block_submission: Optional[bool] = None
    # Indicates whether or not to block custom email accounts.
    email_block_adding_accounts: Optional[bool] = None
    # Indicates whether or not to block location services.
    location_services_blocked: Optional[bool] = None
    # Indicates whether or not to block using a Microsoft Account.
    microsoft_account_blocked: Optional[bool] = None
    # Indicates whether or not to block Near-Field Communication.
    nfc_blocked: Optional[bool] = None
    # Indicates whether or not to block syncing the calendar.
    password_block_simple: Optional[bool] = None
    # Number of days before the password expires.
    password_expiration_days: Optional[int] = None
    # Number of character sets a password must contain.
    password_minimum_character_set_count: Optional[int] = None
    # Minimum length of passwords.
    password_minimum_length: Optional[int] = None
    # Minutes of inactivity before screen timeout.
    password_minutes_of_inactivity_before_screen_timeout: Optional[int] = None
    # Number of previous passwords to block. Valid values 0 to 24
    password_previous_password_block_count: Optional[int] = None
    # Indicates whether or not to require a password.
    password_required: Optional[bool] = None
    # Possible values of required passwords.
    password_required_type: Optional[RequiredPasswordType] = None
    # Number of sign in failures allowed before factory reset.
    password_sign_in_failure_count_before_factory_reset: Optional[int] = None
    # Indicates whether or not to block screenshots.
    screen_capture_blocked: Optional[bool] = None
    # Indicates whether or not to block removable storage.
    storage_block_removable_storage: Optional[bool] = None
    # Indicates whether or not to require encryption.
    storage_require_encryption: Optional[bool] = None
    # Indicates whether or not to block the web browser.
    web_browser_blocked: Optional[bool] = None
    # Indicates whether or not to block automatically connecting to Wi-Fi hotspots. Has no impact if Wi-Fi is blocked.
    wifi_block_automatic_connect_hotspots: Optional[bool] = None
    # Indicates whether or not to block Wi-Fi hotspot reporting. Has no impact if Wi-Fi is blocked.
    wifi_block_hotspot_reporting: Optional[bool] = None
    # Indicates whether or not to block Wi-Fi.
    wifi_blocked: Optional[bool] = None
    # Indicates whether or not to block the Windows Store.
    windows_store_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsPhone81GeneralConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsPhone81GeneralConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsPhone81GeneralConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .required_password_type import RequiredPasswordType

        from .app_list_item import AppListItem
        from .app_list_type import AppListType
        from .device_configuration import DeviceConfiguration
        from .required_password_type import RequiredPasswordType

        fields: Dict[str, Callable[[Any], None]] = {
            "apply_only_to_windows_phone81": lambda n : setattr(self, 'apply_only_to_windows_phone81', n.get_bool_value()),
            "apps_block_copy_paste": lambda n : setattr(self, 'apps_block_copy_paste', n.get_bool_value()),
            "bluetooth_blocked": lambda n : setattr(self, 'bluetooth_blocked', n.get_bool_value()),
            "camera_blocked": lambda n : setattr(self, 'camera_blocked', n.get_bool_value()),
            "cellular_block_wifi_tethering": lambda n : setattr(self, 'cellular_block_wifi_tethering', n.get_bool_value()),
            "compliant_app_list_type": lambda n : setattr(self, 'compliant_app_list_type', n.get_enum_value(AppListType)),
            "compliant_apps_list": lambda n : setattr(self, 'compliant_apps_list', n.get_collection_of_object_values(AppListItem)),
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
            "password_required_type": lambda n : setattr(self, 'password_required_type', n.get_enum_value(RequiredPasswordType)),
            "password_sign_in_failure_count_before_factory_reset": lambda n : setattr(self, 'password_sign_in_failure_count_before_factory_reset', n.get_int_value()),
            "screen_capture_blocked": lambda n : setattr(self, 'screen_capture_blocked', n.get_bool_value()),
            "storage_block_removable_storage": lambda n : setattr(self, 'storage_block_removable_storage', n.get_bool_value()),
            "storage_require_encryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
            "web_browser_blocked": lambda n : setattr(self, 'web_browser_blocked', n.get_bool_value()),
            "wifi_block_automatic_connect_hotspots": lambda n : setattr(self, 'wifi_block_automatic_connect_hotspots', n.get_bool_value()),
            "wifi_block_hotspot_reporting": lambda n : setattr(self, 'wifi_block_hotspot_reporting', n.get_bool_value()),
            "wifi_blocked": lambda n : setattr(self, 'wifi_blocked', n.get_bool_value()),
            "windows_store_blocked": lambda n : setattr(self, 'windows_store_blocked', n.get_bool_value()),
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
        writer.write_bool_value("apps_block_copy_paste", self.apps_block_copy_paste)
        writer.write_bool_value("bluetooth_blocked", self.bluetooth_blocked)
        writer.write_bool_value("camera_blocked", self.camera_blocked)
        writer.write_bool_value("cellular_block_wifi_tethering", self.cellular_block_wifi_tethering)
        writer.write_enum_value("compliant_app_list_type", self.compliant_app_list_type)
        writer.write_collection_of_object_values("compliant_apps_list", self.compliant_apps_list)
        writer.write_bool_value("diagnostic_data_block_submission", self.diagnostic_data_block_submission)
        writer.write_bool_value("email_block_adding_accounts", self.email_block_adding_accounts)
        writer.write_bool_value("location_services_blocked", self.location_services_blocked)
        writer.write_bool_value("microsoft_account_blocked", self.microsoft_account_blocked)
        writer.write_bool_value("nfc_blocked", self.nfc_blocked)
        writer.write_bool_value("password_block_simple", self.password_block_simple)
        writer.write_int_value("password_expiration_days", self.password_expiration_days)
        writer.write_int_value("password_minimum_character_set_count", self.password_minimum_character_set_count)
        writer.write_int_value("password_minimum_length", self.password_minimum_length)
        writer.write_int_value("password_minutes_of_inactivity_before_screen_timeout", self.password_minutes_of_inactivity_before_screen_timeout)
        writer.write_int_value("password_previous_password_block_count", self.password_previous_password_block_count)
        writer.write_bool_value("password_required", self.password_required)
        writer.write_enum_value("password_required_type", self.password_required_type)
        writer.write_int_value("password_sign_in_failure_count_before_factory_reset", self.password_sign_in_failure_count_before_factory_reset)
        writer.write_bool_value("screen_capture_blocked", self.screen_capture_blocked)
        writer.write_bool_value("storage_block_removable_storage", self.storage_block_removable_storage)
        writer.write_bool_value("storage_require_encryption", self.storage_require_encryption)
        writer.write_bool_value("web_browser_blocked", self.web_browser_blocked)
        writer.write_bool_value("wifi_block_automatic_connect_hotspots", self.wifi_block_automatic_connect_hotspots)
        writer.write_bool_value("wifi_block_hotspot_reporting", self.wifi_block_hotspot_reporting)
        writer.write_bool_value("wifi_blocked", self.wifi_blocked)
        writer.write_bool_value("windows_store_blocked", self.windows_store_blocked)
    

