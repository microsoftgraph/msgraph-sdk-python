from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class ReptPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new reptPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The numberTimes property
        self._number_times: Optional[json.Json] = None
        # The text property
        self._text: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReptPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReptPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReptPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "numberTimes": lambda n : setattr(self, 'number_times', n.get_object_value(json.Json)),
            "text": lambda n : setattr(self, 'text', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def number_times(self,) -> Optional[json.Json]:
        """
        Gets the numberTimes property value. The numberTimes property
        Returns: Optional[json.Json]
        """
        return self._number_times
    
    @number_times.setter
    def number_times(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numberTimes property value. The numberTimes property
        Args:
            value: Value to set for the number_times property.
        """
        self._number_times = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("numberTimes", self.number_times)
        writer.write_object_value("text", self.text)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def text(self,) -> Optional[json.Json]:
        """
        Gets the text property value. The text property
        Returns: Optional[json.Json]
        """
        return self._text
    
    @text.setter
    def text(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the text property value. The text property
        Args:
            value: Value to set for the text property.
        """
        self._text = value
    

