from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .schedule_change_request import ScheduleChangeRequest

from .schedule_change_request import ScheduleChangeRequest

@dataclass
class TimeOffRequest(ScheduleChangeRequest, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.timeOffRequest"
    # The date and time the time off ends in ISO 8601 format and in UTC time.
    end_date_time: Optional[datetime.datetime] = None
    # The date and time the time off starts in ISO 8601 format and in UTC time.
    start_date_time: Optional[datetime.datetime] = None
    # The reason for the time off.
    time_off_reason_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeOffRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeOffRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeOffRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .schedule_change_request import ScheduleChangeRequest

        from .schedule_change_request import ScheduleChangeRequest

        fields: dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "timeOffReasonId": lambda n : setattr(self, 'time_off_reason_id', n.get_str_value()),
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
        writer.write_str_value("timeOffReasonId", self.time_off_reason_id)
    

