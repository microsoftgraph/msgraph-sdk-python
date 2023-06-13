from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import authentication_method_target_type, entity, microsoft_authenticator_authentication_method_target, sms_authentication_method_target

from . import entity

@dataclass
class AuthenticationMethodTarget(entity.Entity):
    # Determines if the user is enforced to register the authentication method.
    is_registration_required: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The targetType property
    target_type: Optional[authentication_method_target_type.AuthenticationMethodTargetType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuthenticationMethodTarget:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationMethodTarget
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget":
                from . import microsoft_authenticator_authentication_method_target

                return microsoft_authenticator_authentication_method_target.MicrosoftAuthenticatorAuthenticationMethodTarget()
            if mapping_value == "#microsoft.graph.smsAuthenticationMethodTarget":
                from . import sms_authentication_method_target

                return sms_authentication_method_target.SmsAuthenticationMethodTarget()
        return AuthenticationMethodTarget()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import authentication_method_target_type, entity, microsoft_authenticator_authentication_method_target, sms_authentication_method_target

        fields: Dict[str, Callable[[Any], None]] = {
            "isRegistrationRequired": lambda n : setattr(self, 'is_registration_required', n.get_bool_value()),
            "targetType": lambda n : setattr(self, 'target_type', n.get_enum_value(authentication_method_target_type.AuthenticationMethodTargetType)),
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
        writer.write_bool_value("isRegistrationRequired", self.is_registration_required)
        writer.write_enum_value("targetType", self.target_type)
    

