from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..deleted_item_container import DeletedItemContainer
    from ..entity import Entity
    from .custom_task_extension import CustomTaskExtension
    from .lifecycle_management_settings import LifecycleManagementSettings
    from .task_definition import TaskDefinition
    from .workflow import Workflow
    from .workflow_template import WorkflowTemplate

from ..entity import Entity

@dataclass
class LifecycleWorkflowsContainer(Entity):
    # The customTaskExtension instance.
    custom_task_extensions: Optional[List[CustomTaskExtension]] = None
    # Deleted workflows in your lifecycle workflows instance.
    deleted_items: Optional[DeletedItemContainer] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The settings property
    settings: Optional[LifecycleManagementSettings] = None
    # The definition of tasks within the lifecycle workflows instance.
    task_definitions: Optional[List[TaskDefinition]] = None
    # The workflow templates in the lifecycle workflow instance.
    workflow_templates: Optional[List[WorkflowTemplate]] = None
    # The workflows in the lifecycle workflows instance.
    workflows: Optional[List[Workflow]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LifecycleWorkflowsContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecycleWorkflowsContainer
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LifecycleWorkflowsContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..deleted_item_container import DeletedItemContainer
        from ..entity import Entity
        from .custom_task_extension import CustomTaskExtension
        from .lifecycle_management_settings import LifecycleManagementSettings
        from .task_definition import TaskDefinition
        from .workflow import Workflow
        from .workflow_template import WorkflowTemplate

        from ..deleted_item_container import DeletedItemContainer
        from ..entity import Entity
        from .custom_task_extension import CustomTaskExtension
        from .lifecycle_management_settings import LifecycleManagementSettings
        from .task_definition import TaskDefinition
        from .workflow import Workflow
        from .workflow_template import WorkflowTemplate

        fields: Dict[str, Callable[[Any], None]] = {
            "customTaskExtensions": lambda n : setattr(self, 'custom_task_extensions', n.get_collection_of_object_values(CustomTaskExtension)),
            "deletedItems": lambda n : setattr(self, 'deleted_items', n.get_object_value(DeletedItemContainer)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(LifecycleManagementSettings)),
            "taskDefinitions": lambda n : setattr(self, 'task_definitions', n.get_collection_of_object_values(TaskDefinition)),
            "workflowTemplates": lambda n : setattr(self, 'workflow_templates', n.get_collection_of_object_values(WorkflowTemplate)),
            "workflows": lambda n : setattr(self, 'workflows', n.get_collection_of_object_values(Workflow)),
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
        writer.write_collection_of_object_values("customTaskExtensions", self.custom_task_extensions)
        writer.write_object_value("deletedItems", self.deleted_items)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("taskDefinitions", self.task_definitions)
        writer.write_collection_of_object_values("workflowTemplates", self.workflow_templates)
        writer.write_collection_of_object_values("workflows", self.workflows)
    

