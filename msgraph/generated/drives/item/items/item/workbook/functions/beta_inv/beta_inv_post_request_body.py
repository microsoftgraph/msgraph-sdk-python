from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class Beta_InvPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new beta_InvPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The A property
        self._a: Optional[json.Json] = None
        # The alpha property
        self._alpha: Optional[json.Json] = None
        # The B property
        self._b: Optional[json.Json] = None
        # The beta property
        self._beta: Optional[json.Json] = None
        # The probability property
        self._probability: Optional[json.Json] = None
    
    @property
    def a(self,) -> Optional[json.Json]:
        """
        Gets the a property value. The A property
        Returns: Optional[json.Json]
        """
        return self._a
    
    @a.setter
    def a(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the a property value. The A property
        Args:
            value: Value to set for the A property.
        """
        self._a = value
    
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
    
    @property
    def alpha(self,) -> Optional[json.Json]:
        """
        Gets the alpha property value. The alpha property
        Returns: Optional[json.Json]
        """
        return self._alpha
    
    @alpha.setter
    def alpha(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the alpha property value. The alpha property
        Args:
            value: Value to set for the alpha property.
        """
        self._alpha = value
    
    @property
    def b(self,) -> Optional[json.Json]:
        """
        Gets the b property value. The B property
        Returns: Optional[json.Json]
        """
        return self._b
    
    @b.setter
    def b(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the b property value. The B property
        Args:
            value: Value to set for the B property.
        """
        self._b = value
    
    @property
    def beta(self,) -> Optional[json.Json]:
        """
        Gets the beta property value. The beta property
        Returns: Optional[json.Json]
        """
        return self._beta
    
    @beta.setter
    def beta(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the beta property value. The beta property
        Args:
            value: Value to set for the beta property.
        """
        self._beta = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Beta_InvPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Beta_InvPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Beta_InvPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "A": lambda n : setattr(self, 'a', n.get_object_value(json.Json)),
            "alpha": lambda n : setattr(self, 'alpha', n.get_object_value(json.Json)),
            "B": lambda n : setattr(self, 'b', n.get_object_value(json.Json)),
            "beta": lambda n : setattr(self, 'beta', n.get_object_value(json.Json)),
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
        writer.write_object_value("A", self.a)
        writer.write_object_value("alpha", self.alpha)
        writer.write_object_value("B", self.b)
        writer.write_object_value("beta", self.beta)
        writer.write_object_value("probability", self.probability)
        writer.write_additional_data_value(self.additional_data)
    

