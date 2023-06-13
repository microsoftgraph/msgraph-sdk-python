from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_enrollment_configuration, device_enrollment_platform_restriction

from . import device_enrollment_configuration

@dataclass
class DeviceEnrollmentPlatformRestrictionsConfiguration(device_enrollment_configuration.DeviceEnrollmentConfiguration):
    odata_type = "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration"
    # Android restrictions based on platform, platform operating system version, and device ownership
    android_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
    # Ios restrictions based on platform, platform operating system version, and device ownership
    ios_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
    # Mac restrictions based on platform, platform operating system version, and device ownership
    mac_o_s_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
    # Windows mobile restrictions based on platform, platform operating system version, and device ownership
    windows_mobile_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
    # Windows restrictions based on platform, platform operating system version, and device ownership
    windows_restriction: Optional[device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction] = None
    
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
        from . import device_enrollment_configuration, device_enrollment_platform_restriction

        fields: Dict[str, Callable[[Any], None]] = {
            "androidRestriction": lambda n : setattr(self, 'android_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "iosRestriction": lambda n : setattr(self, 'ios_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "macOSRestriction": lambda n : setattr(self, 'mac_o_s_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "windowsMobileRestriction": lambda n : setattr(self, 'windows_mobile_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
            "windowsRestriction": lambda n : setattr(self, 'windows_restriction', n.get_object_value(device_enrollment_platform_restriction.DeviceEnrollmentPlatformRestriction)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    

