from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_modes, entity, fido2_combination_configuration

from . import entity

class AuthenticationCombinationConfiguration(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationCombinationConfiguration and sets the default values.
        """
        super().__init__()
        # Which authentication method combinations this configuration applies to. Must be an allowedCombinations object that's defined for the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
        self._applies_to_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def applies_to_combinations(self,) -> Optional[List[authentication_method_modes.AuthenticationMethodModes]]:
        """
        Gets the appliesToCombinations property value. Which authentication method combinations this configuration applies to. Must be an allowedCombinations object that's defined for the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
        Returns: Optional[List[authentication_method_modes.AuthenticationMethodModes]]
        """
        return self._applies_to_combinations
    
    @applies_to_combinations.setter
    def applies_to_combinations(self,value: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None) -> None:
        """
        Sets the appliesToCombinations property value. Which authentication method combinations this configuration applies to. Must be an allowedCombinations object that's defined for the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
        Args:
            value: Value to set for the applies_to_combinations property.
        """
        self._applies_to_combinations = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationCombinationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationCombinationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.fido2CombinationConfiguration":
                from . import fido2_combination_configuration

                return fido2_combination_configuration.Fido2CombinationConfiguration()
        return AuthenticationCombinationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_modes, entity, fido2_combination_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesToCombinations": lambda n : setattr(self, 'applies_to_combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("appliesToCombinations", self.applies_to_combinations)
    

