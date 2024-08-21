from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .run import Run
    from .task_report import TaskReport
    from .user_processing_result import UserProcessingResult
    from .workflow_base import WorkflowBase
    from .workflow_version import WorkflowVersion

from .workflow_base import WorkflowBase

@dataclass
class Workflow(WorkflowBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.workflow"
    # When the workflow was deleted.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    deleted_date_time: Optional[datetime.datetime] = None
    # The unique identifier of the Microsoft Entra identity that last modified the workflow object.
    execution_scope: Optional[List[UserProcessingResult]] = None
    # Identifier used for individually addressing a specific workflow.Supports $filter(eq, ne) and $orderby.
    id: Optional[str] = None
    # The date time when the workflow is expected to run next based on the schedule interval, if there are any users matching the execution conditions. Supports $filter(lt,gt) and $orderby.
    next_schedule_run_date_time: Optional[datetime.datetime] = None
    # Workflow runs.
    runs: Optional[List[Run]] = None
    # Represents the aggregation of task execution data for tasks within a workflow object.
    task_reports: Optional[List[TaskReport]] = None
    # Per-user workflow execution results.
    user_processing_results: Optional[List[UserProcessingResult]] = None
    # The current version number of the workflow. Value is 1 when the workflow is first created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    version: Optional[int] = None
    # The workflow versions that are available.
    versions: Optional[List[WorkflowVersion]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Workflow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Workflow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Workflow()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .run import Run
        from .task_report import TaskReport
        from .user_processing_result import UserProcessingResult
        from .workflow_base import WorkflowBase
        from .workflow_version import WorkflowVersion

        from .run import Run
        from .task_report import TaskReport
        from .user_processing_result import UserProcessingResult
        from .workflow_base import WorkflowBase
        from .workflow_version import WorkflowVersion

        fields: Dict[str, Callable[[Any], None]] = {
            "deletedDateTime": lambda n : setattr(self, 'deleted_date_time', n.get_datetime_value()),
            "executionScope": lambda n : setattr(self, 'execution_scope', n.get_collection_of_object_values(UserProcessingResult)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "nextScheduleRunDateTime": lambda n : setattr(self, 'next_schedule_run_date_time', n.get_datetime_value()),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(Run)),
            "taskReports": lambda n : setattr(self, 'task_reports', n.get_collection_of_object_values(TaskReport)),
            "userProcessingResults": lambda n : setattr(self, 'user_processing_results', n.get_collection_of_object_values(UserProcessingResult)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(WorkflowVersion)),
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
        writer.write_datetime_value("deletedDateTime", self.deleted_date_time)
        writer.write_collection_of_object_values("executionScope", self.execution_scope)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("nextScheduleRunDateTime", self.next_schedule_run_date_time)
        writer.write_collection_of_object_values("runs", self.runs)
        writer.write_collection_of_object_values("taskReports", self.task_reports)
        writer.write_collection_of_object_values("userProcessingResults", self.user_processing_results)
        writer.write_int_value("version", self.version)
        writer.write_collection_of_object_values("versions", self.versions)
    

