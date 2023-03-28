from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, planner_plan

from . import entity

class PlannerGroup(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerGroup and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Read-only. Nullable. Returns the plannerPlans owned by the group.
        self._plans: Optional[List[planner_plan.PlannerPlan]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerGroup
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, planner_plan

        fields: Dict[str, Callable[[Any], None]] = {
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def plans(self,) -> Optional[List[planner_plan.PlannerPlan]]:
        """
        Gets the plans property value. Read-only. Nullable. Returns the plannerPlans owned by the group.
        Returns: Optional[List[planner_plan.PlannerPlan]]
        """
        return self._plans
    
    @plans.setter
    def plans(self,value: Optional[List[planner_plan.PlannerPlan]] = None) -> None:
        """
        Sets the plans property value. Read-only. Nullable. Returns the plannerPlans owned by the group.
        Args:
            value: Value to set for the plans property.
        """
        self._plans = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("plans", self.plans)
    

