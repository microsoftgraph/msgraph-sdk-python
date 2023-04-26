from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_combination_configuration, authentication_method_modes, authentication_strength_policy_type, authentication_strength_requirements, entity

from . import entity

class AuthenticationStrengthPolicy(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new AuthenticationStrengthPolicy and sets the default values.
        """
        super().__init__()
        # A collection of authentication method modes that are required be used to satify this authentication strength.
        self._allowed_combinations: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None
        # Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.
        self._combination_configurations: Optional[List[authentication_combination_configuration.AuthenticationCombinationConfiguration]] = None
        # The datetime when this policy was created.
        self._created_date_time: Optional[datetime] = None
        # The human-readable description of this policy.
        self._description: Optional[str] = None
        # The human-readable display name of this policy. Supports $filter (eq, ne, not , and in).
        self._display_name: Optional[str] = None
        # The datetime when this policy was last modified.
        self._modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The policyType property
        self._policy_type: Optional[authentication_strength_policy_type.AuthenticationStrengthPolicyType] = None
        # The requirementsSatisfied property
        self._requirements_satisfied: Optional[authentication_strength_requirements.AuthenticationStrengthRequirements] = None
    
    @property
    def allowed_combinations(self,) -> Optional[List[authentication_method_modes.AuthenticationMethodModes]]:
        """
        Gets the allowedCombinations property value. A collection of authentication method modes that are required be used to satify this authentication strength.
        Returns: Optional[List[authentication_method_modes.AuthenticationMethodModes]]
        """
        return self._allowed_combinations
    
    @allowed_combinations.setter
    def allowed_combinations(self,value: Optional[List[authentication_method_modes.AuthenticationMethodModes]] = None) -> None:
        """
        Sets the allowedCombinations property value. A collection of authentication method modes that are required be used to satify this authentication strength.
        Args:
            value: Value to set for the allowed_combinations property.
        """
        self._allowed_combinations = value
    
    @property
    def combination_configurations(self,) -> Optional[List[authentication_combination_configuration.AuthenticationCombinationConfiguration]]:
        """
        Gets the combinationConfigurations property value. Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.
        Returns: Optional[List[authentication_combination_configuration.AuthenticationCombinationConfiguration]]
        """
        return self._combination_configurations
    
    @combination_configurations.setter
    def combination_configurations(self,value: Optional[List[authentication_combination_configuration.AuthenticationCombinationConfiguration]] = None) -> None:
        """
        Sets the combinationConfigurations property value. Settings that may be used to require specific types or instances of an authentication method to be used when authenticating with a specified combination of authentication methods.
        Args:
            value: Value to set for the combination_configurations property.
        """
        self._combination_configurations = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The datetime when this policy was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The datetime when this policy was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
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
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The human-readable description of this policy.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The human-readable description of this policy.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The human-readable display name of this policy. Supports $filter (eq, ne, not , and in).
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The human-readable display name of this policy. Supports $filter (eq, ne, not , and in).
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
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
    
    @property
    def modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the modifiedDateTime property value. The datetime when this policy was last modified.
        Returns: Optional[datetime]
        """
        return self._modified_date_time
    
    @modified_date_time.setter
    def modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the modifiedDateTime property value. The datetime when this policy was last modified.
        Args:
            value: Value to set for the modified_date_time property.
        """
        self._modified_date_time = value
    
    @property
    def policy_type(self,) -> Optional[authentication_strength_policy_type.AuthenticationStrengthPolicyType]:
        """
        Gets the policyType property value. The policyType property
        Returns: Optional[authentication_strength_policy_type.AuthenticationStrengthPolicyType]
        """
        return self._policy_type
    
    @policy_type.setter
    def policy_type(self,value: Optional[authentication_strength_policy_type.AuthenticationStrengthPolicyType] = None) -> None:
        """
        Sets the policyType property value. The policyType property
        Args:
            value: Value to set for the policy_type property.
        """
        self._policy_type = value
    
    @property
    def requirements_satisfied(self,) -> Optional[authentication_strength_requirements.AuthenticationStrengthRequirements]:
        """
        Gets the requirementsSatisfied property value. The requirementsSatisfied property
        Returns: Optional[authentication_strength_requirements.AuthenticationStrengthRequirements]
        """
        return self._requirements_satisfied
    
    @requirements_satisfied.setter
    def requirements_satisfied(self,value: Optional[authentication_strength_requirements.AuthenticationStrengthRequirements] = None) -> None:
        """
        Sets the requirementsSatisfied property value. The requirementsSatisfied property
        Args:
            value: Value to set for the requirements_satisfied property.
        """
        self._requirements_satisfied = value
    
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
    

