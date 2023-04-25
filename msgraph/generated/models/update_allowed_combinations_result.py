from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_modes

class UpdateAllowedCombinationsResult(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new updateAllowedCombinationsResult and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Information about why the updateAllowedCombinations action was successful or failed.
        self._additional_information: Optional[str] = None
        # References to existing Conditional Access policies that use this authentication strength.
        self._conditional_access_references: Optional[List[str]] = None
        # The list of current authentication method combinations allowed by the authentication strength.
        self._current_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The list of former authentication method combinations allowed by the authentication strength before they were updated through the updateAllowedCombinations action.
        self._previous_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
    
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
    def additional_information(self,) -> Optional[str]:
        """
        Gets the additionalInformation property value. Information about why the updateAllowedCombinations action was successful or failed.
        Returns: Optional[str]
        """
        return self._additional_information
    
    @additional_information.setter
    def additional_information(self,value: Optional[str] = None) -> None:
        """
        Sets the additionalInformation property value. Information about why the updateAllowedCombinations action was successful or failed.
        Args:
            value: Value to set for the additional_information property.
        """
        self._additional_information = value
    
    @property
    def conditional_access_references(self,) -> Optional[List[str]]:
        """
        Gets the conditionalAccessReferences property value. References to existing Conditional Access policies that use this authentication strength.
        Returns: Optional[List[str]]
        """
        return self._conditional_access_references
    
    @conditional_access_references.setter
    def conditional_access_references(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the conditionalAccessReferences property value. References to existing Conditional Access policies that use this authentication strength.
        Args:
            value: Value to set for the conditional_access_references property.
        """
        self._conditional_access_references = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UpdateAllowedCombinationsResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UpdateAllowedCombinationsResult
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UpdateAllowedCombinationsResult()
    
    @property
    def current_combinations(self,) -> Optional[List[authentication_method_modes.AuthenticationMethodModes]]:
        """
        Gets the currentCombinations property value. The list of current authentication method combinations allowed by the authentication strength.
        Returns: Optional[List[authentication_method_modes.AuthenticationMethodModes]]
        """
        return self._current_combinations
    
    @current_combinations.setter
    def current_combinations(self,value: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None) -> None:
        """
        Sets the currentCombinations property value. The list of current authentication method combinations allowed by the authentication strength.
        Args:
            value: Value to set for the current_combinations property.
        """
        self._current_combinations = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_modes

        fields: Dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "conditionalAccessReferences": lambda n : setattr(self, 'conditional_access_references', n.get_collection_of_primitive_values(str)),
            "currentCombinations": lambda n : setattr(self, 'current_combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "previousCombinations": lambda n : setattr(self, 'previous_combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def previous_combinations(self,) -> Optional[List[authentication_method_modes.AuthenticationMethodModes]]:
        """
        Gets the previousCombinations property value. The list of former authentication method combinations allowed by the authentication strength before they were updated through the updateAllowedCombinations action.
        Returns: Optional[List[authentication_method_modes.AuthenticationMethodModes]]
        """
        return self._previous_combinations
    
    @previous_combinations.setter
    def previous_combinations(self,value: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None) -> None:
        """
        Sets the previousCombinations property value. The list of former authentication method combinations allowed by the authentication strength before they were updated through the updateAllowedCombinations action.
        Args:
            value: Value to set for the previous_combinations property.
        """
        self._previous_combinations = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_collection_of_primitive_values("conditionalAccessReferences", self.conditional_access_references)
        writer.write_enum_value("currentCombinations", self.current_combinations)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("previousCombinations", self.previous_combinations)
        writer.write_additional_data_value(self.additional_data)
    

