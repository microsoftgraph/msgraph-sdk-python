from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .workflow_execution_trigger import WorkflowExecutionTrigger
    from .workflow_execution_trigger_operator import WorkflowExecutionTriggerOperator

from .workflow_execution_trigger import WorkflowExecutionTrigger

@dataclass
class TimeBasedAttributeTriggerV2(WorkflowExecutionTrigger, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.timeBasedAttributeTriggerV2"
    # The name of the date-type user attribute to evaluate, such as employeeHireDate or employeeLeaveDateTime.
    attribute: Optional[str] = None
    # The operator property
    operator: Optional[WorkflowExecutionTriggerOperator] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeBasedAttributeTriggerV2:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeBasedAttributeTriggerV2
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeBasedAttributeTriggerV2()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .workflow_execution_trigger import WorkflowExecutionTrigger
        from .workflow_execution_trigger_operator import WorkflowExecutionTriggerOperator

        from .workflow_execution_trigger import WorkflowExecutionTrigger
        from .workflow_execution_trigger_operator import WorkflowExecutionTriggerOperator

        fields: dict[str, Callable[[Any], None]] = {
            "attribute": lambda n : setattr(self, 'attribute', n.get_str_value()),
            "operator": lambda n : setattr(self, 'operator', n.get_object_value(WorkflowExecutionTriggerOperator)),
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
        writer.write_str_value("attribute", self.attribute)
        writer.write_object_value("operator", self.operator)
    

