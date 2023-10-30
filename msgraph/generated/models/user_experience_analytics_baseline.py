from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_category import UserExperienceAnalyticsCategory

from .entity import Entity

@dataclass
class UserExperienceAnalyticsBaseline(Entity):
    """
    The user experience analytics baseline entity contains baseline values against which to compare the user experience analytics scores.
    """
    # The scores and insights for the application health metrics.
    app_health_metrics: Optional[UserExperienceAnalyticsCategory] = None
    # The scores and insights for the battery health metrics.
    battery_health_metrics: Optional[UserExperienceAnalyticsCategory] = None
    # The scores and insights for the best practices metrics.
    best_practices_metrics: Optional[UserExperienceAnalyticsCategory] = None
    # The date the custom baseline was created. The value cannot be modified and is automatically populated when the baseline is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Returned by default.
    created_date_time: Optional[datetime.datetime] = None
    # The scores and insights for the device boot performance metrics.
    device_boot_performance_metrics: Optional[UserExperienceAnalyticsCategory] = None
    # The name of the baseline.
    display_name: Optional[str] = None
    # When TRUE, indicates the current baseline is the commercial median baseline. When FALSE, indicates it is a custom baseline. FALSE by default.
    is_built_in: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scores and insights for the reboot analytics metrics.
    reboot_analytics_metrics: Optional[UserExperienceAnalyticsCategory] = None
    # The scores and insights for the resource performance metrics.
    resource_performance_metrics: Optional[UserExperienceAnalyticsCategory] = None
    # The scores and insights for the work from anywhere metrics.
    work_from_anywhere_metrics: Optional[UserExperienceAnalyticsCategory] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsBaseline:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsBaseline
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsBaseline()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_category import UserExperienceAnalyticsCategory

        from .entity import Entity
        from .user_experience_analytics_category import UserExperienceAnalyticsCategory

        fields: Dict[str, Callable[[Any], None]] = {
            "app_health_metrics": lambda n : setattr(self, 'app_health_metrics', n.get_object_value(UserExperienceAnalyticsCategory)),
            "battery_health_metrics": lambda n : setattr(self, 'battery_health_metrics', n.get_object_value(UserExperienceAnalyticsCategory)),
            "best_practices_metrics": lambda n : setattr(self, 'best_practices_metrics', n.get_object_value(UserExperienceAnalyticsCategory)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device_boot_performance_metrics": lambda n : setattr(self, 'device_boot_performance_metrics', n.get_object_value(UserExperienceAnalyticsCategory)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "is_built_in": lambda n : setattr(self, 'is_built_in', n.get_bool_value()),
            "reboot_analytics_metrics": lambda n : setattr(self, 'reboot_analytics_metrics', n.get_object_value(UserExperienceAnalyticsCategory)),
            "resource_performance_metrics": lambda n : setattr(self, 'resource_performance_metrics', n.get_object_value(UserExperienceAnalyticsCategory)),
            "work_from_anywhere_metrics": lambda n : setattr(self, 'work_from_anywhere_metrics', n.get_object_value(UserExperienceAnalyticsCategory)),
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
        writer.write_object_value("app_health_metrics", self.app_health_metrics)
        writer.write_object_value("battery_health_metrics", self.battery_health_metrics)
        writer.write_object_value("best_practices_metrics", self.best_practices_metrics)
        writer.write_datetime_value("created_date_time", self.created_date_time)
        writer.write_object_value("device_boot_performance_metrics", self.device_boot_performance_metrics)
        writer.write_str_value("display_name", self.display_name)
        writer.write_bool_value("is_built_in", self.is_built_in)
        writer.write_object_value("reboot_analytics_metrics", self.reboot_analytics_metrics)
        writer.write_object_value("resource_performance_metrics", self.resource_performance_metrics)
        writer.write_object_value("work_from_anywhere_metrics", self.work_from_anywhere_metrics)
    

