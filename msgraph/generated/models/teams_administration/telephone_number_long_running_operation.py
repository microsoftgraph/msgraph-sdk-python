from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..long_running_operation_status import LongRunningOperationStatus
    from .telephone_number_long_running_operation_details import TelephoneNumberLongRunningOperationDetails

from ..entity import Entity

@dataclass
class TelephoneNumberLongRunningOperation(Entity, Parsable):
    # Date and time when the asynchronous operation was created.
    created_date_time: Optional[str] = None
    # Asynchronous operation details.
    numbers: Optional[list[TelephoneNumberLongRunningOperationDetails]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[LongRunningOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TelephoneNumberLongRunningOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TelephoneNumberLongRunningOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TelephoneNumberLongRunningOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..long_running_operation_status import LongRunningOperationStatus
        from .telephone_number_long_running_operation_details import TelephoneNumberLongRunningOperationDetails

        from ..entity import Entity
        from ..long_running_operation_status import LongRunningOperationStatus
        from .telephone_number_long_running_operation_details import TelephoneNumberLongRunningOperationDetails

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_str_value()),
            "numbers": lambda n : setattr(self, 'numbers', n.get_collection_of_object_values(TelephoneNumberLongRunningOperationDetails)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LongRunningOperationStatus)),
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
        writer.write_str_value("createdDateTime", self.created_date_time)
        writer.write_collection_of_object_values("numbers", self.numbers)
        writer.write_enum_value("status", self.status)
    

