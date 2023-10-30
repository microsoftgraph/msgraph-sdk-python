from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .day_of_week import DayOfWeek
    from .device_configuration import DeviceConfiguration

from .device_configuration import DeviceConfiguration

@dataclass
class IosUpdateConfiguration(DeviceConfiguration):
    """
    IOS Update Configuration, allows you to configure time window within week to install iOS updates
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.iosUpdateConfiguration"
    # Active Hours End (active hours mean the time window when updates install should not happen)
    active_hours_end: Optional[datetime.time] = None
    # Active Hours Start (active hours mean the time window when updates install should not happen)
    active_hours_start: Optional[datetime.time] = None
    # Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
    scheduled_install_days: Optional[List[DayOfWeek]] = None
    # UTC Time Offset indicated in minutes
    utc_time_offset_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosUpdateConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IosUpdateConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IosUpdateConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .day_of_week import DayOfWeek
        from .device_configuration import DeviceConfiguration

        from .day_of_week import DayOfWeek
        from .device_configuration import DeviceConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "active_hours_end": lambda n : setattr(self, 'active_hours_end', n.get_time_value()),
            "active_hours_start": lambda n : setattr(self, 'active_hours_start', n.get_time_value()),
            "scheduled_install_days": lambda n : setattr(self, 'scheduled_install_days', n.get_collection_of_enum_values(DayOfWeek)),
            "utc_time_offset_in_minutes": lambda n : setattr(self, 'utc_time_offset_in_minutes', n.get_int_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_time_value("active_hours_end", self.active_hours_end)
        writer.write_time_value("active_hours_start", self.active_hours_start)
        writer.write_collection_of_enum_values("scheduled_install_days", self.scheduled_install_days)
        writer.write_int_value("utc_time_offset_in_minutes", self.utc_time_offset_in_minutes)
    

