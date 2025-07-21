from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee

from .entity import Entity

@dataclass
class PlannerAssignedToTaskBoardTaskFormat(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Dictionary of hints used to order tasks on the AssignedTo view of the Task Board. The key of each entry is one of the users the task is assigned to and the value is the order hint. The format of each value is defined as outlined here.
    order_hints_by_assignee: Optional[PlannerOrderHintsByAssignee] = None
    # Hint value used to order the task on the AssignedTo view of the Task Board when the task isn't assigned to anyone, or if the orderHintsByAssignee dictionary doesn't provide an order hint for the user the task is assigned to. The format is defined as outlined here.
    unassigned_order_hint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerAssignedToTaskBoardTaskFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerAssignedToTaskBoardTaskFormat
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerAssignedToTaskBoardTaskFormat()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee

        from .entity import Entity
        from .planner_order_hints_by_assignee import PlannerOrderHintsByAssignee

        fields: dict[str, Callable[[Any], None]] = {
            "orderHintsByAssignee": lambda n : setattr(self, 'order_hints_by_assignee', n.get_object_value(PlannerOrderHintsByAssignee)),
            "unassignedOrderHint": lambda n : setattr(self, 'unassigned_order_hint', n.get_str_value()),
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
        writer.write_object_value("orderHintsByAssignee", self.order_hints_by_assignee)
        writer.write_str_value("unassignedOrderHint", self.unassigned_order_hint)
    

