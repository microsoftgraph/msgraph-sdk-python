from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..user import User
    from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
    from .run import Run
    from .task_processing_result import TaskProcessingResult
    from .workflow_execution_type import WorkflowExecutionType

from ..entity import Entity

@dataclass
class UserProcessingResult(Entity, Parsable):
    # The date time that the workflow execution for a user completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    completed_date_time: Optional[datetime.datetime] = None
    # The number of tasks that failed in the workflow execution.
    failed_tasks_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingStatus property
    processing_status: Optional[LifecycleWorkflowProcessingStatus] = None
    # The related reprocessed workflow run.
    reprocessed_runs: Optional[list[Run]] = None
    # The date time that the workflow is scheduled to be executed for a user.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    scheduled_date_time: Optional[datetime.datetime] = None
    # The date time that the workflow execution started. Value is null if the workflow execution hasn't started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    started_date_time: Optional[datetime.datetime] = None
    # The subject property
    subject: Optional[User] = None
    # The associated individual task execution.
    task_processing_results: Optional[list[TaskProcessingResult]] = None
    # The total number of tasks that in the workflow execution.
    total_tasks_count: Optional[int] = None
    # The total number of unprocessed tasks for the workflow.
    total_unprocessed_tasks_count: Optional[int] = None
    # The workflowExecutionType property
    workflow_execution_type: Optional[WorkflowExecutionType] = None
    # The version of the workflow that was executed.
    workflow_version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserProcessingResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserProcessingResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserProcessingResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..user import User
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .run import Run
        from .task_processing_result import TaskProcessingResult
        from .workflow_execution_type import WorkflowExecutionType

        from ..entity import Entity
        from ..user import User
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .run import Run
        from .task_processing_result import TaskProcessingResult
        from .workflow_execution_type import WorkflowExecutionType

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "failedTasksCount": lambda n : setattr(self, 'failed_tasks_count', n.get_int_value()),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(LifecycleWorkflowProcessingStatus)),
            "reprocessedRuns": lambda n : setattr(self, 'reprocessed_runs', n.get_collection_of_object_values(Run)),
            "scheduledDateTime": lambda n : setattr(self, 'scheduled_date_time', n.get_datetime_value()),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(User)),
            "taskProcessingResults": lambda n : setattr(self, 'task_processing_results', n.get_collection_of_object_values(TaskProcessingResult)),
            "totalTasksCount": lambda n : setattr(self, 'total_tasks_count', n.get_int_value()),
            "totalUnprocessedTasksCount": lambda n : setattr(self, 'total_unprocessed_tasks_count', n.get_int_value()),
            "workflowExecutionType": lambda n : setattr(self, 'workflow_execution_type', n.get_enum_value(WorkflowExecutionType)),
            "workflowVersion": lambda n : setattr(self, 'workflow_version', n.get_int_value()),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_int_value("failedTasksCount", self.failed_tasks_count)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_collection_of_object_values("reprocessedRuns", self.reprocessed_runs)
        writer.write_datetime_value("scheduledDateTime", self.scheduled_date_time)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_object_value("subject", self.subject)
        writer.write_collection_of_object_values("taskProcessingResults", self.task_processing_results)
        writer.write_int_value("totalTasksCount", self.total_tasks_count)
        writer.write_int_value("totalUnprocessedTasksCount", self.total_unprocessed_tasks_count)
        writer.write_enum_value("workflowExecutionType", self.workflow_execution_type)
        writer.write_int_value("workflowVersion", self.workflow_version)
    

