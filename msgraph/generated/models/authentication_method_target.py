from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_target_type import AuthenticationMethodTargetType
    from .entity import Entity
    from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
    from .sms_authentication_method_target import SmsAuthenticationMethodTarget

from .entity import Entity

@dataclass
class AuthenticationMethodTarget(Entity, Parsable):
    # Determines if the user is enforced to register the authentication method.
    is_registration_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The targetType property
    target_type: Optional[AuthenticationMethodTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodTarget
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget".casefold():
            from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget

            return MicrosoftAuthenticatorAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodTarget".casefold():
            from .sms_authentication_method_target import SmsAuthenticationMethodTarget

            return SmsAuthenticationMethodTarget()
        return AuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_target_type import AuthenticationMethodTargetType
        from .entity import Entity
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget

        from .authentication_method_target_type import AuthenticationMethodTargetType
        from .entity import Entity
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget

        fields: dict[str, Callable[[Any], None]] = {
            "isRegistrationRequired": lambda n : setattr(self, 'is_registration_required', n.get_bool_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(AuthenticationMethodTargetType)),
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
        writer.write_bool_value("isRegistrationRequired", self.is_registration_required)
        writer.write_enum_value("targetType", self.target_type)
    

