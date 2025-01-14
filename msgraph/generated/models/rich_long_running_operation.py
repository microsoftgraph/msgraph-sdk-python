from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .long_running_operation import LongRunningOperation
    from .public_error import PublicError

from .long_running_operation import LongRunningOperation

@dataclass
class RichLongRunningOperation(LongRunningOperation, Parsable):
    """
    The status of a long-running operation.
    """
    # Error that caused the operation to fail.
    error: Optional[PublicError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A value between 0 and 100 that indicates the progress of the operation.
    percentage_complete: Optional[int] = None
    # The unique identifier for the result.
    resource_id: Optional[str] = None
    # The type of the operation.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RichLongRunningOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RichLongRunningOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RichLongRunningOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .long_running_operation import LongRunningOperation
        from .public_error import PublicError

        from .long_running_operation import LongRunningOperation
        from .public_error import PublicError

        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "percentageComplete": lambda n : setattr(self, 'percentage_complete', n.get_int_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_object_value("error", self.error)
        writer.write_int_value("percentageComplete", self.percentage_complete)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("type", self.type)
    

