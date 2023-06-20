from __future__ import annotations
from dataclasses import dataclass, field
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import windows_update_install_schedule_type

from . import windows_update_install_schedule_type

@dataclass
class WindowsUpdateActiveHoursInstall(windows_update_install_schedule_type.WindowsUpdateInstallScheduleType):
    odata_type = "#microsoft.graph.windowsUpdateActiveHoursInstall"
    # Active Hours End
    active_hours_end: Optional[time] = None
    # Active Hours Start
    active_hours_start: Optional[time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateActiveHoursInstall:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateActiveHoursInstall
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return WindowsUpdateActiveHoursInstall()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import windows_update_install_schedule_type

        from . import windows_update_install_schedule_type

        fields: Dict[str, Callable[[Any], None]] = {
            "activeHoursEnd": lambda n : setattr(self, 'active_hours_end', n.get_time_value()),
            "activeHoursStart": lambda n : setattr(self, 'active_hours_start', n.get_time_value()),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_time_value("activeHoursEnd", self.active_hours_end)
        writer.write_time_value("activeHoursStart", self.active_hours_start)
    

