from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_target import AuthenticationMethodTarget

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class TemporaryAccessPassAuthenticationMethodConfiguration(AuthenticationMethodConfiguration, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration"
    # Default length in characters of a Temporary Access Pass object. Must be between 8 and 48 characters.
    default_length: Optional[int] = None
    # Default lifetime in minutes for a Temporary Access Pass. Value can be any integer between the minimumLifetimeInMinutes and maximumLifetimeInMinutes.
    default_lifetime_in_minutes: Optional[int] = None
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[list[AuthenticationMethodTarget]] = None
    # If true, all the passes in the tenant will be restricted to one-time use. If false, passes in the tenant can be created to be either one-time use or reusable.
    is_usable_once: Optional[bool] = None
    # Maximum lifetime in minutes for any Temporary Access Pass created in the tenant. Value can be between 10 and 43200 minutes (equivalent to 30 days).
    maximum_lifetime_in_minutes: Optional[int] = None
    # Minimum lifetime in minutes for any Temporary Access Pass created in the tenant. Value can be between 10 and 43200 minutes (equivalent to 30 days).
    minimum_lifetime_in_minutes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TemporaryAccessPassAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TemporaryAccessPassAuthenticationMethodConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TemporaryAccessPassAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget

        fields: dict[str, Callable[[Any], None]] = {
            "defaultLength": lambda n : setattr(self, 'default_length', n.get_int_value()),
            "defaultLifetimeInMinutes": lambda n : setattr(self, 'default_lifetime_in_minutes', n.get_int_value()),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodTarget)),
            "isUsableOnce": lambda n : setattr(self, 'is_usable_once', n.get_bool_value()),
            "maximumLifetimeInMinutes": lambda n : setattr(self, 'maximum_lifetime_in_minutes', n.get_int_value()),
            "minimumLifetimeInMinutes": lambda n : setattr(self, 'minimum_lifetime_in_minutes', n.get_int_value()),
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
        writer.write_int_value("defaultLength", self.default_length)
        writer.write_int_value("defaultLifetimeInMinutes", self.default_lifetime_in_minutes)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
        writer.write_bool_value("isUsableOnce", self.is_usable_once)
        writer.write_int_value("maximumLifetimeInMinutes", self.maximum_lifetime_in_minutes)
        writer.write_int_value("minimumLifetimeInMinutes", self.minimum_lifetime_in_minutes)
    

