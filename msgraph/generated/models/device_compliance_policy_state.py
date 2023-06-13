from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_status, device_compliance_policy_setting_state, entity, policy_platform_type

from . import entity

@dataclass
class DeviceCompliancePolicyState(entity.Entity):
    """
    Device Compliance Policy State for a given device.
    """
    # The name of the policy for this policyBase
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Supported platform types for policies.
    platform_type: Optional[policy_platform_type.PolicyPlatformType] = None
    # Count of how many setting a policy holds
    setting_count: Optional[int] = None
    # The settingStates property
    setting_states: Optional[List[device_compliance_policy_setting_state.DeviceCompliancePolicySettingState]] = None
    # The state property
    state: Optional[compliance_status.ComplianceStatus] = None
    # The version of the policy
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicyState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicyState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicyState()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_status, device_compliance_policy_setting_state, entity, policy_platform_type

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "platformType": lambda n : setattr(self, 'platform_type', n.get_enum_value(policy_platform_type.PolicyPlatformType)),
            "settingCount": lambda n : setattr(self, 'setting_count', n.get_int_value()),
            "settingStates": lambda n : setattr(self, 'setting_states', n.get_collection_of_object_values(device_compliance_policy_setting_state.DeviceCompliancePolicySettingState)),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(compliance_status.ComplianceStatus)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("platformType", self.platform_type)
        writer.write_int_value("settingCount", self.setting_count)
        writer.write_collection_of_object_values("settingStates", self.setting_states)
        writer.write_enum_value("state", self.state)
        writer.write_int_value("version", self.version)
    

