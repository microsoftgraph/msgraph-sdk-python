from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .operator_between import OperatorBetween
    from .operator_equal_to import OperatorEqualTo
    from .operator_less_than_equal_to import OperatorLessThanEqualTo
    from .workflow_execution_trigger_operator import WorkflowExecutionTriggerOperator
    from .workflow_trigger_operator_event_timing import WorkflowTriggerOperatorEventTiming

from .workflow_execution_trigger_operator import WorkflowExecutionTriggerOperator

@dataclass
class WorkflowTriggerTimeBasedOperator(WorkflowExecutionTriggerOperator, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.workflowTriggerTimeBasedOperator"
    # The eventTiming property
    event_timing: Optional[WorkflowTriggerOperatorEventTiming] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkflowTriggerTimeBasedOperator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkflowTriggerTimeBasedOperator
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if not mapping_value:
            return WorkflowTriggerTimeBasedOperator()
        if mapping_value.casefold() == "#microsoft.graph.identityGovernance.operatorBetween".casefold():
            from .operator_between import OperatorBetween

            return OperatorBetween()
        if mapping_value.casefold() == "#microsoft.graph.identityGovernance.operatorEqualTo".casefold():
            from .operator_equal_to import OperatorEqualTo

            return OperatorEqualTo()
        if mapping_value.casefold() == "#microsoft.graph.identityGovernance.operatorLessThanEqualTo".casefold():
            from .operator_less_than_equal_to import OperatorLessThanEqualTo

            return OperatorLessThanEqualTo()
        return WorkflowTriggerTimeBasedOperator()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .operator_between import OperatorBetween
        from .operator_equal_to import OperatorEqualTo
        from .operator_less_than_equal_to import OperatorLessThanEqualTo
        from .workflow_execution_trigger_operator import WorkflowExecutionTriggerOperator
        from .workflow_trigger_operator_event_timing import WorkflowTriggerOperatorEventTiming

        from .operator_between import OperatorBetween
        from .operator_equal_to import OperatorEqualTo
        from .operator_less_than_equal_to import OperatorLessThanEqualTo
        from .workflow_execution_trigger_operator import WorkflowExecutionTriggerOperator
        from .workflow_trigger_operator_event_timing import WorkflowTriggerOperatorEventTiming

        fields: dict[str, Callable[[Any], None]] = {
            "eventTiming": lambda n : setattr(self, 'event_timing', n.get_enum_value(WorkflowTriggerOperatorEventTiming)),
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
        writer.write_enum_value("eventTiming", self.event_timing)
    

