from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class ErfPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new erfPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The lowerLimit property
        self._lower_limit: Optional[json.Json] = None
        # The upperLimit property
        self._upper_limit: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ErfPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ErfPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ErfPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "lowerLimit": lambda n : setattr(self, 'lower_limit', n.get_object_value(json.Json)),
            "upperLimit": lambda n : setattr(self, 'upper_limit', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def lower_limit(self,) -> Optional[json.Json]:
        """
        Gets the lowerLimit property value. The lowerLimit property
        Returns: Optional[json.Json]
        """
        return self._lower_limit
    
    @lower_limit.setter
    def lower_limit(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the lowerLimit property value. The lowerLimit property
        Args:
            value: Value to set for the lower_limit property.
        """
        self._lower_limit = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("lowerLimit", self.lower_limit)
        writer.write_object_value("upperLimit", self.upper_limit)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def upper_limit(self,) -> Optional[json.Json]:
        """
        Gets the upperLimit property value. The upperLimit property
        Returns: Optional[json.Json]
        """
        return self._upper_limit
    
    @upper_limit.setter
    def upper_limit(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the upperLimit property value. The upperLimit property
        Args:
            value: Value to set for the upper_limit property.
        """
        self._upper_limit = value
    

