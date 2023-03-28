from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class ComplexPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new complexPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The iNum property
        self._i_num: Optional[json.Json] = None
        # The realNum property
        self._real_num: Optional[json.Json] = None
        # The suffix property
        self._suffix: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ComplexPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ComplexPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ComplexPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "iNum": lambda n : setattr(self, 'i_num', n.get_object_value(json.Json)),
            "realNum": lambda n : setattr(self, 'real_num', n.get_object_value(json.Json)),
            "suffix": lambda n : setattr(self, 'suffix', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def i_num(self,) -> Optional[json.Json]:
        """
        Gets the iNum property value. The iNum property
        Returns: Optional[json.Json]
        """
        return self._i_num
    
    @i_num.setter
    def i_num(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the iNum property value. The iNum property
        Args:
            value: Value to set for the i_num property.
        """
        self._i_num = value
    
    @property
    def real_num(self,) -> Optional[json.Json]:
        """
        Gets the realNum property value. The realNum property
        Returns: Optional[json.Json]
        """
        return self._real_num
    
    @real_num.setter
    def real_num(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the realNum property value. The realNum property
        Args:
            value: Value to set for the real_num property.
        """
        self._real_num = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("iNum", self.i_num)
        writer.write_object_value("realNum", self.real_num)
        writer.write_object_value("suffix", self.suffix)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def suffix(self,) -> Optional[json.Json]:
        """
        Gets the suffix property value. The suffix property
        Returns: Optional[json.Json]
        """
        return self._suffix
    
    @suffix.setter
    def suffix(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the suffix property value. The suffix property
        Args:
            value: Value to set for the suffix property.
        """
        self._suffix = value
    

