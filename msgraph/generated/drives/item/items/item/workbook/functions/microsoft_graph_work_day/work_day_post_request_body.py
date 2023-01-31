from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class WorkDayPostRequestBody(AdditionalDataHolder, Parsable):
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
        Instantiates a new workDayPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        self._days: Optional[json.Json] = None
        self._holidays: Optional[json.Json] = None
        self._start_date: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WorkDayPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WorkDayPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WorkDayPostRequestBody()
    
    @property
    def days(self,) -> Optional[json.Json]:
        """
        Gets the days property value. 
        Returns: Optional[json.Json]
        """
        return self._days
    
    @days.setter
    def days(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the days property value. 
        Args:
            value: Value to set for the days property.
        """
        self._days = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "days": lambda n : setattr(self, 'days', n.get_object_value(json.Json)),
            "holidays": lambda n : setattr(self, 'holidays', n.get_object_value(json.Json)),
            "startDate": lambda n : setattr(self, 'start_date', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def holidays(self,) -> Optional[json.Json]:
        """
        Gets the holidays property value. 
        Returns: Optional[json.Json]
        """
        return self._holidays
    
    @holidays.setter
    def holidays(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the holidays property value. 
        Args:
            value: Value to set for the holidays property.
        """
        self._holidays = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("days", self.days)
        writer.write_object_value("holidays", self.holidays)
        writer.write_object_value("startDate", self.start_date)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_date(self,) -> Optional[json.Json]:
        """
        Gets the startDate property value. 
        Returns: Optional[json.Json]
        """
        return self._start_date
    
    @start_date.setter
    def start_date(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the startDate property value. 
        Args:
            value: Value to set for the startDate property.
        """
        self._start_date = value
    

