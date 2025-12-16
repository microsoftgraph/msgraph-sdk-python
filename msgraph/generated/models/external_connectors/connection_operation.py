from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from ..public_error import PublicError
    from .connection_operation_status import ConnectionOperationStatus

from ..entity import Entity

@dataclass
class ConnectionOperation(Entity, Parsable):
    # If status is failed, provides more information about the error that caused the failure.
    error: Optional[PublicError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the status of the asynchronous operation. The possible values are: unspecified, inprogress, completed, failed, unknownFutureValue.
    status: Optional[ConnectionOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConnectionOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConnectionOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConnectionOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from ..public_error import PublicError
        from .connection_operation_status import ConnectionOperationStatus

        from ..entity import Entity
        from ..public_error import PublicError
        from .connection_operation_status import ConnectionOperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ConnectionOperationStatus)),
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
        writer.write_enum_value("status", self.status)
    

