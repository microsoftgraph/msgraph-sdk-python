from __future__ import annotations
from datetime import timedelta
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_app_clipboard_sharing_level = lazy_import('msgraph.generated.models.managed_app_clipboard_sharing_level')
managed_app_data_storage_location = lazy_import('msgraph.generated.models.managed_app_data_storage_location')
managed_app_data_transfer_level = lazy_import('msgraph.generated.models.managed_app_data_transfer_level')
managed_app_pin_character_set = lazy_import('msgraph.generated.models.managed_app_pin_character_set')
managed_app_policy = lazy_import('msgraph.generated.models.managed_app_policy')
managed_browser_type = lazy_import('msgraph.generated.models.managed_browser_type')

class ManagedAppProtection(managed_app_policy.ManagedAppPolicy):
    @property
    def allowed_data_storage_locations(self,) -> Optional[List[managed_app_data_storage_location.ManagedAppDataStorageLocation]]:
        """
        Gets the allowedDataStorageLocations property value. Data storage locations where a user may store managed data.
        Returns: Optional[List[managed_app_data_storage_location.ManagedAppDataStorageLocation]]
        """
        return self._allowed_data_storage_locations
    
    @allowed_data_storage_locations.setter
    def allowed_data_storage_locations(self,value: Optional[List[managed_app_data_storage_location.ManagedAppDataStorageLocation]] = None) -> None:
        """
        Sets the allowedDataStorageLocations property value. Data storage locations where a user may store managed data.
        Args:
            value: Value to set for the allowedDataStorageLocations property.
        """
        self._allowed_data_storage_locations = value
    
    @property
    def allowed_inbound_data_transfer_sources(self,) -> Optional[managed_app_data_transfer_level.ManagedAppDataTransferLevel]:
        """
        Gets the allowedInboundDataTransferSources property value. Data can be transferred from/to these classes of apps
        Returns: Optional[managed_app_data_transfer_level.ManagedAppDataTransferLevel]
        """
        return self._allowed_inbound_data_transfer_sources
    
    @allowed_inbound_data_transfer_sources.setter
    def allowed_inbound_data_transfer_sources(self,value: Optional[managed_app_data_transfer_level.ManagedAppDataTransferLevel] = None) -> None:
        """
        Sets the allowedInboundDataTransferSources property value. Data can be transferred from/to these classes of apps
        Args:
            value: Value to set for the allowedInboundDataTransferSources property.
        """
        self._allowed_inbound_data_transfer_sources = value
    
    @property
    def allowed_outbound_clipboard_sharing_level(self,) -> Optional[managed_app_clipboard_sharing_level.ManagedAppClipboardSharingLevel]:
        """
        Gets the allowedOutboundClipboardSharingLevel property value. Represents the level to which the device's clipboard may be shared between apps
        Returns: Optional[managed_app_clipboard_sharing_level.ManagedAppClipboardSharingLevel]
        """
        return self._allowed_outbound_clipboard_sharing_level
    
    @allowed_outbound_clipboard_sharing_level.setter
    def allowed_outbound_clipboard_sharing_level(self,value: Optional[managed_app_clipboard_sharing_level.ManagedAppClipboardSharingLevel] = None) -> None:
        """
        Sets the allowedOutboundClipboardSharingLevel property value. Represents the level to which the device's clipboard may be shared between apps
        Args:
            value: Value to set for the allowedOutboundClipboardSharingLevel property.
        """
        self._allowed_outbound_clipboard_sharing_level = value
    
    @property
    def allowed_outbound_data_transfer_destinations(self,) -> Optional[managed_app_data_transfer_level.ManagedAppDataTransferLevel]:
        """
        Gets the allowedOutboundDataTransferDestinations property value. Data can be transferred from/to these classes of apps
        Returns: Optional[managed_app_data_transfer_level.ManagedAppDataTransferLevel]
        """
        return self._allowed_outbound_data_transfer_destinations
    
    @allowed_outbound_data_transfer_destinations.setter
    def allowed_outbound_data_transfer_destinations(self,value: Optional[managed_app_data_transfer_level.ManagedAppDataTransferLevel] = None) -> None:
        """
        Sets the allowedOutboundDataTransferDestinations property value. Data can be transferred from/to these classes of apps
        Args:
            value: Value to set for the allowedOutboundDataTransferDestinations property.
        """
        self._allowed_outbound_data_transfer_destinations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new ManagedAppProtection and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.managedAppProtection"
        # Data storage locations where a user may store managed data.
        self._allowed_data_storage_locations: Optional[List[managed_app_data_storage_location.ManagedAppDataStorageLocation]] = None
        # Data can be transferred from/to these classes of apps
        self._allowed_inbound_data_transfer_sources: Optional[managed_app_data_transfer_level.ManagedAppDataTransferLevel] = None
        # Represents the level to which the device's clipboard may be shared between apps
        self._allowed_outbound_clipboard_sharing_level: Optional[managed_app_clipboard_sharing_level.ManagedAppClipboardSharingLevel] = None
        # Data can be transferred from/to these classes of apps
        self._allowed_outbound_data_transfer_destinations: Optional[managed_app_data_transfer_level.ManagedAppDataTransferLevel] = None
        # Indicates whether contacts can be synced to the user's device.
        self._contact_sync_blocked: Optional[bool] = None
        # Indicates whether the backup of a managed app's data is blocked.
        self._data_backup_blocked: Optional[bool] = None
        # Indicates whether device compliance is required.
        self._device_compliance_required: Optional[bool] = None
        # Indicates whether use of the app pin is required if the device pin is set.
        self._disable_app_pin_if_device_pin_is_set: Optional[bool] = None
        # Indicates whether use of the fingerprint reader is allowed in place of a pin if PinRequired is set to True.
        self._fingerprint_blocked: Optional[bool] = None
        # Type of managed browser
        self._managed_browser: Optional[managed_browser_type.ManagedBrowserType] = None
        # Indicates whether internet links should be opened in the managed browser app, or any custom browser specified by CustomBrowserProtocol (for iOS) or CustomBrowserPackageId/CustomBrowserDisplayName (for Android)
        self._managed_browser_to_open_links_required: Optional[bool] = None
        # Maximum number of incorrect pin retry attempts before the managed app is either blocked or wiped.
        self._maximum_pin_retries: Optional[int] = None
        # Minimum pin length required for an app-level pin if PinRequired is set to True
        self._minimum_pin_length: Optional[int] = None
        # Versions less than the specified version will block the managed app from accessing company data.
        self._minimum_required_app_version: Optional[str] = None
        # Versions less than the specified version will block the managed app from accessing company data.
        self._minimum_required_os_version: Optional[str] = None
        # Versions less than the specified version will result in warning message on the managed app.
        self._minimum_warning_app_version: Optional[str] = None
        # Versions less than the specified version will result in warning message on the managed app from accessing company data.
        self._minimum_warning_os_version: Optional[str] = None
        # Indicates whether organizational credentials are required for app use.
        self._organizational_credentials_required: Optional[bool] = None
        # TimePeriod before the all-level pin must be reset if PinRequired is set to True.
        self._period_before_pin_reset: Optional[Timedelta] = None
        # The period after which access is checked when the device is not connected to the internet.
        self._period_offline_before_access_check: Optional[Timedelta] = None
        # The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped.
        self._period_offline_before_wipe_is_enforced: Optional[Timedelta] = None
        # The period after which access is checked when the device is connected to the internet.
        self._period_online_before_access_check: Optional[Timedelta] = None
        # Character set which is to be used for a user's app PIN
        self._pin_character_set: Optional[managed_app_pin_character_set.ManagedAppPinCharacterSet] = None
        # Indicates whether an app-level pin is required.
        self._pin_required: Optional[bool] = None
        # Indicates whether printing is allowed from managed apps.
        self._print_blocked: Optional[bool] = None
        # Indicates whether users may use the 'Save As' menu item to save a copy of protected files.
        self._save_as_blocked: Optional[bool] = None
        # Indicates whether simplePin is blocked.
        self._simple_pin_blocked: Optional[bool] = None
    
    @property
    def contact_sync_blocked(self,) -> Optional[bool]:
        """
        Gets the contactSyncBlocked property value. Indicates whether contacts can be synced to the user's device.
        Returns: Optional[bool]
        """
        return self._contact_sync_blocked
    
    @contact_sync_blocked.setter
    def contact_sync_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the contactSyncBlocked property value. Indicates whether contacts can be synced to the user's device.
        Args:
            value: Value to set for the contactSyncBlocked property.
        """
        self._contact_sync_blocked = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppProtection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppProtection()
    
    @property
    def data_backup_blocked(self,) -> Optional[bool]:
        """
        Gets the dataBackupBlocked property value. Indicates whether the backup of a managed app's data is blocked.
        Returns: Optional[bool]
        """
        return self._data_backup_blocked
    
    @data_backup_blocked.setter
    def data_backup_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the dataBackupBlocked property value. Indicates whether the backup of a managed app's data is blocked.
        Args:
            value: Value to set for the dataBackupBlocked property.
        """
        self._data_backup_blocked = value
    
    @property
    def device_compliance_required(self,) -> Optional[bool]:
        """
        Gets the deviceComplianceRequired property value. Indicates whether device compliance is required.
        Returns: Optional[bool]
        """
        return self._device_compliance_required
    
    @device_compliance_required.setter
    def device_compliance_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the deviceComplianceRequired property value. Indicates whether device compliance is required.
        Args:
            value: Value to set for the deviceComplianceRequired property.
        """
        self._device_compliance_required = value
    
    @property
    def disable_app_pin_if_device_pin_is_set(self,) -> Optional[bool]:
        """
        Gets the disableAppPinIfDevicePinIsSet property value. Indicates whether use of the app pin is required if the device pin is set.
        Returns: Optional[bool]
        """
        return self._disable_app_pin_if_device_pin_is_set
    
    @disable_app_pin_if_device_pin_is_set.setter
    def disable_app_pin_if_device_pin_is_set(self,value: Optional[bool] = None) -> None:
        """
        Sets the disableAppPinIfDevicePinIsSet property value. Indicates whether use of the app pin is required if the device pin is set.
        Args:
            value: Value to set for the disableAppPinIfDevicePinIsSet property.
        """
        self._disable_app_pin_if_device_pin_is_set = value
    
    @property
    def fingerprint_blocked(self,) -> Optional[bool]:
        """
        Gets the fingerprintBlocked property value. Indicates whether use of the fingerprint reader is allowed in place of a pin if PinRequired is set to True.
        Returns: Optional[bool]
        """
        return self._fingerprint_blocked
    
    @fingerprint_blocked.setter
    def fingerprint_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the fingerprintBlocked property value. Indicates whether use of the fingerprint reader is allowed in place of a pin if PinRequired is set to True.
        Args:
            value: Value to set for the fingerprintBlocked property.
        """
        self._fingerprint_blocked = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allowed_data_storage_locations": lambda n : setattr(self, 'allowed_data_storage_locations', n.get_collection_of_enum_values(managed_app_data_storage_location.ManagedAppDataStorageLocation)),
            "allowed_inbound_data_transfer_sources": lambda n : setattr(self, 'allowed_inbound_data_transfer_sources', n.get_enum_value(managed_app_data_transfer_level.ManagedAppDataTransferLevel)),
            "allowed_outbound_clipboard_sharing_level": lambda n : setattr(self, 'allowed_outbound_clipboard_sharing_level', n.get_enum_value(managed_app_clipboard_sharing_level.ManagedAppClipboardSharingLevel)),
            "allowed_outbound_data_transfer_destinations": lambda n : setattr(self, 'allowed_outbound_data_transfer_destinations', n.get_enum_value(managed_app_data_transfer_level.ManagedAppDataTransferLevel)),
            "contact_sync_blocked": lambda n : setattr(self, 'contact_sync_blocked', n.get_bool_value()),
            "data_backup_blocked": lambda n : setattr(self, 'data_backup_blocked', n.get_bool_value()),
            "device_compliance_required": lambda n : setattr(self, 'device_compliance_required', n.get_bool_value()),
            "disable_app_pin_if_device_pin_is_set": lambda n : setattr(self, 'disable_app_pin_if_device_pin_is_set', n.get_bool_value()),
            "fingerprint_blocked": lambda n : setattr(self, 'fingerprint_blocked', n.get_bool_value()),
            "managed_browser": lambda n : setattr(self, 'managed_browser', n.get_enum_value(managed_browser_type.ManagedBrowserType)),
            "managed_browser_to_open_links_required": lambda n : setattr(self, 'managed_browser_to_open_links_required', n.get_bool_value()),
            "maximum_pin_retries": lambda n : setattr(self, 'maximum_pin_retries', n.get_int_value()),
            "minimum_pin_length": lambda n : setattr(self, 'minimum_pin_length', n.get_int_value()),
            "minimum_required_app_version": lambda n : setattr(self, 'minimum_required_app_version', n.get_str_value()),
            "minimum_required_os_version": lambda n : setattr(self, 'minimum_required_os_version', n.get_str_value()),
            "minimum_warning_app_version": lambda n : setattr(self, 'minimum_warning_app_version', n.get_str_value()),
            "minimum_warning_os_version": lambda n : setattr(self, 'minimum_warning_os_version', n.get_str_value()),
            "organizational_credentials_required": lambda n : setattr(self, 'organizational_credentials_required', n.get_bool_value()),
            "period_before_pin_reset": lambda n : setattr(self, 'period_before_pin_reset', n.get_object_value(Timedelta)),
            "period_offline_before_access_check": lambda n : setattr(self, 'period_offline_before_access_check', n.get_object_value(Timedelta)),
            "period_offline_before_wipe_is_enforced": lambda n : setattr(self, 'period_offline_before_wipe_is_enforced', n.get_object_value(Timedelta)),
            "period_online_before_access_check": lambda n : setattr(self, 'period_online_before_access_check', n.get_object_value(Timedelta)),
            "pin_character_set": lambda n : setattr(self, 'pin_character_set', n.get_enum_value(managed_app_pin_character_set.ManagedAppPinCharacterSet)),
            "pin_required": lambda n : setattr(self, 'pin_required', n.get_bool_value()),
            "print_blocked": lambda n : setattr(self, 'print_blocked', n.get_bool_value()),
            "save_as_blocked": lambda n : setattr(self, 'save_as_blocked', n.get_bool_value()),
            "simple_pin_blocked": lambda n : setattr(self, 'simple_pin_blocked', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def managed_browser(self,) -> Optional[managed_browser_type.ManagedBrowserType]:
        """
        Gets the managedBrowser property value. Type of managed browser
        Returns: Optional[managed_browser_type.ManagedBrowserType]
        """
        return self._managed_browser
    
    @managed_browser.setter
    def managed_browser(self,value: Optional[managed_browser_type.ManagedBrowserType] = None) -> None:
        """
        Sets the managedBrowser property value. Type of managed browser
        Args:
            value: Value to set for the managedBrowser property.
        """
        self._managed_browser = value
    
    @property
    def managed_browser_to_open_links_required(self,) -> Optional[bool]:
        """
        Gets the managedBrowserToOpenLinksRequired property value. Indicates whether internet links should be opened in the managed browser app, or any custom browser specified by CustomBrowserProtocol (for iOS) or CustomBrowserPackageId/CustomBrowserDisplayName (for Android)
        Returns: Optional[bool]
        """
        return self._managed_browser_to_open_links_required
    
    @managed_browser_to_open_links_required.setter
    def managed_browser_to_open_links_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the managedBrowserToOpenLinksRequired property value. Indicates whether internet links should be opened in the managed browser app, or any custom browser specified by CustomBrowserProtocol (for iOS) or CustomBrowserPackageId/CustomBrowserDisplayName (for Android)
        Args:
            value: Value to set for the managedBrowserToOpenLinksRequired property.
        """
        self._managed_browser_to_open_links_required = value
    
    @property
    def maximum_pin_retries(self,) -> Optional[int]:
        """
        Gets the maximumPinRetries property value. Maximum number of incorrect pin retry attempts before the managed app is either blocked or wiped.
        Returns: Optional[int]
        """
        return self._maximum_pin_retries
    
    @maximum_pin_retries.setter
    def maximum_pin_retries(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumPinRetries property value. Maximum number of incorrect pin retry attempts before the managed app is either blocked or wiped.
        Args:
            value: Value to set for the maximumPinRetries property.
        """
        self._maximum_pin_retries = value
    
    @property
    def minimum_pin_length(self,) -> Optional[int]:
        """
        Gets the minimumPinLength property value. Minimum pin length required for an app-level pin if PinRequired is set to True
        Returns: Optional[int]
        """
        return self._minimum_pin_length
    
    @minimum_pin_length.setter
    def minimum_pin_length(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumPinLength property value. Minimum pin length required for an app-level pin if PinRequired is set to True
        Args:
            value: Value to set for the minimumPinLength property.
        """
        self._minimum_pin_length = value
    
    @property
    def minimum_required_app_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredAppVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Returns: Optional[str]
        """
        return self._minimum_required_app_version
    
    @minimum_required_app_version.setter
    def minimum_required_app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredAppVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Args:
            value: Value to set for the minimumRequiredAppVersion property.
        """
        self._minimum_required_app_version = value
    
    @property
    def minimum_required_os_version(self,) -> Optional[str]:
        """
        Gets the minimumRequiredOsVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Returns: Optional[str]
        """
        return self._minimum_required_os_version
    
    @minimum_required_os_version.setter
    def minimum_required_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumRequiredOsVersion property value. Versions less than the specified version will block the managed app from accessing company data.
        Args:
            value: Value to set for the minimumRequiredOsVersion property.
        """
        self._minimum_required_os_version = value
    
    @property
    def minimum_warning_app_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningAppVersion property value. Versions less than the specified version will result in warning message on the managed app.
        Returns: Optional[str]
        """
        return self._minimum_warning_app_version
    
    @minimum_warning_app_version.setter
    def minimum_warning_app_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningAppVersion property value. Versions less than the specified version will result in warning message on the managed app.
        Args:
            value: Value to set for the minimumWarningAppVersion property.
        """
        self._minimum_warning_app_version = value
    
    @property
    def minimum_warning_os_version(self,) -> Optional[str]:
        """
        Gets the minimumWarningOsVersion property value. Versions less than the specified version will result in warning message on the managed app from accessing company data.
        Returns: Optional[str]
        """
        return self._minimum_warning_os_version
    
    @minimum_warning_os_version.setter
    def minimum_warning_os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the minimumWarningOsVersion property value. Versions less than the specified version will result in warning message on the managed app from accessing company data.
        Args:
            value: Value to set for the minimumWarningOsVersion property.
        """
        self._minimum_warning_os_version = value
    
    @property
    def organizational_credentials_required(self,) -> Optional[bool]:
        """
        Gets the organizationalCredentialsRequired property value. Indicates whether organizational credentials are required for app use.
        Returns: Optional[bool]
        """
        return self._organizational_credentials_required
    
    @organizational_credentials_required.setter
    def organizational_credentials_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the organizationalCredentialsRequired property value. Indicates whether organizational credentials are required for app use.
        Args:
            value: Value to set for the organizationalCredentialsRequired property.
        """
        self._organizational_credentials_required = value
    
    @property
    def period_before_pin_reset(self,) -> Optional[Timedelta]:
        """
        Gets the periodBeforePinReset property value. TimePeriod before the all-level pin must be reset if PinRequired is set to True.
        Returns: Optional[Timedelta]
        """
        return self._period_before_pin_reset
    
    @period_before_pin_reset.setter
    def period_before_pin_reset(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the periodBeforePinReset property value. TimePeriod before the all-level pin must be reset if PinRequired is set to True.
        Args:
            value: Value to set for the periodBeforePinReset property.
        """
        self._period_before_pin_reset = value
    
    @property
    def period_offline_before_access_check(self,) -> Optional[Timedelta]:
        """
        Gets the periodOfflineBeforeAccessCheck property value. The period after which access is checked when the device is not connected to the internet.
        Returns: Optional[Timedelta]
        """
        return self._period_offline_before_access_check
    
    @period_offline_before_access_check.setter
    def period_offline_before_access_check(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the periodOfflineBeforeAccessCheck property value. The period after which access is checked when the device is not connected to the internet.
        Args:
            value: Value to set for the periodOfflineBeforeAccessCheck property.
        """
        self._period_offline_before_access_check = value
    
    @property
    def period_offline_before_wipe_is_enforced(self,) -> Optional[Timedelta]:
        """
        Gets the periodOfflineBeforeWipeIsEnforced property value. The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped.
        Returns: Optional[Timedelta]
        """
        return self._period_offline_before_wipe_is_enforced
    
    @period_offline_before_wipe_is_enforced.setter
    def period_offline_before_wipe_is_enforced(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the periodOfflineBeforeWipeIsEnforced property value. The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped.
        Args:
            value: Value to set for the periodOfflineBeforeWipeIsEnforced property.
        """
        self._period_offline_before_wipe_is_enforced = value
    
    @property
    def period_online_before_access_check(self,) -> Optional[Timedelta]:
        """
        Gets the periodOnlineBeforeAccessCheck property value. The period after which access is checked when the device is connected to the internet.
        Returns: Optional[Timedelta]
        """
        return self._period_online_before_access_check
    
    @period_online_before_access_check.setter
    def period_online_before_access_check(self,value: Optional[Timedelta] = None) -> None:
        """
        Sets the periodOnlineBeforeAccessCheck property value. The period after which access is checked when the device is connected to the internet.
        Args:
            value: Value to set for the periodOnlineBeforeAccessCheck property.
        """
        self._period_online_before_access_check = value
    
    @property
    def pin_character_set(self,) -> Optional[managed_app_pin_character_set.ManagedAppPinCharacterSet]:
        """
        Gets the pinCharacterSet property value. Character set which is to be used for a user's app PIN
        Returns: Optional[managed_app_pin_character_set.ManagedAppPinCharacterSet]
        """
        return self._pin_character_set
    
    @pin_character_set.setter
    def pin_character_set(self,value: Optional[managed_app_pin_character_set.ManagedAppPinCharacterSet] = None) -> None:
        """
        Sets the pinCharacterSet property value. Character set which is to be used for a user's app PIN
        Args:
            value: Value to set for the pinCharacterSet property.
        """
        self._pin_character_set = value
    
    @property
    def pin_required(self,) -> Optional[bool]:
        """
        Gets the pinRequired property value. Indicates whether an app-level pin is required.
        Returns: Optional[bool]
        """
        return self._pin_required
    
    @pin_required.setter
    def pin_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the pinRequired property value. Indicates whether an app-level pin is required.
        Args:
            value: Value to set for the pinRequired property.
        """
        self._pin_required = value
    
    @property
    def print_blocked(self,) -> Optional[bool]:
        """
        Gets the printBlocked property value. Indicates whether printing is allowed from managed apps.
        Returns: Optional[bool]
        """
        return self._print_blocked
    
    @print_blocked.setter
    def print_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the printBlocked property value. Indicates whether printing is allowed from managed apps.
        Args:
            value: Value to set for the printBlocked property.
        """
        self._print_blocked = value
    
    @property
    def save_as_blocked(self,) -> Optional[bool]:
        """
        Gets the saveAsBlocked property value. Indicates whether users may use the 'Save As' menu item to save a copy of protected files.
        Returns: Optional[bool]
        """
        return self._save_as_blocked
    
    @save_as_blocked.setter
    def save_as_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the saveAsBlocked property value. Indicates whether users may use the 'Save As' menu item to save a copy of protected files.
        Args:
            value: Value to set for the saveAsBlocked property.
        """
        self._save_as_blocked = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("allowedDataStorageLocations", self.allowed_data_storage_locations)
        writer.write_enum_value("allowedInboundDataTransferSources", self.allowed_inbound_data_transfer_sources)
        writer.write_enum_value("allowedOutboundClipboardSharingLevel", self.allowed_outbound_clipboard_sharing_level)
        writer.write_enum_value("allowedOutboundDataTransferDestinations", self.allowed_outbound_data_transfer_destinations)
        writer.write_bool_value("contactSyncBlocked", self.contact_sync_blocked)
        writer.write_bool_value("dataBackupBlocked", self.data_backup_blocked)
        writer.write_bool_value("deviceComplianceRequired", self.device_compliance_required)
        writer.write_bool_value("disableAppPinIfDevicePinIsSet", self.disable_app_pin_if_device_pin_is_set)
        writer.write_bool_value("fingerprintBlocked", self.fingerprint_blocked)
        writer.write_enum_value("managedBrowser", self.managed_browser)
        writer.write_bool_value("managedBrowserToOpenLinksRequired", self.managed_browser_to_open_links_required)
        writer.write_int_value("maximumPinRetries", self.maximum_pin_retries)
        writer.write_int_value("minimumPinLength", self.minimum_pin_length)
        writer.write_str_value("minimumRequiredAppVersion", self.minimum_required_app_version)
        writer.write_str_value("minimumRequiredOsVersion", self.minimum_required_os_version)
        writer.write_str_value("minimumWarningAppVersion", self.minimum_warning_app_version)
        writer.write_str_value("minimumWarningOsVersion", self.minimum_warning_os_version)
        writer.write_bool_value("organizationalCredentialsRequired", self.organizational_credentials_required)
        writer.write_object_value("periodBeforePinReset", self.period_before_pin_reset)
        writer.write_object_value("periodOfflineBeforeAccessCheck", self.period_offline_before_access_check)
        writer.write_object_value("periodOfflineBeforeWipeIsEnforced", self.period_offline_before_wipe_is_enforced)
        writer.write_object_value("periodOnlineBeforeAccessCheck", self.period_online_before_access_check)
        writer.write_enum_value("pinCharacterSet", self.pin_character_set)
        writer.write_bool_value("pinRequired", self.pin_required)
        writer.write_bool_value("printBlocked", self.print_blocked)
        writer.write_bool_value("saveAsBlocked", self.save_as_blocked)
        writer.write_bool_value("simplePinBlocked", self.simple_pin_blocked)
    
    @property
    def simple_pin_blocked(self,) -> Optional[bool]:
        """
        Gets the simplePinBlocked property value. Indicates whether simplePin is blocked.
        Returns: Optional[bool]
        """
        return self._simple_pin_blocked
    
    @simple_pin_blocked.setter
    def simple_pin_blocked(self,value: Optional[bool] = None) -> None:
        """
        Sets the simplePinBlocked property value. Indicates whether simplePin is blocked.
        Args:
            value: Value to set for the simplePinBlocked property.
        """
        self._simple_pin_blocked = value
    

