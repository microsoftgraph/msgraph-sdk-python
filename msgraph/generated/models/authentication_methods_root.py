from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .user_registration_details import UserRegistrationDetails

from .entity import Entity

@dataclass
class AuthenticationMethodsRoot(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the state of a user's authentication methods, including which methods are registered and which features the user is registered and capable of (such as multifactor authentication, self-service password reset, and passwordless authentication).
    user_registration_details: Optional[list[UserRegistrationDetails]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationMethodsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodsRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationMethodsRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .user_registration_details import UserRegistrationDetails

        from .entity import Entity
        from .user_registration_details import UserRegistrationDetails

        fields: dict[str, Callable[[Any], None]] = {
            "userRegistrationDetails": lambda n : setattr(self, 'user_registration_details', n.get_collection_of_object_values(UserRegistrationDetails)),
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
        writer.write_collection_of_object_values("userRegistrationDetails", self.user_registration_details)
    

