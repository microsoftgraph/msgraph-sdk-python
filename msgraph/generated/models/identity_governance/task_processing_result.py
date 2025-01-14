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
    from .task import Task

from ..entity import Entity

@dataclass
class TaskProcessingResult(Entity, Parsable):
    # The date time when taskProcessingResult execution ended. Value is null if task execution is still in progress.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    completed_date_time: Optional[datetime.datetime] = None
    # The date time when the taskProcessingResult was created.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    created_date_time: Optional[datetime.datetime] = None
    # Describes why the taskProcessingResult has failed.
    failure_reason: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The processingStatus property
    processing_status: Optional[LifecycleWorkflowProcessingStatus] = None
    # The date time when taskProcessingResult execution started. Value is null if task execution has not yet started.Supports $filter(lt, le, gt, ge, eq, ne) and $orderby.
    started_date_time: Optional[datetime.datetime] = None
    # The subject property
    subject: Optional[User] = None
    # The task property
    task: Optional[Task] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TaskProcessingResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TaskProcessingResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TaskProcessingResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..user import User
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .task import Task

        from ..entity import Entity
        from ..user import User
        from .lifecycle_workflow_processing_status import LifecycleWorkflowProcessingStatus
        from .task import Task

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "failureReason": lambda n : setattr(self, 'failure_reason', n.get_str_value()),
            "processingStatus": lambda n : setattr(self, 'processing_status', n.get_enum_value(LifecycleWorkflowProcessingStatus)),
            "startedDateTime": lambda n : setattr(self, 'started_date_time', n.get_datetime_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(User)),
            "task": lambda n : setattr(self, 'task', n.get_object_value(Task)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("failureReason", self.failure_reason)
        writer.write_enum_value("processingStatus", self.processing_status)
        writer.write_datetime_value("startedDateTime", self.started_date_time)
        writer.write_object_value("subject", self.subject)
        writer.write_object_value("task", self.task)
    

