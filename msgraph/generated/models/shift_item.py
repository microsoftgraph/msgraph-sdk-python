from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .open_shift_item import OpenShiftItem
    from .schedule_entity import ScheduleEntity
    from .shift_activity import ShiftActivity

from .schedule_entity import ScheduleEntity

@dataclass
class ShiftItem(ScheduleEntity):
    # An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.
    activities: Optional[List[ShiftActivity]] = None
    # The shift label of the shiftItem.
    display_name: Optional[str] = None
    # The shift notes for the shiftItem.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ShiftItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ShiftItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftItem".casefold():
            from .open_shift_item import OpenShiftItem

            return OpenShiftItem()
        return ShiftItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .open_shift_item import OpenShiftItem
        from .schedule_entity import ScheduleEntity
        from .shift_activity import ShiftActivity

        from .open_shift_item import OpenShiftItem
        from .schedule_entity import ScheduleEntity
        from .shift_activity import ShiftActivity

        fields: Dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(ShiftActivity)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
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
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("notes", self.notes)
    

