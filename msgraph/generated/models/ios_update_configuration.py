from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import day_of_week, device_configuration

from . import device_configuration

class IosUpdateConfiguration(device_configuration.DeviceConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new IosUpdateConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosUpdateConfiguration"
        # Active Hours End (active hours mean the time window when updates install should not happen)
        self._active_hours_end: Optional[time] = None
        # Active Hours Start (active hours mean the time window when updates install should not happen)
        self._active_hours_start: Optional[time] = None
        # Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
        self._scheduled_install_days: Optional[List[day_of_week.DayOfWeek]] = None
        # UTC Time Offset indicated in minutes
        self._utc_time_offset_in_minutes: Optional[int] = None
    
    @property
    def active_hours_end(self,) -> Optional[time]:
        """
        Gets the activeHoursEnd property value. Active Hours End (active hours mean the time window when updates install should not happen)
        Returns: Optional[time]
        """
        return self._active_hours_end
    
    @active_hours_end.setter
    def active_hours_end(self,value: Optional[time] = None) -> None:
        """
        Sets the activeHoursEnd property value. Active Hours End (active hours mean the time window when updates install should not happen)
        Args:
            value: Value to set for the active_hours_end property.
        """
        self._active_hours_end = value
    
    @property
    def active_hours_start(self,) -> Optional[time]:
        """
        Gets the activeHoursStart property value. Active Hours Start (active hours mean the time window when updates install should not happen)
        Returns: Optional[time]
        """
        return self._active_hours_start
    
    @active_hours_start.setter
    def active_hours_start(self,value: Optional[time] = None) -> None:
        """
        Sets the activeHoursStart property value. Active Hours Start (active hours mean the time window when updates install should not happen)
        Args:
            value: Value to set for the active_hours_start property.
        """
        self._active_hours_start = value
    
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
    
    @property
    def scheduled_install_days(self,) -> Optional[List[day_of_week.DayOfWeek]]:
        """
        Gets the scheduledInstallDays property value. Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
        Returns: Optional[List[day_of_week.DayOfWeek]]
        """
        return self._scheduled_install_days
    
    @scheduled_install_days.setter
    def scheduled_install_days(self,value: Optional[List[day_of_week.DayOfWeek]] = None) -> None:
        """
        Sets the scheduledInstallDays property value. Days in week for which active hours are configured. This collection can contain a maximum of 7 elements.
        Args:
            value: Value to set for the scheduled_install_days property.
        """
        self._scheduled_install_days = value
    
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
    
    @property
    def utc_time_offset_in_minutes(self,) -> Optional[int]:
        """
        Gets the utcTimeOffsetInMinutes property value. UTC Time Offset indicated in minutes
        Returns: Optional[int]
        """
        return self._utc_time_offset_in_minutes
    
    @utc_time_offset_in_minutes.setter
    def utc_time_offset_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the utcTimeOffsetInMinutes property value. UTC Time Offset indicated in minutes
        Args:
            value: Value to set for the utc_time_offset_in_minutes property.
        """
        self._utc_time_offset_in_minutes = value
    

