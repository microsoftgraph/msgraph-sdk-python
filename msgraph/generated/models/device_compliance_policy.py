from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_compliance_policy, android_work_profile_compliance_policy, device_compliance_device_overview, device_compliance_device_status, device_compliance_policy_assignment, device_compliance_scheduled_action_for_rule, device_compliance_user_overview, device_compliance_user_status, entity, ios_compliance_policy, mac_o_s_compliance_policy, setting_state_device_summary, windows10_compliance_policy, windows10_mobile_compliance_policy, windows81_compliance_policy, windows_phone81_compliance_policy

from . import entity

@dataclass
class DeviceCompliancePolicy(entity.Entity):
    """
    This is the base class for Compliance policy. Compliance policies are platform specific and individual per-platform compliance policies inherit from here. 
    """
    # The collection of assignments for this compliance policy.
    assignments: Optional[List[device_compliance_policy_assignment.DeviceCompliancePolicyAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # Compliance Setting State Device Summary
    device_setting_state_summaries: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None
    # Device compliance devices status overview
    device_status_overview: Optional[device_compliance_device_overview.DeviceComplianceDeviceOverview] = None
    # List of DeviceComplianceDeviceStatus.
    device_statuses: Optional[List[device_compliance_device_status.DeviceComplianceDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of scheduled action per rule for this compliance policy. This is a required property when creating any individual per-platform compliance policies.
    scheduled_actions_for_rule: Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]] = None
    # Device compliance users status overview
    user_status_overview: Optional[device_compliance_user_overview.DeviceComplianceUserOverview] = None
    # List of DeviceComplianceUserStatus.
    user_statuses: Optional[List[device_compliance_user_status.DeviceComplianceUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicy
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCompliancePolicy".casefold():
            from . import android_compliance_policy

            return android_compliance_policy.AndroidCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCompliancePolicy".casefold():
            from . import android_work_profile_compliance_policy

            return android_work_profile_compliance_policy.AndroidWorkProfileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCompliancePolicy".casefold():
            from . import ios_compliance_policy

            return ios_compliance_policy.IosCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCompliancePolicy".casefold():
            from . import mac_o_s_compliance_policy

            return mac_o_s_compliance_policy.MacOSCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CompliancePolicy".casefold():
            from . import windows10_compliance_policy

            return windows10_compliance_policy.Windows10CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10MobileCompliancePolicy".casefold():
            from . import windows10_mobile_compliance_policy

            return windows10_mobile_compliance_policy.Windows10MobileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CompliancePolicy".casefold():
            from . import windows81_compliance_policy

            return windows81_compliance_policy.Windows81CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CompliancePolicy".casefold():
            from . import windows_phone81_compliance_policy

            return windows_phone81_compliance_policy.WindowsPhone81CompliancePolicy()
        return DeviceCompliancePolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_compliance_policy, android_work_profile_compliance_policy, device_compliance_device_overview, device_compliance_device_status, device_compliance_policy_assignment, device_compliance_scheduled_action_for_rule, device_compliance_user_overview, device_compliance_user_status, entity, ios_compliance_policy, mac_o_s_compliance_policy, setting_state_device_summary, windows10_compliance_policy, windows10_mobile_compliance_policy, windows81_compliance_policy, windows_phone81_compliance_policy

        from . import android_compliance_policy, android_work_profile_compliance_policy, device_compliance_device_overview, device_compliance_device_status, device_compliance_policy_assignment, device_compliance_scheduled_action_for_rule, device_compliance_user_overview, device_compliance_user_status, entity, ios_compliance_policy, mac_o_s_compliance_policy, setting_state_device_summary, windows10_compliance_policy, windows10_mobile_compliance_policy, windows81_compliance_policy, windows_phone81_compliance_policy

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_compliance_policy_assignment.DeviceCompliancePolicyAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(setting_state_device_summary.SettingStateDeviceSummary)),
            "deviceStatusOverview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(device_compliance_device_overview.DeviceComplianceDeviceOverview)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(device_compliance_device_status.DeviceComplianceDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "scheduledActionsForRule": lambda n : setattr(self, 'scheduled_actions_for_rule', n.get_collection_of_object_values(device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule)),
            "userStatusOverview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(device_compliance_user_overview.DeviceComplianceUserOverview)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(device_compliance_user_status.DeviceComplianceUserStatus)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceSettingStateSummaries", self.device_setting_state_summaries)
        writer.write_object_value("deviceStatusOverview", self.device_status_overview)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("scheduledActionsForRule", self.scheduled_actions_for_rule)
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_int_value("version", self.version)
    

