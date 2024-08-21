from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

from .entity import Entity

@dataclass
class UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails(Entity):
    """
    The user experience analytics application performance entity contains application performance by application version details.
    """
    # The number of crashes for the app. Valid values -2147483648 to 2147483647
    app_crash_count: Optional[int] = None
    # The friendly name of the application.
    app_display_name: Optional[str] = None
    # The name of the application.
    app_name: Optional[str] = None
    # The publisher of the application.
    app_publisher: Optional[str] = None
    # The version of the application.
    app_version: Optional[str] = None
    # The total number of devices that have reported one or more application crashes for this application and version. Valid values 0 to 2147483647. Supports: $select, $OrderBy. Read-only. Valid values -2147483648 to 2147483647
    device_count_with_crashes: Optional[int] = None
    # When TRUE, indicates the version of application is the latest version for that application that is in use. When FALSE, indicates the version is not the latest version. FALSE by default. Supports: $select, $OrderBy.
    is_latest_used_version: Optional[bool] = None
    # When TRUE, indicates the version of application is the most used version for that application. When FALSE, indicates the version is not the most used version. FALSE by default. Supports: $select, $OrderBy. Read-only.
    is_most_used_version: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appCrashCount": lambda n : setattr(self, 'app_crash_count', n.get_int_value()),
            "appDisplayName": lambda n : setattr(self, 'app_display_name', n.get_str_value()),
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "appPublisher": lambda n : setattr(self, 'app_publisher', n.get_str_value()),
            "appVersion": lambda n : setattr(self, 'app_version', n.get_str_value()),
            "deviceCountWithCrashes": lambda n : setattr(self, 'device_count_with_crashes', n.get_int_value()),
            "isLatestUsedVersion": lambda n : setattr(self, 'is_latest_used_version', n.get_bool_value()),
            "isMostUsedVersion": lambda n : setattr(self, 'is_most_used_version', n.get_bool_value()),
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
        writer.write_int_value("appCrashCount", self.app_crash_count)
        writer.write_str_value("appDisplayName", self.app_display_name)
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("appPublisher", self.app_publisher)
        writer.write_str_value("appVersion", self.app_version)
        writer.write_int_value("deviceCountWithCrashes", self.device_count_with_crashes)
        writer.write_bool_value("isLatestUsedVersion", self.is_latest_used_version)
        writer.write_bool_value("isMostUsedVersion", self.is_most_used_version)
    

