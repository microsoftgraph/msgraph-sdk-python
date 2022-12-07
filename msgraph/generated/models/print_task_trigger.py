from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
print_event = lazy_import('msgraph.generated.models.print_event')
print_task_definition = lazy_import('msgraph.generated.models.print_task_definition')

class PrintTaskTrigger(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new printTaskTrigger and sets the default values.
        """
        super().__init__()
        # The definition property
        self._definition: Optional[print_task_definition.PrintTaskDefinition] = None
        # The event property
        self._event: Optional[print_event.PrintEvent] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintTaskTrigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintTaskTrigger
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrintTaskTrigger()
    
    @property
    def definition(self,) -> Optional[print_task_definition.PrintTaskDefinition]:
        """
        Gets the definition property value. The definition property
        Returns: Optional[print_task_definition.PrintTaskDefinition]
        """
        return self._definition
    
    @definition.setter
    def definition(self,value: Optional[print_task_definition.PrintTaskDefinition] = None) -> None:
        """
        Sets the definition property value. The definition property
        Args:
            value: Value to set for the definition property.
        """
        self._definition = value
    
    @property
    def event(self,) -> Optional[print_event.PrintEvent]:
        """
        Gets the event property value. The event property
        Returns: Optional[print_event.PrintEvent]
        """
        return self._event
    
    @event.setter
    def event(self,value: Optional[print_event.PrintEvent] = None) -> None:
        """
        Sets the event property value. The event property
        Args:
            value: Value to set for the event property.
        """
        self._event = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(print_task_definition.PrintTaskDefinition)),
            "event": lambda n : setattr(self, 'event', n.get_enum_value(print_event.PrintEvent)),
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
        writer.write_enum_value("event", self.event)
    

