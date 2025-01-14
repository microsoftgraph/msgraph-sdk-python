from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .printer import Printer
    from .print_operation import PrintOperation

from .print_operation import PrintOperation

@dataclass
class PrinterCreateOperation(PrintOperation, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.printerCreateOperation"
    # The signed certificate created during the registration process. Read-only.
    certificate: Optional[str] = None
    # The created printer entity. Read-only.
    printer: Optional[Printer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrinterCreateOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrinterCreateOperation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrinterCreateOperation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .printer import Printer
        from .print_operation import PrintOperation

        from .printer import Printer
        from .print_operation import PrintOperation

        fields: dict[str, Callable[[Any], None]] = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "printer": lambda n : setattr(self, 'printer', n.get_object_value(Printer)),
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
        writer.write_str_value("certificate", self.certificate)
        writer.write_object_value("printer", self.printer)
    

