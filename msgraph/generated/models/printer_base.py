from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .printer import Printer
    from .printer_capabilities import PrinterCapabilities
    from .printer_defaults import PrinterDefaults
    from .printer_location import PrinterLocation
    from .printer_share import PrinterShare
    from .printer_status import PrinterStatus
    from .print_job import PrintJob

from .entity import Entity

@dataclass
class PrinterBase(Entity, Parsable):
    # The capabilities of the printer/printerShare.
    capabilities: Optional[PrinterCapabilities] = None
    # The default print settings of printer/printerShare.
    defaults: Optional[PrinterDefaults] = None
    # The name of the printer/printerShare.
    display_name: Optional[str] = None
    # Specifies whether the printer/printerShare is currently accepting new print jobs.
    is_accepting_jobs: Optional[bool] = None
    # The list of jobs that are queued for printing by the printer/printerShare.
    jobs: Optional[list[PrintJob]] = None
    # The physical and/or organizational location of the printer/printerShare.
    location: Optional[PrinterLocation] = None
    # The manufacturer of the printer/printerShare.
    manufacturer: Optional[str] = None
    # The model name of the printer/printerShare.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[PrinterStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrinterBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrinterBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printer".casefold():
            from .printer import Printer

            return Printer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerShare".casefold():
            from .printer_share import PrinterShare

            return PrinterShare()
        return PrinterBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .printer import Printer
        from .printer_capabilities import PrinterCapabilities
        from .printer_defaults import PrinterDefaults
        from .printer_location import PrinterLocation
        from .printer_share import PrinterShare
        from .printer_status import PrinterStatus
        from .print_job import PrintJob

        from .entity import Entity
        from .printer import Printer
        from .printer_capabilities import PrinterCapabilities
        from .printer_defaults import PrinterDefaults
        from .printer_location import PrinterLocation
        from .printer_share import PrinterShare
        from .printer_status import PrinterStatus
        from .print_job import PrintJob

        fields: dict[str, Callable[[Any], None]] = {
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(PrinterCapabilities)),
            "defaults": lambda n : setattr(self, 'defaults', n.get_object_value(PrinterDefaults)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isAcceptingJobs": lambda n : setattr(self, 'is_accepting_jobs', n.get_bool_value()),
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(PrintJob)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(PrinterLocation)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(PrinterStatus)),
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
        writer.write_object_value("capabilities", self.capabilities)
        writer.write_object_value("defaults", self.defaults)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isAcceptingJobs", self.is_accepting_jobs)
        writer.write_collection_of_object_values("jobs", self.jobs)
        writer.write_object_value("location", self.location)
        writer.write_str_value("manufacturer", self.manufacturer)
        writer.write_str_value("model", self.model)
        writer.write_object_value("status", self.status)
    

