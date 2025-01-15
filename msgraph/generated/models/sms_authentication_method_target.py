from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_target import AuthenticationMethodTarget

from .authentication_method_target import AuthenticationMethodTarget

@dataclass
class SmsAuthenticationMethodTarget(AuthenticationMethodTarget, Parsable):
    # Determines if users can use this authentication method to sign in to Microsoft Entra ID. true if users can use this method for primary authentication, otherwise false.
    is_usable_for_sign_in: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmsAuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmsAuthenticationMethodTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmsAuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_target import AuthenticationMethodTarget

        from .authentication_method_target import AuthenticationMethodTarget

        fields: dict[str, Callable[[Any], None]] = {
            "isUsableForSignIn": lambda n : setattr(self, 'is_usable_for_sign_in', n.get_bool_value()),
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
        writer.write_bool_value("isUsableForSignIn", self.is_usable_for_sign_in)
    

