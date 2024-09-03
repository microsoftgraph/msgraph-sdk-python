from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .extension import Extension
    from .todo_task import TodoTask
    from .wellknown_list_name import WellknownListName

from .entity import Entity

@dataclass
class TodoTaskList(Entity):
    # The name of the task list.
    display_name: Optional[str] = None
    # The collection of open extensions defined for the task list. Nullable.
    extensions: Optional[List[Extension]] = None
    # True if the user is owner of the given task list.
    is_owner: Optional[bool] = None
    # True if the task list is shared with other users
    is_shared: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The tasks in this task list. Read-only. Nullable.
    tasks: Optional[List[TodoTask]] = None
    # The wellknownListName property
    wellknown_list_name: Optional[WellknownListName] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TodoTaskList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TodoTaskList
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TodoTaskList()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .extension import Extension
        from .todo_task import TodoTask
        from .wellknown_list_name import WellknownListName

        from .entity import Entity
        from .extension import Extension
        from .todo_task import TodoTask
        from .wellknown_list_name import WellknownListName

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(Extension)),
            "isOwner": lambda n : setattr(self, 'is_owner', n.get_bool_value()),
            "isShared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(TodoTask)),
            "wellknownListName": lambda n : setattr(self, 'wellknown_list_name', n.get_enum_value(WellknownListName)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_bool_value("isOwner", self.is_owner)
        writer.write_bool_value("isShared", self.is_shared)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_enum_value("wellknownListName", self.wellknown_list_name)
    

