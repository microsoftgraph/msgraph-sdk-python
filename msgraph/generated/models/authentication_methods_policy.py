from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_configuration = lazy_import('msgraph.generated.models.authentication_method_configuration')
entity = lazy_import('msgraph.generated.models.entity')
registration_enforcement = lazy_import('msgraph.generated.models.registration_enforcement')

class AuthenticationMethodsPolicy(entity.Entity):
    """
    Provides operations to manage the authenticationMethodsPolicy singleton.
    """
    @property
    def authentication_method_configurations(self,) -> Optional[List[authentication_method_configuration.AuthenticationMethodConfiguration]]:
        """
        Gets the authenticationMethodConfigurations property value. Represents the settings for each authentication method. Automatically expanded on GET /policies/authenticationMethodsPolicy.
        Returns: Optional[List[authentication_method_configuration.AuthenticationMethodConfiguration]]
        """
        return self._authentication_method_configurations
    
    @authentication_method_configurations.setter
    def authentication_method_configurations(self,value: Optional[List[authentication_method_configuration.AuthenticationMethodConfiguration]] = None) -> None:
        """
        Sets the authenticationMethodConfigurations property value. Represents the settings for each authentication method. Automatically expanded on GET /policies/authenticationMethodsPolicy.
        Args:
            value: Value to set for the authenticationMethodConfigurations property.
        """
        self._authentication_method_configurations = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new authenticationMethodsPolicy and sets the default values.
        """
        super().__init__()
        # Represents the settings for each authentication method. Automatically expanded on GET /policies/authenticationMethodsPolicy.
        self._authentication_method_configurations: Optional[List[authentication_method_configuration.AuthenticationMethodConfiguration]] = None
        # A description of the policy. Read-only.
        self._description: Optional[str] = None
        # The name of the policy. Read-only.
        self._display_name: Optional[str] = None
        # The date and time of the last update to the policy. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The version of the policy in use. Read-only.
        self._policy_version: Optional[str] = None
        # The reconfirmationInDays property
        self._reconfirmation_in_days: Optional[int] = None
        # Enforce registration at sign-in time. This property can be used to remind users to set up targeted authentication methods.
        self._registration_enforcement: Optional[registration_enforcement.RegistrationEnforcement] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuthenticationMethodsPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A description of the policy. Read-only.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A description of the policy. Read-only.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The name of the policy. Read-only.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The name of the policy. Read-only.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "authentication_method_configurations": lambda n : setattr(self, 'authentication_method_configurations', n.get_collection_of_object_values(authentication_method_configuration.AuthenticationMethodConfiguration)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policy_version": lambda n : setattr(self, 'policy_version', n.get_str_value()),
            "reconfirmation_in_days": lambda n : setattr(self, 'reconfirmation_in_days', n.get_int_value()),
            "registration_enforcement": lambda n : setattr(self, 'registration_enforcement', n.get_object_value(registration_enforcement.RegistrationEnforcement)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. The date and time of the last update to the policy. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. The date and time of the last update to the policy. Read-only.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def policy_version(self,) -> Optional[str]:
        """
        Gets the policyVersion property value. The version of the policy in use. Read-only.
        Returns: Optional[str]
        """
        return self._policy_version
    
    @policy_version.setter
    def policy_version(self,value: Optional[str] = None) -> None:
        """
        Sets the policyVersion property value. The version of the policy in use. Read-only.
        Args:
            value: Value to set for the policyVersion property.
        """
        self._policy_version = value
    
    @property
    def reconfirmation_in_days(self,) -> Optional[int]:
        """
        Gets the reconfirmationInDays property value. The reconfirmationInDays property
        Returns: Optional[int]
        """
        return self._reconfirmation_in_days
    
    @reconfirmation_in_days.setter
    def reconfirmation_in_days(self,value: Optional[int] = None) -> None:
        """
        Sets the reconfirmationInDays property value. The reconfirmationInDays property
        Args:
            value: Value to set for the reconfirmationInDays property.
        """
        self._reconfirmation_in_days = value
    
    @property
    def registration_enforcement(self,) -> Optional[registration_enforcement.RegistrationEnforcement]:
        """
        Gets the registrationEnforcement property value. Enforce registration at sign-in time. This property can be used to remind users to set up targeted authentication methods.
        Returns: Optional[registration_enforcement.RegistrationEnforcement]
        """
        return self._registration_enforcement
    
    @registration_enforcement.setter
    def registration_enforcement(self,value: Optional[registration_enforcement.RegistrationEnforcement] = None) -> None:
        """
        Sets the registrationEnforcement property value. Enforce registration at sign-in time. This property can be used to remind users to set up targeted authentication methods.
        Args:
            value: Value to set for the registrationEnforcement property.
        """
        self._registration_enforcement = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("authenticationMethodConfigurations", self.authentication_method_configurations)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("policyVersion", self.policy_version)
        writer.write_int_value("reconfirmationInDays", self.reconfirmation_in_days)
        writer.write_object_value("registrationEnforcement", self.registration_enforcement)
    

