from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_experience_analytics_autopilot_devices_summary import UserExperienceAnalyticsAutopilotDevicesSummary
    from .user_experience_analytics_cloud_identity_devices_summary import UserExperienceAnalyticsCloudIdentityDevicesSummary
    from .user_experience_analytics_cloud_management_devices_summary import UserExperienceAnalyticsCloudManagementDevicesSummary
    from .user_experience_analytics_windows10_devices_summary import UserExperienceAnalyticsWindows10DevicesSummary

@dataclass
class UserExperienceAnalyticsWorkFromAnywhereDevicesSummary(AdditionalDataHolder, BackedModel, Parsable):
    """
    The user experience analytics Work From Anywhere metrics devices summary.
    """
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The user experience analytics work from anywhere Autopilot devices summary. Read-only.
    autopilot_devices_summary: Optional[UserExperienceAnalyticsAutopilotDevicesSummary] = None
    # The user experience analytics work from anywhere Cloud Identity devices summary. Read-only.
    cloud_identity_devices_summary: Optional[UserExperienceAnalyticsCloudIdentityDevicesSummary] = None
    # The user experience analytics work from anywhere Cloud management devices summary. Read-only.
    cloud_management_devices_summary: Optional[UserExperienceAnalyticsCloudManagementDevicesSummary] = None
    # Total number of co-managed devices. Read-only. Valid values -2147483648 to 2147483647
    co_managed_devices: Optional[int] = None
    # The count of intune devices that are not autopilot registerd. Read-only. Valid values -2147483648 to 2147483647
    devices_not_autopilot_registered: Optional[int] = None
    # The count of intune devices not autopilot profile assigned. Read-only. Valid values -2147483648 to 2147483647
    devices_without_autopilot_profile_assigned: Optional[int] = None
    # The count of devices that are not cloud identity. Read-only. Valid values -2147483648 to 2147483647
    devices_without_cloud_identity: Optional[int] = None
    # The count of intune devices that are not autopilot registerd. Read-only. Valid values -2147483648 to 2147483647
    intune_devices: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total count of tenant attach devices. Read-only. Valid values -2147483648 to 2147483647
    tenant_attach_devices: Optional[int] = None
    # The total count of devices. Read-only. Valid values -2147483648 to 2147483647
    total_devices: Optional[int] = None
    # The count of Windows 10 devices that have unsupported OS versions. Read-only. Valid values -2147483648 to 2147483647
    unsupported_o_sversion_devices: Optional[int] = None
    # The count of windows 10 devices. Read-only. Valid values -2147483648 to 2147483647
    windows10_devices: Optional[int] = None
    # The user experience analytics work from anywhere Windows 10 devices summary. Read-only.
    windows10_devices_summary: Optional[UserExperienceAnalyticsWindows10DevicesSummary] = None
    # The count of windows 10 devices that are Intune and co-managed. Read-only. Valid values -2147483648 to 2147483647
    windows10_devices_without_tenant_attach: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserExperienceAnalyticsWorkFromAnywhereDevicesSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereDevicesSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsWorkFromAnywhereDevicesSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .user_experience_analytics_autopilot_devices_summary import UserExperienceAnalyticsAutopilotDevicesSummary
        from .user_experience_analytics_cloud_identity_devices_summary import UserExperienceAnalyticsCloudIdentityDevicesSummary
        from .user_experience_analytics_cloud_management_devices_summary import UserExperienceAnalyticsCloudManagementDevicesSummary
        from .user_experience_analytics_windows10_devices_summary import UserExperienceAnalyticsWindows10DevicesSummary

        from .user_experience_analytics_autopilot_devices_summary import UserExperienceAnalyticsAutopilotDevicesSummary
        from .user_experience_analytics_cloud_identity_devices_summary import UserExperienceAnalyticsCloudIdentityDevicesSummary
        from .user_experience_analytics_cloud_management_devices_summary import UserExperienceAnalyticsCloudManagementDevicesSummary
        from .user_experience_analytics_windows10_devices_summary import UserExperienceAnalyticsWindows10DevicesSummary

        fields: Dict[str, Callable[[Any], None]] = {
            "autopilot_devices_summary": lambda n : setattr(self, 'autopilot_devices_summary', n.get_object_value(UserExperienceAnalyticsAutopilotDevicesSummary)),
            "cloud_identity_devices_summary": lambda n : setattr(self, 'cloud_identity_devices_summary', n.get_object_value(UserExperienceAnalyticsCloudIdentityDevicesSummary)),
            "cloud_management_devices_summary": lambda n : setattr(self, 'cloud_management_devices_summary', n.get_object_value(UserExperienceAnalyticsCloudManagementDevicesSummary)),
            "co_managed_devices": lambda n : setattr(self, 'co_managed_devices', n.get_int_value()),
            "devices_not_autopilot_registered": lambda n : setattr(self, 'devices_not_autopilot_registered', n.get_int_value()),
            "devices_without_autopilot_profile_assigned": lambda n : setattr(self, 'devices_without_autopilot_profile_assigned', n.get_int_value()),
            "devices_without_cloud_identity": lambda n : setattr(self, 'devices_without_cloud_identity', n.get_int_value()),
            "intune_devices": lambda n : setattr(self, 'intune_devices', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tenant_attach_devices": lambda n : setattr(self, 'tenant_attach_devices', n.get_int_value()),
            "total_devices": lambda n : setattr(self, 'total_devices', n.get_int_value()),
            "unsupported_o_sversion_devices": lambda n : setattr(self, 'unsupported_o_sversion_devices', n.get_int_value()),
            "windows10_devices": lambda n : setattr(self, 'windows10_devices', n.get_int_value()),
            "windows10_devices_summary": lambda n : setattr(self, 'windows10_devices_summary', n.get_object_value(UserExperienceAnalyticsWindows10DevicesSummary)),
            "windows10_devices_without_tenant_attach": lambda n : setattr(self, 'windows10_devices_without_tenant_attach', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("autopilot_devices_summary", self.autopilot_devices_summary)
        writer.write_object_value("cloud_identity_devices_summary", self.cloud_identity_devices_summary)
        writer.write_object_value("cloud_management_devices_summary", self.cloud_management_devices_summary)
        writer.write_int_value("co_managed_devices", self.co_managed_devices)
        writer.write_int_value("devices_not_autopilot_registered", self.devices_not_autopilot_registered)
        writer.write_int_value("devices_without_autopilot_profile_assigned", self.devices_without_autopilot_profile_assigned)
        writer.write_int_value("devices_without_cloud_identity", self.devices_without_cloud_identity)
        writer.write_int_value("intune_devices", self.intune_devices)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("tenant_attach_devices", self.tenant_attach_devices)
        writer.write_int_value("total_devices", self.total_devices)
        writer.write_int_value("unsupported_o_sversion_devices", self.unsupported_o_sversion_devices)
        writer.write_int_value("windows10_devices", self.windows10_devices)
        writer.write_object_value("windows10_devices_summary", self.windows10_devices_summary)
        writer.write_int_value("windows10_devices_without_tenant_attach", self.windows10_devices_without_tenant_attach)
        writer.write_additional_data_value(self.additional_data)
    

