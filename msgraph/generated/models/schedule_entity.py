from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import open_shift_item, schedule_entity_theme, shift_item, time_off_item

@dataclass
class ScheduleEntity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The endDateTime property
    end_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The startDateTime property
    start_date_time: Optional[datetime] = None
    # The theme property
    theme: Optional[schedule_entity_theme.ScheduleEntityTheme] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ScheduleEntity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ScheduleEntity
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftItem".casefold():
            from . import open_shift_item

            return open_shift_item.OpenShiftItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shiftItem".casefold():
            from . import shift_item

            return shift_item.ShiftItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffItem".casefold():
            from . import time_off_item

            return time_off_item.TimeOffItem()
        return ScheduleEntity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import open_shift_item, schedule_entity_theme, shift_item, time_off_item

        from . import open_shift_item, schedule_entity_theme, shift_item, time_off_item

        fields: Dict[str, Callable[[Any], None]] = {
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "theme": lambda n : setattr(self, 'theme', n.get_enum_value(schedule_entity_theme.ScheduleEntityTheme)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("theme", self.theme)
        writer.write_additional_data_value(self.additional_data)
    

