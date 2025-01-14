from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .android_custom_configuration import AndroidCustomConfiguration
    from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
    from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
    from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
    from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
    from .device_configuration_assignment import DeviceConfigurationAssignment
    from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
    from .device_configuration_device_status import DeviceConfigurationDeviceStatus
    from .device_configuration_user_overview import DeviceConfigurationUserOverview
    from .device_configuration_user_status import DeviceConfigurationUserStatus
    from .edition_upgrade_configuration import EditionUpgradeConfiguration
    from .entity import Entity
    from .ios_certificate_profile import IosCertificateProfile
    from .ios_custom_configuration import IosCustomConfiguration
    from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
    from .ios_general_device_configuration import IosGeneralDeviceConfiguration
    from .ios_update_configuration import IosUpdateConfiguration
    from .mac_o_s_custom_configuration import MacOSCustomConfiguration
    from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
    from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
    from .setting_state_device_summary import SettingStateDeviceSummary
    from .shared_p_c_configuration import SharedPCConfiguration
    from .windows10_custom_configuration import Windows10CustomConfiguration
    from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
    from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
    from .windows10_general_configuration import Windows10GeneralConfiguration
    from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
    from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
    from .windows81_general_configuration import Windows81GeneralConfiguration
    from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
    from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
    from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
    from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

from .entity import Entity

@dataclass
class DeviceConfiguration(Entity, Parsable):
    """
    Device Configuration.
    """
    # The list of assignments for the device configuration profile.
    assignments: Optional[list[DeviceConfigurationAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # Device Configuration Setting State Device Summary
    device_setting_state_summaries: Optional[list[SettingStateDeviceSummary]] = None
    # Device Configuration devices status overview
    device_status_overview: Optional[DeviceConfigurationDeviceOverview] = None
    # Device configuration installation status by device.
    device_statuses: Optional[list[DeviceConfigurationDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device Configuration users status overview
    user_status_overview: Optional[DeviceConfigurationUserOverview] = None
    # Device configuration installation status by user.
    user_statuses: Optional[list[DeviceConfigurationUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCustomConfiguration".casefold():
            from .android_custom_configuration import AndroidCustomConfiguration

            return AndroidCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidGeneralDeviceConfiguration".casefold():
            from .android_general_device_configuration import AndroidGeneralDeviceConfiguration

            return AndroidGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCustomConfiguration".casefold():
            from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration

            return AndroidWorkProfileCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration".casefold():
            from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration

            return AndroidWorkProfileGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleDeviceFeaturesConfigurationBase".casefold():
            from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase

            return AppleDeviceFeaturesConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.editionUpgradeConfiguration".casefold():
            from .edition_upgrade_configuration import EditionUpgradeConfiguration

            return EditionUpgradeConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfile".casefold():
            from .ios_certificate_profile import IosCertificateProfile

            return IosCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCustomConfiguration".casefold():
            from .ios_custom_configuration import IosCustomConfiguration

            return IosCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from .ios_device_features_configuration import IosDeviceFeaturesConfiguration

            return IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosGeneralDeviceConfiguration".casefold():
            from .ios_general_device_configuration import IosGeneralDeviceConfiguration

            return IosGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateConfiguration".casefold():
            from .ios_update_configuration import IosUpdateConfiguration

            return IosUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomConfiguration".casefold():
            from .mac_o_s_custom_configuration import MacOSCustomConfiguration

            return MacOSCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

            return MacOSDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSGeneralDeviceConfiguration".casefold():
            from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration

            return MacOSGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedPCConfiguration".casefold():
            from .shared_p_c_configuration import SharedPCConfiguration

            return SharedPCConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CustomConfiguration".casefold():
            from .windows10_custom_configuration import Windows10CustomConfiguration

            return Windows10CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EndpointProtectionConfiguration".casefold():
            from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration

            return Windows10EndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration".casefold():
            from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration

            return Windows10EnterpriseModernAppManagementConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10GeneralConfiguration".casefold():
            from .windows10_general_configuration import Windows10GeneralConfiguration

            return Windows10GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10SecureAssessmentConfiguration".casefold():
            from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration

            return Windows10SecureAssessmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10TeamGeneralConfiguration".casefold():
            from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration

            return Windows10TeamGeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81GeneralConfiguration".casefold():
            from .windows81_general_configuration import Windows81GeneralConfiguration

            return Windows81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration".casefold():
            from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration

            return WindowsDefenderAdvancedThreatProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CustomConfiguration".casefold():
            from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration

            return WindowsPhone81CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81GeneralConfiguration".casefold():
            from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration

            return WindowsPhone81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateForBusinessConfiguration".casefold():
            from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

            return WindowsUpdateForBusinessConfiguration()
        return DeviceConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .android_custom_configuration import AndroidCustomConfiguration
        from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
        from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
        from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .device_configuration_assignment import DeviceConfigurationAssignment
        from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
        from .device_configuration_device_status import DeviceConfigurationDeviceStatus
        from .device_configuration_user_overview import DeviceConfigurationUserOverview
        from .device_configuration_user_status import DeviceConfigurationUserStatus
        from .edition_upgrade_configuration import EditionUpgradeConfiguration
        from .entity import Entity
        from .ios_certificate_profile import IosCertificateProfile
        from .ios_custom_configuration import IosCustomConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .ios_general_device_configuration import IosGeneralDeviceConfiguration
        from .ios_update_configuration import IosUpdateConfiguration
        from .mac_o_s_custom_configuration import MacOSCustomConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
        from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .shared_p_c_configuration import SharedPCConfiguration
        from .windows10_custom_configuration import Windows10CustomConfiguration
        from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
        from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
        from .windows10_general_configuration import Windows10GeneralConfiguration
        from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
        from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
        from .windows81_general_configuration import Windows81GeneralConfiguration
        from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
        from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
        from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
        from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

        from .android_custom_configuration import AndroidCustomConfiguration
        from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
        from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
        from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .device_configuration_assignment import DeviceConfigurationAssignment
        from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
        from .device_configuration_device_status import DeviceConfigurationDeviceStatus
        from .device_configuration_user_overview import DeviceConfigurationUserOverview
        from .device_configuration_user_status import DeviceConfigurationUserStatus
        from .edition_upgrade_configuration import EditionUpgradeConfiguration
        from .entity import Entity
        from .ios_certificate_profile import IosCertificateProfile
        from .ios_custom_configuration import IosCustomConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .ios_general_device_configuration import IosGeneralDeviceConfiguration
        from .ios_update_configuration import IosUpdateConfiguration
        from .mac_o_s_custom_configuration import MacOSCustomConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
        from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .shared_p_c_configuration import SharedPCConfiguration
        from .windows10_custom_configuration import Windows10CustomConfiguration
        from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
        from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
        from .windows10_general_configuration import Windows10GeneralConfiguration
        from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
        from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
        from .windows81_general_configuration import Windows81GeneralConfiguration
        from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
        from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
        from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
        from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(DeviceConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(SettingStateDeviceSummary)),
            "deviceStatusOverview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(DeviceConfigurationDeviceOverview)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(DeviceConfigurationDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "userStatusOverview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(DeviceConfigurationUserOverview)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(DeviceConfigurationUserStatus)),
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
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_int_value("version", self.version)
    

