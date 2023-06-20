from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, printer, printer_capabilities, printer_defaults, printer_location, printer_share, printer_status, print_job

from . import entity

@dataclass
class PrinterBase(entity.Entity):
    # The capabilities of the printer/printerShare.
    capabilities: Optional[printer_capabilities.PrinterCapabilities] = None
    # The default print settings of printer/printerShare.
    defaults: Optional[printer_defaults.PrinterDefaults] = None
    # The name of the printer/printerShare.
    display_name: Optional[str] = None
    # Whether the printer/printerShare is currently accepting new print jobs.
    is_accepting_jobs: Optional[bool] = None
    # The list of jobs that are queued for printing by the printer/printerShare.
    jobs: Optional[List[print_job.PrintJob]] = None
    # The physical and/or organizational location of the printer/printerShare.
    location: Optional[printer_location.PrinterLocation] = None
    # The manufacturer of the printer/printerShare.
    manufacturer: Optional[str] = None
    # The model name of the printer/printerShare.
    model: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[printer_status.PrinterStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterBase
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printer".casefold():
            from . import printer

            return printer.Printer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerShare".casefold():
            from . import printer_share

            return printer_share.PrinterShare()
        return PrinterBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, printer, printer_capabilities, printer_defaults, printer_location, printer_share, printer_status, print_job

        from . import entity, printer, printer_capabilities, printer_defaults, printer_location, printer_share, printer_status, print_job

        fields: Dict[str, Callable[[Any], None]] = {
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_object_value(printer_capabilities.PrinterCapabilities)),
            "defaults": lambda n : setattr(self, 'defaults', n.get_object_value(printer_defaults.PrinterDefaults)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isAcceptingJobs": lambda n : setattr(self, 'is_accepting_jobs', n.get_bool_value()),
            "jobs": lambda n : setattr(self, 'jobs', n.get_collection_of_object_values(print_job.PrintJob)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(printer_location.PrinterLocation)),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_object_value(printer_status.PrinterStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
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
    

