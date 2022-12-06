from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

print_connector = lazy_import('msgraph.generated.models.print_connector')
print_operation = lazy_import('msgraph.generated.models.print_operation')
print_service = lazy_import('msgraph.generated.models.print_service')
print_settings = lazy_import('msgraph.generated.models.print_settings')
print_task_definition = lazy_import('msgraph.generated.models.print_task_definition')
printer = lazy_import('msgraph.generated.models.printer')
printer_share = lazy_import('msgraph.generated.models.printer_share')

class Print(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def connectors(self,) -> Optional[List[print_connector.PrintConnector]]:
        """
        Gets the connectors property value. The list of available print connectors.
        Returns: Optional[List[print_connector.PrintConnector]]
        """
        return self._connectors
    
    @connectors.setter
    def connectors(self,value: Optional[List[print_connector.PrintConnector]] = None) -> None:
        """
        Sets the connectors property value. The list of available print connectors.
        Args:
            value: Value to set for the connectors property.
        """
        self._connectors = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Print and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The list of available print connectors.
        self._connectors: Optional[List[print_connector.PrintConnector]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The list of print long running operations.
        self._operations: Optional[List[print_operation.PrintOperation]] = None
        # The list of printers registered in the tenant.
        self._printers: Optional[List[printer.Printer]] = None
        # The list of available Universal Print service endpoints.
        self._services: Optional[List[print_service.PrintService]] = None
        # Tenant-wide settings for the Universal Print service.
        self._settings: Optional[print_settings.PrintSettings] = None
        # The list of printer shares registered in the tenant.
        self._shares: Optional[List[printer_share.PrinterShare]] = None
        # List of abstract definition for a task that can be triggered when various events occur within Universal Print.
        self._task_definitions: Optional[List[print_task_definition.PrintTaskDefinition]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Print:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Print
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Print()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "connectors": lambda n : setattr(self, 'connectors', n.get_collection_of_object_values(print_connector.PrintConnector)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "operations": lambda n : setattr(self, 'operations', n.get_collection_of_object_values(print_operation.PrintOperation)),
            "printers": lambda n : setattr(self, 'printers', n.get_collection_of_object_values(printer.Printer)),
            "services": lambda n : setattr(self, 'services', n.get_collection_of_object_values(print_service.PrintService)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(print_settings.PrintSettings)),
            "shares": lambda n : setattr(self, 'shares', n.get_collection_of_object_values(printer_share.PrinterShare)),
            "task_definitions": lambda n : setattr(self, 'task_definitions', n.get_collection_of_object_values(print_task_definition.PrintTaskDefinition)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def operations(self,) -> Optional[List[print_operation.PrintOperation]]:
        """
        Gets the operations property value. The list of print long running operations.
        Returns: Optional[List[print_operation.PrintOperation]]
        """
        return self._operations
    
    @operations.setter
    def operations(self,value: Optional[List[print_operation.PrintOperation]] = None) -> None:
        """
        Sets the operations property value. The list of print long running operations.
        Args:
            value: Value to set for the operations property.
        """
        self._operations = value
    
    @property
    def printers(self,) -> Optional[List[printer.Printer]]:
        """
        Gets the printers property value. The list of printers registered in the tenant.
        Returns: Optional[List[printer.Printer]]
        """
        return self._printers
    
    @printers.setter
    def printers(self,value: Optional[List[printer.Printer]] = None) -> None:
        """
        Sets the printers property value. The list of printers registered in the tenant.
        Args:
            value: Value to set for the printers property.
        """
        self._printers = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("connectors", self.connectors)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("operations", self.operations)
        writer.write_collection_of_object_values("printers", self.printers)
        writer.write_collection_of_object_values("services", self.services)
        writer.write_object_value("settings", self.settings)
        writer.write_collection_of_object_values("shares", self.shares)
        writer.write_collection_of_object_values("taskDefinitions", self.task_definitions)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def services(self,) -> Optional[List[print_service.PrintService]]:
        """
        Gets the services property value. The list of available Universal Print service endpoints.
        Returns: Optional[List[print_service.PrintService]]
        """
        return self._services
    
    @services.setter
    def services(self,value: Optional[List[print_service.PrintService]] = None) -> None:
        """
        Sets the services property value. The list of available Universal Print service endpoints.
        Args:
            value: Value to set for the services property.
        """
        self._services = value
    
    @property
    def settings(self,) -> Optional[print_settings.PrintSettings]:
        """
        Gets the settings property value. Tenant-wide settings for the Universal Print service.
        Returns: Optional[print_settings.PrintSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[print_settings.PrintSettings] = None) -> None:
        """
        Sets the settings property value. Tenant-wide settings for the Universal Print service.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def shares(self,) -> Optional[List[printer_share.PrinterShare]]:
        """
        Gets the shares property value. The list of printer shares registered in the tenant.
        Returns: Optional[List[printer_share.PrinterShare]]
        """
        return self._shares
    
    @shares.setter
    def shares(self,value: Optional[List[printer_share.PrinterShare]] = None) -> None:
        """
        Sets the shares property value. The list of printer shares registered in the tenant.
        Args:
            value: Value to set for the shares property.
        """
        self._shares = value
    
    @property
    def task_definitions(self,) -> Optional[List[print_task_definition.PrintTaskDefinition]]:
        """
        Gets the taskDefinitions property value. List of abstract definition for a task that can be triggered when various events occur within Universal Print.
        Returns: Optional[List[print_task_definition.PrintTaskDefinition]]
        """
        return self._task_definitions
    
    @task_definitions.setter
    def task_definitions(self,value: Optional[List[print_task_definition.PrintTaskDefinition]] = None) -> None:
        """
        Sets the taskDefinitions property value. List of abstract definition for a task that can be triggered when various events occur within Universal Print.
        Args:
            value: Value to set for the taskDefinitions property.
        """
        self._task_definitions = value
    

