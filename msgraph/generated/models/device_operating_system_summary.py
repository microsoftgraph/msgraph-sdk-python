from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DeviceOperatingSystemSummary(AdditionalDataHolder, BackedModel, Parsable):
    """
    Device operating system summary.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The count of Corporate work profile Android devices. Also known as Corporate Owned Personally Enabled (COPE). Valid values -1 to 2147483647
    android_corporate_work_profile_count: Optional[int] = None
    # Number of android device count.
    android_count: Optional[int] = None
    # Number of dedicated Android devices.
    android_dedicated_count: Optional[int] = None
    # Number of device admin Android devices.
    android_device_admin_count: Optional[int] = None
    # Number of fully managed Android devices.
    android_fully_managed_count: Optional[int] = None
    # Number of work profile Android devices.
    android_work_profile_count: Optional[int] = None
    # Number of ConfigMgr managed devices.
    config_mgr_device_count: Optional[int] = None
    # Number of iOS device count.
    ios_count: Optional[int] = None
    # Number of Mac OS X device count.
    mac_o_s_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Number of unknown device count.
    unknown_count: Optional[int] = None
    # Number of Windows device count.
    windows_count: Optional[int] = None
    # Number of Windows mobile device count.
    windows_mobile_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceOperatingSystemSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceOperatingSystemSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceOperatingSystemSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "androidCorporateWorkProfileCount": lambda n : setattr(self, 'android_corporate_work_profile_count', n.get_int_value()),
            "androidCount": lambda n : setattr(self, 'android_count', n.get_int_value()),
            "androidDedicatedCount": lambda n : setattr(self, 'android_dedicated_count', n.get_int_value()),
            "androidDeviceAdminCount": lambda n : setattr(self, 'android_device_admin_count', n.get_int_value()),
            "androidFullyManagedCount": lambda n : setattr(self, 'android_fully_managed_count', n.get_int_value()),
            "androidWorkProfileCount": lambda n : setattr(self, 'android_work_profile_count', n.get_int_value()),
            "configMgrDeviceCount": lambda n : setattr(self, 'config_mgr_device_count', n.get_int_value()),
            "iosCount": lambda n : setattr(self, 'ios_count', n.get_int_value()),
            "macOSCount": lambda n : setattr(self, 'mac_o_s_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "unknownCount": lambda n : setattr(self, 'unknown_count', n.get_int_value()),
            "windowsCount": lambda n : setattr(self, 'windows_count', n.get_int_value()),
            "windowsMobileCount": lambda n : setattr(self, 'windows_mobile_count', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("androidCorporateWorkProfileCount", self.android_corporate_work_profile_count)
        writer.write_int_value("androidCount", self.android_count)
        writer.write_int_value("androidDedicatedCount", self.android_dedicated_count)
        writer.write_int_value("androidDeviceAdminCount", self.android_device_admin_count)
        writer.write_int_value("androidFullyManagedCount", self.android_fully_managed_count)
        writer.write_int_value("androidWorkProfileCount", self.android_work_profile_count)
        writer.write_int_value("configMgrDeviceCount", self.config_mgr_device_count)
        writer.write_int_value("iosCount", self.ios_count)
        writer.write_int_value("macOSCount", self.mac_o_s_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("unknownCount", self.unknown_count)
        writer.write_int_value("windowsCount", self.windows_count)
        writer.write_int_value("windowsMobileCount", self.windows_mobile_count)
        writer.write_additional_data_value(self.additional_data)
    

