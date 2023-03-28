from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class MirrPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new mirrPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The financeRate property
        self._finance_rate: Optional[json.Json] = None
        # The reinvestRate property
        self._reinvest_rate: Optional[json.Json] = None
        # The values property
        self._values: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MirrPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MirrPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MirrPostRequestBody()
    
    @property
    def finance_rate(self,) -> Optional[json.Json]:
        """
        Gets the financeRate property value. The financeRate property
        Returns: Optional[json.Json]
        """
        return self._finance_rate
    
    @finance_rate.setter
    def finance_rate(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the financeRate property value. The financeRate property
        Args:
            value: Value to set for the finance_rate property.
        """
        self._finance_rate = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "financeRate": lambda n : setattr(self, 'finance_rate', n.get_object_value(json.Json)),
            "reinvestRate": lambda n : setattr(self, 'reinvest_rate', n.get_object_value(json.Json)),
            "values": lambda n : setattr(self, 'values', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def reinvest_rate(self,) -> Optional[json.Json]:
        """
        Gets the reinvestRate property value. The reinvestRate property
        Returns: Optional[json.Json]
        """
        return self._reinvest_rate
    
    @reinvest_rate.setter
    def reinvest_rate(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the reinvestRate property value. The reinvestRate property
        Args:
            value: Value to set for the reinvest_rate property.
        """
        self._reinvest_rate = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("financeRate", self.finance_rate)
        writer.write_object_value("reinvestRate", self.reinvest_rate)
        writer.write_object_value("values", self.values)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def values(self,) -> Optional[json.Json]:
        """
        Gets the values property value. The values property
        Returns: Optional[json.Json]
        """
        return self._values
    
    @values.setter
    def values(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the values property value. The values property
        Args:
            value: Value to set for the values property.
        """
        self._values = value
    

