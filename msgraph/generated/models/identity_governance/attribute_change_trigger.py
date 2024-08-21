from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .trigger_attribute import TriggerAttribute
    from .workflow_execution_trigger import WorkflowExecutionTrigger

from .workflow_execution_trigger import WorkflowExecutionTrigger

@dataclass
class AttributeChangeTrigger(WorkflowExecutionTrigger):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.attributeChangeTrigger"
    # The trigger attribute being changed that triggers the workflowexecutiontrigger of a workflow.)
    trigger_attributes: Optional[List[TriggerAttribute]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttributeChangeTrigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttributeChangeTrigger
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttributeChangeTrigger()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .trigger_attribute import TriggerAttribute
        from .workflow_execution_trigger import WorkflowExecutionTrigger

        from .trigger_attribute import TriggerAttribute
        from .workflow_execution_trigger import WorkflowExecutionTrigger

        fields: Dict[str, Callable[[Any], None]] = {
            "triggerAttributes": lambda n : setattr(self, 'trigger_attributes', n.get_collection_of_object_values(TriggerAttribute)),
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
        writer.write_collection_of_object_values("triggerAttributes", self.trigger_attributes)
    

