from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
    from .user_experience_analytics_work_from_anywhere_model_performance_cloud_identity_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudIdentityScore
    from .user_experience_analytics_work_from_anywhere_model_performance_cloud_management_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudManagementScore
    from .user_experience_analytics_work_from_anywhere_model_performance_cloud_provisioning_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudProvisioningScore
    from .user_experience_analytics_work_from_anywhere_model_performance_windows_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_windowsScore
    from .user_experience_analytics_work_from_anywhere_model_performance_work_from_anywhere_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_workFromAnywhereScore

from .entity import Entity

@dataclass
class UserExperienceAnalyticsWorkFromAnywhereModelPerformance(Entity):
    """
    The user experience analytics work from anywhere model performance.
    """
    # The cloud identity score of the device model. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_identity_score: Optional[UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudIdentityScore] = None
    # The cloud management score of the device model. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_management_score: Optional[UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudManagementScore] = None
    # The cloud provisioning score of the device model.  Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_provisioning_score: Optional[UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudProvisioningScore] = None
    # The healthStatus property
    health_status: Optional[UserExperienceAnalyticsHealthState] = None
    # The manufacturer name of the device. Supports: $select, $OrderBy. Read-only.
    manufacturer: Optional[str] = None
    # The model name of the device. Supports: $select, $OrderBy. Read-only.
    model: Optional[str] = None
    # The devices count for the model. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    model_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The window score of the device model. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    windows_score: Optional[UserExperienceAnalyticsWorkFromAnywhereModelPerformance_windowsScore] = None
    # The work from anywhere score of the device model. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    work_from_anywhere_score: Optional[UserExperienceAnalyticsWorkFromAnywhereModelPerformance_workFromAnywhereScore] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsWorkFromAnywhereModelPerformance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsWorkFromAnywhereModelPerformance()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
        from .user_experience_analytics_work_from_anywhere_model_performance_cloud_identity_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudIdentityScore
        from .user_experience_analytics_work_from_anywhere_model_performance_cloud_management_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudManagementScore
        from .user_experience_analytics_work_from_anywhere_model_performance_cloud_provisioning_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudProvisioningScore
        from .user_experience_analytics_work_from_anywhere_model_performance_windows_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_windowsScore
        from .user_experience_analytics_work_from_anywhere_model_performance_work_from_anywhere_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_workFromAnywhereScore

        from .entity import Entity
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState
        from .user_experience_analytics_work_from_anywhere_model_performance_cloud_identity_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudIdentityScore
        from .user_experience_analytics_work_from_anywhere_model_performance_cloud_management_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudManagementScore
        from .user_experience_analytics_work_from_anywhere_model_performance_cloud_provisioning_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudProvisioningScore
        from .user_experience_analytics_work_from_anywhere_model_performance_windows_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_windowsScore
        from .user_experience_analytics_work_from_anywhere_model_performance_work_from_anywhere_score import UserExperienceAnalyticsWorkFromAnywhereModelPerformance_workFromAnywhereScore

        fields: Dict[str, Callable[[Any], None]] = {
            "cloudIdentityScore": lambda n : setattr(self, 'cloud_identity_score', n.get_object_value(UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudIdentityScore)),
            "cloudManagementScore": lambda n : setattr(self, 'cloud_management_score', n.get_object_value(UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudManagementScore)),
            "cloudProvisioningScore": lambda n : setattr(self, 'cloud_provisioning_score', n.get_object_value(UserExperienceAnalyticsWorkFromAnywhereModelPerformance_cloudProvisioningScore)),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "modelDeviceCount": lambda n : setattr(self, 'model_device_count', n.get_int_value()),
            "windowsScore": lambda n : setattr(self, 'windows_score', n.get_object_value(UserExperienceAnalyticsWorkFromAnywhereModelPerformance_windowsScore)),
            "workFromAnywhereScore": lambda n : setattr(self, 'work_from_anywhere_score', n.get_object_value(UserExperienceAnalyticsWorkFromAnywhereModelPerformance_workFromAnywhereScore)),
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
        writer.write_object_value("cloudIdentityScore", self.cloud_identity_score)
        writer.write_object_value("cloudManagementScore", self.cloud_management_score)
        writer.write_object_value("cloudProvisioningScore", self.cloud_provisioning_score)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_int_value("modelDeviceCount", self.model_device_count)
        writer.write_object_value("windowsScore", self.windows_score)
        writer.write_object_value("workFromAnywhereScore", self.work_from_anywhere_score)
    

