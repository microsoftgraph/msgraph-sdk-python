from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_identity import AppIdentity
    from .entity import Entity
    from .print_task import PrintTask

from .entity import Entity

@dataclass
class PrintTaskDefinition(Entity):
    # The createdBy property
    created_by: Optional[AppIdentity] = None
    # The name of the printTaskDefinition.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A list of tasks that have been created based on this definition. The list includes currently running tasks and recently completed tasks. Read-only.
    tasks: Optional[List[PrintTask]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintTaskDefinition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintTaskDefinition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrintTaskDefinition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_identity import AppIdentity
        from .entity import Entity
        from .print_task import PrintTask

        from .app_identity import AppIdentity
        from .entity import Entity
        from .print_task import PrintTask

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(AppIdentity)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "tasks": lambda n : setattr(self, 'tasks', n.get_collection_of_object_values(PrintTask)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("tasks", self.tasks)
    

