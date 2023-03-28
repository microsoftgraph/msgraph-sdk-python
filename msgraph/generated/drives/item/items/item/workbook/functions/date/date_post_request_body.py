from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class DatePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new datePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The day property
        self._day: Optional[json.Json] = None
        # The month property
        self._month: Optional[json.Json] = None
        # The year property
        self._year: Optional[json.Json] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DatePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DatePostRequestBody()
    
    @property
    def day(self,) -> Optional[json.Json]:
        """
        Gets the day property value. The day property
        Returns: Optional[json.Json]
        """
        return self._day
    
    @day.setter
    def day(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the day property value. The day property
        Args:
            value: Value to set for the day property.
        """
        self._day = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "day": lambda n : setattr(self, 'day', n.get_object_value(json.Json)),
            "month": lambda n : setattr(self, 'month', n.get_object_value(json.Json)),
            "year": lambda n : setattr(self, 'year', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def month(self,) -> Optional[json.Json]:
        """
        Gets the month property value. The month property
        Returns: Optional[json.Json]
        """
        return self._month
    
    @month.setter
    def month(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the month property value. The month property
        Args:
            value: Value to set for the month property.
        """
        self._month = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("day", self.day)
        writer.write_object_value("month", self.month)
        writer.write_object_value("year", self.year)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def year(self,) -> Optional[json.Json]:
        """
        Gets the year property value. The year property
        Returns: Optional[json.Json]
        """
        return self._year
    
    @year.setter
    def year(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the year property value. The year property
        Args:
            value: Value to set for the year property.
        """
        self._year = value
    

