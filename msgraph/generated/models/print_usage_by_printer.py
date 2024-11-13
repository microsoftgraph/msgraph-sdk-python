from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .print_usage import PrintUsage

from .print_usage import PrintUsage

@dataclass
class PrintUsageByPrinter(PrintUsage, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.printUsageByPrinter"
    # The ID of the printer represented by these statistics.
    printer_id: Optional[str] = None
    # The name of the printer represented by these statistics.
    printer_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintUsageByPrinter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintUsageByPrinter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrintUsageByPrinter()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .print_usage import PrintUsage

        from .print_usage import PrintUsage

        fields: Dict[str, Callable[[Any], None]] = {
            "printerId": lambda n : setattr(self, 'printer_id', n.get_str_value()),
            "printerName": lambda n : setattr(self, 'printer_name', n.get_str_value()),
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
        from .print_usage import PrintUsage

        writer.write_str_value("printerId", self.printer_id)
        writer.write_str_value("printerName", self.printer_name)
    

