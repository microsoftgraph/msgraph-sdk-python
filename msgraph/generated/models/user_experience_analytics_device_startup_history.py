from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_operating_system_restart_category import UserExperienceAnalyticsOperatingSystemRestartCategory

from .entity import Entity

@dataclass
class UserExperienceAnalyticsDeviceStartupHistory(Entity):
    """
    The user experience analytics device startup history entity contains device boot performance history details.
    """
    # The device core boot time in milliseconds. Supports: $select, $OrderBy. Read-only.
    core_boot_time_in_ms: Optional[int] = None
    # The device core login time in milliseconds. Supports: $select, $OrderBy. Read-only.
    core_login_time_in_ms: Optional[int] = None
    # The Intune device id of the device. Supports: $select, $OrderBy. Read-only.
    device_id: Optional[str] = None
    # The impact of device feature updates on boot time in milliseconds. Supports: $select, $OrderBy. Read-only.
    feature_update_boot_time_in_ms: Optional[int] = None
    # The impact of device group policy client on boot time in milliseconds. Supports: $select, $OrderBy. Read-only.
    group_policy_boot_time_in_ms: Optional[int] = None
    # The impact of device group policy client on login time in milliseconds. Supports: $select, $OrderBy. Read-only.
    group_policy_login_time_in_ms: Optional[int] = None
    # When TRUE, indicates the device boot record is associated with feature updates. When FALSE, indicates the device boot record is not associated with feature updates. Supports: $select, $OrderBy. Read-only.
    is_feature_update: Optional[bool] = None
    # When TRUE, indicates the device login is the first login after a reboot. When FALSE, indicates the device login is not the first login after a reboot. Supports: $select, $OrderBy. Read-only.
    is_first_login: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The user experience analytics device boot record's operating system version. Supports: $select, $OrderBy. Read-only.
    operating_system_version: Optional[str] = None
    # The time for desktop to become responsive during login process in milliseconds. Supports: $select, $OrderBy. Read-only.
    responsive_desktop_time_in_ms: Optional[int] = None
    # Operating System restart category.
    restart_category: Optional[UserExperienceAnalyticsOperatingSystemRestartCategory] = None
    # OS restart fault bucket. The fault bucket is used to find additional information about a system crash. Supports: $select, $OrderBy. Read-only.
    restart_fault_bucket: Optional[str] = None
    # OS restart stop code. This shows the bug check code which can be used to look up the blue screen reason. Supports: $select, $OrderBy. Read-only.
    restart_stop_code: Optional[str] = None
    # The device boot start time. The value cannot be modified and is automatically populated when the device performs a reboot. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2022 would look like this: '2022-01-01T00:00:00Z'. Returned by default. Read-only.
    start_time: Optional[datetime.datetime] = None
    # The device total boot time in milliseconds. Supports: $select, $OrderBy. Read-only.
    total_boot_time_in_ms: Optional[int] = None
    # The device total login time in milliseconds. Supports: $select, $OrderBy. Read-only.
    total_login_time_in_ms: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsDeviceStartupHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsDeviceStartupHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsDeviceStartupHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_operating_system_restart_category import UserExperienceAnalyticsOperatingSystemRestartCategory

        from .entity import Entity
        from .user_experience_analytics_operating_system_restart_category import UserExperienceAnalyticsOperatingSystemRestartCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "coreBootTimeInMs": lambda n : setattr(self, 'core_boot_time_in_ms', n.get_int_value()),
            "coreLoginTimeInMs": lambda n : setattr(self, 'core_login_time_in_ms', n.get_int_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "featureUpdateBootTimeInMs": lambda n : setattr(self, 'feature_update_boot_time_in_ms', n.get_int_value()),
            "groupPolicyBootTimeInMs": lambda n : setattr(self, 'group_policy_boot_time_in_ms', n.get_int_value()),
            "groupPolicyLoginTimeInMs": lambda n : setattr(self, 'group_policy_login_time_in_ms', n.get_int_value()),
            "isFeatureUpdate": lambda n : setattr(self, 'is_feature_update', n.get_bool_value()),
            "isFirstLogin": lambda n : setattr(self, 'is_first_login', n.get_bool_value()),
            "operatingSystemVersion": lambda n : setattr(self, 'operating_system_version', n.get_str_value()),
            "responsiveDesktopTimeInMs": lambda n : setattr(self, 'responsive_desktop_time_in_ms', n.get_int_value()),
            "restartCategory": lambda n : setattr(self, 'restart_category', n.get_enum_value(UserExperienceAnalyticsOperatingSystemRestartCategory)),
            "restartFaultBucket": lambda n : setattr(self, 'restart_fault_bucket', n.get_str_value()),
            "restartStopCode": lambda n : setattr(self, 'restart_stop_code', n.get_str_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_datetime_value()),
            "totalBootTimeInMs": lambda n : setattr(self, 'total_boot_time_in_ms', n.get_int_value()),
            "totalLoginTimeInMs": lambda n : setattr(self, 'total_login_time_in_ms', n.get_int_value()),
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
        writer.write_int_value("coreBootTimeInMs", self.core_boot_time_in_ms)
        writer.write_int_value("coreLoginTimeInMs", self.core_login_time_in_ms)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_int_value("featureUpdateBootTimeInMs", self.feature_update_boot_time_in_ms)
        writer.write_int_value("groupPolicyBootTimeInMs", self.group_policy_boot_time_in_ms)
        writer.write_int_value("groupPolicyLoginTimeInMs", self.group_policy_login_time_in_ms)
        writer.write_bool_value("isFeatureUpdate", self.is_feature_update)
        writer.write_bool_value("isFirstLogin", self.is_first_login)
        writer.write_str_value("operatingSystemVersion", self.operating_system_version)
        writer.write_int_value("responsiveDesktopTimeInMs", self.responsive_desktop_time_in_ms)
        writer.write_enum_value("restartCategory", self.restart_category)
        writer.write_str_value("restartFaultBucket", self.restart_fault_bucket)
        writer.write_str_value("restartStopCode", self.restart_stop_code)
        writer.write_datetime_value("startTime", self.start_time)
        writer.write_int_value("totalBootTimeInMs", self.total_boot_time_in_ms)
        writer.write_int_value("totalLoginTimeInMs", self.total_login_time_in_ms)
    

