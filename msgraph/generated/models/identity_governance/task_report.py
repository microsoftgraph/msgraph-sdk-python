from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
    from .task import Task
    from .task_definition import TaskDefinition
    from .task_processing_result import TaskProcessingResult

from ..entity import Entity

@dataclass
class TaskReport(Entity, Parsable):
    # The date time that the associated run completed. Value is null if the run has not completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    completed_date_time: Optional[datetime.datetime] = None
    # The number of users in the run execution for which the associated task failed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    failed_users_count: Optional[int] = None
    # The date and time that the task report was last updated.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingStatus property
    processing_status: Optional[LifecycleWorkflowProcessingStatus] = None
    # The unique identifier of the associated run.
    run_id: Optional[str] = None
    # The date time that the associated run started. Value is null if the run has not started.
    started_date_time: Optional[datetime.datetime] = None
    # The number of users in the run execution for which the associated task succeeded.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    successful_users_count: Optional[int] = None
    # The task property
    task: Optional[Task] = None
    # The taskDefinition property
    task_definition: Optional[TaskDefinition] = None
    # The related lifecycle workflow taskProcessingResults.
    task_processing_results: Optional[list[TaskProcessingResult]] = None
    # The total number of users in the run execution for which the associated task was scheduled to execute.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    total_users_count: Optional[int] = None
    # The number of users in the run execution for which the associated task is queued, in progress, or canceled.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    unprocessed_users_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TaskReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TaskReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TaskReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .task import Task
        from .task_definition import TaskDefinition
        from .task_processing_result import TaskProcessingResult

        from ..entity import Entity
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .task import Task
        from .task_definition import TaskDefinition
        from .task_processing_result import TaskProcessingResult

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "failedUsersCount": lambda n : setattr(self, 'failed_users_count', n.get_int_value()),
            "lastUpdatedDateTime": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(LifecycleWorkflowProcessingStatus)),
            "runId": lambda n : setattr(self, 'run_id', n.get_str_value()),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "successfulUsersCount": lambda n : setattr(self, 'successful_users_count', n.get_int_value()),
            "task": lambda n : setattr(self, 'task', n.get_object_value(Task)),
            "taskDefinition": lambda n : setattr(self, 'task_definition', n.get_object_value(TaskDefinition)),
            "taskProcessingResults": lambda n : setattr(self, 'task_processing_results', n.get_collection_of_object_values(TaskProcessingResult)),
            "totalUsersCount": lambda n : setattr(self, 'total_users_count', n.get_int_value()),
            "unprocessedUsersCount": lambda n : setattr(self, 'unprocessed_users_count', n.get_int_value()),
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
        writer.write_int_value("failedUsersCount", self.failed_users_count)
        writer.write_datetime_value("lastUpdatedDateTime", self.last_updated_date_time)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_str_value("runId", self.run_id)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_int_value("successfulUsersCount", self.successful_users_count)
        writer.write_object_value("task", self.task)
        writer.write_object_value("taskDefinition", self.task_definition)
        writer.write_collection_of_object_values("taskProcessingResults", self.task_processing_results)
        writer.write_int_value("totalUsersCount", self.total_users_count)
        writer.write_int_value("unprocessedUsersCount", self.unprocessed_users_count)
    

