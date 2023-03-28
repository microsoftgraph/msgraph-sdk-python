from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..........models import json

class AddPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new addPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The index property
        self._index: Optional[int] = None
        # The name property
        self._name: Optional[str] = None
        # The values property
        self._values: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AddPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AddPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AddPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "index": lambda n : setattr(self, 'index', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "values": lambda n : setattr(self, 'values', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def index(self,) -> Optional[int]:
        """
        Gets the index property value. The index property
        Returns: Optional[int]
        """
        return self._index
    
    @index.setter
    def index(self,value: Optional[int] = None) -> None:
        """
        Sets the index property value. The index property
        Args:
            value: Value to set for the index property.
        """
        self._index = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name property
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name property
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("index", self.index)
        writer.write_str_value("name", self.name)
        writer.write_object_value("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def values(self,) -> Optional[json.Json]:
        """
        Gets the values property value. The values property
        Returns: Optional[json.Json]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the values property value. The values property
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

