from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class Weibull_DistPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new weibull_DistPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The alpha property
        self._alpha: Optional[json.Json] = None
        # The beta property
        self._beta: Optional[json.Json] = None
        # The cumulative property
        self._cumulative: Optional[json.Json] = None
        # The x property
        self._x: Optional[json.Json] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Weibull_DistPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Weibull_DistPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Weibull_DistPostRequestBody()
    
    @property
    def cumulative(self,) -> Optional[json.Json]:
        """
        Gets the cumulative property value. The cumulative property
        Returns: Optional[json.Json]
        """
        return self._cumulative
    
    @cumulative.setter
    def cumulative(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the cumulative property value. The cumulative property
        Args:
            value: Value to set for the cumulative property.
        """
        self._cumulative = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "alpha": lambda n : setattr(self, 'alpha', n.get_object_value(json.Json)),
            "beta": lambda n : setattr(self, 'beta', n.get_object_value(json.Json)),
            "cumulative": lambda n : setattr(self, 'cumulative', n.get_object_value(json.Json)),
            "x": lambda n : setattr(self, 'x', n.get_object_value(json.Json)),
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
        writer.write_object_value("alpha", self.alpha)
        writer.write_object_value("beta", self.beta)
        writer.write_object_value("cumulative", self.cumulative)
        writer.write_object_value("x", self.x)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def x(self,) -> Optional[json.Json]:
        """
        Gets the x property value. The x property
        Returns: Optional[json.Json]
        """
        return self._x
    
    @x.setter
    def x(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the x property value. The x property
        Args:
            value: Value to set for the x property.
        """
        self._x = value
    

