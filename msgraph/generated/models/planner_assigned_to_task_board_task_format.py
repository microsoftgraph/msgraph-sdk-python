from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
planner_order_hints_by_assignee = lazy_import('msgraph.generated.models.planner_order_hints_by_assignee')

class PlannerAssignedToTaskBoardTaskFormat(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerAssignedToTaskBoardTaskFormat and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Dictionary of hints used to order tasks on the AssignedTo view of the Task Board. The key of each entry is one of the users the task is assigned to and the value is the order hint. The format of each value is defined as outlined here.
        self._order_hints_by_assignee: Optional[planner_order_hints_by_assignee.PlannerOrderHintsByAssignee] = None
        # Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.
        self._unassigned_order_hint: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerAssignedToTaskBoardTaskFormat:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerAssignedToTaskBoardTaskFormat
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerAssignedToTaskBoardTaskFormat()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "order_hints_by_assignee": lambda n : setattr(self, 'order_hints_by_assignee', n.get_object_value(planner_order_hints_by_assignee.PlannerOrderHintsByAssignee)),
            "unassigned_order_hint": lambda n : setattr(self, 'unassigned_order_hint', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def order_hints_by_assignee(self,) -> Optional[planner_order_hints_by_assignee.PlannerOrderHintsByAssignee]:
        """
        Gets the orderHintsByAssignee property value. Dictionary of hints used to order tasks on the AssignedTo view of the Task Board. The key of each entry is one of the users the task is assigned to and the value is the order hint. The format of each value is defined as outlined here.
        Returns: Optional[planner_order_hints_by_assignee.PlannerOrderHintsByAssignee]
        """
        return self._order_hints_by_assignee
    
    @order_hints_by_assignee.setter
    def order_hints_by_assignee(self,value: Optional[planner_order_hints_by_assignee.PlannerOrderHintsByAssignee] = None) -> None:
        """
        Sets the orderHintsByAssignee property value. Dictionary of hints used to order tasks on the AssignedTo view of the Task Board. The key of each entry is one of the users the task is assigned to and the value is the order hint. The format of each value is defined as outlined here.
        Args:
            value: Value to set for the orderHintsByAssignee property.
        """
        self._order_hints_by_assignee = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("orderHintsByAssignee", self.order_hints_by_assignee)
        writer.write_str_value("unassignedOrderHint", self.unassigned_order_hint)
    
    @property
    def unassigned_order_hint(self,) -> Optional[str]:
        """
        Gets the unassignedOrderHint property value. Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.
        Returns: Optional[str]
        """
        return self._unassigned_order_hint
    
    @unassigned_order_hint.setter
    def unassigned_order_hint(self,value: Optional[str] = None) -> None:
        """
        Sets the unassignedOrderHint property value. Hint value used to order the task on the AssignedTo view of the Task Board when the task is not assigned to anyone, or if the orderHintsByAssignee dictionary does not provide an order hint for the user the task is assigned to. The format is defined as outlined here.
        Args:
            value: Value to set for the unassignedOrderHint property.
        """
        self._unassigned_order_hint = value
    

