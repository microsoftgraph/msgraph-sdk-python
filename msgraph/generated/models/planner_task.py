from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
identity_set = lazy_import('msgraph.generated.models.identity_set')
planner_applied_categories = lazy_import('msgraph.generated.models.planner_applied_categories')
planner_assigned_to_task_board_task_format = lazy_import('msgraph.generated.models.planner_assigned_to_task_board_task_format')
planner_assignments = lazy_import('msgraph.generated.models.planner_assignments')
planner_bucket_task_board_task_format = lazy_import('msgraph.generated.models.planner_bucket_task_board_task_format')
planner_preview_type = lazy_import('msgraph.generated.models.planner_preview_type')
planner_progress_task_board_task_format = lazy_import('msgraph.generated.models.planner_progress_task_board_task_format')
planner_task_details = lazy_import('msgraph.generated.models.planner_task_details')

class PlannerTask(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def active_checklist_item_count(self,) -> Optional[int]:
        """
        Gets the activeChecklistItemCount property value. Number of checklist items with value set to false, representing incomplete items.
        Returns: Optional[int]
        """
        return self._active_checklist_item_count
    
    @active_checklist_item_count.setter
    def active_checklist_item_count(self,value: Optional[int] = None) -> None:
        """
        Sets the activeChecklistItemCount property value. Number of checklist items with value set to false, representing incomplete items.
        Args:
            value: Value to set for the activeChecklistItemCount property.
        """
        self._active_checklist_item_count = value
    
    @property
    def applied_categories(self,) -> Optional[planner_applied_categories.PlannerAppliedCategories]:
        """
        Gets the appliedCategories property value. The categories to which the task has been applied. See applied Categories for possible values.
        Returns: Optional[planner_applied_categories.PlannerAppliedCategories]
        """
        return self._applied_categories
    
    @applied_categories.setter
    def applied_categories(self,value: Optional[planner_applied_categories.PlannerAppliedCategories] = None) -> None:
        """
        Sets the appliedCategories property value. The categories to which the task has been applied. See applied Categories for possible values.
        Args:
            value: Value to set for the appliedCategories property.
        """
        self._applied_categories = value
    
    @property
    def assigned_to_task_board_format(self,) -> Optional[planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat]:
        """
        Gets the assignedToTaskBoardFormat property value. Read-only. Nullable. Used to render the task correctly in the task board view when grouped by assignedTo.
        Returns: Optional[planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat]
        """
        return self._assigned_to_task_board_format
    
    @assigned_to_task_board_format.setter
    def assigned_to_task_board_format(self,value: Optional[planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat] = None) -> None:
        """
        Sets the assignedToTaskBoardFormat property value. Read-only. Nullable. Used to render the task correctly in the task board view when grouped by assignedTo.
        Args:
            value: Value to set for the assignedToTaskBoardFormat property.
        """
        self._assigned_to_task_board_format = value
    
    @property
    def assignee_priority(self,) -> Optional[str]:
        """
        Gets the assigneePriority property value. Hint used to order items of this type in a list view. The format is defined as outlined here.
        Returns: Optional[str]
        """
        return self._assignee_priority
    
    @assignee_priority.setter
    def assignee_priority(self,value: Optional[str] = None) -> None:
        """
        Sets the assigneePriority property value. Hint used to order items of this type in a list view. The format is defined as outlined here.
        Args:
            value: Value to set for the assigneePriority property.
        """
        self._assignee_priority = value
    
    @property
    def assignments(self,) -> Optional[planner_assignments.PlannerAssignments]:
        """
        Gets the assignments property value. The set of assignees the task is assigned to.
        Returns: Optional[planner_assignments.PlannerAssignments]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[planner_assignments.PlannerAssignments] = None) -> None:
        """
        Sets the assignments property value. The set of assignees the task is assigned to.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def bucket_id(self,) -> Optional[str]:
        """
        Gets the bucketId property value. Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.
        Returns: Optional[str]
        """
        return self._bucket_id
    
    @bucket_id.setter
    def bucket_id(self,value: Optional[str] = None) -> None:
        """
        Sets the bucketId property value. Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.
        Args:
            value: Value to set for the bucketId property.
        """
        self._bucket_id = value
    
    @property
    def bucket_task_board_format(self,) -> Optional[planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat]:
        """
        Gets the bucketTaskBoardFormat property value. Read-only. Nullable. Used to render the task correctly in the task board view when grouped by bucket.
        Returns: Optional[planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat]
        """
        return self._bucket_task_board_format
    
    @bucket_task_board_format.setter
    def bucket_task_board_format(self,value: Optional[planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat] = None) -> None:
        """
        Sets the bucketTaskBoardFormat property value. Read-only. Nullable. Used to render the task correctly in the task board view when grouped by bucket.
        Args:
            value: Value to set for the bucketTaskBoardFormat property.
        """
        self._bucket_task_board_format = value
    
    @property
    def checklist_item_count(self,) -> Optional[int]:
        """
        Gets the checklistItemCount property value. Number of checklist items that are present on the task.
        Returns: Optional[int]
        """
        return self._checklist_item_count
    
    @checklist_item_count.setter
    def checklist_item_count(self,value: Optional[int] = None) -> None:
        """
        Sets the checklistItemCount property value. Number of checklist items that are present on the task.
        Args:
            value: Value to set for the checklistItemCount property.
        """
        self._checklist_item_count = value
    
    @property
    def completed_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the completedBy property value. Identity of the user that completed the task.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._completed_by
    
    @completed_by.setter
    def completed_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the completedBy property value. Identity of the user that completed the task.
        Args:
            value: Value to set for the completedBy property.
        """
        self._completed_by = value
    
    @property
    def completed_date_time(self,) -> Optional[datetime]:
        """
        Gets the completedDateTime property value. Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._completed_date_time
    
    @completed_date_time.setter
    def completed_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the completedDateTime property value. Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the completedDateTime property.
        """
        self._completed_date_time = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new plannerTask and sets the default values.
        """
        super().__init__()
        # Number of checklist items with value set to false, representing incomplete items.
        self._active_checklist_item_count: Optional[int] = None
        # The categories to which the task has been applied. See applied Categories for possible values.
        self._applied_categories: Optional[planner_applied_categories.PlannerAppliedCategories] = None
        # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by assignedTo.
        self._assigned_to_task_board_format: Optional[planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat] = None
        # Hint used to order items of this type in a list view. The format is defined as outlined here.
        self._assignee_priority: Optional[str] = None
        # The set of assignees the task is assigned to.
        self._assignments: Optional[planner_assignments.PlannerAssignments] = None
        # Bucket ID to which the task belongs. The bucket needs to be in the plan that the task is in. It is 28 characters long and case-sensitive. Format validation is done on the service.
        self._bucket_id: Optional[str] = None
        # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by bucket.
        self._bucket_task_board_format: Optional[planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat] = None
        # Number of checklist items that are present on the task.
        self._checklist_item_count: Optional[int] = None
        # Identity of the user that completed the task.
        self._completed_by: Optional[identity_set.IdentitySet] = None
        # Read-only. Date and time at which the 'percentComplete' of the task is set to '100'. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._completed_date_time: Optional[datetime] = None
        # Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.
        self._conversation_thread_id: Optional[str] = None
        # Identity of the user that created the task.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._created_date_time: Optional[datetime] = None
        # Read-only. Nullable. Additional details about the task.
        self._details: Optional[planner_task_details.PlannerTaskDetails] = None
        # Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._due_date_time: Optional[datetime] = None
        # Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.
        self._has_description: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Hint used to order items of this type in a list view. The format is defined as outlined here.
        self._order_hint: Optional[str] = None
        # Percentage of task completion. When set to 100, the task is considered completed.
        self._percent_complete: Optional[int] = None
        # Plan ID to which the task belongs.
        self._plan_id: Optional[str] = None
        # This sets the type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference.
        self._preview_type: Optional[planner_preview_type.PlannerPreviewType] = None
        # Priority of the task. The valid range of values is between 0 and 10, with the increasing value being lower priority (0 has the highest priority and 10 has the lowest priority).  Currently, Planner interprets values 0 and 1 as 'urgent', 2, 3 and 4 as 'important', 5, 6, and 7 as 'medium', and 8, 9, and 10 as 'low'.  Additionally, Planner sets the value 1 for 'urgent', 3 for 'important', 5 for 'medium', and 9 for 'low'.
        self._priority: Optional[int] = None
        # Read-only. Nullable. Used to render the task correctly in the task board view when grouped by progress.
        self._progress_task_board_format: Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat] = None
        # Number of external references that exist on the task.
        self._reference_count: Optional[int] = None
        # Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        self._start_date_time: Optional[datetime] = None
        # Title of the task.
        self._title: Optional[str] = None
    
    @property
    def conversation_thread_id(self,) -> Optional[str]:
        """
        Gets the conversationThreadId property value. Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.
        Returns: Optional[str]
        """
        return self._conversation_thread_id
    
    @conversation_thread_id.setter
    def conversation_thread_id(self,value: Optional[str] = None) -> None:
        """
        Sets the conversationThreadId property value. Thread ID of the conversation on the task. This is the ID of the conversation thread object created in the group.
        Args:
            value: Value to set for the conversationThreadId property.
        """
        self._conversation_thread_id = value
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity of the user that created the task.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user that created the task.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Read-only. Date and time at which the task is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PlannerTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PlannerTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PlannerTask()
    
    @property
    def details(self,) -> Optional[planner_task_details.PlannerTaskDetails]:
        """
        Gets the details property value. Read-only. Nullable. Additional details about the task.
        Returns: Optional[planner_task_details.PlannerTaskDetails]
        """
        return self._details
    
    @details.setter
    def details(self,value: Optional[planner_task_details.PlannerTaskDetails] = None) -> None:
        """
        Sets the details property value. Read-only. Nullable. Additional details about the task.
        Args:
            value: Value to set for the details property.
        """
        self._details = value
    
    @property
    def due_date_time(self,) -> Optional[datetime]:
        """
        Gets the dueDateTime property value. Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._due_date_time
    
    @due_date_time.setter
    def due_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the dueDateTime property value. Date and time at which the task is due. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the dueDateTime property.
        """
        self._due_date_time = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "active_checklist_item_count": lambda n : setattr(self, 'active_checklist_item_count', n.get_int_value()),
            "applied_categories": lambda n : setattr(self, 'applied_categories', n.get_object_value(planner_applied_categories.PlannerAppliedCategories)),
            "assigned_to_task_board_format": lambda n : setattr(self, 'assigned_to_task_board_format', n.get_object_value(planner_assigned_to_task_board_task_format.PlannerAssignedToTaskBoardTaskFormat)),
            "assignee_priority": lambda n : setattr(self, 'assignee_priority', n.get_str_value()),
            "assignments": lambda n : setattr(self, 'assignments', n.get_object_value(planner_assignments.PlannerAssignments)),
            "bucket_id": lambda n : setattr(self, 'bucket_id', n.get_str_value()),
            "bucket_task_board_format": lambda n : setattr(self, 'bucket_task_board_format', n.get_object_value(planner_bucket_task_board_task_format.PlannerBucketTaskBoardTaskFormat)),
            "checklist_item_count": lambda n : setattr(self, 'checklist_item_count', n.get_int_value()),
            "completed_by": lambda n : setattr(self, 'completed_by', n.get_object_value(identity_set.IdentitySet)),
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "conversation_thread_id": lambda n : setattr(self, 'conversation_thread_id', n.get_str_value()),
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "details": lambda n : setattr(self, 'details', n.get_object_value(planner_task_details.PlannerTaskDetails)),
            "due_date_time": lambda n : setattr(self, 'due_date_time', n.get_datetime_value()),
            "has_description": lambda n : setattr(self, 'has_description', n.get_bool_value()),
            "order_hint": lambda n : setattr(self, 'order_hint', n.get_str_value()),
            "percent_complete": lambda n : setattr(self, 'percent_complete', n.get_int_value()),
            "plan_id": lambda n : setattr(self, 'plan_id', n.get_str_value()),
            "preview_type": lambda n : setattr(self, 'preview_type', n.get_enum_value(planner_preview_type.PlannerPreviewType)),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "progress_task_board_format": lambda n : setattr(self, 'progress_task_board_format', n.get_object_value(planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat)),
            "reference_count": lambda n : setattr(self, 'reference_count', n.get_int_value()),
            "start_date_time": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def has_description(self,) -> Optional[bool]:
        """
        Gets the hasDescription property value. Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.
        Returns: Optional[bool]
        """
        return self._has_description
    
    @has_description.setter
    def has_description(self,value: Optional[bool] = None) -> None:
        """
        Sets the hasDescription property value. Read-only. Value is true if the details object of the task has a non-empty description and false otherwise.
        Args:
            value: Value to set for the hasDescription property.
        """
        self._has_description = value
    
    @property
    def order_hint(self,) -> Optional[str]:
        """
        Gets the orderHint property value. Hint used to order items of this type in a list view. The format is defined as outlined here.
        Returns: Optional[str]
        """
        return self._order_hint
    
    @order_hint.setter
    def order_hint(self,value: Optional[str] = None) -> None:
        """
        Sets the orderHint property value. Hint used to order items of this type in a list view. The format is defined as outlined here.
        Args:
            value: Value to set for the orderHint property.
        """
        self._order_hint = value
    
    @property
    def percent_complete(self,) -> Optional[int]:
        """
        Gets the percentComplete property value. Percentage of task completion. When set to 100, the task is considered completed.
        Returns: Optional[int]
        """
        return self._percent_complete
    
    @percent_complete.setter
    def percent_complete(self,value: Optional[int] = None) -> None:
        """
        Sets the percentComplete property value. Percentage of task completion. When set to 100, the task is considered completed.
        Args:
            value: Value to set for the percentComplete property.
        """
        self._percent_complete = value
    
    @property
    def plan_id(self,) -> Optional[str]:
        """
        Gets the planId property value. Plan ID to which the task belongs.
        Returns: Optional[str]
        """
        return self._plan_id
    
    @plan_id.setter
    def plan_id(self,value: Optional[str] = None) -> None:
        """
        Sets the planId property value. Plan ID to which the task belongs.
        Args:
            value: Value to set for the planId property.
        """
        self._plan_id = value
    
    @property
    def preview_type(self,) -> Optional[planner_preview_type.PlannerPreviewType]:
        """
        Gets the previewType property value. This sets the type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference.
        Returns: Optional[planner_preview_type.PlannerPreviewType]
        """
        return self._preview_type
    
    @preview_type.setter
    def preview_type(self,value: Optional[planner_preview_type.PlannerPreviewType] = None) -> None:
        """
        Sets the previewType property value. This sets the type of preview that shows up on the task. The possible values are: automatic, noPreview, checklist, description, reference.
        Args:
            value: Value to set for the previewType property.
        """
        self._preview_type = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. Priority of the task. The valid range of values is between 0 and 10, with the increasing value being lower priority (0 has the highest priority and 10 has the lowest priority).  Currently, Planner interprets values 0 and 1 as 'urgent', 2, 3 and 4 as 'important', 5, 6, and 7 as 'medium', and 8, 9, and 10 as 'low'.  Additionally, Planner sets the value 1 for 'urgent', 3 for 'important', 5 for 'medium', and 9 for 'low'.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. Priority of the task. The valid range of values is between 0 and 10, with the increasing value being lower priority (0 has the highest priority and 10 has the lowest priority).  Currently, Planner interprets values 0 and 1 as 'urgent', 2, 3 and 4 as 'important', 5, 6, and 7 as 'medium', and 8, 9, and 10 as 'low'.  Additionally, Planner sets the value 1 for 'urgent', 3 for 'important', 5 for 'medium', and 9 for 'low'.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    @property
    def progress_task_board_format(self,) -> Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat]:
        """
        Gets the progressTaskBoardFormat property value. Read-only. Nullable. Used to render the task correctly in the task board view when grouped by progress.
        Returns: Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat]
        """
        return self._progress_task_board_format
    
    @progress_task_board_format.setter
    def progress_task_board_format(self,value: Optional[planner_progress_task_board_task_format.PlannerProgressTaskBoardTaskFormat] = None) -> None:
        """
        Sets the progressTaskBoardFormat property value. Read-only. Nullable. Used to render the task correctly in the task board view when grouped by progress.
        Args:
            value: Value to set for the progressTaskBoardFormat property.
        """
        self._progress_task_board_format = value
    
    @property
    def reference_count(self,) -> Optional[int]:
        """
        Gets the referenceCount property value. Number of external references that exist on the task.
        Returns: Optional[int]
        """
        return self._reference_count
    
    @reference_count.setter
    def reference_count(self,value: Optional[int] = None) -> None:
        """
        Sets the referenceCount property value. Number of external references that exist on the task.
        Args:
            value: Value to set for the referenceCount property.
        """
        self._reference_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. Date and time at which the task starts. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z
        Args:
            value: Value to set for the startDateTime property.
        """
        self._start_date_time = value
    
    @property
    def title(self,) -> Optional[str]:
        """
        Gets the title property value. Title of the task.
        Returns: Optional[str]
        """
        return self._title
    
    @title.setter
    def title(self,value: Optional[str] = None) -> None:
        """
        Sets the title property value. Title of the task.
        Args:
            value: Value to set for the title property.
        """
        self._title = value
    

