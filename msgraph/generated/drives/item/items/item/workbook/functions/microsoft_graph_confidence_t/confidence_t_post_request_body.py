from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class Confidence_TPostRequestBody(AdditionalDataHolder, Parsable):
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
    def alpha(self,) -> Optional[json.Json]:
        """
        Gets the alpha property value. 
        Returns: Optional[json.Json]
        """
        return self._alpha
    
    @alpha.setter
    def alpha(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the alpha property value. 
        Args:
            value: Value to set for the alpha property.
        """
        self._alpha = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new confidence_TPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        self._alpha: Optional[json.Json] = None
        self._size: Optional[json.Json] = None
        self._standard_dev: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Confidence_TPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Confidence_TPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Confidence_TPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "alpha": lambda n : setattr(self, 'alpha', n.get_object_value(json.Json)),
            "size": lambda n : setattr(self, 'size', n.get_object_value(json.Json)),
            "standardDev": lambda n : setattr(self, 'standard_dev', n.get_object_value(json.Json)),
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
        writer.write_object_value("alpha", self.alpha)
        writer.write_object_value("size", self.size)
        writer.write_object_value("standardDev", self.standard_dev)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def size(self,) -> Optional[json.Json]:
        """
        Gets the size property value. 
        Returns: Optional[json.Json]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the size property value. 
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def standard_dev(self,) -> Optional[json.Json]:
        """
        Gets the standardDev property value. 
        Returns: Optional[json.Json]
        """
        return self._standard_dev
    
    @standard_dev.setter
    def standard_dev(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the standardDev property value. 
        Args:
            value: Value to set for the standardDev property.
        """
        self._standard_dev = value
    

