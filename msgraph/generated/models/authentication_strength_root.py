from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_modes, authentication_method_mode_detail, authentication_strength_policy, entity

from . import entity

@dataclass
class AuthenticationStrengthRoot(entity.Entity):
    # Names and descriptions of all valid authentication method modes in the system.
    authentication_method_modes: Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]] = None
    # The combinations property
    combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.
    policies: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationStrengthRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrengthRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationStrengthRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_modes, authentication_method_mode_detail, authentication_strength_policy, entity

        from . import authentication_method_modes, authentication_method_mode_detail, authentication_strength_policy, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethodModes": lambda n : setattr(self, 'authentication_method_modes', n.get_collection_of_object_values(authentication_method_mode_detail.AuthenticationMethodModeDetail)),
            "combinations": lambda n : setattr(self, 'combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(authentication_strength_policy.AuthenticationStrengthPolicy)),
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
        writer.write_collection_of_object_values("authenticationMethodModes", self.authentication_method_modes)
        writer.write_collection_of_enum_values("combinations", self.combinations)
        writer.write_collection_of_object_values("policies", self.policies)
    

