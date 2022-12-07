from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
managed_device_mobile_app_configuration_assignment = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration_assignment')
managed_device_mobile_app_configuration_device_status = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration_device_status')
managed_device_mobile_app_configuration_device_summary = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration_device_summary')
managed_device_mobile_app_configuration_user_status = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration_user_status')
managed_device_mobile_app_configuration_user_summary = lazy_import('msgraph.generated.models.managed_device_mobile_app_configuration_user_summary')

class ManagedDeviceMobileAppConfiguration(entity.Entity):
    """
    An abstract class for Mobile app configuration for enrolled devices.
    """
    @property
    def assignments(self,) -> Optional[List[managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment]]:
        """
        Gets the assignments property value. The list of group assignemenets for app configration.
        Returns: Optional[List[managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of group assignemenets for app configration.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedDeviceMobileAppConfiguration and sets the default values.
        """
        super().__init__()
        # The list of group assignemenets for app configration.
        self._assignments: Optional[List[managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment]] = None
        # DateTime the object was created.
        self._created_date_time: Optional[datetime] = None
        # Admin provided description of the Device Configuration.
        self._description: Optional[str] = None
        # List of ManagedDeviceMobileAppConfigurationDeviceStatus.
        self._device_statuses: Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]] = None
        # App configuration device status summary.
        self._device_status_summary: Optional[managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary] = None
        # Admin provided name of the device configuration.
        self._display_name: Optional[str] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # the associated app.
        self._targeted_mobile_apps: Optional[List[str]] = None
        # List of ManagedDeviceMobileAppConfigurationUserStatus.
        self._user_statuses: Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]] = None
        # App configuration user status summary.
        self._user_status_summary: Optional[managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary] = None
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceMobileAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceMobileAppConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceMobileAppConfiguration()
    
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
    def device_statuses(self,) -> Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]]:
        """
        Gets the deviceStatuses property value. List of ManagedDeviceMobileAppConfigurationDeviceStatus.
        Returns: Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. List of ManagedDeviceMobileAppConfigurationDeviceStatus.
        Args:
            value: Value to set for the deviceStatuses property.
        """
        self._device_statuses = value
    
    @property
    def device_status_summary(self,) -> Optional[managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary]:
        """
        Gets the deviceStatusSummary property value. App configuration device status summary.
        Returns: Optional[managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary]
        """
        return self._device_status_summary
    
    @device_status_summary.setter
    def device_status_summary(self,value: Optional[managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary] = None) -> None:
        """
        Sets the deviceStatusSummary property value. App configuration device status summary.
        Args:
            value: Value to set for the deviceStatusSummary property.
        """
        self._device_status_summary = value
    
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
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "device_statuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus)),
            "device_status_summary": lambda n : setattr(self, 'device_status_summary', n.get_object_value(managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "targeted_mobile_apps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_primitive_values(str)),
            "user_statuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus)),
            "user_status_summary": lambda n : setattr(self, 'user_status_summary', n.get_object_value(managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary)),
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
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_object_value("deviceStatusSummary", self.device_status_summary)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_object_value("userStatusSummary", self.user_status_summary)
        writer.write_int_value("version", self.version)
    
    @property
    def targeted_mobile_apps(self,) -> Optional[List[str]]:
        """
        Gets the targetedMobileApps property value. the associated app.
        Returns: Optional[List[str]]
        """
        return self._targeted_mobile_apps
    
    @targeted_mobile_apps.setter
    def targeted_mobile_apps(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the targetedMobileApps property value. the associated app.
        Args:
            value: Value to set for the targetedMobileApps property.
        """
        self._targeted_mobile_apps = value
    
    @property
    def user_statuses(self,) -> Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]]:
        """
        Gets the userStatuses property value. List of ManagedDeviceMobileAppConfigurationUserStatus.
        Returns: Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]]
        """
        return self._user_statuses
    
    @user_statuses.setter
    def user_statuses(self,value: Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]] = None) -> None:
        """
        Sets the userStatuses property value. List of ManagedDeviceMobileAppConfigurationUserStatus.
        Args:
            value: Value to set for the userStatuses property.
        """
        self._user_statuses = value
    
    @property
    def user_status_summary(self,) -> Optional[managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary]:
        """
        Gets the userStatusSummary property value. App configuration user status summary.
        Returns: Optional[managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary]
        """
        return self._user_status_summary
    
    @user_status_summary.setter
    def user_status_summary(self,value: Optional[managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary] = None) -> None:
        """
        Sets the userStatusSummary property value. App configuration user status summary.
        Args:
            value: Value to set for the userStatusSummary property.
        """
        self._user_status_summary = value
    
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
    

