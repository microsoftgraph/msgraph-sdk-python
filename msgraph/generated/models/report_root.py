from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import print_usage_by_printer, print_usage_by_user, security_reports_root

@dataclass
class ReportRoot(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The dailyPrintUsageByPrinter property
    daily_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
    # The dailyPrintUsageByUser property
    daily_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
    # The monthlyPrintUsageByPrinter property
    monthly_print_usage_by_printer: Optional[List[print_usage_by_printer.PrintUsageByPrinter]] = None
    # The monthlyPrintUsageByUser property
    monthly_print_usage_by_user: Optional[List[print_usage_by_user.PrintUsageByUser]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The security property
    security: Optional[security_reports_root.SecurityReportsRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReportRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReportRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ReportRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import print_usage_by_printer, print_usage_by_user, security_reports_root

        from . import print_usage_by_printer, print_usage_by_user, security_reports_root

        fields: Dict[str, Callable[[Any], None]] = {
            "dailyPrintUsageByPrinter": lambda n : setattr(self, 'daily_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "dailyPrintUsageByUser": lambda n : setattr(self, 'daily_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "monthlyPrintUsageByPrinter": lambda n : setattr(self, 'monthly_print_usage_by_printer', n.get_collection_of_object_values(print_usage_by_printer.PrintUsageByPrinter)),
            "monthlyPrintUsageByUser": lambda n : setattr(self, 'monthly_print_usage_by_user', n.get_collection_of_object_values(print_usage_by_user.PrintUsageByUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "security": lambda n : setattr(self, 'security', n.get_object_value(security_reports_root.SecurityReportsRoot)),
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
        writer.write_collection_of_object_values("dailyPrintUsageByPrinter", self.daily_print_usage_by_printer)
        writer.write_collection_of_object_values("dailyPrintUsageByUser", self.daily_print_usage_by_user)
        writer.write_collection_of_object_values("monthlyPrintUsageByPrinter", self.monthly_print_usage_by_printer)
        writer.write_collection_of_object_values("monthlyPrintUsageByUser", self.monthly_print_usage_by_user)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("security", self.security)
        writer.write_additional_data_value(self.additional_data)
    

