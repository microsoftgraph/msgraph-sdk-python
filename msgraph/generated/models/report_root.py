from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_methods_root import AuthenticationMethodsRoot
    from .partners.partners import Partners
    from .print_usage_by_printer import PrintUsageByPrinter
    from .print_usage_by_user import PrintUsageByUser
    from .security_reports_root import SecurityReportsRoot

@dataclass
class ReportRoot(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Container for navigation properties for Microsoft Entra authentication methods resources.
    authentication_methods: Optional[AuthenticationMethodsRoot] = None
    # Retrieve a list of daily print usage summaries, grouped by printer.
    daily_print_usage_by_printer: Optional[list[PrintUsageByPrinter]] = None
    # Retrieve a list of daily print usage summaries, grouped by user.
    daily_print_usage_by_user: Optional[list[PrintUsageByUser]] = None
    # Retrieve a list of monthly print usage summaries, grouped by printer.
    monthly_print_usage_by_printer: Optional[list[PrintUsageByPrinter]] = None
    # Retrieve a list of monthly print usage summaries, grouped by user.
    monthly_print_usage_by_user: Optional[list[PrintUsageByUser]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents billing details for a Microsoft direct partner.
    partners: Optional[Partners] = None
    # Represents an abstract type that contains resources for attack simulation and training reports.
    security: Optional[SecurityReportsRoot] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ReportRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ReportRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ReportRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_methods_root import AuthenticationMethodsRoot
        from .partners.partners import Partners
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser
        from .security_reports_root import SecurityReportsRoot

        from .authentication_methods_root import AuthenticationMethodsRoot
        from .partners.partners import Partners
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser
        from .security_reports_root import SecurityReportsRoot

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethods": lambda n : setattr(self, 'authentication_methods', n.get_object_value(AuthenticationMethodsRoot)),
            "dailyPrintUsageByPrinter": lambda n : setattr(self, 'daily_print_usage_by_printer', n.get_collection_of_object_values(PrintUsageByPrinter)),
            "dailyPrintUsageByUser": lambda n : setattr(self, 'daily_print_usage_by_user', n.get_collection_of_object_values(PrintUsageByUser)),
            "monthlyPrintUsageByPrinter": lambda n : setattr(self, 'monthly_print_usage_by_printer', n.get_collection_of_object_values(PrintUsageByPrinter)),
            "monthlyPrintUsageByUser": lambda n : setattr(self, 'monthly_print_usage_by_user', n.get_collection_of_object_values(PrintUsageByUser)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "partners": lambda n : setattr(self, 'partners', n.get_object_value(Partners)),
            "security": lambda n : setattr(self, 'security', n.get_object_value(SecurityReportsRoot)),
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
        writer.write_object_value("authenticationMethods", self.authentication_methods)
        writer.write_collection_of_object_values("dailyPrintUsageByPrinter", self.daily_print_usage_by_printer)
        writer.write_collection_of_object_values("dailyPrintUsageByUser", self.daily_print_usage_by_user)
        writer.write_collection_of_object_values("monthlyPrintUsageByPrinter", self.monthly_print_usage_by_printer)
        writer.write_collection_of_object_values("monthlyPrintUsageByUser", self.monthly_print_usage_by_user)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("partners", self.partners)
        writer.write_object_value("security", self.security)
        writer.write_additional_data_value(self.additional_data)
    

