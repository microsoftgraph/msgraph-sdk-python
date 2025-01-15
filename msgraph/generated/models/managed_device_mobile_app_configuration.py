from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .ios_mobile_app_configuration import IosMobileAppConfiguration
    from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
    from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
    from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
    from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
    from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary

from .entity import Entity

@dataclass
class ManagedDeviceMobileAppConfiguration(Entity, Parsable):
    """
    An abstract class for Mobile app configuration for enrolled devices.
    """
    # The list of group assignemenets for app configration.
    assignments: Optional[list[ManagedDeviceMobileAppConfigurationAssignment]] = None
    # DateTime the object was created.
    created_date_time: Optional[datetime.datetime] = None
    # Admin provided description of the Device Configuration.
    description: Optional[str] = None
    # App configuration device status summary.
    device_status_summary: Optional[ManagedDeviceMobileAppConfigurationDeviceSummary] = None
    # List of ManagedDeviceMobileAppConfigurationDeviceStatus.
    device_statuses: Optional[list[ManagedDeviceMobileAppConfigurationDeviceStatus]] = None
    # Admin provided name of the device configuration.
    display_name: Optional[str] = None
    # DateTime the object was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # the associated app.
    targeted_mobile_apps: Optional[list[str]] = None
    # App configuration user status summary.
    user_status_summary: Optional[ManagedDeviceMobileAppConfigurationUserSummary] = None
    # List of ManagedDeviceMobileAppConfigurationUserStatus.
    user_statuses: Optional[list[ManagedDeviceMobileAppConfigurationUserStatus]] = None
    # Version of the device configuration.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ManagedDeviceMobileAppConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceMobileAppConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosMobileAppConfiguration".casefold():
            from .ios_mobile_app_configuration import IosMobileAppConfiguration

            return IosMobileAppConfiguration()
        return ManagedDeviceMobileAppConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .ios_mobile_app_configuration import IosMobileAppConfiguration
        from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
        from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
        from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
        from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
        from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary

        from .entity import Entity
        from .ios_mobile_app_configuration import IosMobileAppConfiguration
        from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
        from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
        from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
        from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
        from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary

        fields: dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(ManagedDeviceMobileAppConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceStatusSummary": lambda n : setattr(self, 'device_status_summary', n.get_object_value(ManagedDeviceMobileAppConfigurationDeviceSummary)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(ManagedDeviceMobileAppConfigurationDeviceStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "targetedMobileApps": lambda n : setattr(self, 'targeted_mobile_apps', n.get_collection_of_primitive_values(str)),
            "userStatusSummary": lambda n : setattr(self, 'user_status_summary', n.get_object_value(ManagedDeviceMobileAppConfigurationUserSummary)),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(ManagedDeviceMobileAppConfigurationUserStatus)),
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
        writer.write_object_value("deviceStatusSummary", self.device_status_summary)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_primitive_values("targetedMobileApps", self.targeted_mobile_apps)
        writer.write_object_value("userStatusSummary", self.user_status_summary)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_int_value("version", self.version)
    

