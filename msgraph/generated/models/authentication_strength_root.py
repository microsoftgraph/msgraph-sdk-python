from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_modes, authentication_method_mode_detail, authentication_strength_policy, entity

from . import entity

class AuthenticationStrengthRoot(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationStrengthRoot and sets the default values.
        """
        super().__init__()
        # Names and descriptions of all valid authentication method modes in the system.
        self._authentication_method_modes: Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]] = None
        # The combinations property
        self._combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.
        self._policies: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]] = None
    
    @property
    def authentication_method_modes(self,) -> Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]]:
        """
        Gets the authenticationMethodModes property value. Names and descriptions of all valid authentication method modes in the system.
        Returns: Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]]
        """
        return self._authentication_method_modes
    
    @authentication_method_modes.setter
    def authentication_method_modes(self,value: Optional[List[authentication_method_mode_detail.AuthenticationMethodModeDetail]] = None) -> None:
        """
        Sets the authenticationMethodModes property value. Names and descriptions of all valid authentication method modes in the system.
        Args:
            value: Value to set for the authentication_method_modes property.
        """
        self._authentication_method_modes = value
    
    @property
    def combinations(self,) -> Optional[List[authentication_method_modes.AuthenticationMethodModes]]:
        """
        Gets the combinations property value. The combinations property
        Returns: Optional[List[authentication_method_modes.AuthenticationMethodModes]]
        """
        return self._combinations
    
    @combinations.setter
    def combinations(self,value: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None) -> None:
        """
        Sets the combinations property value. The combinations property
        Args:
            value: Value to set for the combinations property.
        """
        self._combinations = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationStrengthRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrengthRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationStrengthRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_modes, authentication_method_mode_detail, authentication_strength_policy, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMethodModes": lambda n : setattr(self, 'authentication_method_modes', n.get_collection_of_object_values(authentication_method_mode_detail.AuthenticationMethodModeDetail)),
            "combinations": lambda n : setattr(self, 'combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
            "policies": lambda n : setattr(self, 'policies', n.get_collection_of_object_values(authentication_strength_policy.AuthenticationStrengthPolicy)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def policies(self,) -> Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]]:
        """
        Gets the policies property value. A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.
        Returns: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]]
        """
        return self._policies
    
    @policies.setter
    def policies(self,value: Optional[List[authentication_strength_policy.AuthenticationStrengthPolicy]] = None) -> None:
        """
        Sets the policies property value. A collection of authentication strength policies that exist for this tenant, including both built-in and custom policies.
        Args:
            value: Value to set for the policies property.
        """
        self._policies = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("authenticationMethodModes", self.authentication_method_modes)
        writer.write_enum_value("combinations", self.combinations)
        writer.write_collection_of_object_values("policies", self.policies)
    

