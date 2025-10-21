from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_managed_app_protection import AndroidManagedAppProtection
    from .default_managed_app_protection import DefaultManagedAppProtection
    from .ios_managed_app_protection import IosManagedAppProtection
    from .managed_app_clipboard_sharing_level import ManagedAppClipboardSharingLevel
    from .managed_app_data_storage_location import ManagedAppDataStorageLocation
    from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
    from .managed_app_pin_character_set import ManagedAppPinCharacterSet
    from .managed_app_policy import ManagedAppPolicy
    from .managed_browser_type import ManagedBrowserType
    from .targeted_managed_app_protection import TargetedManagedAppProtection

from .managed_app_policy import ManagedAppPolicy

@dataclass
class ManagedAppProtection(ManagedAppPolicy, Parsable):
    """
    Policy used to configure detailed management settings for a specified set of apps
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.managedAppProtection"
    # Data storage locations where a user may store managed data.
    allowed_data_storage_locations: Optional[list[ManagedAppDataStorageLocation]] = None
    # Data can be transferred from/to these classes of apps
    allowed_inbound_data_transfer_sources: Optional[ManagedAppDataTransferLevel] = None
    # Represents the level to which the device's clipboard may be shared between apps
    allowed_outbound_clipboard_sharing_level: Optional[ManagedAppClipboardSharingLevel] = None
    # Data can be transferred from/to these classes of apps
    allowed_outbound_data_transfer_destinations: Optional[ManagedAppDataTransferLevel] = None
    # Indicates whether contacts can be synced to the user's device.
    contact_sync_blocked: Optional[bool] = None
    # Indicates whether the backup of a managed app's data is blocked.
    data_backup_blocked: Optional[bool] = None
    # Indicates whether device compliance is required.
    device_compliance_required: Optional[bool] = None
    # Indicates whether use of the app pin is required if the device pin is set.
    disable_app_pin_if_device_pin_is_set: Optional[bool] = None
    # Indicates whether use of the fingerprint reader is allowed in place of a pin if PinRequired is set to True.
    fingerprint_blocked: Optional[bool] = None
    # Type of managed browser
    managed_browser: Optional[ManagedBrowserType] = None
    # Indicates whether internet links should be opened in the managed browser app, or any custom browser specified by CustomBrowserProtocol (for iOS) or CustomBrowserPackageId/CustomBrowserDisplayName (for Android)
    managed_browser_to_open_links_required: Optional[bool] = None
    # Maximum number of incorrect pin retry attempts before the managed app is either blocked or wiped. Valid values 1 to 65535
    maximum_pin_retries: Optional[int] = None
    # Minimum pin length required for an app-level pin if PinRequired is set to True
    minimum_pin_length: Optional[int] = None
    # Versions less than the specified version will block the managed app from accessing company data.
    minimum_required_app_version: Optional[str] = None
    # Versions less than the specified version will block the managed app from accessing company data.
    minimum_required_os_version: Optional[str] = None
    # Versions less than the specified version will result in warning message on the managed app.
    minimum_warning_app_version: Optional[str] = None
    # Versions less than the specified version will result in warning message on the managed app from accessing company data.
    minimum_warning_os_version: Optional[str] = None
    # Indicates whether organizational credentials are required for app use.
    organizational_credentials_required: Optional[bool] = None
    # TimePeriod before the all-level pin must be reset if PinRequired is set to True.
    period_before_pin_reset: Optional[datetime.timedelta] = None
    # The period after which access is checked when the device is not connected to the internet.
    period_offline_before_access_check: Optional[datetime.timedelta] = None
    # The amount of time an app is allowed to remain disconnected from the internet before all managed data it is wiped.
    period_offline_before_wipe_is_enforced: Optional[datetime.timedelta] = None
    # The period after which access is checked when the device is connected to the internet.
    period_online_before_access_check: Optional[datetime.timedelta] = None
    # Character set which is to be used for a user's app PIN
    pin_character_set: Optional[ManagedAppPinCharacterSet] = None
    # Indicates whether an app-level pin is required.
    pin_required: Optional[bool] = None
    # Indicates whether printing is allowed from managed apps.
    print_blocked: Optional[bool] = None
    # Indicates whether users may use the 'Save As' menu item to save a copy of protected files.
    save_as_blocked: Optional[bool] = None
    # Indicates whether simplePin is blocked.
    simple_pin_blocked: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedAppProtection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppProtection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppProtection".casefold():
            from .android_managed_app_protection import AndroidManagedAppProtection

            return AndroidManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.defaultManagedAppProtection".casefold():
            from .default_managed_app_protection import DefaultManagedAppProtection

            return DefaultManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppProtection".casefold():
            from .ios_managed_app_protection import IosManagedAppProtection

            return IosManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppProtection".casefold():
            from .targeted_managed_app_protection import TargetedManagedAppProtection

            return TargetedManagedAppProtection()
        return ManagedAppProtection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_clipboard_sharing_level import ManagedAppClipboardSharingLevel
        from .managed_app_data_storage_location import ManagedAppDataStorageLocation
        from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
        from .managed_app_pin_character_set import ManagedAppPinCharacterSet
        from .managed_app_policy import ManagedAppPolicy
        from .managed_browser_type import ManagedBrowserType
        from .targeted_managed_app_protection import TargetedManagedAppProtection

        from .android_managed_app_protection import AndroidManagedAppProtection
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .ios_managed_app_protection import IosManagedAppProtection
        from .managed_app_clipboard_sharing_level import ManagedAppClipboardSharingLevel
        from .managed_app_data_storage_location import ManagedAppDataStorageLocation
        from .managed_app_data_transfer_level import ManagedAppDataTransferLevel
        from .managed_app_pin_character_set import ManagedAppPinCharacterSet
        from .managed_app_policy import ManagedAppPolicy
        from .managed_browser_type import ManagedBrowserType
        from .targeted_managed_app_protection import TargetedManagedAppProtection

        fields: dict[str, Callable[[Any], None]] = {
            "allowedDataStorageLocations": lambda n : setattr(self, 'allowed_data_storage_locations', n.get_collection_of_enum_values(ManagedAppDataStorageLocation)),
            "allowedInboundDataTransferSources": lambda n : setattr(self, 'allowed_inbound_data_transfer_sources', n.get_enum_value(ManagedAppDataTransferLevel)),
            "allowedOutboundClipboardSharingLevel": lambda n : setattr(self, 'allowed_outbound_clipboard_sharing_level', n.get_enum_value(ManagedAppClipboardSharingLevel)),
            "allowedOutboundDataTransferDestinations": lambda n : setattr(self, 'allowed_outbound_data_transfer_destinations', n.get_enum_value(ManagedAppDataTransferLevel)),
            "contactSyncBlocked": lambda n : setattr(self, 'contact_sync_blocked', n.get_bool_value()),
            "dataBackupBlocked": lambda n : setattr(self, 'data_backup_blocked', n.get_bool_value()),
            "deviceComplianceRequired": lambda n : setattr(self, 'device_compliance_required', n.get_bool_value()),
            "disableAppPinIfDevicePinIsSet": lambda n : setattr(self, 'disable_app_pin_if_device_pin_is_set', n.get_bool_value()),
            "fingerprintBlocked": lambda n : setattr(self, 'fingerprint_blocked', n.get_bool_value()),
            "managedBrowser": lambda n : setattr(self, 'managed_browser', n.get_collection_of_enum_values(ManagedBrowserType)),
            "managedBrowserToOpenLinksRequired": lambda n : setattr(self, 'managed_browser_to_open_links_required', n.get_bool_value()),
            "maximumPinRetries": lambda n : setattr(self, 'maximum_pin_retries', n.get_int_value()),
            "minimumPinLength": lambda n : setattr(self, 'minimum_pin_length', n.get_int_value()),
            "minimumRequiredAppVersion": lambda n : setattr(self, 'minimum_required_app_version', n.get_str_value()),
            "minimumRequiredOsVersion": lambda n : setattr(self, 'minimum_required_os_version', n.get_str_value()),
            "minimumWarningAppVersion": lambda n : setattr(self, 'minimum_warning_app_version', n.get_str_value()),
            "minimumWarningOsVersion": lambda n : setattr(self, 'minimum_warning_os_version', n.get_str_value()),
            "organizationalCredentialsRequired": lambda n : setattr(self, 'organizational_credentials_required', n.get_bool_value()),
            "periodBeforePinReset": lambda n : setattr(self, 'period_before_pin_reset', n.get_timedelta_value()),
            "periodOfflineBeforeAccessCheck": lambda n : setattr(self, 'period_offline_before_access_check', n.get_timedelta_value()),
            "periodOfflineBeforeWipeIsEnforced": lambda n : setattr(self, 'period_offline_before_wipe_is_enforced', n.get_timedelta_value()),
            "periodOnlineBeforeAccessCheck": lambda n : setattr(self, 'period_online_before_access_check', n.get_timedelta_value()),
            "pinCharacterSet": lambda n : setattr(self, 'pin_character_set', n.get_enum_value(ManagedAppPinCharacterSet)),
            "pinRequired": lambda n : setattr(self, 'pin_required', n.get_bool_value()),
            "printBlocked": lambda n : setattr(self, 'print_blocked', n.get_bool_value()),
            "saveAsBlocked": lambda n : setattr(self, 'save_as_blocked', n.get_bool_value()),
            "simplePinBlocked": lambda n : setattr(self, 'simple_pin_blocked', n.get_bool_value()),
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
        writer.write_collection_of_enum_values("allowedDataStorageLocations", self.allowed_data_storage_locations)
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
        writer.write_timedelta_value("periodBeforePinReset", self.period_before_pin_reset)
        writer.write_timedelta_value("periodOfflineBeforeAccessCheck", self.period_offline_before_access_check)
        writer.write_timedelta_value("periodOfflineBeforeWipeIsEnforced", self.period_offline_before_wipe_is_enforced)
        writer.write_timedelta_value("periodOnlineBeforeAccessCheck", self.period_online_before_access_check)
        writer.write_enum_value("pinCharacterSet", self.pin_character_set)
        writer.write_bool_value("pinRequired", self.pin_required)
        writer.write_bool_value("printBlocked", self.print_blocked)
        writer.write_bool_value("saveAsBlocked", self.save_as_blocked)
        writer.write_bool_value("simplePinBlocked", self.simple_pin_blocked)
    

