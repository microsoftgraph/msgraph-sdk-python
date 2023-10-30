from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

from .entity import Entity

@dataclass
class UserExperienceAnalyticsAppHealthDevicePerformance(Entity):
    """
    The user experience analytics device performance entity contains device performance details.
    """
    # The number of application crashes for the device. Valid values 0 to 2147483647. Supports: $filter, $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    app_crash_count: Optional[int] = None
    # The number of application hangs for the device. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    app_hang_count: Optional[int] = None
    # The number of distinct application crashes for the device. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    crashed_app_count: Optional[int] = None
    # The application health score of the device. Valid values 0 to 100. Supports: $filter, $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    device_app_health_score: Optional[float] = None
    # The name of the device. Supports: $select, $OrderBy. Read-only.
    device_display_name: Optional[str] = None
    # The Intune device id of the device. Supports: $select, $OrderBy. Read-only.
    device_id: Optional[str] = None
    # The manufacturer name of the device. Supports: $select, $OrderBy. Read-only.
    device_manufacturer: Optional[str] = None
    # The model name of the device. Supports: $select, $OrderBy. Read-only.
    device_model: Optional[str] = None
    # The healthStatus property
    health_status: Optional[UserExperienceAnalyticsHealthState] = None
    # The mean time to failure for the application in minutes. Valid values 0 to 2147483647. Supports: $filter, $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    mean_time_to_failure_in_minutes: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the statistics were last computed. The value cannot be modified and is automatically populated when the statistics are computed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2022 would look like this: '2022-01-01T00:00:00Z'. Returned by default. Read-only.
    processed_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsAppHealthDevicePerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthDevicePerformance
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAppHealthDevicePerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        fields: Dict[str, Callable[[Any], None]] = {
            "app_crash_count": lambda n : setattr(self, 'app_crash_count', n.get_int_value()),
            "app_hang_count": lambda n : setattr(self, 'app_hang_count', n.get_int_value()),
            "crashed_app_count": lambda n : setattr(self, 'crashed_app_count', n.get_int_value()),
            "device_app_health_score": lambda n : setattr(self, 'device_app_health_score', n.get_float_value()),
            "device_display_name": lambda n : setattr(self, 'device_display_name', n.get_str_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "device_manufacturer": lambda n : setattr(self, 'device_manufacturer', n.get_str_value()),
            "device_model": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "health_status": lambda n : setattr(self, 'health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "mean_time_to_failure_in_minutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "processed_date_time": lambda n : setattr(self, 'processed_date_time', n.get_datetime_value()),
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
        writer.write_int_value("app_crash_count", self.app_crash_count)
        writer.write_int_value("app_hang_count", self.app_hang_count)
        writer.write_int_value("crashed_app_count", self.crashed_app_count)
        writer.write_float_value("device_app_health_score", self.device_app_health_score)
        writer.write_str_value("device_display_name", self.device_display_name)
        writer.write_str_value("device_id", self.device_id)
        writer.write_str_value("device_manufacturer", self.device_manufacturer)
        writer.write_str_value("device_model", self.device_model)
        writer.write_enum_value("health_status", self.health_status)
        writer.write_int_value("mean_time_to_failure_in_minutes", self.mean_time_to_failure_in_minutes)
        writer.write_datetime_value("processed_date_time", self.processed_date_time)
    

