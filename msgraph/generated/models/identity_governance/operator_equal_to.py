from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .workflow_trigger_time_based_operator import WorkflowTriggerTimeBasedOperator

from .workflow_trigger_time_based_operator import WorkflowTriggerTimeBasedOperator

@dataclass
class OperatorEqualTo(WorkflowTriggerTimeBasedOperator, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.operatorEqualTo"
    # The exact number of days between the current date and the date in the user attribute. The value must be a nonnegative integer.
    offset_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperatorEqualTo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperatorEqualTo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperatorEqualTo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .workflow_trigger_time_based_operator import WorkflowTriggerTimeBasedOperator

        from .workflow_trigger_time_based_operator import WorkflowTriggerTimeBasedOperator

        fields: dict[str, Callable[[Any], None]] = {
            "offsetInDays": lambda n : setattr(self, 'offset_in_days', n.get_int_value()),
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
    

