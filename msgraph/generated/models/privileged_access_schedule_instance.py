from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
    from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance

from .entity import Entity

@dataclass
class PrivilegedAccessScheduleInstance(Entity, Parsable):
    # When the schedule instance ends. Required.
    end_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # When this instance starts. Required.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrivilegedAccessScheduleInstance:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrivilegedAccessScheduleInstance
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleInstance".casefold():
            from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance

            return PrivilegedAccessGroupAssignmentScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleInstance".casefold():
            from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance

            return PrivilegedAccessGroupEligibilityScheduleInstance()
        return PrivilegedAccessScheduleInstance()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
        from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance

        from .entity import Entity
        from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
        from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance

        fields: dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

