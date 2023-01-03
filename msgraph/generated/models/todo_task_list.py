from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
extension = lazy_import('msgraph.generated.models.extension')
todo_task = lazy_import('msgraph.generated.models.todo_task')
wellknown_list_name = lazy_import('msgraph.generated.models.wellknown_list_name')

class TodoTaskList(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new todoTaskList and sets the default values.
        """
        super().__init__()
        # The name of the task list.
        self._display_name: Optional[str] = None
        # The collection of open extensions defined for the task list. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # True if the user is owner of the given task list.
        self._is_owner: Optional[bool] = None
        # True if the task list is shared with other users
        self._is_shared: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The tasks in this task list. Read-only. Nullable.
        self._tasks: Optional[List[todo_task.TodoTask]] = None
        # The wellknownListName property
        self._wellknown_list_name: Optional[wellknown_list_name.WellknownListName] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TodoTaskList:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TodoTaskList
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TodoTaskList()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the task list.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the task list.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the task list. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the task list. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "is_owner": lambda n : setattr(self, 'is_owner', n.get_bool_value()),
            "is_shared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(todo_task.TodoTask)),
            "wellknown_list_name": lambda n : setattr(self, 'wellknown_list_name', n.get_enum_value(wellknown_list_name.WellknownListName)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_owner(self,) -> Optional[bool]:
        """
        Gets the isOwner property value. True if the user is owner of the given task list.
        Returns: Optional[bool]
        """
        return self._is_owner
    
    @is_owner.setter
    def is_owner(self,value: Optional[bool] = None) -> None:
        """
        Sets the isOwner property value. True if the user is owner of the given task list.
        Args:
            value: Value to set for the isOwner property.
        """
        self._is_owner = value
    
    @property
    def is_shared(self,) -> Optional[bool]:
        """
        Gets the isShared property value. True if the task list is shared with other users
        Returns: Optional[bool]
        """
        return self._is_shared
    
    @is_shared.setter
    def is_shared(self,value: Optional[bool] = None) -> None:
        """
        Sets the isShared property value. True if the task list is shared with other users
        Args:
            value: Value to set for the isShared property.
        """
        self._is_shared = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_bool_value("isOwner", self.is_owner)
        writer.write_bool_value("isShared", self.is_shared)
        writer.write_collection_of_object_values("tasks", self.tasks)
        writer.write_enum_value("wellknownListName", self.wellknown_list_name)
    
    @property
    def tasks(self,) -> Optional[List[todo_task.TodoTask]]:
        """
        Gets the tasks property value. The tasks in this task list. Read-only. Nullable.
        Returns: Optional[List[todo_task.TodoTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[todo_task.TodoTask]] = None) -> None:
        """
        Sets the tasks property value. The tasks in this task list. Read-only. Nullable.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    
    @property
    def wellknown_list_name(self,) -> Optional[wellknown_list_name.WellknownListName]:
        """
        Gets the wellknownListName property value. The wellknownListName property
        Returns: Optional[wellknown_list_name.WellknownListName]
        """
        return self._wellknown_list_name
    
    @wellknown_list_name.setter
    def wellknown_list_name(self,value: Optional[wellknown_list_name.WellknownListName] = None) -> None:
        """
        Sets the wellknownListName property value. The wellknownListName property
        Args:
            value: Value to set for the wellknownListName property.
        """
        self._wellknown_list_name = value
    

