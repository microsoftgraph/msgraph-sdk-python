from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, Union

from . import entity, planner_plan, planner_task

class PlannerUser(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new plannerUser and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.plannerUser"
        # Read-only. Nullable. Returns the plannerTasks assigned to the user.
        self._plans: Optional[List[planner_plan.PlannerPlan]] = None
        # Read-only. Nullable. Returns the plannerPlans shared with the user.
        self._tasks: Optional[List[planner_task.PlannerTask]] = None

    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerUser
        """
        if not parse_node:
            raise Exception("parse_node cannot be undefined")
        return PlannerUser()

    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "plans": lambda n : setattr(self, 'plans', n.get_collection_of_object_values(planner_plan.PlannerPlan)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(planner_task.PlannerTask)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields

    @property
    def plans(self,) -> Optional[List[planner_plan.PlannerPlan]]:
        """
        Gets the plans property value. Read-only. Nullable. Returns the plannerTasks assigned to the user.
        Returns: Optional[List[planner_plan.PlannerPlan]]
        """
        return self._plans

    @plans.setter
    def plans(self,value: Optional[List[planner_plan.PlannerPlan]] = None) -> None:
        """
        Sets the plans property value. Read-only. Nullable. Returns the plannerTasks assigned to the user.
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
        if not writer:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("plans", self.plans)
        writer.write_collection_of_object_values("tasks", self.tasks)

    @property
    def tasks(self,) -> Optional[List[planner_task.PlannerTask]]:
        """
        Gets the tasks property value. Read-only. Nullable. Returns the plannerPlans shared with the user.
        Returns: Optional[List[planner_task.PlannerTask]]
        """
        return self._tasks

    @tasks.setter
    def tasks(self,value: Optional[List[planner_task.PlannerTask]] = None) -> None:
        """
        Sets the tasks property value. Read-only. Nullable. Returns the plannerPlans shared with the user.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value


