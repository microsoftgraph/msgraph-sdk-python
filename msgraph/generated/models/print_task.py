from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
print_task_definition = lazy_import('msgraph.generated.models.print_task_definition')
print_task_status = lazy_import('msgraph.generated.models.print_task_status')
print_task_trigger = lazy_import('msgraph.generated.models.print_task_trigger')

class PrintTask(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new printTask and sets the default values.
        """
        super().__init__()
        # The definition property
        self._definition: Optional[print_task_definition.PrintTaskDefinition] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The URL for the print entity that triggered this task. For example, https://graph.microsoft.com/v1.0/print/printers/{printerId}/jobs/{jobId}. Read-only.
        self._parent_url: Optional[str] = None
        # The status property
        self._status: Optional[print_task_status.PrintTaskStatus] = None
        # The trigger property
        self._trigger: Optional[print_task_trigger.PrintTaskTrigger] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "definition": lambda n : setattr(self, 'definition', n.get_object_value(print_task_definition.PrintTaskDefinition)),
            "parent_url": lambda n : setattr(self, 'parent_url', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(print_task_status.PrintTaskStatus)),
            "trigger": lambda n : setattr(self, 'trigger', n.get_object_value(print_task_trigger.PrintTaskTrigger)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def parent_url(self,) -> Optional[str]:
        """
        Gets the parentUrl property value. The URL for the print entity that triggered this task. For example, https://graph.microsoft.com/v1.0/print/printers/{printerId}/jobs/{jobId}. Read-only.
        Returns: Optional[str]
        """
        return self._parent_url
    
    @parent_url.setter
    def parent_url(self,value: Optional[str] = None) -> None:
        """
        Sets the parentUrl property value. The URL for the print entity that triggered this task. For example, https://graph.microsoft.com/v1.0/print/printers/{printerId}/jobs/{jobId}. Read-only.
        Args:
            value: Value to set for the parentUrl property.
        """
        self._parent_url = value
    
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
    
    @property
    def status(self,) -> Optional[print_task_status.PrintTaskStatus]:
        """
        Gets the status property value. The status property
        Returns: Optional[print_task_status.PrintTaskStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[print_task_status.PrintTaskStatus] = None) -> None:
        """
        Sets the status property value. The status property
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    
    @property
    def trigger(self,) -> Optional[print_task_trigger.PrintTaskTrigger]:
        """
        Gets the trigger property value. The trigger property
        Returns: Optional[print_task_trigger.PrintTaskTrigger]
        """
        return self._trigger
    
    @trigger.setter
    def trigger(self,value: Optional[print_task_trigger.PrintTaskTrigger] = None) -> None:
        """
        Sets the trigger property value. The trigger property
        Args:
            value: Value to set for the trigger property.
        """
        self._trigger = value
    

