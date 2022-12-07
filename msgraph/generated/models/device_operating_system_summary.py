from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceOperatingSystemSummary(AdditionalDataHolder, Parsable):
    """
    Device operating system summary.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def android_corporate_work_profile_count(self,) -> Optional[int]:
        """
        Gets the androidCorporateWorkProfileCount property value. The count of Corporate work profile Android devices. Also known as Corporate Owned Personally Enabled (COPE). Valid values -1 to 2147483647
        Returns: Optional[int]
        """
        return self._android_corporate_work_profile_count
    
    @android_corporate_work_profile_count.setter
    def android_corporate_work_profile_count(self,value: Optional[int] = None) -> None:
        """
        Sets the androidCorporateWorkProfileCount property value. The count of Corporate work profile Android devices. Also known as Corporate Owned Personally Enabled (COPE). Valid values -1 to 2147483647
        Args:
            value: Value to set for the androidCorporateWorkProfileCount property.
        """
        self._android_corporate_work_profile_count = value
    
    @property
    def android_count(self,) -> Optional[int]:
        """
        Gets the androidCount property value. Number of android device count.
        Returns: Optional[int]
        """
        return self._android_count
    
    @android_count.setter
    def android_count(self,value: Optional[int] = None) -> None:
        """
        Sets the androidCount property value. Number of android device count.
        Args:
            value: Value to set for the androidCount property.
        """
        self._android_count = value
    
    @property
    def android_dedicated_count(self,) -> Optional[int]:
        """
        Gets the androidDedicatedCount property value. Number of dedicated Android devices.
        Returns: Optional[int]
        """
        return self._android_dedicated_count
    
    @android_dedicated_count.setter
    def android_dedicated_count(self,value: Optional[int] = None) -> None:
        """
        Sets the androidDedicatedCount property value. Number of dedicated Android devices.
        Args:
            value: Value to set for the androidDedicatedCount property.
        """
        self._android_dedicated_count = value
    
    @property
    def android_device_admin_count(self,) -> Optional[int]:
        """
        Gets the androidDeviceAdminCount property value. Number of device admin Android devices.
        Returns: Optional[int]
        """
        return self._android_device_admin_count
    
    @android_device_admin_count.setter
    def android_device_admin_count(self,value: Optional[int] = None) -> None:
        """
        Sets the androidDeviceAdminCount property value. Number of device admin Android devices.
        Args:
            value: Value to set for the androidDeviceAdminCount property.
        """
        self._android_device_admin_count = value
    
    @property
    def android_fully_managed_count(self,) -> Optional[int]:
        """
        Gets the androidFullyManagedCount property value. Number of fully managed Android devices.
        Returns: Optional[int]
        """
        return self._android_fully_managed_count
    
    @android_fully_managed_count.setter
    def android_fully_managed_count(self,value: Optional[int] = None) -> None:
        """
        Sets the androidFullyManagedCount property value. Number of fully managed Android devices.
        Args:
            value: Value to set for the androidFullyManagedCount property.
        """
        self._android_fully_managed_count = value
    
    @property
    def android_work_profile_count(self,) -> Optional[int]:
        """
        Gets the androidWorkProfileCount property value. Number of work profile Android devices.
        Returns: Optional[int]
        """
        return self._android_work_profile_count
    
    @android_work_profile_count.setter
    def android_work_profile_count(self,value: Optional[int] = None) -> None:
        """
        Sets the androidWorkProfileCount property value. Number of work profile Android devices.
        Args:
            value: Value to set for the androidWorkProfileCount property.
        """
        self._android_work_profile_count = value
    
    @property
    def config_mgr_device_count(self,) -> Optional[int]:
        """
        Gets the configMgrDeviceCount property value. Number of ConfigMgr managed devices.
        Returns: Optional[int]
        """
        return self._config_mgr_device_count
    
    @config_mgr_device_count.setter
    def config_mgr_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the configMgrDeviceCount property value. Number of ConfigMgr managed devices.
        Args:
            value: Value to set for the configMgrDeviceCount property.
        """
        self._config_mgr_device_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceOperatingSystemSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The count of Corporate work profile Android devices. Also known as Corporate Owned Personally Enabled (COPE). Valid values -1 to 2147483647
        self._android_corporate_work_profile_count: Optional[int] = None
        # Number of android device count.
        self._android_count: Optional[int] = None
        # Number of dedicated Android devices.
        self._android_dedicated_count: Optional[int] = None
        # Number of device admin Android devices.
        self._android_device_admin_count: Optional[int] = None
        # Number of fully managed Android devices.
        self._android_fully_managed_count: Optional[int] = None
        # Number of work profile Android devices.
        self._android_work_profile_count: Optional[int] = None
        # Number of ConfigMgr managed devices.
        self._config_mgr_device_count: Optional[int] = None
        # Number of iOS device count.
        self._ios_count: Optional[int] = None
        # Number of Mac OS X device count.
        self._mac_o_s_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Number of unknown device count.
        self._unknown_count: Optional[int] = None
        # Number of Windows device count.
        self._windows_count: Optional[int] = None
        # Number of Windows mobile device count.
        self._windows_mobile_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceOperatingSystemSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceOperatingSystemSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceOperatingSystemSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "android_corporate_work_profile_count": lambda n : setattr(self, 'android_corporate_work_profile_count', n.get_int_value()),
            "android_count": lambda n : setattr(self, 'android_count', n.get_int_value()),
            "android_dedicated_count": lambda n : setattr(self, 'android_dedicated_count', n.get_int_value()),
            "android_device_admin_count": lambda n : setattr(self, 'android_device_admin_count', n.get_int_value()),
            "android_fully_managed_count": lambda n : setattr(self, 'android_fully_managed_count', n.get_int_value()),
            "android_work_profile_count": lambda n : setattr(self, 'android_work_profile_count', n.get_int_value()),
            "config_mgr_device_count": lambda n : setattr(self, 'config_mgr_device_count', n.get_int_value()),
            "ios_count": lambda n : setattr(self, 'ios_count', n.get_int_value()),
            "mac_o_s_count": lambda n : setattr(self, 'mac_o_s_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "unknown_count": lambda n : setattr(self, 'unknown_count', n.get_int_value()),
            "windows_count": lambda n : setattr(self, 'windows_count', n.get_int_value()),
            "windows_mobile_count": lambda n : setattr(self, 'windows_mobile_count', n.get_int_value()),
        }
        return fields
    
    @property
    def ios_count(self,) -> Optional[int]:
        """
        Gets the iosCount property value. Number of iOS device count.
        Returns: Optional[int]
        """
        return self._ios_count
    
    @ios_count.setter
    def ios_count(self,value: Optional[int] = None) -> None:
        """
        Sets the iosCount property value. Number of iOS device count.
        Args:
            value: Value to set for the iosCount property.
        """
        self._ios_count = value
    
    @property
    def mac_o_s_count(self,) -> Optional[int]:
        """
        Gets the macOSCount property value. Number of Mac OS X device count.
        Returns: Optional[int]
        """
        return self._mac_o_s_count
    
    @mac_o_s_count.setter
    def mac_o_s_count(self,value: Optional[int] = None) -> None:
        """
        Sets the macOSCount property value. Number of Mac OS X device count.
        Args:
            value: Value to set for the macOSCount property.
        """
        self._mac_o_s_count = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def unknown_count(self,) -> Optional[int]:
        """
        Gets the unknownCount property value. Number of unknown device count.
        Returns: Optional[int]
        """
        return self._unknown_count
    
    @unknown_count.setter
    def unknown_count(self,value: Optional[int] = None) -> None:
        """
        Sets the unknownCount property value. Number of unknown device count.
        Args:
            value: Value to set for the unknownCount property.
        """
        self._unknown_count = value
    
    @property
    def windows_count(self,) -> Optional[int]:
        """
        Gets the windowsCount property value. Number of Windows device count.
        Returns: Optional[int]
        """
        return self._windows_count
    
    @windows_count.setter
    def windows_count(self,value: Optional[int] = None) -> None:
        """
        Sets the windowsCount property value. Number of Windows device count.
        Args:
            value: Value to set for the windowsCount property.
        """
        self._windows_count = value
    
    @property
    def windows_mobile_count(self,) -> Optional[int]:
        """
        Gets the windowsMobileCount property value. Number of Windows mobile device count.
        Returns: Optional[int]
        """
        return self._windows_mobile_count
    
    @windows_mobile_count.setter
    def windows_mobile_count(self,value: Optional[int] = None) -> None:
        """
        Sets the windowsMobileCount property value. Number of Windows mobile device count.
        Args:
            value: Value to set for the windowsMobileCount property.
        """
        self._windows_mobile_count = value
    

