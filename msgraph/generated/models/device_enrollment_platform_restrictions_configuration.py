from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_enrollment_configuration = lazy_import('msgraph.generated.models.device_enrollment_configuration')
device_enrollment_platform_restriction = lazy_import('msgraph.generated.models.device_enrollment_platform_restriction')

class DeviceEnrollmentPlatformRestrictionsConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    @property
    def android_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the androidRestriction property value. Android restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._android_restriction
    
    @android_restriction.setter
    def android_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the androidRestriction property value. Android restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the androidRestriction property.
        """
        self._android_restriction = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceEnrollmentPlatformRestrictionsConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration"
        # Android restrictions based on platform, platform operating system version, and device ownership
        self._android_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Ios restrictions based on platform, platform operating system version, and device ownership
        self._ios_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Mac restrictions based on platform, platform operating system version, and device ownership
        self._mac_o_s_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Windows mobile restrictions based on platform, platform operating system version, and device ownership
        self._windows_mobile_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
        # Windows restrictions based on platform, platform operating system version, and device ownership
        self._windows_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceEnrollmentPlatformRestrictionsConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceEnrollmentPlatformRestrictionsConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceEnrollmentPlatformRestrictionsConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "android_restriction": lambda n : setattr(self, 'android_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "ios_restriction": lambda n : setattr(self, 'ios_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "mac_o_s_restriction": lambda n : setattr(self, 'mac_o_s_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "windows_mobile_restriction": lambda n : setattr(self, 'windows_mobile_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "windows_restriction": lambda n : setattr(self, 'windows_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ios_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the iosRestriction property value. Ios restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._ios_restriction
    
    @ios_restriction.setter
    def ios_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the iosRestriction property value. Ios restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the iosRestriction property.
        """
        self._ios_restriction = value
    
    @property
    def mac_o_s_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the macOSRestriction property value. Mac restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._mac_o_s_restriction
    
    @mac_o_s_restriction.setter
    def mac_o_s_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the macOSRestriction property value. Mac restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the macOSRestriction property.
        """
        self._mac_o_s_restriction = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("androidRestriction", self.android_restriction)
        writer.write_object_value("iosRestriction", self.ios_restriction)
        writer.write_object_value("macOSRestriction", self.mac_o_s_restriction)
        writer.write_object_value("windowsMobileRestriction", self.windows_mobile_restriction)
        writer.write_object_value("windowsRestriction", self.windows_restriction)
    
    @property
    def windows_mobile_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the windowsMobileRestriction property value. Windows mobile restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._windows_mobile_restriction
    
    @windows_mobile_restriction.setter
    def windows_mobile_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the windowsMobileRestriction property value. Windows mobile restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the windowsMobileRestriction property.
        """
        self._windows_mobile_restriction = value
    
    @property
    def windows_restriction(self,) -> Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]:
        """
        Gets the windowsRestriction property value. Windows restrictions based on platform, platform operating system version, and device ownership
        Returns: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction]
        """
        return self._windows_restriction
    
    @windows_restriction.setter
    def windows_restriction(self,value: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None) -> None:
        """
        Sets the windowsRestriction property value. Windows restrictions based on platform, platform operating system version, and device ownership
        Args:
            value: Value to set for the windowsRestriction property.
        """
        self._windows_restriction = value
    

