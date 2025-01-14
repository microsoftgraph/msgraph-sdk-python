from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .print_task_definition import PrintTaskDefinition
    from .print_task_status import PrintTaskStatus
    from .print_task_trigger import PrintTaskTrigger

from .entity import Entity

@dataclass
class PrintTask(Entity, Parsable):
    # The definition property
    definition: Optional[PrintTaskDefinition] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL for the print entity that triggered this task. For example, https://graph.microsoft.com/v1.0/print/printers/{printerId}/jobs/{jobId}. Read-only.
    parent_url: Optional[str] = None
    # The status property
    status: Optional[PrintTaskStatus] = None
    # The trigger property
    trigger: Optional[PrintTaskTrigger] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintTask
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrintTask()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .print_task_definition import PrintTaskDefinition
        from .print_task_status import PrintTaskStatus
        from .print_task_trigger import PrintTaskTrigger

        from .entity import Entity
        from .print_task_definition import PrintTaskDefinition
        from .print_task_status import PrintTaskStatus
        from .print_task_trigger import PrintTaskTrigger

        fields: dict[str, Callable[[Any], None]] = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(PrintTaskDefinition)),
            "parentUrl": lambda n : setattr(self, 'parent_url', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(PrintTaskStatus)),
            "trigger": lambda n : setattr(self, 'trigger', n.get_object_value(PrintTaskTrigger)),
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
        writer.write_object_value("definition", self.definition)
        writer.write_str_value("parentUrl", self.parent_url)
        writer.write_object_value("status", self.status)
        writer.write_object_value("trigger", self.trigger)
    

