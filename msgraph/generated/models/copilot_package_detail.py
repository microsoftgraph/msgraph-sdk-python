from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_package import CopilotPackage
    from .package_access_entity import PackageAccessEntity
    from .package_element_detail import PackageElementDetail

from .copilot_package import CopilotPackage

@dataclass
class CopilotPackageDetail(CopilotPackage, Parsable):
    # The acquireUsersAndGroups property
    acquire_users_and_groups: Optional[list[PackageAccessEntity]] = None
    # The number of distinct users who actively used the package during the reporting period.
    active_users: Optional[int] = None
    # The allowedUsersAndGroups property
    allowed_users_and_groups: Optional[list[PackageAccessEntity]] = None
    # The categories property
    categories: Optional[list[str]] = None
    # The elementDetails property
    element_details: Optional[list[PackageElementDetail]] = None
    # The fraction of sessions that resulted in an exception, expressed as a value between 0 and 1.
    exception_rate: Optional[float] = None
    # The date and time when the package was last used, in ISO 8601 format and UTC.
    last_used_date_time: Optional[datetime.datetime] = None
    # The longDescription property
    long_description: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The sensitivity property
    sensitivity: Optional[str] = None
    # The sharedWithUsersAndGroups property
    shared_with_users_and_groups: Optional[list[PackageAccessEntity]] = None
    # Total hours worked by the agent.
    total_run_time_in_hours: Optional[float] = None
    # The total number of sessions served by the package during the reporting period.
    total_sessions: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPackageDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPackageDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPackageDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_package import CopilotPackage
        from .package_access_entity import PackageAccessEntity
        from .package_element_detail import PackageElementDetail

        from .copilot_package import CopilotPackage
        from .package_access_entity import PackageAccessEntity
        from .package_element_detail import PackageElementDetail

        fields: dict[str, Callable[[Any], None]] = {
            "acquireUsersAndGroups": lambda n : setattr(self, 'acquire_users_and_groups', n.get_collection_of_object_values(PackageAccessEntity)),
            "activeUsers": lambda n : setattr(self, 'active_users', n.get_int_value()),
            "allowedUsersAndGroups": lambda n : setattr(self, 'allowed_users_and_groups', n.get_collection_of_object_values(PackageAccessEntity)),
            "categories": lambda n : setattr(self, 'categories', n.get_collection_of_primitive_values(str)),
            "elementDetails": lambda n : setattr(self, 'element_details', n.get_collection_of_object_values(PackageElementDetail)),
            "exceptionRate": lambda n : setattr(self, 'exception_rate', n.get_float_value()),
            "lastUsedDateTime": lambda n : setattr(self, 'last_used_date_time', n.get_datetime_value()),
            "longDescription": lambda n : setattr(self, 'long_description', n.get_str_value()),
            "sensitivity": lambda n : setattr(self, 'sensitivity', n.get_str_value()),
            "sharedWithUsersAndGroups": lambda n : setattr(self, 'shared_with_users_and_groups', n.get_collection_of_object_values(PackageAccessEntity)),
            "totalRunTimeInHours": lambda n : setattr(self, 'total_run_time_in_hours', n.get_float_value()),
            "totalSessions": lambda n : setattr(self, 'total_sessions', n.get_int_value()),
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
        writer.write_collection_of_object_values("acquireUsersAndGroups", self.acquire_users_and_groups)
        writer.write_int_value("activeUsers", self.active_users)
        writer.write_collection_of_object_values("allowedUsersAndGroups", self.allowed_users_and_groups)
        writer.write_collection_of_primitive_values("categories", self.categories)
        writer.write_collection_of_object_values("elementDetails", self.element_details)
        writer.write_float_value("exceptionRate", self.exception_rate)
        writer.write_datetime_value("lastUsedDateTime", self.last_used_date_time)
        writer.write_str_value("longDescription", self.long_description)
        writer.write_str_value("sensitivity", self.sensitivity)
        writer.write_collection_of_object_values("sharedWithUsersAndGroups", self.shared_with_users_and_groups)
        writer.write_float_value("totalRunTimeInHours", self.total_run_time_in_hours)
        writer.write_int_value("totalSessions", self.total_sessions)
    

