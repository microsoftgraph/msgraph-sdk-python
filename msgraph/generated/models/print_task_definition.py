from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_identity = lazy_import('msgraph.generated.models.app_identity')
entity = lazy_import('msgraph.generated.models.entity')
print_task = lazy_import('msgraph.generated.models.print_task')

class PrintTaskDefinition(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new printTaskDefinition and sets the default values.
        """
        super().__init__()
        # The createdBy property
        self._created_by: Optional[app_identity.AppIdentity] = None
        # The name of the printTaskDefinition.
        self._display_name: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A list of tasks that have been created based on this definition. The list includes currently running tasks and recently completed tasks. Read-only.
        self._tasks: Optional[List[print_task.PrintTask]] = None
    
    @property
    def created_by(self,) -> Optional[app_identity.AppIdentity]:
        """
        Gets the createdBy property value. The createdBy property
        Returns: Optional[app_identity.AppIdentity]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[app_identity.AppIdentity] = None) -> None:
        """
        Sets the createdBy property value. The createdBy property
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintTaskDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintTaskDefinition
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintTaskDefinition()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the printTaskDefinition.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the printTaskDefinition.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(app_identity.AppIdentity)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(print_task.PrintTask)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("tasks", self.tasks)
    
    @property
    def tasks(self,) -> Optional[List[print_task.PrintTask]]:
        """
        Gets the tasks property value. A list of tasks that have been created based on this definition. The list includes currently running tasks and recently completed tasks. Read-only.
        Returns: Optional[List[print_task.PrintTask]]
        """
        return self._tasks
    
    @tasks.setter
    def tasks(self,value: Optional[List[print_task.PrintTask]] = None) -> None:
        """
        Sets the tasks property value. A list of tasks that have been created based on this definition. The list includes currently running tasks and recently completed tasks. Read-only.
        Args:
            value: Value to set for the tasks property.
        """
        self._tasks = value
    

