from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class RandBetweenPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new randBetweenPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The bottom property
        self._bottom: Optional[json.Json] = None
        # The top property
        self._top: Optional[json.Json] = None
    
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
    
    @property
    def bottom(self,) -> Optional[json.Json]:
        """
        Gets the bottom property value. The bottom property
        Returns: Optional[json.Json]
        """
        return self._bottom
    
    @bottom.setter
    def bottom(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the bottom property value. The bottom property
        Args:
            value: Value to set for the bottom property.
        """
        self._bottom = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RandBetweenPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RandBetweenPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RandBetweenPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "bottom": lambda n : setattr(self, 'bottom', n.get_object_value(json.Json)),
            "top": lambda n : setattr(self, 'top', n.get_object_value(json.Json)),
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
        writer.write_object_value("bottom", self.bottom)
        writer.write_object_value("top", self.top)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def top(self,) -> Optional[json.Json]:
        """
        Gets the top property value. The top property
        Returns: Optional[json.Json]
        """
        return self._top
    
    @top.setter
    def top(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the top property value. The top property
        Args:
            value: Value to set for the top property.
        """
        self._top = value
    

