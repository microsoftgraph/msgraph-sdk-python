from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion(Entity, Parsable):
    """
    The user experience analytics application performance entity contains app performance details by OS version.
    """
    # The number of devices where the application has been active. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    active_device_count: Optional[int] = None
    # The number of crashes for the application. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    app_crash_count: Optional[int] = None
    # The friendly name of the application. The possible values are: Outlook, Excel. Supports: $select, $OrderBy. Read-only.
    app_display_name: Optional[str] = None
    # The name of the application. The possible values are: outlook.exe, excel.exe. Supports: $select, $OrderBy. Read-only.
    app_name: Optional[str] = None
    # The publisher of the application. Supports: $select, $OrderBy. Read-only.
    app_publisher: Optional[str] = None
    # The total usage time of the application in minutes. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    app_usage_duration: Optional[int] = None
    # The mean time to failure for the application in minutes. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    mean_time_to_failure_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The OS build number of the application. Supports: $select, $OrderBy. Read-only.
    os_build_number: Optional[str] = None
    # The OS version of the application. Supports: $select, $OrderBy. Read-only.
    os_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "activeDeviceCount": lambda n : setattr(self, 'active_device_count', n.get_int_value()),
            "appCrashCount": lambda n : setattr(self, 'app_crash_count', n.get_int_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "appPublisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "appUsageDuration": lambda n : setattr(self, 'app_usage_duration', n.get_int_value()),
            "meanTimeToFailureInMinutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "osBuildNumber": lambda n : setattr(self, 'os_build_number', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
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
        writer.write_int_value("activeDeviceCount", self.active_device_count)
        writer.write_int_value("appCrashCount", self.app_crash_count)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_int_value("appUsageDuration", self.app_usage_duration)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
        writer.write_str_value("osBuildNumber", self.os_build_number)
        writer.write_str_value("osVersion", self.os_version)
    

