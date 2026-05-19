from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .authentication_method_target import AuthenticationMethodTarget

from .authentication_method_target import AuthenticationMethodTarget

@dataclass
class VerifiableCredentialAuthenticationMethodTarget(AuthenticationMethodTarget, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # A collection of Verified ID profile IDs. The profiles define the credentials that users can present to prove their id when signing in, onboarding, or recovering. Verified ID profiles are managed through the Verified ID APIs.
    verified_id_profiles: Optional[list[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VerifiableCredentialAuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VerifiableCredentialAuthenticationMethodTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VerifiableCredentialAuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_target import AuthenticationMethodTarget

        from .authentication_method_target import AuthenticationMethodTarget

        fields: dict[str, Callable[[Any], None]] = {
            "verifiedIdProfiles": lambda n : setattr(self, 'verified_id_profiles', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_collection_of_primitive_values("verifiedIdProfiles", self.verified_id_profiles)
    

