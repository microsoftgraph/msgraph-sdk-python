from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .lifecycle_workflow_category import LifecycleWorkflowCategory
    from .task import Task
    from .workflow_execution_conditions import WorkflowExecutionConditions

from ..entity import Entity

@dataclass
class WorkflowTemplate(Entity):
    # The category property
    category: Optional[LifecycleWorkflowCategory] = None
    # The description of the workflowTemplate.
    description: Optional[str] = None
    # The display name of the workflowTemplate.Supports $filter(eq, ne) and $orderby.
    display_name: Optional[str] = None
    # Conditions describing when to execute the workflow and the criteria to identify in-scope subject set.
    execution_conditions: Optional[WorkflowExecutionConditions] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the configured tasks to execute and their execution sequence within a workflow. This relationship is expanded by default.
    tasks: Optional[List[Task]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkflowTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkflowTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkflowTemplate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .lifecycle_workflow_category import LifecycleWorkflowCategory
        from .task import Task
        from .workflow_execution_conditions import WorkflowExecutionConditions

        from ..entity import Entity
        from .lifecycle_workflow_category import LifecycleWorkflowCategory
        from .task import Task
        from .workflow_execution_conditions import WorkflowExecutionConditions

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(LifecycleWorkflowCategory)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "executionConditions": lambda n : setattr(self, 'execution_conditions', n.get_object_value(WorkflowExecutionConditions)),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(Task)),
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
        writer.write_enum_value("category", self.category)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("executionConditions", self.execution_conditions)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

