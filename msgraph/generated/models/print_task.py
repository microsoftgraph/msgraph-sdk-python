from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, print_task_definition, print_task_status, print_task_trigger

from . import entity

@dataclass
class PrintTask(entity.Entity):
    # The definition property
    definition: Optional[print_task_definition.PrintTaskDefinition] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL for the print entity that triggered this task. For example, https://graph.microsoft.com/v1.0/print/printers/{printerId}/jobs/{jobId}. Read-only.
    parent_url: Optional[str] = None
    # The status property
    status: Optional[print_task_status.PrintTaskStatus] = None
    # The trigger property
    trigger: Optional[print_task_trigger.PrintTaskTrigger] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintTask:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintTask
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintTask()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, print_task_definition, print_task_status, print_task_trigger

        fields: Dict[str, Callable[[Any], None]] = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(print_task_definition.PrintTaskDefinition)),
            "parentUrl": lambda n : setattr(self, 'parent_url', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(print_task_status.PrintTaskStatus)),
            "trigger": lambda n : setattr(self, 'trigger', n.get_object_value(print_task_trigger.PrintTaskTrigger)),
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
        writer.write_object_value("definition", self.definition)
        writer.write_str_value("parentUrl", self.parent_url)
        writer.write_object_value("status", self.status)
        writer.write_object_value("trigger", self.trigger)
    

