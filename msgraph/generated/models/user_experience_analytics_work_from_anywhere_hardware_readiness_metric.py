from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric(Entity):
    """
    The user experience analytics hardware readiness entity contains account level information about hardware blockers for windows upgrade.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # The percentage of devices for which OS check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    os_check_failed_percentage: Optional[float] = None
    # The percentage of devices for which processor hardware core count check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    processor_core_count_check_failed_percentage: Optional[float] = None
    # The percentage of devices for which processor hardware family check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    processor_family_check_failed_percentage: Optional[float] = None
    # The percentage of devices for which processor hardware speed check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    processor_speed_check_failed_percentage: Optional[float] = None
    # The percentage of devices for which processor hardware 64-bit architecture check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    processor64_bit_check_failed_percentage: Optional[float] = None
    # The percentage of devices for which RAM hardware check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    ram_check_failed_percentage: Optional[float] = None
    # The percentage of devices for which secure boot hardware check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    secure_boot_check_failed_percentage: Optional[float] = None
    # The percentage of devices for which storage hardware check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    storage_check_failed_percentage: Optional[float] = None
    # The count of total devices in an organization. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    total_device_count: Optional[int] = None
    # The percentage of devices for which Trusted Platform Module (TPM) hardware check has failed. Valid values 0 to 100. Supports: $select, $OrderBy. Read-only. Valid values -1.79769313486232E+308 to 1.79769313486232E+308
    tpm_check_failed_percentage: Optional[float] = None
    # The count of devices in an organization eligible for windows upgrade. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    upgrade_eligible_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "osCheckFailedPercentage": lambda n : setattr(self, 'os_check_failed_percentage', n.get_float_value()),
            "processorCoreCountCheckFailedPercentage": lambda n : setattr(self, 'processor_core_count_check_failed_percentage', n.get_float_value()),
            "processorFamilyCheckFailedPercentage": lambda n : setattr(self, 'processor_family_check_failed_percentage', n.get_float_value()),
            "processorSpeedCheckFailedPercentage": lambda n : setattr(self, 'processor_speed_check_failed_percentage', n.get_float_value()),
            "processor64BitCheckFailedPercentage": lambda n : setattr(self, 'processor64_bit_check_failed_percentage', n.get_float_value()),
            "ramCheckFailedPercentage": lambda n : setattr(self, 'ram_check_failed_percentage', n.get_float_value()),
            "secureBootCheckFailedPercentage": lambda n : setattr(self, 'secure_boot_check_failed_percentage', n.get_float_value()),
            "storageCheckFailedPercentage": lambda n : setattr(self, 'storage_check_failed_percentage', n.get_float_value()),
            "totalDeviceCount": lambda n : setattr(self, 'total_device_count', n.get_int_value()),
            "tpmCheckFailedPercentage": lambda n : setattr(self, 'tpm_check_failed_percentage', n.get_float_value()),
            "upgradeEligibleDeviceCount": lambda n : setattr(self, 'upgrade_eligible_device_count', n.get_int_value()),
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
        writer.write_float_value("osCheckFailedPercentage", self.os_check_failed_percentage)
        writer.write_float_value("processorCoreCountCheckFailedPercentage", self.processor_core_count_check_failed_percentage)
        writer.write_float_value("processorFamilyCheckFailedPercentage", self.processor_family_check_failed_percentage)
        writer.write_float_value("processorSpeedCheckFailedPercentage", self.processor_speed_check_failed_percentage)
        writer.write_float_value("processor64BitCheckFailedPercentage", self.processor64_bit_check_failed_percentage)
        writer.write_float_value("ramCheckFailedPercentage", self.ram_check_failed_percentage)
        writer.write_float_value("secureBootCheckFailedPercentage", self.secure_boot_check_failed_percentage)
        writer.write_float_value("storageCheckFailedPercentage", self.storage_check_failed_percentage)
        writer.write_int_value("totalDeviceCount", self.total_device_count)
        writer.write_float_value("tpmCheckFailedPercentage", self.tpm_check_failed_percentage)
        writer.write_int_value("upgradeEligibleDeviceCount", self.upgrade_eligible_device_count)
    

