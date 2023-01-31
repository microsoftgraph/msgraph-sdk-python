from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class WeekdayPostRequestBody(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new weekdayPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        self._return_type: Optional[json.Json] = None
        self._serial_number: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WeekdayPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WeekdayPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WeekdayPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "returnType": lambda n : setattr(self, 'return_type', n.get_object_value(json.Json)),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def return_type(self,) -> Optional[json.Json]:
        """
        Gets the returnType property value. 
        Returns: Optional[json.Json]
        """
        return self._return_type
    
    @return_type.setter
    def return_type(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the returnType property value. 
        Args:
            value: Value to set for the returnType property.
        """
        self._return_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("returnType", self.return_type)
        writer.write_object_value("serialNumber", self.serial_number)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def serial_number(self,) -> Optional[json.Json]:
        """
        Gets the serialNumber property value. 
        Returns: Optional[json.Json]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the serialNumber property value. 
        Args:
            value: Value to set for the serialNumber property.
        """
        self._serial_number = value
    

