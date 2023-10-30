from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
    from .task_processing_result import TaskProcessingResult
    from .user_processing_result import UserProcessingResult
    from .workflow_execution_type import WorkflowExecutionType

from ..entity import Entity

@dataclass
class Run(Entity):
    # The date time that the run completed. Value is null if the workflow hasn't completed.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    completed_date_time: Optional[datetime.datetime] = None
    # The number of tasks that failed in the run execution.
    failed_tasks_count: Optional[int] = None
    # The number of users that failed in the run execution.
    failed_users_count: Optional[int] = None
    # The datetime that the run was last updated.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    last_updated_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingStatus property
    processing_status: Optional[LifecycleWorkflowProcessingStatus] = None
    # The date time that the run is scheduled to be executed for a workflow.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    scheduled_date_time: Optional[datetime.datetime] = None
    # The date time that the run execution started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    started_date_time: Optional[datetime.datetime] = None
    # The number of successfully completed users in the run.
    successful_users_count: Optional[int] = None
    # The related taskProcessingResults.
    task_processing_results: Optional[List[TaskProcessingResult]] = None
    # The totalTasksCount property
    total_tasks_count: Optional[int] = None
    # The total number of unprocessed tasks in the run execution.
    total_unprocessed_tasks_count: Optional[int] = None
    # The total number of users in the workflow execution.
    total_users_count: Optional[int] = None
    # The associated individual user execution.
    user_processing_results: Optional[List[UserProcessingResult]] = None
    # The workflowExecutionType property
    workflow_execution_type: Optional[WorkflowExecutionType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Run:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Run
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Run()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .task_processing_result import TaskProcessingResult
        from .user_processing_result import UserProcessingResult
        from .workflow_execution_type import WorkflowExecutionType

        from ..entity import Entity
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .task_processing_result import TaskProcessingResult
        from .user_processing_result import UserProcessingResult
        from .workflow_execution_type import WorkflowExecutionType

        fields: Dict[str, Callable[[Any], None]] = {
            "completed_date_time": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "failed_tasks_count": lambda n : setattr(self, 'failed_tasks_count', n.get_int_value()),
            "failed_users_count": lambda n : setattr(self, 'failed_users_count', n.get_int_value()),
            "last_updated_date_time": lambda n : setattr(self, 'last_updated_date_time', n.get_datetime_value()),
            "processing_status": lambda n : setattr(self, 'processing_status', n.get_enum_value(LifecycleWorkflowProcessingStatus)),
            "scheduled_date_time": lambda n : setattr(self, 'scheduled_date_time', n.get_datetime_value()),
            "started_date_time": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "successful_users_count": lambda n : setattr(self, 'successful_users_count', n.get_int_value()),
            "task_processing_results": lambda n : setattr(self, 'task_processing_results', n.get_collection_of_object_values(TaskProcessingResult)),
            "total_tasks_count": lambda n : setattr(self, 'total_tasks_count', n.get_int_value()),
            "total_unprocessed_tasks_count": lambda n : setattr(self, 'total_unprocessed_tasks_count', n.get_int_value()),
            "total_users_count": lambda n : setattr(self, 'total_users_count', n.get_int_value()),
            "user_processing_results": lambda n : setattr(self, 'user_processing_results', n.get_collection_of_object_values(UserProcessingResult)),
            "workflow_execution_type": lambda n : setattr(self, 'workflow_execution_type', n.get_enum_value(WorkflowExecutionType)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_datetime_value("completed_date_time", self.completed_date_time)
        writer.write_int_value("failed_tasks_count", self.failed_tasks_count)
        writer.write_int_value("failed_users_count", self.failed_users_count)
        writer.write_datetime_value("last_updated_date_time", self.last_updated_date_time)
        writer.write_enum_value("processing_status", self.processing_status)
        writer.write_datetime_value("scheduled_date_time", self.scheduled_date_time)
        writer.write_datetime_value("started_date_time", self.started_date_time)
        writer.write_int_value("successful_users_count", self.successful_users_count)
        writer.write_collection_of_object_values("task_processing_results", self.task_processing_results)
        writer.write_int_value("total_tasks_count", self.total_tasks_count)
        writer.write_int_value("total_unprocessed_tasks_count", self.total_unprocessed_tasks_count)
        writer.write_int_value("total_users_count", self.total_users_count)
        writer.write_collection_of_object_values("user_processing_results", self.user_processing_results)
        writer.write_enum_value("workflow_execution_type", self.workflow_execution_type)
    

