from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .shift_item import ShiftItem

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class Shift(ChangeTrackedEntity):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.shift"
    # Draft changes in the shift. Draft changes are only visible to managers. The changes are visible to employees when they are shared, which copies the changes from the draftShift to the sharedShift property.
    draft_shift: Optional[ShiftItem] = None
    # ID of the scheduling group the shift is part of. Required.
    scheduling_group_id: Optional[str] = None
    # The shared version of this shift that is viewable by both employees and managers. Updates to the sharedShift property send notifications to users in the Teams client.
    shared_shift: Optional[ShiftItem] = None
    # ID of the user assigned to the shift. Required.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Shift:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Shift
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Shift()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .shift_item import ShiftItem

        from .change_tracked_entity import ChangeTrackedEntity
        from .shift_item import ShiftItem

        fields: Dict[str, Callable[[Any], None]] = {
            "draftShift": lambda n : setattr(self, 'draft_shift', n.get_object_value(ShiftItem)),
            "schedulingGroupId": lambda n : setattr(self, 'scheduling_group_id', n.get_str_value()),
            "sharedShift": lambda n : setattr(self, 'shared_shift', n.get_object_value(ShiftItem)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("draftShift", self.draft_shift)
        writer.write_str_value("schedulingGroupId", self.scheduling_group_id)
        writer.write_object_value("sharedShift", self.shared_shift)
        writer.write_str_value("userId", self.user_id)
    

