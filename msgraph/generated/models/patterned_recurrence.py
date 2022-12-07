from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

recurrence_pattern = lazy_import('msgraph.generated.models.recurrence_pattern')
recurrence_range = lazy_import('msgraph.generated.models.recurrence_range')

class PatternedRecurrence(AdditionalDataHolder, Parsable):
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
        Instantiates a new patternedRecurrence and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The frequency of an event.  For access reviews: Do not specify this property for a one-time access review.  Only interval, dayOfMonth, and type (weekly, absoluteMonthly) properties of recurrencePattern are supported.
        self._pattern: Optional[recurrence_pattern.RecurrencePattern] = None
        # The duration of an event.
        self._range: Optional[recurrence_range.RecurrenceRange] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PatternedRecurrence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PatternedRecurrence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return PatternedRecurrence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "pattern": lambda n : setattr(self, 'pattern', n.get_object_value(recurrence_pattern.RecurrencePattern)),
            "range": lambda n : setattr(self, 'range', n.get_object_value(recurrence_range.RecurrenceRange)),
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
    def pattern(self,) -> Optional[recurrence_pattern.RecurrencePattern]:
        """
        Gets the pattern property value. The frequency of an event.  For access reviews: Do not specify this property for a one-time access review.  Only interval, dayOfMonth, and type (weekly, absoluteMonthly) properties of recurrencePattern are supported.
        Returns: Optional[recurrence_pattern.RecurrencePattern]
        """
        return self._pattern
    
    @pattern.setter
    def pattern(self,value: Optional[recurrence_pattern.RecurrencePattern] = None) -> None:
        """
        Sets the pattern property value. The frequency of an event.  For access reviews: Do not specify this property for a one-time access review.  Only interval, dayOfMonth, and type (weekly, absoluteMonthly) properties of recurrencePattern are supported.
        Args:
            value: Value to set for the pattern property.
        """
        self._pattern = value
    
    @property
    def range(self,) -> Optional[recurrence_range.RecurrenceRange]:
        """
        Gets the range property value. The duration of an event.
        Returns: Optional[recurrence_range.RecurrenceRange]
        """
        return self._range
    
    @range.setter
    def range(self,value: Optional[recurrence_range.RecurrenceRange] = None) -> None:
        """
        Sets the range property value. The duration of an event.
        Args:
            value: Value to set for the range property.
        """
        self._range = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("pattern", self.pattern)
        writer.write_object_value("range", self.range)
        writer.write_additional_data_value(self.additional_data)
    

