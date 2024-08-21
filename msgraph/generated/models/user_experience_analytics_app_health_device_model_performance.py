from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

from .entity import Entity

@dataclass
class UserExperienceAnalyticsAppHealthDeviceModelPerformance(Entity):
    """
    The user experience analytics device model performance entity contains device model performance details.
    """
    # The number of active devices for the model. Valid values 0 to 2147483647. Supports: $filter, $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    active_device_count: Optional[int] = None
    # The manufacturer name of the device. Supports: $select, $OrderBy. Read-only.
    device_manufacturer: Optional[str] = None
    # The model name of the device. Supports: $select, $OrderBy. Read-only.
    device_model: Optional[str] = None
    # The healthStatus property
    health_status: Optional[UserExperienceAnalyticsHealthState] = None
    # The mean time to failure for the application in minutes. Valid values 0 to 2147483647. Supports: $filter, $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    mean_time_to_failure_in_minutes: Optional[int] = None
    # The application health score of the device model. Valid values 0 to 100. Supports: $filter, $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    model_app_health_score: Optional[float] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsAppHealthDeviceModelPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthDeviceModelPerformance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAppHealthDeviceModelPerformance()
    
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
            "activeDeviceCount": lambda n : setattr(self, 'active_device_count', n.get_int_value()),
            "deviceManufacturer": lambda n : setattr(self, 'device_manufacturer', n.get_str_value()),
            "deviceModel": lambda n : setattr(self, 'device_model', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "meanTimeToFailureInMinutes": lambda n : setattr(self, 'mean_time_to_failure_in_minutes', n.get_int_value()),
            "modelAppHealthScore": lambda n : setattr(self, 'model_app_health_score', n.get_float_value()),
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
        writer.write_str_value("deviceManufacturer", self.device_manufacturer)
        writer.write_str_value("deviceModel", self.device_model)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_int_value("meanTimeToFailureInMinutes", self.mean_time_to_failure_in_minutes)
        writer.write_float_value("modelAppHealthScore", self.model_app_health_score)
    

