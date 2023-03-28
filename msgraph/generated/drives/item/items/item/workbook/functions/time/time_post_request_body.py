from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class TimePostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new timePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The hour property
        self._hour: Optional[json.Json] = None
        # The minute property
        self._minute: Optional[json.Json] = None
        # The second property
        self._second: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TimePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TimePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TimePostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "hour": lambda n : setattr(self, 'hour', n.get_object_value(json.Json)),
            "minute": lambda n : setattr(self, 'minute', n.get_object_value(json.Json)),
            "second": lambda n : setattr(self, 'second', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def hour(self,) -> Optional[json.Json]:
        """
        Gets the hour property value. The hour property
        Returns: Optional[json.Json]
        """
        return self._hour
    
    @hour.setter
    def hour(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the hour property value. The hour property
        Args:
            value: Value to set for the hour property.
        """
        self._hour = value
    
    @property
    def minute(self,) -> Optional[json.Json]:
        """
        Gets the minute property value. The minute property
        Returns: Optional[json.Json]
        """
        return self._minute
    
    @minute.setter
    def minute(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the minute property value. The minute property
        Args:
            value: Value to set for the minute property.
        """
        self._minute = value
    
    @property
    def second(self,) -> Optional[json.Json]:
        """
        Gets the second property value. The second property
        Returns: Optional[json.Json]
        """
        return self._second
    
    @second.setter
    def second(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the second property value. The second property
        Args:
            value: Value to set for the second property.
        """
        self._second = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("hour", self.hour)
        writer.write_object_value("minute", self.minute)
        writer.write_object_value("second", self.second)
        writer.write_additional_data_value(self.additional_data)
    

