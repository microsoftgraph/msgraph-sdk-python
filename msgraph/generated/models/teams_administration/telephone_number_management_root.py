from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .number_assignment import NumberAssignment
    from .telephone_number_long_running_operation import TelephoneNumberLongRunningOperation

from ..entity import Entity

@dataclass
class TelephoneNumberManagementRoot(Entity, Parsable):
    # Represents a collection of synchronous telephone number management operations.
    number_assignments: Optional[list[NumberAssignment]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents a collection of asynchronous telephone number management operations.
    operations: Optional[list[TelephoneNumberLongRunningOperation]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TelephoneNumberManagementRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TelephoneNumberManagementRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TelephoneNumberManagementRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .number_assignment import NumberAssignment
        from .telephone_number_long_running_operation import TelephoneNumberLongRunningOperation

        from ..entity import Entity
        from .number_assignment import NumberAssignment
        from .telephone_number_long_running_operation import TelephoneNumberLongRunningOperation

        fields: dict[str, Callable[[Any], None]] = {
            "numberAssignments": lambda n : setattr(self, 'number_assignments', n.get_collection_of_object_values(NumberAssignment)),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(TelephoneNumberLongRunningOperation)),
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
        writer.write_collection_of_object_values("numberAssignments", self.number_assignments)
        writer.write_collection_of_object_values("operations", self.operations)
    

