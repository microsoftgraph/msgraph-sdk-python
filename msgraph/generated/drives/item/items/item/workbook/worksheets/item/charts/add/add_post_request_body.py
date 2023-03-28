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

        # The seriesBy property
        self._series_by: Optional[str] = None
        # The sourceData property
        self._source_data: Optional[json.Json] = None
        # The type property
        self._type: Optional[str] = None
    
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
            "seriesBy": lambda n : setattr(self, 'series_by', n.get_str_value()),
            "sourceData": lambda n : setattr(self, 'source_data', n.get_object_value(json.Json)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("seriesBy", self.series_by)
        writer.write_object_value("sourceData", self.source_data)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def series_by(self,) -> Optional[str]:
        """
        Gets the seriesBy property value. The seriesBy property
        Returns: Optional[str]
        """
        return self._series_by
    
    @series_by.setter
    def series_by(self,value: Optional[str] = None) -> None:
        """
        Sets the seriesBy property value. The seriesBy property
        Args:
            value: Value to set for the series_by property.
        """
        self._series_by = value
    
    @property
    def source_data(self,) -> Optional[json.Json]:
        """
        Gets the sourceData property value. The sourceData property
        Returns: Optional[json.Json]
        """
        return self._source_data
    
    @source_data.setter
    def source_data(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the sourceData property value. The sourceData property
        Args:
            value: Value to set for the source_data property.
        """
        self._source_data = value
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. The type property
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

