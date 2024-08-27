from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..custom_extension_data import CustomExtensionData
    from ..user import User
    from .task import Task
    from .task_processing_result import TaskProcessingResult
    from .workflow import Workflow

from ..custom_extension_data import CustomExtensionData

@dataclass
class CustomTaskExtensionCalloutData(CustomExtensionData):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.customTaskExtensionCalloutData"
    # The subject property
    subject: Optional[User] = None
    # The task property
    task: Optional[Task] = None
    # The taskProcessingresult property
    task_processingresult: Optional[TaskProcessingResult] = None
    # The workflow property
    workflow: Optional[Workflow] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomTaskExtensionCalloutData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomTaskExtensionCalloutData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomTaskExtensionCalloutData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..custom_extension_data import CustomExtensionData
        from ..user import User
        from .task import Task
        from .task_processing_result import TaskProcessingResult
        from .workflow import Workflow

        from ..custom_extension_data import CustomExtensionData
        from ..user import User
        from .task import Task
        from .task_processing_result import TaskProcessingResult
        from .workflow import Workflow

        fields: Dict[str, Callable[[Any], None]] = {
            "subject": lambda n : setattr(self, 'subject', n.get_object_value(User)),
            "task": lambda n : setattr(self, 'task', n.get_object_value(Task)),
            "taskProcessingresult": lambda n : setattr(self, 'task_processingresult', n.get_object_value(TaskProcessingResult)),
            "workflow": lambda n : setattr(self, 'workflow', n.get_object_value(Workflow)),
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
        writer.write_object_value("subject", self.subject)
        writer.write_object_value("task", self.task)
        writer.write_object_value("taskProcessingresult", self.task_processingresult)
        writer.write_object_value("workflow", self.workflow)
    

