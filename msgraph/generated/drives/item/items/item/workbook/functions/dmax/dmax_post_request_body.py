from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class DmaxPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new dmaxPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The criteria property
        self._criteria: Optional[json.Json] = None
        # The database property
        self._database: Optional[json.Json] = None
        # The field property
        self._field: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DmaxPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DmaxPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DmaxPostRequestBody()
    
    @property
    def criteria(self,) -> Optional[json.Json]:
        """
        Gets the criteria property value. The criteria property
        Returns: Optional[json.Json]
        """
        return self._criteria
    
    @criteria.setter
    def criteria(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the criteria property value. The criteria property
        Args:
            value: Value to set for the criteria property.
        """
        self._criteria = value
    
    @property
    def database(self,) -> Optional[json.Json]:
        """
        Gets the database property value. The database property
        Returns: Optional[json.Json]
        """
        return self._database
    
    @database.setter
    def database(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the database property value. The database property
        Args:
            value: Value to set for the database property.
        """
        self._database = value
    
    @property
    def field(self,) -> Optional[json.Json]:
        """
        Gets the field property value. The field property
        Returns: Optional[json.Json]
        """
        return self._field
    
    @field.setter
    def field(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the field property value. The field property
        Args:
            value: Value to set for the field property.
        """
        self._field = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "criteria": lambda n : setattr(self, 'criteria', n.get_object_value(json.Json)),
            "database": lambda n : setattr(self, 'database', n.get_object_value(json.Json)),
            "field": lambda n : setattr(self, 'field', n.get_object_value(json.Json)),
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
        writer.write_object_value("criteria", self.criteria)
        writer.write_object_value("database", self.database)
        writer.write_object_value("field", self.field)
        writer.write_additional_data_value(self.additional_data)
    

