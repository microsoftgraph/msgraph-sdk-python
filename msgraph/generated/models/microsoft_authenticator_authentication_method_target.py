from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_target import AuthenticationMethodTarget
    from .microsoft_authenticator_authentication_mode import MicrosoftAuthenticatorAuthenticationMode

from .authentication_method_target import AuthenticationMethodTarget

@dataclass
class MicrosoftAuthenticatorAuthenticationMethodTarget(AuthenticationMethodTarget, Parsable):
    # The authenticationMode property
    authentication_mode: Optional[MicrosoftAuthenticatorAuthenticationMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MicrosoftAuthenticatorAuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorAuthenticationMethodTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MicrosoftAuthenticatorAuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_target import AuthenticationMethodTarget
        from .microsoft_authenticator_authentication_mode import MicrosoftAuthenticatorAuthenticationMode

        from .authentication_method_target import AuthenticationMethodTarget
        from .microsoft_authenticator_authentication_mode import MicrosoftAuthenticatorAuthenticationMode

        fields: dict[str, Callable[[Any], None]] = {
            "authenticationMode": lambda n : setattr(self, 'authentication_mode', n.get_enum_value(MicrosoftAuthenticatorAuthenticationMode)),
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
        writer.write_enum_value("authenticationMode", self.authentication_mode)
    

