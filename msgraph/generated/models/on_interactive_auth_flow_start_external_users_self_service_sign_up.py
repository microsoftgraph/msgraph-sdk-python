from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler

from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler

@dataclass
class OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp(OnInteractiveAuthFlowStartHandler, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onInteractiveAuthFlowStartExternalUsersSelfServiceSignUp"
    # Optional. Specifies whether the authentication flow includes an option to sign up (create account) and sign in. Default value is false meaning only sign in is enabled.
    is_sign_up_allowed: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnInteractiveAuthFlowStartExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler

        from .on_interactive_auth_flow_start_handler import OnInteractiveAuthFlowStartHandler

        fields: dict[str, Callable[[Any], None]] = {
            "isSignUpAllowed": lambda n : setattr(self, 'is_sign_up_allowed', n.get_bool_value()),
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
        writer.write_bool_value("isSignUpAllowed", self.is_sign_up_allowed)
    

