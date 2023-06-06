from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_target, microsoft_authenticator_authentication_mode

from . import authentication_method_target

@dataclass
class MicrosoftAuthenticatorAuthenticationMethodTarget(authentication_method_target.AuthenticationMethodTarget):
    # The authenticationMode property
    authentication_mode: Optional[microsoft_authenticator_authentication_mode.MicrosoftAuthenticatorAuthenticationMode] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MicrosoftAuthenticatorAuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MicrosoftAuthenticatorAuthenticationMethodTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MicrosoftAuthenticatorAuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_target, microsoft_authenticator_authentication_mode

        fields: Dict[str, Callable[[Any], None]] = {
            "authenticationMode": lambda n : setattr(self, 'authentication_mode', n.get_enum_value(microsoft_authenticator_authentication_mode.MicrosoftAuthenticatorAuthenticationMode)),
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
        writer.write_enum_value("authenticationMode", self.authentication_mode)
    

