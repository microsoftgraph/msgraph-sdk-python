from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disk_type import DiskType
    from .entity import Entity
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

from .entity import Entity

@dataclass
class UserExperienceAnalyticsDevicePerformance(Entity, Parsable):
    """
    The user experience analytics device performance entity contains device boot performance details.
    """
    # Average (mean) number of Blue Screens per device in the last 30 days. Valid values 0 to 9999999
    average_blue_screens: Optional[float] = None
    # Average (mean) number of Restarts per device in the last 30 days. Valid values 0 to 9999999
    average_restarts: Optional[float] = None
    # Number of Blue Screens in the last 30 days. Valid values 0 to 9999999
    blue_screen_count: Optional[int] = None
    # The user experience analytics device boot score.
    boot_score: Optional[int] = None
    # The user experience analytics device core boot time in milliseconds.
    core_boot_time_in_ms: Optional[int] = None
    # The user experience analytics device core login time in milliseconds.
    core_login_time_in_ms: Optional[int] = None
    # User experience analytics summarized device count.
    device_count: Optional[int] = None
    # The user experience analytics device name.
    device_name: Optional[str] = None
    # The diskType property
    disk_type: Optional[DiskType] = None
    # The user experience analytics device group policy boot time in milliseconds.
    group_policy_boot_time_in_ms: Optional[int] = None
    # The user experience analytics device group policy login time in milliseconds.
    group_policy_login_time_in_ms: Optional[int] = None
    # The healthStatus property
    health_status: Optional[UserExperienceAnalyticsHealthState] = None
    # The user experience analytics device login score.
    login_score: Optional[int] = None
    # The user experience analytics device manufacturer.
    manufacturer: Optional[str] = None
    # The user experience analytics device model.
    model: Optional[str] = None
    # The user experience analytics model level startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    model_startup_performance_score: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user experience analytics device Operating System version.
    operating_system_version: Optional[str] = None
    # The user experience analytics responsive desktop time in milliseconds.
    responsive_desktop_time_in_ms: Optional[int] = None
    # Number of Restarts in the last 30 days. Valid values 0 to 9999999
    restart_count: Optional[int] = None
    # The user experience analytics device startup performance score. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    startup_performance_score: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsDevicePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDevicePerformance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDevicePerformance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .disk_type import DiskType
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        from .disk_type import DiskType
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        fields: dict[str, Callable[[Any], None]] = {
            "averageBlueScreens": lambda n : setattr(self, 'average_blue_screens', n.get_float_value()),
            "averageRestarts": lambda n : setattr(self, 'average_restarts', n.get_float_value()),
            "blueScreenCount": lambda n : setattr(self, 'blue_screen_count', n.get_int_value()),
            "bootScore": lambda n : setattr(self, 'boot_score', n.get_int_value()),
            "coreBootTimeInMs": lambda n : setattr(self, 'core_boot_time_in_ms', n.get_int_value()),
            "coreLoginTimeInMs": lambda n : setattr(self, 'core_login_time_in_ms', n.get_int_value()),
            "deviceCount": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "diskType": lambda n : setattr(self, 'disk_type', n.get_enum_value(DiskType)),
            "groupPolicyBootTimeInMs": lambda n : setattr(self, 'group_policy_boot_time_in_ms', n.get_int_value()),
            "groupPolicyLoginTimeInMs": lambda n : setattr(self, 'group_policy_login_time_in_ms', n.get_int_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "loginScore": lambda n : setattr(self, 'login_score', n.get_int_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "modelStartupPerformanceScore": lambda n : setattr(self, 'model_startup_performance_score', n.get_float_value()),
            "operatingSystemVersion": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "responsiveDesktopTimeInMs": lambda n : setattr(self, 'responsive_desktop_time_in_ms', n.get_int_value()),
            "restartCount": lambda n : setattr(self, 'restart_count', n.get_int_value()),
            "startupPerformanceScore": lambda n : setattr(self, 'startup_performance_score', n.get_float_value()),
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
        writer.write_float_value("averageBlueScreens", self.average_blue_screens)
        writer.write_float_value("averageRestarts", self.average_restarts)
        writer.write_int_value("blueScreenCount", self.blue_screen_count)
        writer.write_int_value("bootScore", self.boot_score)
        writer.write_int_value("coreBootTimeInMs", self.core_boot_time_in_ms)
        writer.write_int_value("coreLoginTimeInMs", self.core_login_time_in_ms)
        writer.write_int_value("deviceCount", self.device_count)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("diskType", self.disk_type)
        writer.write_int_value("groupPolicyBootTimeInMs", self.group_policy_boot_time_in_ms)
        writer.write_int_value("groupPolicyLoginTimeInMs", self.group_policy_login_time_in_ms)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_int_value("loginScore", self.login_score)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("modelStartupPerformanceScore", self.model_startup_performance_score)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_int_value("responsiveDesktopTimeInMs", self.responsive_desktop_time_in_ms)
        writer.write_int_value("restartCount", self.restart_count)
        writer.write_float_value("startupPerformanceScore", self.startup_performance_score)
    

