from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_modes, entity, fido2_combination_configuration

from . import entity

@dataclass
class AuthenticationCombinationConfiguration(entity.Entity):
    # Which authentication method combinations this configuration applies to. Must be an allowedCombinations object that's defined for the authenticationStrengthPolicy. The only possible value for fido2combinationConfigurations is 'fido2'.
    applies_to_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationCombinationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationCombinationConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2CombinationConfiguration".casefold():
            from . import fido2_combination_configuration

            return fido2_combination_configuration.Fido2CombinationConfiguration()
        return AuthenticationCombinationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_modes, entity, fido2_combination_configuration

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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_enum_values("appliesToCombinations", self.applies_to_combinations)
    

