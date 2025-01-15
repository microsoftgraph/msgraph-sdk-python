from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .printer_base import PrinterBase
    from .printer_share import PrinterShare
    from .print_connector import PrintConnector
    from .print_task_trigger import PrintTaskTrigger

from .printer_base import PrinterBase

@dataclass
class Printer(PrinterBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.printer"
    # The connectors that are associated with the printer.
    connectors: Optional[list[PrintConnector]] = None
    # True if the printer has a physical device for printing. Read-only.
    has_physical_device: Optional[bool] = None
    # True if the printer is shared; false otherwise. Read-only.
    is_shared: Optional[bool] = None
    # The most recent dateTimeOffset when a printer interacted with Universal Print. Read-only.
    last_seen_date_time: Optional[datetime.datetime] = None
    # The DateTimeOffset when the printer was registered. Read-only.
    registered_date_time: Optional[datetime.datetime] = None
    # The list of printerShares that are associated with the printer. Currently, only one printerShare can be associated with the printer. Read-only. Nullable.
    shares: Optional[list[PrinterShare]] = None
    # A list of task triggers that are associated with the printer.
    task_triggers: Optional[list[PrintTaskTrigger]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Printer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Printer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Printer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .printer_base import PrinterBase
        from .printer_share import PrinterShare
        from .print_connector import PrintConnector
        from .print_task_trigger import PrintTaskTrigger

        from .printer_base import PrinterBase
        from .printer_share import PrinterShare
        from .print_connector import PrintConnector
        from .print_task_trigger import PrintTaskTrigger

        fields: dict[str, Callable[[Any], None]] = {
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(PrintConnector)),
            "hasPhysicalDevice": lambda n : setattr(self, 'has_physical_device', n.get_bool_value()),
            "isShared": lambda n : setattr(self, 'is_shared', n.get_bool_value()),
            "lastSeenDateTime": lambda n : setattr(self, 'last_seen_date_time', n.get_datetime_value()),
            "registeredDateTime": lambda n : setattr(self, 'registered_date_time', n.get_datetime_value()),
            "shares": lambda n : setattr(self, 'shares', n.get_collection_of_object_values(PrinterShare)),
            "taskTriggers": lambda n : setattr(self, 'task_triggers', n.get_collection_of_object_values(PrintTaskTrigger)),
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
        writer.write_collection_of_object_values("connectors", self.connectors)
        writer.write_bool_value("hasPhysicalDevice", self.has_physical_device)
        writer.write_bool_value("isShared", self.is_shared)
        writer.write_datetime_value("lastSeenDateTime", self.last_seen_date_time)
        writer.write_datetime_value("registeredDateTime", self.registered_date_time)
        writer.write_collection_of_object_values("shares", self.shares)
        writer.write_collection_of_object_values("taskTriggers", self.task_triggers)
    

