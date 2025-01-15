from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_operation_error import WorkbookOperationError
    from .workbook_operation_status import WorkbookOperationStatus

from .entity import Entity

@dataclass
class WorkbookOperation(Entity, Parsable):
    # The error returned by the operation.
    error: Optional[WorkbookOperationError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The resource URI for the result.
    resource_location: Optional[str] = None
    # The status property
    status: Optional[WorkbookOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_operation_error import WorkbookOperationError
        from .workbook_operation_status import WorkbookOperationStatus

        from .entity import Entity
        from .workbook_operation_error import WorkbookOperationError
        from .workbook_operation_status import WorkbookOperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(WorkbookOperationError)),
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(WorkbookOperationStatus)),
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
        writer.write_str_value("resourceLocation", self.resource_location)
        writer.write_enum_value("status", self.status)
    

