from __future__ import annotations
from datetime import date
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')

class PrintUsage(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
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
            value: Value to set for the completedBlackAndWhiteJobCount property.
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
            value: Value to set for the completedColorJobCount property.
        """
        self._completed_color_job_count = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new printUsage and sets the default values.
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
        self._usage_date: Optional[Date] = None
    
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
        return PrintUsage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "completed_black_and_white_job_count": lambda n : setattr(self, 'completed_black_and_white_job_count', n.get_int_value()),
            "completed_color_job_count": lambda n : setattr(self, 'completed_color_job_count', n.get_int_value()),
            "incomplete_job_count": lambda n : setattr(self, 'incomplete_job_count', n.get_int_value()),
            "usage_date": lambda n : setattr(self, 'usage_date', n.get_object_value(Date)),
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
            value: Value to set for the incompleteJobCount property.
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
        writer.write_object_value("usageDate", self.usage_date)
    
    @property
    def usage_date(self,) -> Optional[Date]:
        """
        Gets the usageDate property value. The usageDate property
        Returns: Optional[Date]
        """
        return self._usage_date
    
    @usage_date.setter
    def usage_date(self,value: Optional[Date] = None) -> None:
        """
        Sets the usageDate property value. The usageDate property
        Args:
            value: Value to set for the usageDate property.
        """
        self._usage_date = value
    

