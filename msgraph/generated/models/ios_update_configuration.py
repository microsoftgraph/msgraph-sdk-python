from __future__ import annotations
from dataclasses import dataclass, field
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import day_of_week, device_configuration

from . import device_configuration

@dataclass
class IosUpdateConfiguration(device_configuration.DeviceConfiguration):
    odata_type = "#microsoft.graph.iosUpdateConfiguration"
    # Active Hours End (active hours mean the time window when updates install should not happen)
    active_hours_end: Optional[time] = None
    # Active Hours Start (active hours mean the time window when updates install should not happen)
    active_hours_start: Optional[time] = None
    # Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
    scheduled_install_days: Optional[List[day_of_week.DayOfWeek]] = None
    # UTC Time Offset indicated in minutes
    utc_time_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosUpdateConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosUpdateConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosUpdateConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import day_of_week, device_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "activeHoursEnd": lambda n : setattr(self, 'active_hours_end', n.get_time_value()),
            "activeHoursStart": lambda n : setattr(self, 'active_hours_start', n.get_time_value()),
            "scheduledInstallDays": lambda n : setattr(self, 'scheduled_install_days', n.get_collection_of_enum_values(day_of_week.DayOfWeek)),
            "utcTimeOffsetInMinutes": lambda n : setattr(self, 'utc_time_offset_in_minutes', n.get_int_value()),
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
        writer.write_time_value("activeHoursEnd", self.active_hours_end)
        writer.write_time_value("activeHoursStart", self.active_hours_start)
        writer.write_enum_value("scheduledInstallDays", self.scheduled_install_days)
        writer.write_int_value("utcTimeOffsetInMinutes", self.utc_time_offset_in_minutes)
    

