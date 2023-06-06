from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import open_shift_item, schedule_entity, shift_activity

from . import schedule_entity

@dataclass
class ShiftItem(schedule_entity.ScheduleEntity):
    # An incremental part of a shift which can cover details of when and where an employee is during their shift. For example, an assignment or a scheduled break or lunch. Required.
    activities: Optional[List[shift_activity.ShiftActivity]] = None
    # The shift label of the shiftItem.
    display_name: Optional[str] = None
    # The shift notes for the shiftItem.
    notes: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ShiftItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ShiftItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.openShiftItem":
                from . import open_shift_item

                return open_shift_item.OpenShiftItem()
        return ShiftItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import open_shift_item, schedule_entity, shift_activity

        fields: Dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_object_values(shift_activity.ShiftActivity)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
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
        writer.write_collection_of_object_values("activities", self.activities)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("notes", self.notes)
    

