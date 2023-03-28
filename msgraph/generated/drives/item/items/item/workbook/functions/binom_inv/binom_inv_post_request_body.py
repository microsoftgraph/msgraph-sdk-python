from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models import json

class Binom_InvPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new binom_InvPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The alpha property
        self._alpha: Optional[json.Json] = None
        # The probabilityS property
        self._probability_s: Optional[json.Json] = None
        # The trials property
        self._trials: Optional[json.Json] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Binom_InvPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Binom_InvPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Binom_InvPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ........models import json

        fields: Dict[str, Callable[[Any], None]] = {
            "alpha": lambda n : setattr(self, 'alpha', n.get_object_value(json.Json)),
            "probabilityS": lambda n : setattr(self, 'probability_s', n.get_object_value(json.Json)),
            "trials": lambda n : setattr(self, 'trials', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def probability_s(self,) -> Optional[json.Json]:
        """
        Gets the probabilityS property value. The probabilityS property
        Returns: Optional[json.Json]
        """
        return self._probability_s
    
    @probability_s.setter
    def probability_s(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the probabilityS property value. The probabilityS property
        Args:
            value: Value to set for the probability_s property.
        """
        self._probability_s = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("alpha", self.alpha)
        writer.write_object_value("probabilityS", self.probability_s)
        writer.write_object_value("trials", self.trials)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def trials(self,) -> Optional[json.Json]:
        """
        Gets the trials property value. The trials property
        Returns: Optional[json.Json]
        """
        return self._trials
    
    @trials.setter
    def trials(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the trials property value. The trials property
        Args:
            value: Value to set for the trials property.
        """
        self._trials = value
    

