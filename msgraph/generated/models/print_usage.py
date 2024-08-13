from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .print_usage_by_printer import PrintUsageByPrinter
    from .print_usage_by_user import PrintUsageByUser

from .entity import Entity

@dataclass
class PrintUsage(Entity):
    # The blackAndWhitePageCount property
    black_and_white_page_count: Optional[int] = None
    # The colorPageCount property
    color_page_count: Optional[int] = None
    # The completedBlackAndWhiteJobCount property
    completed_black_and_white_job_count: Optional[int] = None
    # The completedColorJobCount property
    completed_color_job_count: Optional[int] = None
    # The completedJobCount property
    completed_job_count: Optional[int] = None
    # The doubleSidedSheetCount property
    double_sided_sheet_count: Optional[int] = None
    # The incompleteJobCount property
    incomplete_job_count: Optional[int] = None
    # The mediaSheetCount property
    media_sheet_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The pageCount property
    page_count: Optional[int] = None
    # The singleSidedSheetCount property
    single_sided_sheet_count: Optional[int] = None
    # The usageDate property
    usage_date: Optional[datetime.date] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrintUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrintUsage
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsageByPrinter".casefold():
            from .print_usage_by_printer import PrintUsageByPrinter

            return PrintUsageByPrinter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsageByUser".casefold():
            from .print_usage_by_user import PrintUsageByUser

            return PrintUsageByUser()
        return PrintUsage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser

        from .entity import Entity
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser

        fields: Dict[str, Callable[[Any], None]] = {
            "blackAndWhitePageCount": lambda n : setattr(self, 'black_and_white_page_count', n.get_int_value()),
            "colorPageCount": lambda n : setattr(self, 'color_page_count', n.get_int_value()),
            "completedBlackAndWhiteJobCount": lambda n : setattr(self, 'completed_black_and_white_job_count', n.get_int_value()),
            "completedColorJobCount": lambda n : setattr(self, 'completed_color_job_count', n.get_int_value()),
            "completedJobCount": lambda n : setattr(self, 'completed_job_count', n.get_int_value()),
            "doubleSidedSheetCount": lambda n : setattr(self, 'double_sided_sheet_count', n.get_int_value()),
            "incompleteJobCount": lambda n : setattr(self, 'incomplete_job_count', n.get_int_value()),
            "mediaSheetCount": lambda n : setattr(self, 'media_sheet_count', n.get_int_value()),
            "pageCount": lambda n : setattr(self, 'page_count', n.get_int_value()),
            "singleSidedSheetCount": lambda n : setattr(self, 'single_sided_sheet_count', n.get_int_value()),
            "usageDate": lambda n : setattr(self, 'usage_date', n.get_date_value()),
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
        writer.write_int_value("blackAndWhitePageCount", self.black_and_white_page_count)
        writer.write_int_value("colorPageCount", self.color_page_count)
        writer.write_int_value("completedBlackAndWhiteJobCount", self.completed_black_and_white_job_count)
        writer.write_int_value("completedColorJobCount", self.completed_color_job_count)
        writer.write_int_value("completedJobCount", self.completed_job_count)
        writer.write_int_value("doubleSidedSheetCount", self.double_sided_sheet_count)
        writer.write_int_value("incompleteJobCount", self.incomplete_job_count)
        writer.write_int_value("mediaSheetCount", self.media_sheet_count)
        writer.write_int_value("pageCount", self.page_count)
        writer.write_int_value("singleSidedSheetCount", self.single_sided_sheet_count)
        writer.write_date_value("usageDate", self.usage_date)
    

