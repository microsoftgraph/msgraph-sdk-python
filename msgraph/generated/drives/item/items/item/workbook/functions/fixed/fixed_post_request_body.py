from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class FixedPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new fixedPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The decimals property
        self._decimals: Optional[json.Json] = None
        # The noCommas property
        self._no_commas: Optional[json.Json] = None
        # The number property
        self._number: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FixedPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FixedPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FixedPostRequestBody()
    
    @property
    def decimals(self,) -> Optional[json.Json]:
        """
        Gets the decimals property value. The decimals property
        Returns: Optional[json.Json]
        """
        return self._decimals
    
    @decimals.setter
    def decimals(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the decimals property value. The decimals property
        Args:
            value: Value to set for the decimals property.
        """
        self._decimals = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "decimals": lambda n : setattr(self, 'decimals', n.get_object_value(json.Json)),
            "noCommas": lambda n : setattr(self, 'no_commas', n.get_object_value(json.Json)),
            "number": lambda n : setattr(self, 'number', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def no_commas(self,) -> Optional[json.Json]:
        """
        Gets the noCommas property value. The noCommas property
        Returns: Optional[json.Json]
        """
        return self._no_commas
    
    @no_commas.setter
    def no_commas(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the noCommas property value. The noCommas property
        Args:
            value: Value to set for the no_commas property.
        """
        self._no_commas = value
    
    @property
    def number(self,) -> Optional[json.Json]:
        """
        Gets the number property value. The number property
        Returns: Optional[json.Json]
        """
        return self._number
    
    @number.setter
    def number(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the number property value. The number property
        Args:
            value: Value to set for the number property.
        """
        self._number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("decimals", self.decimals)
        writer.write_object_value("noCommas", self.no_commas)
        writer.write_object_value("number", self.number)
        writer.write_additional_data_value(self.additional_data)
    

