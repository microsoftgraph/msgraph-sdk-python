from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .planner_bucket import PlannerBucket
    from .planner_plan_container import PlannerPlanContainer
    from .planner_plan_details import PlannerPlanDetails
    from .planner_task import PlannerTask

from .entity import Entity

@dataclass
class PlannerPlan(Entity, Parsable):
    # Read-only. Nullable. Collection of buckets in the plan.
    buckets: Optional[list[PlannerBucket]] = None
    # Identifies the container of the plan. Specify only the url, the containerId and type, or all properties. After it's set, this property can’t be updated. Required.
    container: Optional[PlannerPlanContainer] = None
    # Read-only. The user who created the plan.
    created_by: Optional[IdentitySet] = None
    # Read-only. Date and time at which the plan is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # Read-only. Nullable. Extra details about the plan.
    details: Optional[PlannerPlanDetails] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Use the container property instead. ID of the group that owns the plan. After it's set, this property can’t be updated. This property won't return a valid group ID if the container of the plan isn't a group.
    owner: Optional[str] = None
    # Read-only. Nullable. Collection of tasks in the plan.
    tasks: Optional[list[PlannerTask]] = None
    # Required. Title of the plan.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerPlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerPlan
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerPlan()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .planner_bucket import PlannerBucket
        from .planner_plan_container import PlannerPlanContainer
        from .planner_plan_details import PlannerPlanDetails
        from .planner_task import PlannerTask

        from .entity import Entity
        from .identity_set import IdentitySet
        from .planner_bucket import PlannerBucket
        from .planner_plan_container import PlannerPlanContainer
        from .planner_plan_details import PlannerPlanDetails
        from .planner_task import PlannerTask

        fields: dict[str, Callable[[Any], None]] = {
            "buckets": lambda n : setattr(self, 'buckets', n.get_collection_of_object_values(PlannerBucket)),
            "container": lambda n : setattr(self, 'container', n.get_object_value(PlannerPlanContainer)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(PlannerPlanDetails)),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PlannerTask)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_collection_of_object_values("buckets", self.buckets)
        writer.write_object_value("container", self.container)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("details", self.details)
        writer.write_str_value("owner", self.owner)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_str_value("title", self.title)
    

