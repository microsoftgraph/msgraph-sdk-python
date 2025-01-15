from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_modes import AuthenticationMethodModes
    from .authentication_method_mode_detail import AuthenticationMethodModeDetail
    from .authentication_strength_policy import AuthenticationStrengthPolicy
    from .entity import Entity

from .entity import Entity

@dataclass
class AuthenticationStrengthRoot(Entity, Parsable):
    # Names and descriptions of all valid authentication method modes in the system.
    authentication_method_modes: Optional[list[AuthenticationMethodModeDetail]] = None
    # The combinations property
    combinations: Optional[list[AuthenticationMethodModes]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.
    policies: Optional[list[AuthenticationStrengthPolicy]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationStrengthRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrengthRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationStrengthRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_modes import AuthenticationMethodModes
        from .authentication_method_mode_detail import AuthenticationMethodModeDetail
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .entity import Entity

        from .authentication_method_modes import AuthenticationMethodModes
        from .authentication_method_mode_detail import AuthenticationMethodModeDetail
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMethodModes": lambda n : setattr(self, 'authentication_method_modes', n.get_collection_of_object_values(AuthenticationMethodModeDetail)),
            "combinations": lambda n : setattr(self, 'combinations', n.get_collection_of_enum_values(AuthenticationMethodModes)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(AuthenticationStrengthPolicy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("authenticationMethodModes", self.authentication_method_modes)
        writer.write_collection_of_enum_values("combinations", self.combinations)
        writer.write_collection_of_object_values("policies", self.policies)
    

