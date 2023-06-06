from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import change_tracked_entity, shift_item

from . import change_tracked_entity

@dataclass
class Shift(change_tracked_entity.ChangeTrackedEntity):
    odata_type = "#microsoft.graph.shift"
    # The draft version of this shift that is viewable by managers. Required.
    draft_shift: Optional[shift_item.ShiftItem] = None
    # ID of the scheduling group the shift is part of. Required.
    scheduling_group_id: Optional[str] = None
    # The shared version of this shift that is viewable by both employees and managers. Required.
    shared_shift: Optional[shift_item.ShiftItem] = None
    # ID of the user assigned to the shift. Required.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Shift:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Shift
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Shift()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import change_tracked_entity, shift_item

        fields: Dict[str, Callable[[Any], None]] = {
            "draftShift": lambda n : setattr(self, 'draft_shift', n.get_object_value(shift_item.ShiftItem)),
            "schedulingGroupId": lambda n : setattr(self, 'scheduling_group_id', n.get_str_value()),
            "sharedShift": lambda n : setattr(self, 'shared_shift', n.get_object_value(shift_item.ShiftItem)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("draftShift", self.draft_shift)
        writer.write_str_value("schedulingGroupId", self.scheduling_group_id)
        writer.write_object_value("sharedShift", self.shared_shift)
        writer.write_str_value("userId", self.user_id)
    

