from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .membership_change_type import MembershipChangeType
    from .workflow_execution_trigger import WorkflowExecutionTrigger

from .workflow_execution_trigger import WorkflowExecutionTrigger

@dataclass
class MembershipChangeTrigger(WorkflowExecutionTrigger, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.membershipChangeTrigger"
    # The changeType property
    change_type: Optional[MembershipChangeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MembershipChangeTrigger:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MembershipChangeTrigger
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MembershipChangeTrigger()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .membership_change_type import MembershipChangeType
        from .workflow_execution_trigger import WorkflowExecutionTrigger

        from .membership_change_type import MembershipChangeType
        from .workflow_execution_trigger import WorkflowExecutionTrigger

        fields: dict[str, Callable[[Any], None]] = {
            "changeType": lambda n : setattr(self, 'change_type', n.get_enum_value(MembershipChangeType)),
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
        writer.write_enum_value("changeType", self.change_type)
    

