from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_target, microsoft_authenticator_authentication_mode

from . import authentication_method_target

class MicrosoftAuthenticatorAuthenticationMethodTarget(authentication_method_target.AuthenticationMethodTarget):
    def __init__(self,) -> None:
        """
        Instantiates a new MicrosoftAuthenticatorAuthenticationMethodTarget and sets the default values.
        """
        super().__init__()
        # The authenticationMode property
        self._authentication_mode: Optional[microsoft_authenticator_authentication_mode.MicrosoftAuthenticatorAuthenticationMode] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def authentication_mode(self,) -> Optional[microsoft_authenticator_authentication_mode.MicrosoftAuthenticatorAuthenticationMode]:
        """
        Gets the authenticationMode property value. The authenticationMode property
        Returns: Optional[microsoft_authenticator_authentication_mode.MicrosoftAuthenticatorAuthenticationMode]
        """
        return self._authentication_mode
    
    @authentication_mode.setter
    def authentication_mode(self,value: Optional[microsoft_authenticator_authentication_mode.MicrosoftAuthenticatorAuthenticationMode] = None) -> None:
        """
        Sets the authenticationMode property value. The authenticationMode property
        Args:
            value: Value to set for the authentication_mode property.
        """
        self._authentication_mode = value
    
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
    

