from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .workflow_execution_trigger import WorkflowExecutionTrigger
    from .workflow_trigger_time_based_attribute import WorkflowTriggerTimeBasedAttribute

from .workflow_execution_trigger import WorkflowExecutionTrigger

@dataclass
class TimeBasedAttributeTrigger(WorkflowExecutionTrigger, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.timeBasedAttributeTrigger"
    # How many days before or after the time-based attribute specified the workflow should trigger. For example, if the attribute is employeeHireDate and offsetInDays is -1, then the workflow should trigger one day before the employee hire date. The value can range between -180 and 180 days.
    offset_in_days: Optional[int] = None
    # The timeBasedAttribute property
    time_based_attribute: Optional[WorkflowTriggerTimeBasedAttribute] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeBasedAttributeTrigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeBasedAttributeTrigger
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeBasedAttributeTrigger()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .workflow_execution_trigger import WorkflowExecutionTrigger
        from .workflow_trigger_time_based_attribute import WorkflowTriggerTimeBasedAttribute

        from .workflow_execution_trigger import WorkflowExecutionTrigger
        from .workflow_trigger_time_based_attribute import WorkflowTriggerTimeBasedAttribute

        fields: dict[str, Callable[[Any], None]] = {
            "offsetInDays": lambda n : setattr(self, 'offset_in_days', n.get_int_value()),
            "timeBasedAttribute": lambda n : setattr(self, 'time_based_attribute', n.get_enum_value(WorkflowTriggerTimeBasedAttribute)),
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
        writer.write_int_value("offsetInDays", self.offset_in_days)
        writer.write_enum_value("timeBasedAttribute", self.time_based_attribute)
    

