from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, ios_mobile_app_configuration, managed_device_mobile_app_configuration_assignment, managed_device_mobile_app_configuration_device_status, managed_device_mobile_app_configuration_device_summary, managed_device_mobile_app_configuration_user_status, managed_device_mobile_app_configuration_user_summary

from . import entity

@dataclass
class ManagedDeviceMobileAppConfiguration(entity.Entity):
    """
    An abstract class for Mobile app configuration for enrolled devices.
    """
    # The list of group assignemenets for app configration.
    assignments: Optional[List[managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # App configuration device status summary.
    device_status_summary: Optional[managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary] = None
    # List of ManagedDeviceMobileAppConfigurationDeviceStatus.
    device_statuses: Optional[List[managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # the associated app.
    targeted_mobile_apps: Optional[List[str]] = None
    # App configuration user status summary.
    user_status_summary: Optional[managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary] = None
    # List of ManagedDeviceMobileAppConfigurationUserStatus.
    user_statuses: Optional[List[managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
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
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.iosMobileAppConfiguration":
                from . import ios_mobile_app_configuration

                return ios_mobile_app_configuration.IosMobileAppConfiguration()
        return ManagedDeviceMobileAppConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, ios_mobile_app_configuration, managed_device_mobile_app_configuration_assignment, managed_device_mobile_app_configuration_device_status, managed_device_mobile_app_configuration_device_summary, managed_device_mobile_app_configuration_user_status, managed_device_mobile_app_configuration_user_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(managed_device_mobile_app_configuration_assignment.ManagedDeviceMobileAppConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(managed_device_mobile_app_configuration_device_status.ManagedDeviceMobileAppConfigurationDeviceStatus)),
            "deviceStatusSummary": lambda n : setattr(self, 'device_status_summary', n.get_object_value(managed_device_mobile_app_configuration_device_summary.ManagedDeviceMobileAppConfigurationDeviceSummary)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "targetedMobileApps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_primitive_values(str)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(managed_device_mobile_app_configuration_user_status.ManagedDeviceMobileAppConfigurationUserStatus)),
            "userStatusSummary": lambda n : setattr(self, 'user_status_summary', n.get_object_value(managed_device_mobile_app_configuration_user_summary.ManagedDeviceMobileAppConfigurationUserSummary)),
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
    

