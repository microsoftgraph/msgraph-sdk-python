from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class ImSubPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new imSubPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The inumber1 property
        self._inumber1: Optional[json.Json] = None
        # The inumber2 property
        self._inumber2: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ImSubPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ImSubPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ImSubPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "inumber1": lambda n : setattr(self, 'inumber1', n.get_object_value(json.Json)),
            "inumber2": lambda n : setattr(self, 'inumber2', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def inumber1(self,) -> Optional[json.Json]:
        """
        Gets the inumber1 property value. The inumber1 property
        Returns: Optional[json.Json]
        """
        return self._inumber1
    
    @inumber1.setter
    def inumber1(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the inumber1 property value. The inumber1 property
        Args:
            value: Value to set for the inumber1 property.
        """
        self._inumber1 = value
    
    @property
    def inumber2(self,) -> Optional[json.Json]:
        """
        Gets the inumber2 property value. The inumber2 property
        Returns: Optional[json.Json]
        """
        return self._inumber2
    
    @inumber2.setter
    def inumber2(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the inumber2 property value. The inumber2 property
        Args:
            value: Value to set for the inumber2 property.
        """
        self._inumber2 = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("inumber1", self.inumber1)
        writer.write_object_value("inumber2", self.inumber2)
        writer.write_additional_data_value(self.additional_data)
    

