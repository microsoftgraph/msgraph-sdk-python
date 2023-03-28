from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

print_operation = lazy_import('msgraph.generated.models.print_operation')
printer = lazy_import('msgraph.generated.models.printer')

class PrinterCreateOperation(print_operation.PrintOperation):
    @property
    def certificate(self,) -> Optional[str]:
        """
        Gets the certificate property value. The signed certificate created during the registration process. Read-only.
        Returns: Optional[str]
        """
        return self._certificate
    
    @certificate.setter
    def certificate(self,value: Optional[str] = None) -> None:
        """
        Sets the certificate property value. The signed certificate created during the registration process. Read-only.
        Args:
            value: Value to set for the certificate property.
        """
        self._certificate = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new PrinterCreateOperation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.printerCreateOperation"
        # The signed certificate created during the registration process. Read-only.
        self._certificate: Optional[str] = None
        # The created printer entity. Read-only.
        self._printer: Optional[printer.Printer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterCreateOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterCreateOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PrinterCreateOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "certificate": lambda n : setattr(self, 'certificate', n.get_str_value()),
            "printer": lambda n : setattr(self, 'printer', n.get_object_value(printer.Printer)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def printer(self,) -> Optional[printer.Printer]:
        """
        Gets the printer property value. The created printer entity. Read-only.
        Returns: Optional[printer.Printer]
        """
        return self._printer
    
    @printer.setter
    def printer(self,value: Optional[printer.Printer] = None) -> None:
        """
        Sets the printer property value. The created printer entity. Read-only.
        Args:
            value: Value to set for the printer property.
        """
        self._printer = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("certificate", self.certificate)
        writer.write_object_value("printer", self.printer)
    

