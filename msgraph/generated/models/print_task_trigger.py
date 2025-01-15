from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .print_event import PrintEvent
    from .print_task_definition import PrintTaskDefinition

from .entity import Entity

@dataclass
class PrintTaskTrigger(Entity, Parsable):
    # The definition property
    definition: Optional[PrintTaskDefinition] = None
    # The event property
    event: Optional[PrintEvent] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintTaskTrigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintTaskTrigger
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrintTaskTrigger()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .print_event import PrintEvent
        from .print_task_definition import PrintTaskDefinition

        from .entity import Entity
        from .print_event import PrintEvent
        from .print_task_definition import PrintTaskDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(PrintTaskDefinition)),
            "event": lambda n : setattr(self, 'event', n.get_enum_value(PrintEvent)),
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
        writer.write_enum_value("event", self.event)
    

