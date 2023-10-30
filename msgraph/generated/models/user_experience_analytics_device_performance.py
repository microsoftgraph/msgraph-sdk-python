from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disk_type import DiskType
    from .entity import Entity
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

from .entity import Entity

@dataclass
class UserExperienceAnalyticsDevicePerformance(Entity):
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsDevicePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDevicePerformance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDevicePerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .disk_type import DiskType
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        from .disk_type import DiskType
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        fields: Dict[str, Callable[[Any], None]] = {
            "average_blue_screens": lambda n : setattr(self, 'average_blue_screens', n.get_float_value()),
            "average_restarts": lambda n : setattr(self, 'average_restarts', n.get_float_value()),
            "blue_screen_count": lambda n : setattr(self, 'blue_screen_count', n.get_int_value()),
            "boot_score": lambda n : setattr(self, 'boot_score', n.get_int_value()),
            "core_boot_time_in_ms": lambda n : setattr(self, 'core_boot_time_in_ms', n.get_int_value()),
            "core_login_time_in_ms": lambda n : setattr(self, 'core_login_time_in_ms', n.get_int_value()),
            "device_count": lambda n : setattr(self, 'device_count', n.get_int_value()),
            "device_name": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "disk_type": lambda n : setattr(self, 'disk_type', n.get_enum_value(DiskType)),
            "group_policy_boot_time_in_ms": lambda n : setattr(self, 'group_policy_boot_time_in_ms', n.get_int_value()),
            "group_policy_login_time_in_ms": lambda n : setattr(self, 'group_policy_login_time_in_ms', n.get_int_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "login_score": lambda n : setattr(self, 'login_score', n.get_int_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "model_startup_performance_score": lambda n : setattr(self, 'model_startup_performance_score', n.get_float_value()),
            "operating_system_version": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "responsive_desktop_time_in_ms": lambda n : setattr(self, 'responsive_desktop_time_in_ms', n.get_int_value()),
            "restart_count": lambda n : setattr(self, 'restart_count', n.get_int_value()),
            "startup_performance_score": lambda n : setattr(self, 'startup_performance_score', n.get_float_value()),
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
        writer.write_float_value("average_blue_screens", self.average_blue_screens)
        writer.write_float_value("average_restarts", self.average_restarts)
        writer.write_int_value("blue_screen_count", self.blue_screen_count)
        writer.write_int_value("boot_score", self.boot_score)
        writer.write_int_value("core_boot_time_in_ms", self.core_boot_time_in_ms)
        writer.write_int_value("core_login_time_in_ms", self.core_login_time_in_ms)
        writer.write_int_value("device_count", self.device_count)
        writer.write_str_value("device_name", self.device_name)
        writer.write_enum_value("disk_type", self.disk_type)
        writer.write_int_value("group_policy_boot_time_in_ms", self.group_policy_boot_time_in_ms)
        writer.write_int_value("group_policy_login_time_in_ms", self.group_policy_login_time_in_ms)
        writer.write_enum_value("health_status", self.health_status)
        writer.write_int_value("login_score", self.login_score)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_float_value("model_startup_performance_score", self.model_startup_performance_score)
        writer.write_str_value("operating_system_version", self.operating_system_version)
        writer.write_int_value("responsive_desktop_time_in_ms", self.responsive_desktop_time_in_ms)
        writer.write_int_value("restart_count", self.restart_count)
        writer.write_float_value("startup_performance_score", self.startup_performance_score)
    

