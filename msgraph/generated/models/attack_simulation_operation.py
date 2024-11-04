from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attack_simulation_operation_type import AttackSimulationOperationType
    from .long_running_operation import LongRunningOperation

from .long_running_operation import LongRunningOperation

@dataclass
class AttackSimulationOperation(LongRunningOperation):
    """
    The status of a long-running operation.
    """
    # The OdataType property
    odata_type: Optional[str] = None
    # Percentage of completion of the respective operation.
    percentage_completed: Optional[int] = None
    # Tenant identifier.
    tenant_id: Optional[str] = None
    # The attack simulation operation type. Possible values are: createSimulation, updateSimulation, unknownFutureValue.
    type: Optional[AttackSimulationOperationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AttackSimulationOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AttackSimulationOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AttackSimulationOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .attack_simulation_operation_type import AttackSimulationOperationType
        from .long_running_operation import LongRunningOperation

        from .attack_simulation_operation_type import AttackSimulationOperationType
        from .long_running_operation import LongRunningOperation

        fields: Dict[str, Callable[[Any], None]] = {
            "percentageCompleted": lambda n : setattr(self, 'percentage_completed', n.get_int_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(AttackSimulationOperationType)),
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
        writer.write_int_value("percentageCompleted", self.percentage_completed)
        writer.write_str_value("tenantId", self.tenant_id)
        writer.write_enum_value("type", self.type)
    

