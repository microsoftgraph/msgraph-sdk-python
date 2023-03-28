from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class F_InvPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new f_InvPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The degFreedom1 property
        self._deg_freedom1: Optional[json.Json] = None
        # The degFreedom2 property
        self._deg_freedom2: Optional[json.Json] = None
        # The probability property
        self._probability: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> F_InvPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: F_InvPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return F_InvPostRequestBody()
    
    @property
    def deg_freedom1(self,) -> Optional[json.Json]:
        """
        Gets the degFreedom1 property value. The degFreedom1 property
        Returns: Optional[json.Json]
        """
        return self._deg_freedom1
    
    @deg_freedom1.setter
    def deg_freedom1(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the degFreedom1 property value. The degFreedom1 property
        Args:
            value: Value to set for the deg_freedom1 property.
        """
        self._deg_freedom1 = value
    
    @property
    def deg_freedom2(self,) -> Optional[json.Json]:
        """
        Gets the degFreedom2 property value. The degFreedom2 property
        Returns: Optional[json.Json]
        """
        return self._deg_freedom2
    
    @deg_freedom2.setter
    def deg_freedom2(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the degFreedom2 property value. The degFreedom2 property
        Args:
            value: Value to set for the deg_freedom2 property.
        """
        self._deg_freedom2 = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "degFreedom1": lambda n : setattr(self, 'deg_freedom1', n.get_object_value(json.Json)),
            "degFreedom2": lambda n : setattr(self, 'deg_freedom2', n.get_object_value(json.Json)),
            "probability": lambda n : setattr(self, 'probability', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def probability(self,) -> Optional[json.Json]:
        """
        Gets the probability property value. The probability property
        Returns: Optional[json.Json]
        """
        return self._probability
    
    @probability.setter
    def probability(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the probability property value. The probability property
        Args:
            value: Value to set for the probability property.
        """
        self._probability = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("degFreedom1", self.deg_freedom1)
        writer.write_object_value("degFreedom2", self.deg_freedom2)
        writer.write_object_value("probability", self.probability)
        writer.write_additional_data_value(self.additional_data)
    

