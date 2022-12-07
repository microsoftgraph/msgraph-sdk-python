from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

device_compliance_device_overview = lazy_import('msgraph.generated.models.device_compliance_device_overview')
device_compliance_device_status = lazy_import('msgraph.generated.models.device_compliance_device_status')
device_compliance_policy_assignment = lazy_import('msgraph.generated.models.device_compliance_policy_assignment')
device_compliance_scheduled_action_for_rule = lazy_import('msgraph.generated.models.device_compliance_scheduled_action_for_rule')
device_compliance_user_overview = lazy_import('msgraph.generated.models.device_compliance_user_overview')
device_compliance_user_status = lazy_import('msgraph.generated.models.device_compliance_user_status')
entity = lazy_import('msgraph.generated.models.entity')
setting_state_device_summary = lazy_import('msgraph.generated.models.setting_state_device_summary')

class DeviceCompliancePolicy(entity.Entity):
    """
    This is the base class for Compliance policy. Compliance policies are platform specific and individual per-platform compliance policies inherit from here. 
    """
    @property
    def assignments(self,) -> Optional[List[device_compliance_policy_assignment.DeviceCompliancePolicyAssignment]]:
        """
        Gets the assignments property value. The collection of assignments for this compliance policy.
        Returns: Optional[List[device_compliance_policy_assignment.DeviceCompliancePolicyAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_compliance_policy_assignment.DeviceCompliancePolicyAssignment]] = None) -> None:
        """
        Sets the assignments property value. The collection of assignments for this compliance policy.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceCompliancePolicy and sets the default values.
        """
        super().__init__()
        # The collection of assignments for this compliance policy.
        self._assignments: Optional[List[device_compliance_policy_assignment.DeviceCompliancePolicyAssignment]] = None
        # DateTime the object was created.
        self._created_date_time: Optional[datetime] = None
        # Admin provided description of the Device Configuration.
        self._description: Optional[str] = None
        # Compliance Setting State Device Summary
        self._device_setting_state_summaries: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None
        # List of DeviceComplianceDeviceStatus.
        self._device_statuses: Optional[List[device_compliance_device_status.DeviceComplianceDeviceStatus]] = None
        # Device compliance devices status overview
        self._device_status_overview: Optional[device_compliance_device_overview.DeviceComplianceDeviceOverview] = None
        # Admin provided name of the device configuration.
        self._display_name: Optional[str] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The list of scheduled action per rule for this compliance policy. This is a required property when creating any individual per-platform compliance policies.
        self._scheduled_actions_for_rule: Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]] = None
        # List of DeviceComplianceUserStatus.
        self._user_statuses: Optional[List[device_compliance_user_status.DeviceComplianceUserStatus]] = None
        # Device compliance users status overview
        self._user_status_overview: Optional[device_compliance_user_overview.DeviceComplianceUserOverview] = None
        # Version of the device configuration.
        self._version: Optional[int] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. DateTime the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. DateTime the object was created.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceCompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceCompliancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceCompliancePolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Admin provided description of the Device Configuration.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Admin provided description of the Device Configuration.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_setting_state_summaries(self,) -> Optional[List[setting_state_device_summary.SettingStateDeviceSummary]]:
        """
        Gets the deviceSettingStateSummaries property value. Compliance Setting State Device Summary
        Returns: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]]
        """
        return self._device_setting_state_summaries
    
    @device_setting_state_summaries.setter
    def device_setting_state_summaries(self,value: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None) -> None:
        """
        Sets the deviceSettingStateSummaries property value. Compliance Setting State Device Summary
        Args:
            value: Value to set for the deviceSettingStateSummaries property.
        """
        self._device_setting_state_summaries = value
    
    @property
    def device_statuses(self,) -> Optional[List[device_compliance_device_status.DeviceComplianceDeviceStatus]]:
        """
        Gets the deviceStatuses property value. List of DeviceComplianceDeviceStatus.
        Returns: Optional[List[device_compliance_device_status.DeviceComplianceDeviceStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[device_compliance_device_status.DeviceComplianceDeviceStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. List of DeviceComplianceDeviceStatus.
        Args:
            value: Value to set for the deviceStatuses property.
        """
        self._device_statuses = value
    
    @property
    def device_status_overview(self,) -> Optional[device_compliance_device_overview.DeviceComplianceDeviceOverview]:
        """
        Gets the deviceStatusOverview property value. Device compliance devices status overview
        Returns: Optional[device_compliance_device_overview.DeviceComplianceDeviceOverview]
        """
        return self._device_status_overview
    
    @device_status_overview.setter
    def device_status_overview(self,value: Optional[device_compliance_device_overview.DeviceComplianceDeviceOverview] = None) -> None:
        """
        Sets the deviceStatusOverview property value. Device compliance devices status overview
        Args:
            value: Value to set for the deviceStatusOverview property.
        """
        self._device_status_overview = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Admin provided name of the device configuration.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Admin provided name of the device configuration.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_compliance_policy_assignment.DeviceCompliancePolicyAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_setting_state_summaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(setting_state_device_summary.SettingStateDeviceSummary)),
            "device_statuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(device_compliance_device_status.DeviceComplianceDeviceStatus)),
            "device_status_overview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(device_compliance_device_overview.DeviceComplianceDeviceOverview)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "scheduled_actions_for_rule": lambda n : setattr(self, 'scheduled_actions_for_rule', n.get_collection_of_object_values(device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule)),
            "user_statuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(device_compliance_user_status.DeviceComplianceUserStatus)),
            "user_status_overview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(device_compliance_user_overview.DeviceComplianceUserOverview)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def scheduled_actions_for_rule(self,) -> Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]]:
        """
        Gets the scheduledActionsForRule property value. The list of scheduled action per rule for this compliance policy. This is a required property when creating any individual per-platform compliance policies.
        Returns: Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]]
        """
        return self._scheduled_actions_for_rule
    
    @scheduled_actions_for_rule.setter
    def scheduled_actions_for_rule(self,value: Optional[List[device_compliance_scheduled_action_for_rule.DeviceComplianceScheduledActionForRule]] = None) -> None:
        """
        Sets the scheduledActionsForRule property value. The list of scheduled action per rule for this compliance policy. This is a required property when creating any individual per-platform compliance policies.
        Args:
            value: Value to set for the scheduledActionsForRule property.
        """
        self._scheduled_actions_for_rule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceSettingStateSummaries", self.device_setting_state_summaries)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_object_value("deviceStatusOverview", self.device_status_overview)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("scheduledActionsForRule", self.scheduled_actions_for_rule)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_int_value("version", self.version)
    
    @property
    def user_statuses(self,) -> Optional[List[device_compliance_user_status.DeviceComplianceUserStatus]]:
        """
        Gets the userStatuses property value. List of DeviceComplianceUserStatus.
        Returns: Optional[List[device_compliance_user_status.DeviceComplianceUserStatus]]
        """
        return self._user_statuses
    
    @user_statuses.setter
    def user_statuses(self,value: Optional[List[device_compliance_user_status.DeviceComplianceUserStatus]] = None) -> None:
        """
        Sets the userStatuses property value. List of DeviceComplianceUserStatus.
        Args:
            value: Value to set for the userStatuses property.
        """
        self._user_statuses = value
    
    @property
    def user_status_overview(self,) -> Optional[device_compliance_user_overview.DeviceComplianceUserOverview]:
        """
        Gets the userStatusOverview property value. Device compliance users status overview
        Returns: Optional[device_compliance_user_overview.DeviceComplianceUserOverview]
        """
        return self._user_status_overview
    
    @user_status_overview.setter
    def user_status_overview(self,value: Optional[device_compliance_user_overview.DeviceComplianceUserOverview] = None) -> None:
        """
        Sets the userStatusOverview property value. Device compliance users status overview
        Args:
            value: Value to set for the userStatusOverview property.
        """
        self._user_status_overview = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Version of the device configuration.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Version of the device configuration.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

