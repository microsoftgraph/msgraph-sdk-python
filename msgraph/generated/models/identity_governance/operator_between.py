from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .workflow_trigger_time_based_operator import WorkflowTriggerTimeBasedOperator

from .workflow_trigger_time_based_operator import WorkflowTriggerTimeBasedOperator

@dataclass
class OperatorBetween(WorkflowTriggerTimeBasedOperator, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.operatorBetween"
    # The exclusive lower bound of the date range, in days. The value must be a nonnegative integer and less than lessThanOffsetInDays.
    greater_than_offset_in_days: Optional[int] = None
    # The exclusive upper bound of the date range, in days. The value must be a nonnegative integer and greater than greaterThanOffsetInDays. The difference between the upper and lower bounds can't exceed 180 days.
    less_than_offset_in_days: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OperatorBetween:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OperatorBetween
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OperatorBetween()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .workflow_trigger_time_based_operator import WorkflowTriggerTimeBasedOperator

        from .workflow_trigger_time_based_operator import WorkflowTriggerTimeBasedOperator

        fields: dict[str, Callable[[Any], None]] = {
            "greaterThanOffsetInDays": lambda n : setattr(self, 'greater_than_offset_in_days', n.get_int_value()),
            "lessThanOffsetInDays": lambda n : setattr(self, 'less_than_offset_in_days', n.get_int_value()),
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
        writer.write_int_value("greaterThanOffsetInDays", self.greater_than_offset_in_days)
        writer.write_int_value("lessThanOffsetInDays", self.less_than_offset_in_days)
    

