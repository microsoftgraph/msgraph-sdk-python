from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class FindBPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new findBPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The findText property
        self._find_text: Optional[json.Json] = None
        # The startNum property
        self._start_num: Optional[json.Json] = None
        # The withinText property
        self._within_text: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FindBPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FindBPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FindBPostRequestBody()
    
    @property
    def find_text(self,) -> Optional[json.Json]:
        """
        Gets the findText property value. The findText property
        Returns: Optional[json.Json]
        """
        return self._find_text
    
    @find_text.setter
    def find_text(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the findText property value. The findText property
        Args:
            value: Value to set for the find_text property.
        """
        self._find_text = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "findText": lambda n : setattr(self, 'find_text', n.get_object_value(json.Json)),
            "startNum": lambda n : setattr(self, 'start_num', n.get_object_value(json.Json)),
            "withinText": lambda n : setattr(self, 'within_text', n.get_object_value(json.Json)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("findText", self.find_text)
        writer.write_object_value("startNum", self.start_num)
        writer.write_object_value("withinText", self.within_text)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def start_num(self,) -> Optional[json.Json]:
        """
        Gets the startNum property value. The startNum property
        Returns: Optional[json.Json]
        """
        return self._start_num
    
    @start_num.setter
    def start_num(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the startNum property value. The startNum property
        Args:
            value: Value to set for the start_num property.
        """
        self._start_num = value
    
    @property
    def within_text(self,) -> Optional[json.Json]:
        """
        Gets the withinText property value. The withinText property
        Returns: Optional[json.Json]
        """
        return self._within_text
    
    @within_text.setter
    def within_text(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the withinText property value. The withinText property
        Args:
            value: Value to set for the within_text property.
        """
        self._within_text = value
    

