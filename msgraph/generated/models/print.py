from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import printer, printer_share, print_connector, print_operation, print_service, print_settings, print_task_definition

@dataclass
class Print(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The list of available print connectors.
    connectors: Optional[List[print_connector.PrintConnector]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of print long running operations.
    operations: Optional[List[print_operation.PrintOperation]] = None
    # The list of printers registered in the tenant.
    printers: Optional[List[printer.Printer]] = None
    # The list of available Universal Print service endpoints.
    services: Optional[List[print_service.PrintService]] = None
    # Tenant-wide settings for the Universal Print service.
    settings: Optional[print_settings.PrintSettings] = None
    # The list of printer shares registered in the tenant.
    shares: Optional[List[printer_share.PrinterShare]] = None
    # List of abstract definition for a task that can be triggered when various events occur within Universal Print.
    task_definitions: Optional[List[print_task_definition.PrintTaskDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Print:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Print
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Print()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import printer, printer_share, print_connector, print_operation, print_service, print_settings, print_task_definition

        from . import printer, printer_share, print_connector, print_operation, print_service, print_settings, print_task_definition

        fields: Dict[str, Callable[[Any], None]] = {
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(print_connector.PrintConnector)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(print_operation.PrintOperation)),
            "printers": lambda n : setattr(self, 'printers', n.get_collection_of_object_values(printer.Printer)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(print_service.PrintService)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(print_settings.PrintSettings)),
            "shares": lambda n : setattr(self, 'shares', n.get_collection_of_object_values(printer_share.PrinterShare)),
            "taskDefinitions": lambda n : setattr(self, 'task_definitions', n.get_collection_of_object_values(print_task_definition.PrintTaskDefinition)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("connectors", self.connectors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("printers", self.printers)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("shares", self.shares)
        writer.write_collection_of_object_values("taskDefinitions", self.task_definitions)
        writer.write_additional_data_value(self.additional_data)
    

