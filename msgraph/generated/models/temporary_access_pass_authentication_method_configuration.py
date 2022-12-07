from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

authentication_method_configuration = lazy_import('msgraph.generated.models.authentication_method_configuration')
authentication_method_target = lazy_import('msgraph.generated.models.authentication_method_target')

class TemporaryAccessPassAuthenticationMethodConfiguration(authentication_method_configuration.AuthenticationMethodConfiguration):
    def __init__(self,) -> None:
        """
        Instantiates a new TemporaryAccessPassAuthenticationMethodConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration"
        # Default length in characters of a Temporary Access Pass object. Must be between 8 and 48 characters.
        self._default_length: Optional[int] = None
        # Default lifetime in minutes for a Temporary Access Pass. Value can be any integer between the minimumLifetimeInMinutes and maximumLifetimeInMinutes.
        self._default_lifetime_in_minutes: Optional[int] = None
        # A collection of users or groups who are enabled to use the authentication method.
        self._include_targets: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None
        # If true, all the passes in the tenant will be restricted to one-time use. If false, passes in the tenant can be created to be either one-time use or reusable.
        self._is_usable_once: Optional[bool] = None
        # Maximum lifetime in minutes for any Temporary Access Pass created in the tenant. Value can be between 10 and 43200 minutes (equivalent to 30 days).
        self._maximum_lifetime_in_minutes: Optional[int] = None
        # Minimum lifetime in minutes for any Temporary Access Pass created in the tenant. Value can be between 10 and 43200 minutes (equivalent to 30 days).
        self._minimum_lifetime_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TemporaryAccessPassAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TemporaryAccessPassAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TemporaryAccessPassAuthenticationMethodConfiguration()
    
    @property
    def default_length(self,) -> Optional[int]:
        """
        Gets the defaultLength property value. Default length in characters of a Temporary Access Pass object. Must be between 8 and 48 characters.
        Returns: Optional[int]
        """
        return self._default_length
    
    @default_length.setter
    def default_length(self,value: Optional[int] = None) -> None:
        """
        Sets the defaultLength property value. Default length in characters of a Temporary Access Pass object. Must be between 8 and 48 characters.
        Args:
            value: Value to set for the defaultLength property.
        """
        self._default_length = value
    
    @property
    def default_lifetime_in_minutes(self,) -> Optional[int]:
        """
        Gets the defaultLifetimeInMinutes property value. Default lifetime in minutes for a Temporary Access Pass. Value can be any integer between the minimumLifetimeInMinutes and maximumLifetimeInMinutes.
        Returns: Optional[int]
        """
        return self._default_lifetime_in_minutes
    
    @default_lifetime_in_minutes.setter
    def default_lifetime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the defaultLifetimeInMinutes property value. Default lifetime in minutes for a Temporary Access Pass. Value can be any integer between the minimumLifetimeInMinutes and maximumLifetimeInMinutes.
        Args:
            value: Value to set for the defaultLifetimeInMinutes property.
        """
        self._default_lifetime_in_minutes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "default_length": lambda n : setattr(self, 'default_length', n.get_int_value()),
            "default_lifetime_in_minutes": lambda n : setattr(self, 'default_lifetime_in_minutes', n.get_int_value()),
            "include_targets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(authentication_method_target.AuthenticationMethodTarget)),
            "is_usable_once": lambda n : setattr(self, 'is_usable_once', n.get_bool_value()),
            "maximum_lifetime_in_minutes": lambda n : setattr(self, 'maximum_lifetime_in_minutes', n.get_int_value()),
            "minimum_lifetime_in_minutes": lambda n : setattr(self, 'minimum_lifetime_in_minutes', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def include_targets(self,) -> Optional[List[authentication_method_target.AuthenticationMethodTarget]]:
        """
        Gets the includeTargets property value. A collection of users or groups who are enabled to use the authentication method.
        Returns: Optional[List[authentication_method_target.AuthenticationMethodTarget]]
        """
        return self._include_targets
    
    @include_targets.setter
    def include_targets(self,value: Optional[List[authentication_method_target.AuthenticationMethodTarget]] = None) -> None:
        """
        Sets the includeTargets property value. A collection of users or groups who are enabled to use the authentication method.
        Args:
            value: Value to set for the includeTargets property.
        """
        self._include_targets = value
    
    @property
    def is_usable_once(self,) -> Optional[bool]:
        """
        Gets the isUsableOnce property value. If true, all the passes in the tenant will be restricted to one-time use. If false, passes in the tenant can be created to be either one-time use or reusable.
        Returns: Optional[bool]
        """
        return self._is_usable_once
    
    @is_usable_once.setter
    def is_usable_once(self,value: Optional[bool] = None) -> None:
        """
        Sets the isUsableOnce property value. If true, all the passes in the tenant will be restricted to one-time use. If false, passes in the tenant can be created to be either one-time use or reusable.
        Args:
            value: Value to set for the isUsableOnce property.
        """
        self._is_usable_once = value
    
    @property
    def maximum_lifetime_in_minutes(self,) -> Optional[int]:
        """
        Gets the maximumLifetimeInMinutes property value. Maximum lifetime in minutes for any Temporary Access Pass created in the tenant. Value can be between 10 and 43200 minutes (equivalent to 30 days).
        Returns: Optional[int]
        """
        return self._maximum_lifetime_in_minutes
    
    @maximum_lifetime_in_minutes.setter
    def maximum_lifetime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the maximumLifetimeInMinutes property value. Maximum lifetime in minutes for any Temporary Access Pass created in the tenant. Value can be between 10 and 43200 minutes (equivalent to 30 days).
        Args:
            value: Value to set for the maximumLifetimeInMinutes property.
        """
        self._maximum_lifetime_in_minutes = value
    
    @property
    def minimum_lifetime_in_minutes(self,) -> Optional[int]:
        """
        Gets the minimumLifetimeInMinutes property value. Minimum lifetime in minutes for any Temporary Access Pass created in the tenant. Value can be between 10 and 43200 minutes (equivalent to 30 days).
        Returns: Optional[int]
        """
        return self._minimum_lifetime_in_minutes
    
    @minimum_lifetime_in_minutes.setter
    def minimum_lifetime_in_minutes(self,value: Optional[int] = None) -> None:
        """
        Sets the minimumLifetimeInMinutes property value. Minimum lifetime in minutes for any Temporary Access Pass created in the tenant. Value can be between 10 and 43200 minutes (equivalent to 30 days).
        Args:
            value: Value to set for the minimumLifetimeInMinutes property.
        """
        self._minimum_lifetime_in_minutes = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("defaultLength", self.default_length)
        writer.write_int_value("defaultLifetimeInMinutes", self.default_lifetime_in_minutes)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_bool_value("isUsableOnce", self.is_usable_once)
        writer.write_int_value("maximumLifetimeInMinutes", self.maximum_lifetime_in_minutes)
        writer.write_int_value("minimumLifetimeInMinutes", self.minimum_lifetime_in_minutes)
    

