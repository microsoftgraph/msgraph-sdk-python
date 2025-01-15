from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .onenote_operation_error import OnenoteOperationError
    from .operation import Operation

from .operation import Operation

@dataclass
class OnenoteOperation(Operation, Parsable):
    # The error returned by the operation.
    error: Optional[OnenoteOperationError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The operation percent complete if the operation is still in running status.
    percent_complete: Optional[str] = None
    # The resource id.
    resource_id: Optional[str] = None
    # The resource URI for the object. For example, the resource URI for a copied page or section.
    resource_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnenoteOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnenoteOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .onenote_operation_error import OnenoteOperationError
        from .operation import Operation

        from .onenote_operation_error import OnenoteOperationError
        from .operation import Operation

        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(OnenoteOperationError)),
            "percentComplete": lambda n : setattr(self, 'percent_complete', n.get_str_value()),
            "resourceId": lambda n : setattr(self, 'resource_id', n.get_str_value()),
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_str_value()),
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
        writer.write_str_value("percentComplete", self.percent_complete)
        writer.write_str_value("resourceId", self.resource_id)
        writer.write_str_value("resourceLocation", self.resource_location)
    

