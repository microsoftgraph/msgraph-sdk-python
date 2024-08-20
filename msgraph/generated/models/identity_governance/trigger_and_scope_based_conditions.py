from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..subject_set import SubjectSet
    from .workflow_execution_conditions import WorkflowExecutionConditions
    from .workflow_execution_trigger import WorkflowExecutionTrigger

from .workflow_execution_conditions import WorkflowExecutionConditions

@dataclass
class TriggerAndScopeBasedConditions(WorkflowExecutionConditions):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.triggerAndScopeBasedConditions"
    # Defines who the workflow runs for.
    scope: Optional[SubjectSet] = None
    # What triggers a workflow to run.
    trigger: Optional[WorkflowExecutionTrigger] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TriggerAndScopeBasedConditions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TriggerAndScopeBasedConditions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TriggerAndScopeBasedConditions()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..subject_set import SubjectSet
        from .workflow_execution_conditions import WorkflowExecutionConditions
        from .workflow_execution_trigger import WorkflowExecutionTrigger

        from ..subject_set import SubjectSet
        from .workflow_execution_conditions import WorkflowExecutionConditions
        from .workflow_execution_trigger import WorkflowExecutionTrigger

        fields: Dict[str, Callable[[Any], None]] = {
            "scope": lambda n : setattr(self, 'scope', n.get_object_value(SubjectSet)),
            "trigger": lambda n : setattr(self, 'trigger', n.get_object_value(WorkflowExecutionTrigger)),
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
        writer.write_object_value("scope", self.scope)
        writer.write_object_value("trigger", self.trigger)
    

