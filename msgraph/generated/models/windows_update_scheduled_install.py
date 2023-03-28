from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import weekly_schedule, windows_update_install_schedule_type

from . import windows_update_install_schedule_type

class WindowsUpdateScheduledInstall(windows_update_install_schedule_type.WindowsUpdateInstallScheduleType):
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsUpdateScheduledInstall and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdateScheduledInstall"
        # Possible values for a weekly schedule.
        self._scheduled_install_day: Optional[weekly_schedule.WeeklySchedule] = None
        # Scheduled Install Time during day
        self._scheduled_install_time: Optional[time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateScheduledInstall:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateScheduledInstall
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsUpdateScheduledInstall()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import weekly_schedule, windows_update_install_schedule_type

        fields: Dict[str, Callable[[Any], None]] = {
            "scheduledInstallDay": lambda n : setattr(self, 'scheduled_install_day', n.get_enum_value(weekly_schedule.WeeklySchedule)),
            "scheduledInstallTime": lambda n : setattr(self, 'scheduled_install_time', n.get_time_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def scheduled_install_day(self,) -> Optional[weekly_schedule.WeeklySchedule]:
        """
        Gets the scheduledInstallDay property value. Possible values for a weekly schedule.
        Returns: Optional[weekly_schedule.WeeklySchedule]
        """
        return self._scheduled_install_day
    
    @scheduled_install_day.setter
    def scheduled_install_day(self,value: Optional[weekly_schedule.WeeklySchedule] = None) -> None:
        """
        Sets the scheduledInstallDay property value. Possible values for a weekly schedule.
        Args:
            value: Value to set for the scheduled_install_day property.
        """
        self._scheduled_install_day = value
    
    @property
    def scheduled_install_time(self,) -> Optional[time]:
        """
        Gets the scheduledInstallTime property value. Scheduled Install Time during day
        Returns: Optional[time]
        """
        return self._scheduled_install_time
    
    @scheduled_install_time.setter
    def scheduled_install_time(self,value: Optional[time] = None) -> None:
        """
        Sets the scheduledInstallTime property value. Scheduled Install Time during day
        Args:
            value: Value to set for the scheduled_install_time property.
        """
        self._scheduled_install_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("scheduledInstallDay", self.scheduled_install_day)
        writer.write_time_value("scheduledInstallTime", self.scheduled_install_time)
    

