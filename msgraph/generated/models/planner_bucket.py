from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, planner_task

from . import entity

@dataclass
class PlannerBucket(entity.Entity):
    # Name of the bucket.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Hint used to order items of this type in a list view. For details about the supported format, see Using order hints in Planner.
    order_hint: Optional[str] = None
    # Plan ID to which the bucket belongs.
    plan_id: Optional[str] = None
    # Read-only. Nullable. The collection of tasks in the bucket.
    tasks: Optional[List[planner_task.PlannerTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerBucket:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerBucket
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerBucket()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, planner_task

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "orderHint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(planner_task.PlannerTask)),
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
        writer.write_str_value("name", self.name)
        writer.write_str_value("orderHint", self.order_hint)
        writer.write_str_value("planId", self.plan_id)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

