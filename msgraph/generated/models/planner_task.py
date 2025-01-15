from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .identity_set import IdentitySet
    from .planner_applied_categories import PlannerAppliedCategories
    from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
    from .planner_assignments import PlannerAssignments
    from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
    from .planner_preview_type import PlannerPreviewType
    from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
    from .planner_task_details import PlannerTaskDetails

from .entity import Entity

@dataclass
class PlannerTask(Entity, Parsable):
    # Number of checklist items with value set to false, representing incomplete items.
    active_checklist_item_count: Optional[int] = None
    # The categories to which the task has been applied. See applied Categories for possible values.
    applied_categories: Optional[PlannerAppliedCategories] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by assignedTo.
    assigned_to_task_board_format: Optional[PlannerAssignedToTaskBoardTaskFormat] = None
    # Hint used to order items of this type in a list view. The format is defined as outlined here.
    assignee_priority: Optional[str] = None
    # The set of assignees the task is assigned to.
    assignments: Optional[PlannerAssignments] = None
    # Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It's 28 characters long and case-sensitive. Format validation is done on the service.
    bucket_id: Optional[str] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by bucket.
    bucket_task_board_format: Optional[PlannerBucketTaskBoardTaskFormat] = None
    # Number of checklist items that are present on the task.
    checklist_item_count: Optional[int] = None
    # Identity of the user that completed the task.
    completed_by: Optional[IdentitySet] = None
    # Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    completed_date_time: Optional[datetime.datetime] = None
    # Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.
    conversation_thread_id: Optional[str] = None
    # Identity of the user that created the task.
    created_by: Optional[IdentitySet] = None
    # Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    created_date_time: Optional[datetime.datetime] = None
    # Read-only. Nullable. More details about the task.
    details: Optional[PlannerTaskDetails] = None
    # Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    due_date_time: Optional[datetime.datetime] = None
    # Read-only. Value is true if the details object of the task has a nonempty description and false otherwise.
    has_description: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Hint used to order items of this type in a list view. The format is defined as outlined here.
    order_hint: Optional[str] = None
    # Percentage of task completion. When set to 100, the task is considered completed.
    percent_complete: Optional[int] = None
    # Plan ID to which the task belongs.
    plan_id: Optional[str] = None
    # This sets the type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference.
    preview_type: Optional[PlannerPreviewType] = None
    # Priority of the task. The valid range of values is between 0 and 10, with the increasing value being lower priority (0 has the highest priority and 10 has the lowest priority).  Currently, Planner interprets values 0 and 1 as 'urgent', 2, 3 and 4 as 'important', 5, 6, and 7 as 'medium', and 8, 9, and 10 as 'low'.  Additionally, Planner sets the value 1 for 'urgent', 3 for 'important', 5 for 'medium', and 9 for 'low'.
    priority: Optional[int] = None
    # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by progress.
    progress_task_board_format: Optional[PlannerProgressTaskBoardTaskFormat] = None
    # Number of external references that exist on the task.
    reference_count: Optional[int] = None
    # Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
    start_date_time: Optional[datetime.datetime] = None
    # Title of the task.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PlannerTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PlannerTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .identity_set import IdentitySet
        from .planner_applied_categories import PlannerAppliedCategories
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_assignments import PlannerAssignments
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_preview_type import PlannerPreviewType
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task_details import PlannerTaskDetails

        from .entity import Entity
        from .identity_set import IdentitySet
        from .planner_applied_categories import PlannerAppliedCategories
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_assignments import PlannerAssignments
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_preview_type import PlannerPreviewType
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task_details import PlannerTaskDetails

        fields: dict[str, Callable[[Any], None]] = {
            "activeChecklistItemCount": lambda n : setattr(self, 'active_checklist_item_count', n.get_int_value()),
            "appliedCategories": lambda n : setattr(self, 'applied_categories', n.get_object_value(PlannerAppliedCategories)),
            "assignedToTaskBoardFormat": lambda n : setattr(self, 'assigned_to_task_board_format', n.get_object_value(PlannerAssignedToTaskBoardTaskFormat)),
            "assigneePriority": lambda n : setattr(self, 'assignee_priority', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_object_value(PlannerAssignments)),
            "bucketId": lambda n : setattr(self, 'bucket_id', n.get_str_value()),
            "bucketTaskBoardFormat": lambda n : setattr(self, 'bucket_task_board_format', n.get_object_value(PlannerBucketTaskBoardTaskFormat)),
            "checklistItemCount": lambda n : setattr(self, 'checklist_item_count', n.get_int_value()),
            "completedBy": lambda n : setattr(self, 'completed_by', n.get_object_value(IdentitySet)),
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "conversationThreadId": lambda n : setattr(self, 'conversation_thread_id', n.get_str_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(PlannerTaskDetails)),
            "dueDateTime": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "hasDescription": lambda n : setattr(self, 'has_description', n.get_bool_value()),
            "orderHint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "planId": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "previewType": lambda n : setattr(self, 'preview_type', n.get_enum_value(PlannerPreviewType)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "progressTaskBoardFormat": lambda n : setattr(self, 'progress_task_board_format', n.get_object_value(PlannerProgressTaskBoardTaskFormat)),
            "referenceCount": lambda n : setattr(self, 'reference_count', n.get_int_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_int_value("activeChecklistItemCount", self.active_checklist_item_count)
        writer.write_object_value("appliedCategories", self.applied_categories)
        writer.write_object_value("assignedToTaskBoardFormat", self.assigned_to_task_board_format)
        writer.write_str_value("assigneePriority", self.assignee_priority)
        writer.write_object_value("assignments", self.assignments)
        writer.write_str_value("bucketId", self.bucket_id)
        writer.write_object_value("bucketTaskBoardFormat", self.bucket_task_board_format)
        writer.write_int_value("checklistItemCount", self.checklist_item_count)
        writer.write_object_value("completedBy", self.completed_by)
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_str_value("conversationThreadId", self.conversation_thread_id)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("details", self.details)
        writer.write_datetime_value("dueDateTime", self.due_date_time)
        writer.write_bool_value("hasDescription", self.has_description)
        writer.write_str_value("orderHint", self.order_hint)
        writer.write_int_value("percentComplete", self.percent_complete)
        writer.write_str_value("planId", self.plan_id)
        writer.write_enum_value("previewType", self.preview_type)
        writer.write_int_value("priority", self.priority)
        writer.write_object_value("progressTaskBoardFormat", self.progress_task_board_format)
        writer.write_int_value("referenceCount", self.reference_count)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("title", self.title)
    

