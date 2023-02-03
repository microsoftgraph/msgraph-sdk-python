from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

print_usage_by_printer = lazy_import('msgraph.generated.models.print_usage_by_printer')
print_usage_by_user = lazy_import('msgraph.generated.models.print_usage_by_user')
security_reports_root = lazy_import('msgraph.generated.models.security_reports_root')

class ReportRoot(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new ReportRoot and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The dailyPrintUsageByPrinter property
        self._daily_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
        # The dailyPrintUsageByUser property
        self._daily_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
        # The monthlyPrintUsageByPrinter property
        self._monthly_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
        # The monthlyPrintUsageByUser property
        self._monthly_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The security property
        self._security: Optional[security_reports_root.SecurityReportsRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReportRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReportRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReportRoot()
    
    @property
    def daily_print_usage_by_printer(self,) -> Optional[List[print_usage_by_printer.PrintUsageByPrinter]]:
        """
        Gets the dailyPrintUsageByPrinter property value. The dailyPrintUsageByPrinter property
        Returns: Optional[List[print_usage_by_printer.PrintUsageByPrinter]]
        """
        return self._daily_print_usage_by_printer
    
    @daily_print_usage_by_printer.setter
    def daily_print_usage_by_printer(self,value: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None) -> None:
        """
        Sets the dailyPrintUsageByPrinter property value. The dailyPrintUsageByPrinter property
        Args:
            value: Value to set for the daily_print_usage_by_printer property.
        """
        self._daily_print_usage_by_printer = value
    
    @property
    def daily_print_usage_by_user(self,) -> Optional[List[print_usage_by_user.PrintUsageByUser]]:
        """
        Gets the dailyPrintUsageByUser property value. The dailyPrintUsageByUser property
        Returns: Optional[List[print_usage_by_user.PrintUsageByUser]]
        """
        return self._daily_print_usage_by_user
    
    @daily_print_usage_by_user.setter
    def daily_print_usage_by_user(self,value: Optional[List[print_usage_by_user.PrintUsageByUser]] = None) -> None:
        """
        Sets the dailyPrintUsageByUser property value. The dailyPrintUsageByUser property
        Args:
            value: Value to set for the daily_print_usage_by_user property.
        """
        self._daily_print_usage_by_user = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "dailyPrintUsageByPrinter": lambda n : setattr(self, 'daily_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "dailyPrintUsageByUser": lambda n : setattr(self, 'daily_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "monthlyPrintUsageByPrinter": lambda n : setattr(self, 'monthly_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "monthlyPrintUsageByUser": lambda n : setattr(self, 'monthly_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "security": lambda n : setattr(self, 'security', n.get_object_value(security_reports_root.SecurityReportsRoot)),
        }
        return fields
    
    @property
    def monthly_print_usage_by_printer(self,) -> Optional[List[print_usage_by_printer.PrintUsageByPrinter]]:
        """
        Gets the monthlyPrintUsageByPrinter property value. The monthlyPrintUsageByPrinter property
        Returns: Optional[List[print_usage_by_printer.PrintUsageByPrinter]]
        """
        return self._monthly_print_usage_by_printer
    
    @monthly_print_usage_by_printer.setter
    def monthly_print_usage_by_printer(self,value: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None) -> None:
        """
        Sets the monthlyPrintUsageByPrinter property value. The monthlyPrintUsageByPrinter property
        Args:
            value: Value to set for the monthly_print_usage_by_printer property.
        """
        self._monthly_print_usage_by_printer = value
    
    @property
    def monthly_print_usage_by_user(self,) -> Optional[List[print_usage_by_user.PrintUsageByUser]]:
        """
        Gets the monthlyPrintUsageByUser property value. The monthlyPrintUsageByUser property
        Returns: Optional[List[print_usage_by_user.PrintUsageByUser]]
        """
        return self._monthly_print_usage_by_user
    
    @monthly_print_usage_by_user.setter
    def monthly_print_usage_by_user(self,value: Optional[List[print_usage_by_user.PrintUsageByUser]] = None) -> None:
        """
        Sets the monthlyPrintUsageByUser property value. The monthlyPrintUsageByUser property
        Args:
            value: Value to set for the monthly_print_usage_by_user property.
        """
        self._monthly_print_usage_by_user = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def security(self,) -> Optional[security_reports_root.SecurityReportsRoot]:
        """
        Gets the security property value. The security property
        Returns: Optional[security_reports_root.SecurityReportsRoot]
        """
        return self._security
    
    @security.setter
    def security(self,value: Optional[security_reports_root.SecurityReportsRoot] = None) -> None:
        """
        Sets the security property value. The security property
        Args:
            value: Value to set for the security property.
        """
        self._security = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_collection_of_object_values("dailyPrintUsageByPrinter", self.daily_print_usage_by_printer)
        writer.write_collection_of_object_values("dailyPrintUsageByUser", self.daily_print_usage_by_user)
        writer.write_collection_of_object_values("monthlyPrintUsageByPrinter", self.monthly_print_usage_by_printer)
        writer.write_collection_of_object_values("monthlyPrintUsageByUser", self.monthly_print_usage_by_user)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("security", self.security)
        writer.write_additional_data_value(self.additional_data)
    

