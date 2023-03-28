from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, print_usage_by_printer, print_usage_by_user

from . import entity

class PrintUsage(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new PrintUsage and sets the default values.
        """
        super().__init__()
        # The completedBlackAndWhiteJobCount property
        self._completed_black_and_white_job_count: Optional[int] = None
        # The completedColorJobCount property
        self._completed_color_job_count: Optional[int] = None
        # The incompleteJobCount property
        self._incomplete_job_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The usageDate property
        self._usage_date: Optional[date] = None
    
    @property
    def completed_black_and_white_job_count(self,) -> Optional[int]:
        """
        Gets the completedBlackAndWhiteJobCount property value. The completedBlackAndWhiteJobCount property
        Returns: Optional[int]
        """
        return self._completed_black_and_white_job_count
    
    @completed_black_and_white_job_count.setter
    def completed_black_and_white_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the completedBlackAndWhiteJobCount property value. The completedBlackAndWhiteJobCount property
        Args:
            value: Value to set for the completed_black_and_white_job_count property.
        """
        self._completed_black_and_white_job_count = value
    
    @property
    def completed_color_job_count(self,) -> Optional[int]:
        """
        Gets the completedColorJobCount property value. The completedColorJobCount property
        Returns: Optional[int]
        """
        return self._completed_color_job_count
    
    @completed_color_job_count.setter
    def completed_color_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the completedColorJobCount property value. The completedColorJobCount property
        Args:
            value: Value to set for the completed_color_job_count property.
        """
        self._completed_color_job_count = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintUsage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintUsage
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.printUsageByPrinter":
                from . import print_usage_by_printer

                return print_usage_by_printer.PrintUsageByPrinter()
            if mapping_value == "#microsoft.graph.printUsageByUser":
                from . import print_usage_by_user

                return print_usage_by_user.PrintUsageByUser()
        return PrintUsage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, print_usage_by_printer, print_usage_by_user

        fields: Dict[str, Callable[[Any], None]] = {
            "completedBlackAndWhiteJobCount": lambda n : setattr(self, 'completed_black_and_white_job_count', n.get_int_value()),
            "completedColorJobCount": lambda n : setattr(self, 'completed_color_job_count', n.get_int_value()),
            "incompleteJobCount": lambda n : setattr(self, 'incomplete_job_count', n.get_int_value()),
            "usageDate": lambda n : setattr(self, 'usage_date', n.get_date_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def incomplete_job_count(self,) -> Optional[int]:
        """
        Gets the incompleteJobCount property value. The incompleteJobCount property
        Returns: Optional[int]
        """
        return self._incomplete_job_count
    
    @incomplete_job_count.setter
    def incomplete_job_count(self,value: Optional[int] = None) -> None:
        """
        Sets the incompleteJobCount property value. The incompleteJobCount property
        Args:
            value: Value to set for the incomplete_job_count property.
        """
        self._incomplete_job_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("completedBlackAndWhiteJobCount", self.completed_black_and_white_job_count)
        writer.write_int_value("completedColorJobCount", self.completed_color_job_count)
        writer.write_int_value("incompleteJobCount", self.incomplete_job_count)
        writer.write_date_value("usageDate", self.usage_date)
    
    @property
    def usage_date(self,) -> Optional[date]:
        """
        Gets the usageDate property value. The usageDate property
        Returns: Optional[date]
        """
        return self._usage_date
    
    @usage_date.setter
    def usage_date(self,value: Optional[date] = None) -> None:
        """
        Sets the usageDate property value. The usageDate property
        Args:
            value: Value to set for the usage_date property.
        """
        self._usage_date = value
    

