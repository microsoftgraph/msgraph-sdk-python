from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .weekly_schedule import WeeklySchedule
    from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType

from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType

@dataclass
class WindowsUpdateScheduledInstall(WindowsUpdateInstallScheduleType):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.windowsUpdateScheduledInstall"
    # Possible values for a weekly schedule.
    scheduled_install_day: Optional[WeeklySchedule] = None
    # Scheduled Install Time during day
    scheduled_install_time: Optional[datetime.time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WindowsUpdateScheduledInstall:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateScheduledInstall
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WindowsUpdateScheduledInstall()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .weekly_schedule import WeeklySchedule
        from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType

        from .weekly_schedule import WeeklySchedule
        from .windows_update_install_schedule_type import WindowsUpdateInstallScheduleType

        fields: Dict[str, Callable[[Any], None]] = {
            "scheduledInstallDay": lambda n : setattr(self, 'scheduled_install_day', n.get_enum_value(WeeklySchedule)),
            "scheduledInstallTime": lambda n : setattr(self, 'scheduled_install_time', n.get_time_value()),
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
        writer.write_enum_value("scheduledInstallDay", self.scheduled_install_day)
        writer.write_time_value("scheduledInstallTime", self.scheduled_install_time)
    

