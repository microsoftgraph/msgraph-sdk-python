from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
    from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
    from .request_schedule import RequestSchedule

from .entity import Entity

@dataclass
class PrivilegedAccessSchedule(Entity, Parsable):
    # When the schedule was created. Optional.
    created_date_time: Optional[datetime.datetime] = None
    # The identifier of the access assignment or eligibility request that created this schedule. Optional.
    created_using: Optional[str] = None
    # When the schedule was last modified. Optional.
    modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the period of the access assignment or eligibility. The scheduleInfo can represent a single occurrence or multiple recurring instances. Required.
    schedule_info: Optional[RequestSchedule] = None
    # The status of the access assignment or eligibility request. The possible values are: Canceled, Denied, Failed, Granted, PendingAdminDecision, PendingApproval, PendingProvisioning, PendingScheduleCreation, Provisioned, Revoked, and ScheduleCreated. Not nullable. Optional.
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedAccessSchedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessSchedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentSchedule".casefold():
            from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule

            return PrivilegedAccessGroupAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilitySchedule".casefold():
            from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

            return PrivilegedAccessGroupEligibilitySchedule()
        return PrivilegedAccessSchedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .request_schedule import RequestSchedule

        from .entity import Entity
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .request_schedule import RequestSchedule

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "createdUsing": lambda n : setattr(self, 'created_using', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "scheduleInfo": lambda n : setattr(self, 'schedule_info', n.get_object_value(RequestSchedule)),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("createdUsing", self.created_using)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_object_value("scheduleInfo", self.schedule_info)
        writer.write_str_value("status", self.status)
    

