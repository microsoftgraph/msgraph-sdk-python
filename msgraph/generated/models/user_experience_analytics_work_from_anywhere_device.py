from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .operating_system_upgrade_eligibility import OperatingSystemUpgradeEligibility
    from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

from .entity import Entity

@dataclass
class UserExperienceAnalyticsWorkFromAnywhereDevice(Entity):
    """
    The user experience analytics device for work from anywhere report.
    """
    # When TRUE, indicates the intune device's autopilot profile is assigned. When FALSE, indicates it's not Assigned. Supports: $select, $OrderBy. Read-only.
    auto_pilot_profile_assigned: Optional[bool] = None
    # When TRUE, indicates the intune device's autopilot is registered. When FALSE, indicates it's not registered. Supports: $select, $OrderBy. Read-only.
    auto_pilot_registered: Optional[bool] = None
    # The Azure Active Directory (Azure AD) device Id. Supports: $select, $OrderBy. Read-only.
    azure_ad_device_id: Optional[str] = None
    # The work from anywhere device's Azure Active Directory (Azure AD) join type. Supports: $select, $OrderBy. Read-only.
    azure_ad_join_type: Optional[str] = None
    # When TRUE, indicates the device's Azure Active Directory (Azure AD) is registered. When False, indicates it's not registered. Supports: $select, $OrderBy. Read-only.
    azure_ad_registered: Optional[bool] = None
    # Indicates per device cloud identity score. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_identity_score: Optional[float] = None
    # Indicates per device cloud management score. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_management_score: Optional[float] = None
    # Indicates per device cloud provisioning score. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    cloud_provisioning_score: Optional[float] = None
    # When TRUE, indicates the device's compliance policy is set to intune. When FALSE, indicates it's not set to intune. Supports: $select, $OrderBy. Read-only.
    compliance_policy_set_to_intune: Optional[bool] = None
    # The Intune device id of the device. Supports: $select, $OrderBy. Read-only.
    device_id: Optional[str] = None
    # The name of the device. Supports: $select, $OrderBy. Read-only.
    device_name: Optional[str] = None
    # The healthStatus property
    health_status: Optional[UserExperienceAnalyticsHealthState] = None
    # When TRUE, indicates the device's Cloud Management Gateway for Configuration Manager is enabled. When FALSE, indicates it's not enabled. Supports: $select, $OrderBy. Read-only.
    is_cloud_managed_gateway_enabled: Optional[bool] = None
    # The management agent of the device. Supports: $select, $OrderBy. Read-only.
    managed_by: Optional[str] = None
    # The manufacturer name of the device. Supports: $select, $OrderBy. Read-only.
    manufacturer: Optional[str] = None
    # The model name of the device. Supports: $select, $OrderBy. Read-only.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When TRUE, indicates OS check failed for device to upgrade to the latest version of windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    os_check_failed: Optional[bool] = None
    # The OS description of the device. Supports: $select, $OrderBy. Read-only.
    os_description: Optional[str] = None
    # The OS version of the device. Supports: $select, $OrderBy. Read-only.
    os_version: Optional[str] = None
    # When TRUE, indicates the device's other workloads is set to intune. When FALSE, indicates it's not set to intune. Supports: $select, $OrderBy. Read-only.
    other_workloads_set_to_intune: Optional[bool] = None
    # Ownership of the device. Supports: $select, $OrderBy. Read-only.
    ownership: Optional[str] = None
    # When TRUE, indicates processor hardware core count check failed for device to upgrade to the latest version of windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    processor_core_count_check_failed: Optional[bool] = None
    # When TRUE, indicates processor hardware family check failed for device to upgrade to the latest version of windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    processor_family_check_failed: Optional[bool] = None
    # When TRUE, indicates processor hardware speed check failed for device to upgrade to the latest version of windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    processor_speed_check_failed: Optional[bool] = None
    # When TRUE, indicates processor hardware 64-bit architecture check failed for device to upgrade to the latest version of windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    processor64_bit_check_failed: Optional[bool] = None
    # When TRUE, indicates RAM hardware check failed for device to upgrade to the latest version of windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    ram_check_failed: Optional[bool] = None
    # When TRUE, indicates secure boot hardware check failed for device to upgrade to the latest version of windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    secure_boot_check_failed: Optional[bool] = None
    # The serial number of the device. Supports: $select, $OrderBy. Read-only.
    serial_number: Optional[str] = None
    # When TRUE, indicates storage hardware check failed for device to upgrade to the latest version of windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    storage_check_failed: Optional[bool] = None
    # When TRUE, indicates the device is Tenant Attached. When FALSE, indicates it's not Tenant Attached. Supports: $select, $OrderBy. Read-only.
    tenant_attached: Optional[bool] = None
    # When TRUE, indicates Trusted Platform Module (TPM) hardware check failed for device to the latest version of upgrade to windows. When FALSE, indicates the check succeeded. Supports: $select, $OrderBy. Read-only.
    tpm_check_failed: Optional[bool] = None
    # Work From Anywhere windows device upgrade eligibility status.
    upgrade_eligibility: Optional[OperatingSystemUpgradeEligibility] = None
    # Indicates per device windows score. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    windows_score: Optional[float] = None
    # Indicates work from anywhere per device overall score. Valid values 0 to 100. Value -1 means associated score is unavailable. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    work_from_anywhere_score: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsWorkFromAnywhereDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereDevice
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsWorkFromAnywhereDevice()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .operating_system_upgrade_eligibility import OperatingSystemUpgradeEligibility
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        from .entity import Entity
        from .operating_system_upgrade_eligibility import OperatingSystemUpgradeEligibility
        from .user_experience_analytics_health_state import UserExperienceAnalyticsHealthState

        fields: Dict[str, Callable[[Any], None]] = {
            "autoPilotProfileAssigned": lambda n : setattr(self, 'auto_pilot_profile_assigned', n.get_bool_value()),
            "autoPilotRegistered": lambda n : setattr(self, 'auto_pilot_registered', n.get_bool_value()),
            "azureAdDeviceId": lambda n : setattr(self, 'azure_ad_device_id', n.get_str_value()),
            "azureAdJoinType": lambda n : setattr(self, 'azure_ad_join_type', n.get_str_value()),
            "azureAdRegistered": lambda n : setattr(self, 'azure_ad_registered', n.get_bool_value()),
            "cloudIdentityScore": lambda n : setattr(self, 'cloud_identity_score', n.get_float_value()),
            "cloudManagementScore": lambda n : setattr(self, 'cloud_management_score', n.get_float_value()),
            "cloudProvisioningScore": lambda n : setattr(self, 'cloud_provisioning_score', n.get_float_value()),
            "compliancePolicySetToIntune": lambda n : setattr(self, 'compliance_policy_set_to_intune', n.get_bool_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(UserExperienceAnalyticsHealthState)),
            "isCloudManagedGatewayEnabled": lambda n : setattr(self, 'is_cloud_managed_gateway_enabled', n.get_bool_value()),
            "managedBy": lambda n : setattr(self, 'managed_by', n.get_str_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "osCheckFailed": lambda n : setattr(self, 'os_check_failed', n.get_bool_value()),
            "osDescription": lambda n : setattr(self, 'os_description', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "otherWorkloadsSetToIntune": lambda n : setattr(self, 'other_workloads_set_to_intune', n.get_bool_value()),
            "ownership": lambda n : setattr(self, 'ownership', n.get_str_value()),
            "processorCoreCountCheckFailed": lambda n : setattr(self, 'processor_core_count_check_failed', n.get_bool_value()),
            "processorFamilyCheckFailed": lambda n : setattr(self, 'processor_family_check_failed', n.get_bool_value()),
            "processorSpeedCheckFailed": lambda n : setattr(self, 'processor_speed_check_failed', n.get_bool_value()),
            "processor64BitCheckFailed": lambda n : setattr(self, 'processor64_bit_check_failed', n.get_bool_value()),
            "ramCheckFailed": lambda n : setattr(self, 'ram_check_failed', n.get_bool_value()),
            "secureBootCheckFailed": lambda n : setattr(self, 'secure_boot_check_failed', n.get_bool_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "storageCheckFailed": lambda n : setattr(self, 'storage_check_failed', n.get_bool_value()),
            "tenantAttached": lambda n : setattr(self, 'tenant_attached', n.get_bool_value()),
            "tpmCheckFailed": lambda n : setattr(self, 'tpm_check_failed', n.get_bool_value()),
            "upgradeEligibility": lambda n : setattr(self, 'upgrade_eligibility', n.get_enum_value(OperatingSystemUpgradeEligibility)),
            "windowsScore": lambda n : setattr(self, 'windows_score', n.get_float_value()),
            "workFromAnywhereScore": lambda n : setattr(self, 'work_from_anywhere_score', n.get_float_value()),
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
        writer.write_bool_value("autoPilotProfileAssigned", self.auto_pilot_profile_assigned)
        writer.write_bool_value("autoPilotRegistered", self.auto_pilot_registered)
        writer.write_str_value("azureAdDeviceId", self.azure_ad_device_id)
        writer.write_str_value("azureAdJoinType", self.azure_ad_join_type)
        writer.write_bool_value("azureAdRegistered", self.azure_ad_registered)
        writer.write_float_value("cloudIdentityScore", self.cloud_identity_score)
        writer.write_float_value("cloudManagementScore", self.cloud_management_score)
        writer.write_float_value("cloudProvisioningScore", self.cloud_provisioning_score)
        writer.write_bool_value("compliancePolicySetToIntune", self.compliance_policy_set_to_intune)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("deviceName", self.device_name)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_bool_value("isCloudManagedGatewayEnabled", self.is_cloud_managed_gateway_enabled)
        writer.write_str_value("managedBy", self.managed_by)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_bool_value("osCheckFailed", self.os_check_failed)
        writer.write_str_value("osDescription", self.os_description)
        writer.write_str_value("osVersion", self.os_version)
        writer.write_bool_value("otherWorkloadsSetToIntune", self.other_workloads_set_to_intune)
        writer.write_str_value("ownership", self.ownership)
        writer.write_bool_value("processorCoreCountCheckFailed", self.processor_core_count_check_failed)
        writer.write_bool_value("processorFamilyCheckFailed", self.processor_family_check_failed)
        writer.write_bool_value("processorSpeedCheckFailed", self.processor_speed_check_failed)
        writer.write_bool_value("processor64BitCheckFailed", self.processor64_bit_check_failed)
        writer.write_bool_value("ramCheckFailed", self.ram_check_failed)
        writer.write_bool_value("secureBootCheckFailed", self.secure_boot_check_failed)
        writer.write_str_value("serialNumber", self.serial_number)
        writer.write_bool_value("storageCheckFailed", self.storage_check_failed)
        writer.write_bool_value("tenantAttached", self.tenant_attached)
        writer.write_bool_value("tpmCheckFailed", self.tpm_check_failed)
        writer.write_enum_value("upgradeEligibility", self.upgrade_eligibility)
        writer.write_float_value("windowsScore", self.windows_score)
        writer.write_float_value("workFromAnywhereScore", self.work_from_anywhere_score)
    

