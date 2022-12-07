from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
print_usage_by_printer = lazy_import('msgraph.generated.models.print_usage_by_printer')
print_usage_by_user = lazy_import('msgraph.generated.models.print_usage_by_user')
security_reports_root = lazy_import('msgraph.generated.models.security_reports_root')

class ReportRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new ReportRoot and sets the default values.
        """
        super().__init__()
        # The dailyPrintUsageByPrinter property
        self._daily_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
        # The dailyPrintUsageByUser property
        self._daily_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
        # The monthlyPrintUsageByPrinter property
        self._monthly_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
        # The monthlyPrintUsageByUser property
        self._monthly_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
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
            value: Value to set for the dailyPrintUsageByPrinter property.
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
            value: Value to set for the dailyPrintUsageByUser property.
        """
        self._daily_print_usage_by_user = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "daily_print_usage_by_printer": lambda n : setattr(self, 'daily_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "daily_print_usage_by_user": lambda n : setattr(self, 'daily_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "monthly_print_usage_by_printer": lambda n : setattr(self, 'monthly_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "monthly_print_usage_by_user": lambda n : setattr(self, 'monthly_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "security": lambda n : setattr(self, 'security', n.get_object_value(security_reports_root.SecurityReportsRoot)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
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
            value: Value to set for the monthlyPrintUsageByPrinter property.
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
            value: Value to set for the monthlyPrintUsageByUser property.
        """
        self._monthly_print_usage_by_user = value
    
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
        super().serialize(writer)
        writer.write_collection_of_object_values("dailyPrintUsageByPrinter", self.daily_print_usage_by_printer)
        writer.write_collection_of_object_values("dailyPrintUsageByUser", self.daily_print_usage_by_user)
        writer.write_collection_of_object_values("monthlyPrintUsageByPrinter", self.monthly_print_usage_by_printer)
        writer.write_collection_of_object_values("monthlyPrintUsageByUser", self.monthly_print_usage_by_user)
        writer.write_object_value("security", self.security)
    

