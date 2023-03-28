from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class LookupPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new lookupPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The lookupValue property
        self._lookup_value: Optional[json.Json] = None
        # The lookupVector property
        self._lookup_vector: Optional[json.Json] = None
        # The resultVector property
        self._result_vector: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LookupPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LookupPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LookupPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "lookupValue": lambda n : setattr(self, 'lookup_value', n.get_object_value(json.Json)),
            "lookupVector": lambda n : setattr(self, 'lookup_vector', n.get_object_value(json.Json)),
            "resultVector": lambda n : setattr(self, 'result_vector', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def lookup_value(self,) -> Optional[json.Json]:
        """
        Gets the lookupValue property value. The lookupValue property
        Returns: Optional[json.Json]
        """
        return self._lookup_value
    
    @lookup_value.setter
    def lookup_value(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the lookupValue property value. The lookupValue property
        Args:
            value: Value to set for the lookup_value property.
        """
        self._lookup_value = value
    
    @property
    def lookup_vector(self,) -> Optional[json.Json]:
        """
        Gets the lookupVector property value. The lookupVector property
        Returns: Optional[json.Json]
        """
        return self._lookup_vector
    
    @lookup_vector.setter
    def lookup_vector(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the lookupVector property value. The lookupVector property
        Args:
            value: Value to set for the lookup_vector property.
        """
        self._lookup_vector = value
    
    @property
    def result_vector(self,) -> Optional[json.Json]:
        """
        Gets the resultVector property value. The resultVector property
        Returns: Optional[json.Json]
        """
        return self._result_vector
    
    @result_vector.setter
    def result_vector(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the resultVector property value. The resultVector property
        Args:
            value: Value to set for the result_vector property.
        """
        self._result_vector = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("lookupValue", self.lookup_value)
        writer.write_object_value("lookupVector", self.lookup_vector)
        writer.write_object_value("resultVector", self.result_vector)
        writer.write_additional_data_value(self.additional_data)
    

