from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class ReplaceBPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new replaceBPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The newText property
        self._new_text: Optional[json.Json] = None
        # The numBytes property
        self._num_bytes: Optional[json.Json] = None
        # The oldText property
        self._old_text: Optional[json.Json] = None
        # The startNum property
        self._start_num: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ReplaceBPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ReplaceBPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ReplaceBPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "newText": lambda n : setattr(self, 'new_text', n.get_object_value(json.Json)),
            "numBytes": lambda n : setattr(self, 'num_bytes', n.get_object_value(json.Json)),
            "oldText": lambda n : setattr(self, 'old_text', n.get_object_value(json.Json)),
            "startNum": lambda n : setattr(self, 'start_num', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def new_text(self,) -> Optional[json.Json]:
        """
        Gets the newText property value. The newText property
        Returns: Optional[json.Json]
        """
        return self._new_text
    
    @new_text.setter
    def new_text(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the newText property value. The newText property
        Args:
            value: Value to set for the new_text property.
        """
        self._new_text = value
    
    @property
    def num_bytes(self,) -> Optional[json.Json]:
        """
        Gets the numBytes property value. The numBytes property
        Returns: Optional[json.Json]
        """
        return self._num_bytes
    
    @num_bytes.setter
    def num_bytes(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the numBytes property value. The numBytes property
        Args:
            value: Value to set for the num_bytes property.
        """
        self._num_bytes = value
    
    @property
    def old_text(self,) -> Optional[json.Json]:
        """
        Gets the oldText property value. The oldText property
        Returns: Optional[json.Json]
        """
        return self._old_text
    
    @old_text.setter
    def old_text(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the oldText property value. The oldText property
        Args:
            value: Value to set for the old_text property.
        """
        self._old_text = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("newText", self.new_text)
        writer.write_object_value("numBytes", self.num_bytes)
        writer.write_object_value("oldText", self.old_text)
        writer.write_object_value("startNum", self.start_num)
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
    

