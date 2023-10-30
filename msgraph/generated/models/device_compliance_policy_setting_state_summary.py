from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_compliance_setting_state import DeviceComplianceSettingState
    from .entity import Entity
    from .policy_platform_type import PolicyPlatformType

from .entity import Entity

@dataclass
class DeviceCompliancePolicySettingStateSummary(Entity):
    """
    Device Compilance Policy Setting State summary across the account.
    """
    # Number of compliant devices
    compliant_device_count: Optional[int] = None
    # Number of conflict devices
    conflict_device_count: Optional[int] = None
    # Not yet documented
    device_compliance_setting_states: Optional[List[DeviceComplianceSettingState]] = None
    # Number of error devices
    error_device_count: Optional[int] = None
    # Number of NonCompliant devices
    non_compliant_device_count: Optional[int] = None
    # Number of not applicable devices
    not_applicable_device_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform_type: Optional[PolicyPlatformType] = None
    # Number of remediated devices
    remediated_device_count: Optional[int] = None
    # The setting class name and property name.
    setting: Optional[str] = None
    # Name of the setting.
    setting_name: Optional[str] = None
    # Number of unknown devices
    unknown_device_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicySettingStateSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicySettingStateSummary
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceCompliancePolicySettingStateSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_compliance_setting_state import DeviceComplianceSettingState
        from .entity import Entity
        from .policy_platform_type import PolicyPlatformType

        from .device_compliance_setting_state import DeviceComplianceSettingState
        from .entity import Entity
        from .policy_platform_type import PolicyPlatformType

        fields: Dict[str, Callable[[Any], None]] = {
            "compliant_device_count": lambda n : setattr(self, 'compliant_device_count', n.get_int_value()),
            "conflict_device_count": lambda n : setattr(self, 'conflict_device_count', n.get_int_value()),
            "device_compliance_setting_states": lambda n : setattr(self, 'device_compliance_setting_states', n.get_collection_of_object_values(DeviceComplianceSettingState)),
            "error_device_count": lambda n : setattr(self, 'error_device_count', n.get_int_value()),
            "non_compliant_device_count": lambda n : setattr(self, 'non_compliant_device_count', n.get_int_value()),
            "not_applicable_device_count": lambda n : setattr(self, 'not_applicable_device_count', n.get_int_value()),
            "platform_type": lambda n : setattr(self, 'platform_type', n.get_enum_value(PolicyPlatformType)),
            "remediated_device_count": lambda n : setattr(self, 'remediated_device_count', n.get_int_value()),
            "setting": lambda n : setattr(self, 'setting', n.get_str_value()),
            "setting_name": lambda n : setattr(self, 'setting_name', n.get_str_value()),
            "unknown_device_count": lambda n : setattr(self, 'unknown_device_count', n.get_int_value()),
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
        writer.write_int_value("compliant_device_count", self.compliant_device_count)
        writer.write_int_value("conflict_device_count", self.conflict_device_count)
        writer.write_collection_of_object_values("device_compliance_setting_states", self.device_compliance_setting_states)
        writer.write_int_value("error_device_count", self.error_device_count)
        writer.write_int_value("non_compliant_device_count", self.non_compliant_device_count)
        writer.write_int_value("not_applicable_device_count", self.not_applicable_device_count)
        writer.write_enum_value("platform_type", self.platform_type)
        writer.write_int_value("remediated_device_count", self.remediated_device_count)
        writer.write_str_value("setting", self.setting)
        writer.write_str_value("setting_name", self.setting_name)
        writer.write_int_value("unknown_device_count", self.unknown_device_count)
    

