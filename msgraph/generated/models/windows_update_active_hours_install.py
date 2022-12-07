from __future__ import annotations
from datetime import time
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

windows_update_install_schedule_type = lazy_import('msgraph.generated.models.windows_update_install_schedule_type')

class WindowsUpdateActiveHoursInstall(windows_update_install_schedule_type.WindowsUpdateInstallScheduleType):
    @property
    def active_hours_end(self,) -> Optional[Time]:
        """
        Gets the activeHoursEnd property value. Active Hours End
        Returns: Optional[Time]
        """
        return self._active_hours_end
    
    @active_hours_end.setter
    def active_hours_end(self,value: Optional[Time] = None) -> None:
        """
        Sets the activeHoursEnd property value. Active Hours End
        Args:
            value: Value to set for the activeHoursEnd property.
        """
        self._active_hours_end = value
    
    @property
    def active_hours_start(self,) -> Optional[Time]:
        """
        Gets the activeHoursStart property value. Active Hours Start
        Returns: Optional[Time]
        """
        return self._active_hours_start
    
    @active_hours_start.setter
    def active_hours_start(self,value: Optional[Time] = None) -> None:
        """
        Sets the activeHoursStart property value. Active Hours Start
        Args:
            value: Value to set for the activeHoursStart property.
        """
        self._active_hours_start = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new WindowsUpdateActiveHoursInstall and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windowsUpdateActiveHoursInstall"
        # Active Hours End
        self._active_hours_end: Optional[Time] = None
        # Active Hours Start
        self._active_hours_start: Optional[Time] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsUpdateActiveHoursInstall:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsUpdateActiveHoursInstall
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsUpdateActiveHoursInstall()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_hours_end": lambda n : setattr(self, 'active_hours_end', n.get_object_value(Time)),
            "active_hours_start": lambda n : setattr(self, 'active_hours_start', n.get_object_value(Time)),
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
        writer.write_object_value("activeHoursEnd", self.active_hours_end)
        writer.write_object_value("activeHoursStart", self.active_hours_start)
    

