from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_compliance_policy import AndroidCompliancePolicy
    from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
    from .device_compliance_device_overview import DeviceComplianceDeviceOverview
    from .device_compliance_device_status import DeviceComplianceDeviceStatus
    from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
    from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
    from .device_compliance_user_overview import DeviceComplianceUserOverview
    from .device_compliance_user_status import DeviceComplianceUserStatus
    from .entity import Entity
    from .ios_compliance_policy import IosCompliancePolicy
    from .mac_o_s_compliance_policy import MacOSCompliancePolicy
    from .setting_state_device_summary import SettingStateDeviceSummary
    from .windows10_compliance_policy import Windows10CompliancePolicy
    from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
    from .windows81_compliance_policy import Windows81CompliancePolicy
    from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy

from .entity import Entity

@dataclass
class DeviceCompliancePolicy(Entity, Parsable):
    """
    This is the base class for Compliance policy. Compliance policies are platform specific and individual per-platform compliance policies inherit from here. 
    """
    # The collection of assignments for this compliance policy.
    assignments: Optional[list[DeviceCompliancePolicyAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # Compliance Setting State Device Summary
    device_setting_state_summaries: Optional[list[SettingStateDeviceSummary]] = None
    # Device compliance devices status overview
    device_status_overview: Optional[DeviceComplianceDeviceOverview] = None
    # List of DeviceComplianceDeviceStatus.
    device_statuses: Optional[list[DeviceComplianceDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of scheduled action per rule for this compliance policy. This is a required property when creating any individual per-platform compliance policies.
    scheduled_actions_for_rule: Optional[list[DeviceComplianceScheduledActionForRule]] = None
    # Device compliance users status overview
    user_status_overview: Optional[DeviceComplianceUserOverview] = None
    # List of DeviceComplianceUserStatus.
    user_statuses: Optional[list[DeviceComplianceUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCompliancePolicy".casefold():
            from .android_compliance_policy import AndroidCompliancePolicy

            return AndroidCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCompliancePolicy".casefold():
            from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy

            return AndroidWorkProfileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCompliancePolicy".casefold():
            from .ios_compliance_policy import IosCompliancePolicy

            return IosCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCompliancePolicy".casefold():
            from .mac_o_s_compliance_policy import MacOSCompliancePolicy

            return MacOSCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CompliancePolicy".casefold():
            from .windows10_compliance_policy import Windows10CompliancePolicy

            return Windows10CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10MobileCompliancePolicy".casefold():
            from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy

            return Windows10MobileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CompliancePolicy".casefold():
            from .windows81_compliance_policy import Windows81CompliancePolicy

            return Windows81CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CompliancePolicy".casefold():
            from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy

            return WindowsPhone81CompliancePolicy()
        return DeviceCompliancePolicy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_compliance_policy import AndroidCompliancePolicy
        from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
        from .device_compliance_device_overview import DeviceComplianceDeviceOverview
        from .device_compliance_device_status import DeviceComplianceDeviceStatus
        from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
        from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
        from .device_compliance_user_overview import DeviceComplianceUserOverview
        from .device_compliance_user_status import DeviceComplianceUserStatus
        from .entity import Entity
        from .ios_compliance_policy import IosCompliancePolicy
        from .mac_o_s_compliance_policy import MacOSCompliancePolicy
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .windows10_compliance_policy import Windows10CompliancePolicy
        from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
        from .windows81_compliance_policy import Windows81CompliancePolicy
        from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy

        from .android_compliance_policy import AndroidCompliancePolicy
        from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
        from .device_compliance_device_overview import DeviceComplianceDeviceOverview
        from .device_compliance_device_status import DeviceComplianceDeviceStatus
        from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
        from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
        from .device_compliance_user_overview import DeviceComplianceUserOverview
        from .device_compliance_user_status import DeviceComplianceUserStatus
        from .entity import Entity
        from .ios_compliance_policy import IosCompliancePolicy
        from .mac_o_s_compliance_policy import MacOSCompliancePolicy
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .windows10_compliance_policy import Windows10CompliancePolicy
        from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
        from .windows81_compliance_policy import Windows81CompliancePolicy
        from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(DeviceCompliancePolicyAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(SettingStateDeviceSummary)),
            "deviceStatusOverview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(DeviceComplianceDeviceOverview)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(DeviceComplianceDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "scheduledActionsForRule": lambda n : setattr(self, 'scheduled_actions_for_rule', n.get_collection_of_object_values(DeviceComplianceScheduledActionForRule)),
            "userStatusOverview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(DeviceComplianceUserOverview)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(DeviceComplianceUserStatus)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
    

