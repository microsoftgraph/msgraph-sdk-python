from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .self_service_sign_up_authentication_flow_configuration import SelfServiceSignUpAuthenticationFlowConfiguration

from .entity import Entity

@dataclass
class AuthenticationFlowsPolicy(Entity):
    # Inherited property. A description of the policy. Optional. Read-only.
    description: Optional[str] = None
    # Inherited property. The human-readable name of the policy. Optional. Read-only.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Contains selfServiceSignUpAuthenticationFlowConfiguration settings that convey whether self-service sign-up is enabled or disabled. Optional. Read-only.
    self_service_sign_up: Optional[SelfServiceSignUpAuthenticationFlowConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationFlowsPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationFlowsPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationFlowsPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .self_service_sign_up_authentication_flow_configuration import SelfServiceSignUpAuthenticationFlowConfiguration

        from .entity import Entity
        from .self_service_sign_up_authentication_flow_configuration import SelfServiceSignUpAuthenticationFlowConfiguration

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "selfServiceSignUp": lambda n : setattr(self, 'self_service_sign_up', n.get_object_value(SelfServiceSignUpAuthenticationFlowConfiguration)),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("selfServiceSignUp", self.self_service_sign_up)
    

