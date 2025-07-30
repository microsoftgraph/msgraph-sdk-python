from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes
    from .sign_in_identity import SignInIdentity

from .sign_in_identity import SignInIdentity

@dataclass
class UserSignIn(SignInIdentity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.userSignIn"
    # TenantId of the guest user as applies to Microsoft Entra B2B scenarios.
    external_tenant_id: Optional[str] = None
    # The externalUserType property
    external_user_type: Optional[ConditionalAccessGuestOrExternalUserTypes] = None
    # Object ID of the user.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserSignIn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserSignIn
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserSignIn()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes
        from .sign_in_identity import SignInIdentity

        from .conditional_access_guest_or_external_user_types import ConditionalAccessGuestOrExternalUserTypes
        from .sign_in_identity import SignInIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "externalTenantId": lambda n : setattr(self, 'external_tenant_id', n.get_str_value()),
            "externalUserType": lambda n : setattr(self, 'external_user_type', n.get_collection_of_enum_values(ConditionalAccessGuestOrExternalUserTypes)),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_str_value("externalTenantId", self.external_tenant_id)
        writer.write_enum_value("externalUserType", self.external_user_type)
        writer.write_str_value("userId", self.user_id)
    

