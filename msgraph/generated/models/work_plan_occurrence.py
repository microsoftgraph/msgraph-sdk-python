from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .date_time_time_zone import DateTimeTimeZone
    from .entity import Entity
    from .time_off_details import TimeOffDetails
    from .work_location_type import WorkLocationType

from .entity import Entity

@dataclass
class WorkPlanOccurrence(Entity, Parsable):
    # The end property
    end: Optional[DateTimeTimeZone] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Identifier of a place from the Microsoft Graph Places Directory API. Only applicable when workLocationType is set to office.
    place_id: Optional[str] = None
    # The identifier of the parent recurrence pattern that generated this occurrence. The value is null for time-off occurrences because they don't have a parent recurrence.
    recurrence_id: Optional[str] = None
    # The start property
    start: Optional[DateTimeTimeZone] = None
    # The details about the time off. Only applicable when workLocationType is set to timeOff.
    time_off_details: Optional[TimeOffDetails] = None
    # The workLocationType property
    work_location_type: Optional[WorkLocationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkPlanOccurrence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkPlanOccurrence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkPlanOccurrence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .time_off_details import TimeOffDetails
        from .work_location_type import WorkLocationType

        from .date_time_time_zone import DateTimeTimeZone
        from .entity import Entity
        from .time_off_details import TimeOffDetails
        from .work_location_type import WorkLocationType

        fields: dict[str, Callable[[Any], None]] = {
            "end": lambda n : setattr(self, 'end', n.get_object_value(DateTimeTimeZone)),
            "placeId": lambda n : setattr(self, 'place_id', n.get_str_value()),
            "recurrenceId": lambda n : setattr(self, 'recurrence_id', n.get_str_value()),
            "start": lambda n : setattr(self, 'start', n.get_object_value(DateTimeTimeZone)),
            "timeOffDetails": lambda n : setattr(self, 'time_off_details', n.get_object_value(TimeOffDetails)),
            "workLocationType": lambda n : setattr(self, 'work_location_type', n.get_enum_value(WorkLocationType)),
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
        writer.write_object_value("end", self.end)
        writer.write_str_value("placeId", self.place_id)
        writer.write_str_value("recurrenceId", self.recurrence_id)
        writer.write_object_value("start", self.start)
        writer.write_object_value("timeOffDetails", self.time_off_details)
        writer.write_enum_value("workLocationType", self.work_location_type)
    

