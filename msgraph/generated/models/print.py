from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .printer import Printer
    from .printer_share import PrinterShare
    from .print_connector import PrintConnector
    from .print_operation import PrintOperation
    from .print_service import PrintService
    from .print_settings import PrintSettings
    from .print_task_definition import PrintTaskDefinition

@dataclass
class Print(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The list of available print connectors.
    connectors: Optional[list[PrintConnector]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of print long running operations.
    operations: Optional[list[PrintOperation]] = None
    # The list of printers registered in the tenant.
    printers: Optional[list[Printer]] = None
    # The list of available Universal Print service endpoints.
    services: Optional[list[PrintService]] = None
    # Tenant-wide settings for the Universal Print service.
    settings: Optional[PrintSettings] = None
    # The list of printer shares registered in the tenant.
    shares: Optional[list[PrinterShare]] = None
    # List of abstract definition for a task that can be triggered when various events occur within Universal Print.
    task_definitions: Optional[list[PrintTaskDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Print:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Print
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Print()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .printer import Printer
        from .printer_share import PrinterShare
        from .print_connector import PrintConnector
        from .print_operation import PrintOperation
        from .print_service import PrintService
        from .print_settings import PrintSettings
        from .print_task_definition import PrintTaskDefinition

        from .printer import Printer
        from .printer_share import PrinterShare
        from .print_connector import PrintConnector
        from .print_operation import PrintOperation
        from .print_service import PrintService
        from .print_settings import PrintSettings
        from .print_task_definition import PrintTaskDefinition

        fields: dict[str, Callable[[Any], None]] = {
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(PrintConnector)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(PrintOperation)),
            "printers": lambda n : setattr(self, 'printers', n.get_collection_of_object_values(Printer)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(PrintService)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(PrintSettings)),
            "shares": lambda n : setattr(self, 'shares', n.get_collection_of_object_values(PrinterShare)),
            "taskDefinitions": lambda n : setattr(self, 'task_definitions', n.get_collection_of_object_values(PrintTaskDefinition)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
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
    

