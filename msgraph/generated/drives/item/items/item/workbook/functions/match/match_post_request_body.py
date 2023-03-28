from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class MatchPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new matchPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The lookupArray property
        self._lookup_array: Optional[json.Json] = None
        # The lookupValue property
        self._lookup_value: Optional[json.Json] = None
        # The matchType property
        self._match_type: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MatchPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MatchPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MatchPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "lookupArray": lambda n : setattr(self, 'lookup_array', n.get_object_value(json.Json)),
            "lookupValue": lambda n : setattr(self, 'lookup_value', n.get_object_value(json.Json)),
            "matchType": lambda n : setattr(self, 'match_type', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def lookup_array(self,) -> Optional[json.Json]:
        """
        Gets the lookupArray property value. The lookupArray property
        Returns: Optional[json.Json]
        """
        return self._lookup_array
    
    @lookup_array.setter
    def lookup_array(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the lookupArray property value. The lookupArray property
        Args:
            value: Value to set for the lookup_array property.
        """
        self._lookup_array = value
    
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
    def match_type(self,) -> Optional[json.Json]:
        """
        Gets the matchType property value. The matchType property
        Returns: Optional[json.Json]
        """
        return self._match_type
    
    @match_type.setter
    def match_type(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the matchType property value. The matchType property
        Args:
            value: Value to set for the match_type property.
        """
        self._match_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("lookupArray", self.lookup_array)
        writer.write_object_value("lookupValue", self.lookup_value)
        writer.write_object_value("matchType", self.match_type)
        writer.write_additional_data_value(self.additional_data)
    

