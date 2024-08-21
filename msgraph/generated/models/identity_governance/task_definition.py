from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .lifecycle_task_category import LifecycleTaskCategory
    from .parameter import Parameter

from ..entity import Entity

@dataclass
class TaskDefinition(Entity):
    # The category property
    category: Optional[LifecycleTaskCategory] = None
    # Defines if the workflow will continue if the task has an error.
    continue_on_error: Optional[bool] = None
    # The description of the taskDefinition.
    description: Optional[str] = None
    # The display name of the taskDefinition.Supports $filter(eq, ne) and $orderby.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The parameters that must be supplied when creating a workflow task object.Supports $filter(any).
    parameters: Optional[List[Parameter]] = None
    # The version number of the taskDefinition. New records are pushed when we add support for new parameters.Supports $filter(ge, gt, le, lt, eq, ne) and $orderby.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TaskDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TaskDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TaskDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .lifecycle_task_category import LifecycleTaskCategory
        from .parameter import Parameter

        from ..entity import Entity
        from .lifecycle_task_category import LifecycleTaskCategory
        from .parameter import Parameter

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_collection_of_enum_values(LifecycleTaskCategory)),
            "continueOnError": lambda n : setattr(self, 'continue_on_error', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "parameters": lambda n : setattr(self, 'parameters', n.get_collection_of_object_values(Parameter)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_bool_value("continueOnError", self.continue_on_error)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("parameters", self.parameters)
        writer.write_int_value("version", self.version)
    

