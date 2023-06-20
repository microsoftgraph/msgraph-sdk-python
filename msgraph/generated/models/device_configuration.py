from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_custom_configuration, android_general_device_configuration, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, apple_device_features_configuration_base, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_user_overview, device_configuration_user_status, edition_upgrade_configuration, entity, ios_certificate_profile, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_update_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, setting_state_device_summary, shared_p_c_configuration, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_general_configuration, windows_defender_advanced_threat_protection_configuration, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_update_for_business_configuration

from . import entity

@dataclass
class DeviceConfiguration(entity.Entity):
    """
    Device Configuration.
    """
    # The list of assignments for the device configuration profile.
    assignments: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # Device Configuration Setting State Device Summary
    device_setting_state_summaries: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None
    # Device Configuration devices status overview
    device_status_overview: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview] = None
    # Device configuration installation status by device.
    device_statuses: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device Configuration users status overview
    user_status_overview: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview] = None
    # Device configuration installation status by user.
    user_statuses: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCustomConfiguration".casefold():
            from . import android_custom_configuration

            return android_custom_configuration.AndroidCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidGeneralDeviceConfiguration".casefold():
            from . import android_general_device_configuration

            return android_general_device_configuration.AndroidGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCustomConfiguration".casefold():
            from . import android_work_profile_custom_configuration

            return android_work_profile_custom_configuration.AndroidWorkProfileCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration".casefold():
            from . import android_work_profile_general_device_configuration

            return android_work_profile_general_device_configuration.AndroidWorkProfileGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleDeviceFeaturesConfigurationBase".casefold():
            from . import apple_device_features_configuration_base

            return apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.editionUpgradeConfiguration".casefold():
            from . import edition_upgrade_configuration

            return edition_upgrade_configuration.EditionUpgradeConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfile".casefold():
            from . import ios_certificate_profile

            return ios_certificate_profile.IosCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCustomConfiguration".casefold():
            from . import ios_custom_configuration

            return ios_custom_configuration.IosCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from . import ios_device_features_configuration

            return ios_device_features_configuration.IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosGeneralDeviceConfiguration".casefold():
            from . import ios_general_device_configuration

            return ios_general_device_configuration.IosGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateConfiguration".casefold():
            from . import ios_update_configuration

            return ios_update_configuration.IosUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomConfiguration".casefold():
            from . import mac_o_s_custom_configuration

            return mac_o_s_custom_configuration.MacOSCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from . import mac_o_s_device_features_configuration

            return mac_o_s_device_features_configuration.MacOSDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSGeneralDeviceConfiguration".casefold():
            from . import mac_o_s_general_device_configuration

            return mac_o_s_general_device_configuration.MacOSGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedPCConfiguration".casefold():
            from . import shared_p_c_configuration

            return shared_p_c_configuration.SharedPCConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CustomConfiguration".casefold():
            from . import windows10_custom_configuration

            return windows10_custom_configuration.Windows10CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EndpointProtectionConfiguration".casefold():
            from . import windows10_endpoint_protection_configuration

            return windows10_endpoint_protection_configuration.Windows10EndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration".casefold():
            from . import windows10_enterprise_modern_app_management_configuration

            return windows10_enterprise_modern_app_management_configuration.Windows10EnterpriseModernAppManagementConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10GeneralConfiguration".casefold():
            from . import windows10_general_configuration

            return windows10_general_configuration.Windows10GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10SecureAssessmentConfiguration".casefold():
            from . import windows10_secure_assessment_configuration

            return windows10_secure_assessment_configuration.Windows10SecureAssessmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10TeamGeneralConfiguration".casefold():
            from . import windows10_team_general_configuration

            return windows10_team_general_configuration.Windows10TeamGeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81GeneralConfiguration".casefold():
            from . import windows81_general_configuration

            return windows81_general_configuration.Windows81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration".casefold():
            from . import windows_defender_advanced_threat_protection_configuration

            return windows_defender_advanced_threat_protection_configuration.WindowsDefenderAdvancedThreatProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CustomConfiguration".casefold():
            from . import windows_phone81_custom_configuration

            return windows_phone81_custom_configuration.WindowsPhone81CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81GeneralConfiguration".casefold():
            from . import windows_phone81_general_configuration

            return windows_phone81_general_configuration.WindowsPhone81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateForBusinessConfiguration".casefold():
            from . import windows_update_for_business_configuration

            return windows_update_for_business_configuration.WindowsUpdateForBusinessConfiguration()
        return DeviceConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_custom_configuration, android_general_device_configuration, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, apple_device_features_configuration_base, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_user_overview, device_configuration_user_status, edition_upgrade_configuration, entity, ios_certificate_profile, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_update_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, setting_state_device_summary, shared_p_c_configuration, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_general_configuration, windows_defender_advanced_threat_protection_configuration, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_update_for_business_configuration

        from . import android_custom_configuration, android_general_device_configuration, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, apple_device_features_configuration_base, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_user_overview, device_configuration_user_status, edition_upgrade_configuration, entity, ios_certificate_profile, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_update_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, setting_state_device_summary, shared_p_c_configuration, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_general_configuration, windows_defender_advanced_threat_protection_configuration, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_update_for_business_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_configuration_assignment.DeviceConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(setting_state_device_summary.SettingStateDeviceSummary)),
            "deviceStatusOverview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(device_configuration_device_overview.DeviceConfigurationDeviceOverview)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(device_configuration_device_status.DeviceConfigurationDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "userStatusOverview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(device_configuration_user_overview.DeviceConfigurationUserOverview)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(device_configuration_user_status.DeviceConfigurationUserStatus)),
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
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_int_value("version", self.version)
    

