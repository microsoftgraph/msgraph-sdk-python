from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .planner_plan import PlannerPlan

from .entity import Entity

@dataclass
class PlannerGroup(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Read-only. Nullable. Returns the plannerPlans owned by the group.
    plans: Optional[List[PlannerPlan]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .planner_plan import PlannerPlan

        from .entity import Entity
        from .planner_plan import PlannerPlan

        fields: Dict[str, Callable[[Any], None]] = {
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(PlannerPlan)),
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
        from .entity import Entity
        from .planner_plan import PlannerPlan

        writer.write_collection_of_object_values("plans", self.plans)
    

