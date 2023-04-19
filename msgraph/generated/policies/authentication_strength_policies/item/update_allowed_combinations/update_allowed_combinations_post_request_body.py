from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models import authentication_method_modes

class UpdateAllowedCombinationsPostRequestBody(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new updateAllowedCombinationsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The allowedCombinations property
        self._allowed_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
    
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
    def allowed_combinations(self,) -> Optional[List[authentication_method_modes.AuthenticationMethodModes]]:
        """
        Gets the allowedCombinations property value. The allowedCombinations property
        Returns: Optional[List[authentication_method_modes.AuthenticationMethodModes]]
        """
        return self._allowed_combinations
    
    @allowed_combinations.setter
    def allowed_combinations(self,value: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None) -> None:
        """
        Sets the allowedCombinations property value. The allowedCombinations property
        Args:
            value: Value to set for the allowed_combinations property.
        """
        self._allowed_combinations = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateAllowedCombinationsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateAllowedCombinationsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateAllowedCombinationsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....models import authentication_method_modes

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedCombinations": lambda n : setattr(self, 'allowed_combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
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
        writer.write_enum_value("allowedCombinations", self.allowed_combinations)
        writer.write_additional_data_value(self.additional_data)
    

