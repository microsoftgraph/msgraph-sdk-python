from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..user import User
    from .lifecycle_workflow_category import LifecycleWorkflowCategory
    from .task import Task
    from .workflow import Workflow
    from .workflow_execution_conditions import WorkflowExecutionConditions
    from .workflow_version import WorkflowVersion

@dataclass
class WorkflowBase(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The category property
    category: Optional[LifecycleWorkflowCategory] = None
    # The user who created the workflow.
    created_by: Optional[User] = None
    # When a workflow was created.
    created_date_time: Optional[datetime.datetime] = None
    # A string that describes the purpose of the workflow.
    description: Optional[str] = None
    # A string to identify the workflow.
    display_name: Optional[str] = None
    # Defines when and for who the workflow will run.
    execution_conditions: Optional[WorkflowExecutionConditions] = None
    # Whether the workflow is enabled or disabled. If this setting is true, the workflow can be run on demand or on schedule when isSchedulingEnabled is true.
    is_enabled: Optional[bool] = None
    # If true, the Lifecycle Workflow engine executes the workflow based on the schedule defined by tenant settings. Can't be true for a disabled workflow (where isEnabled is false).
    is_scheduling_enabled: Optional[bool] = None
    # The unique identifier of the Microsoft Entra identity that last modified the workflow.
    last_modified_by: Optional[User] = None
    # When the workflow was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tasks in the workflow.
    tasks: Optional[list[Task]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkflowBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkflowBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.workflow".casefold():
            from .workflow import Workflow

            return Workflow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.workflowVersion".casefold():
            from .workflow_version import WorkflowVersion

            return WorkflowVersion()
        return WorkflowBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..user import User
        from .lifecycle_workflow_category import LifecycleWorkflowCategory
        from .task import Task
        from .workflow import Workflow
        from .workflow_execution_conditions import WorkflowExecutionConditions
        from .workflow_version import WorkflowVersion

        from ..user import User
        from .lifecycle_workflow_category import LifecycleWorkflowCategory
        from .task import Task
        from .workflow import Workflow
        from .workflow_execution_conditions import WorkflowExecutionConditions
        from .workflow_version import WorkflowVersion

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_enum_value(LifecycleWorkflowCategory)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(User)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "executionConditions": lambda n : setattr(self, 'execution_conditions', n.get_object_value(WorkflowExecutionConditions)),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "isSchedulingEnabled": lambda n : setattr(self, 'is_scheduling_enabled', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(User)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(Task)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("category", self.category)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("executionConditions", self.execution_conditions)
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_bool_value("isSchedulingEnabled", self.is_scheduling_enabled)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_additional_data_value(self.additional_data)
    

