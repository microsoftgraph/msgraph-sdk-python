from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_combination_configuration, authentication_method_modes, authentication_strength_policy_type, authentication_strength_requirements, entity

from . import entity

@dataclass
class AuthenticationStrengthPolicy(entity.Entity):
    # A collection of authentication method modes that are required be used to satify this authentication strength.
    allowed_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
    # Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.
    combination_configurations: Optional[List[authentication_combination_configuration.AuthenticationCombinationConfiguration]] = None
    # The datetime when this policy was created.
    created_date_time: Optional[datetime] = None
    # The human-readable description of this policy.
    description: Optional[str] = None
    # The human-readable display name of this policy. Supports $filter (eq, ne, not , and in).
    display_name: Optional[str] = None
    # The datetime when this policy was last modified.
    modified_date_time: Optional[datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The policyType property
    policy_type: Optional[authentication_strength_policy_type.AuthenticationStrengthPolicyType] = None
    # The requirementsSatisfied property
    requirements_satisfied: Optional[authentication_strength_requirements.AuthenticationStrengthRequirements] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationStrengthPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationStrengthPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationStrengthPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_combination_configuration, authentication_method_modes, authentication_strength_policy_type, authentication_strength_requirements, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "allowedCombinations": lambda n : setattr(self, 'allowed_combinations', n.get_collection_of_enum_values(authentication_method_modes.AuthenticationMethodModes)),
            "combinationConfigurations": lambda n : setattr(self, 'combination_configurations', n.get_collection_of_object_values(authentication_combination_configuration.AuthenticationCombinationConfiguration)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "modifiedDateTime": lambda n : setattr(self, 'modified_date_time', n.get_datetime_value()),
            "policyType": lambda n : setattr(self, 'policy_type', n.get_enum_value(authentication_strength_policy_type.AuthenticationStrengthPolicyType)),
            "requirementsSatisfied": lambda n : setattr(self, 'requirements_satisfied', n.get_enum_value(authentication_strength_requirements.AuthenticationStrengthRequirements)),
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
        writer.write_enum_value("allowedCombinations", self.allowed_combinations)
        writer.write_collection_of_object_values("combinationConfigurations", self.combination_configurations)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("modifiedDateTime", self.modified_date_time)
        writer.write_enum_value("policyType", self.policy_type)
        writer.write_enum_value("requirementsSatisfied", self.requirements_satisfied)
    

