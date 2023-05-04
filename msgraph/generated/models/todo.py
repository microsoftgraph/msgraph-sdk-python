from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, todo_task_list

from . import entity

class Todo(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Todo and sets the default values.
        """
        super().__init__()
        # The task lists in the users mailbox.
        self._lists: Optional[List[todo_task_list.TodoTaskList]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Todo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Todo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Todo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, todo_task_list

        fields: Dict[str, Callable[[Any], None]] = {
            "lists": lambda n : setattr(self, 'lists', n.get_collection_of_object_values(todo_task_list.TodoTaskList)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def lists(self,) -> Optional[List[todo_task_list.TodoTaskList]]:
        """
        Gets the lists property value. The task lists in the users mailbox.
        Returns: Optional[List[todo_task_list.TodoTaskList]]
        """
        return self._lists
    
    @lists.setter
    def lists(self,value: Optional[List[todo_task_list.TodoTaskList]] = None) -> None:
        """
        Sets the lists property value. The task lists in the users mailbox.
        Args:
            value: Value to set for the lists property.
        """
        self._lists = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("lists", self.lists)
    

