from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sign_in_context import SignInContext
    from .user_action import UserAction

from .sign_in_context import SignInContext

@dataclass
class UserActionContext(SignInContext, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.userActionContext"
    # Represents the user action that the authenticating identity is performing. The possible values are: registerSecurityInformation, registerOrJoinDevices, unknownFutureValue.
    user_action: Optional[UserAction] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserActionContext:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserActionContext
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserActionContext()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .sign_in_context import SignInContext
        from .user_action import UserAction

        from .sign_in_context import SignInContext
        from .user_action import UserAction

        fields: dict[str, Callable[[Any], None]] = {
            "userAction": lambda n : setattr(self, 'user_action', n.get_enum_value(UserAction)),
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
        writer.write_enum_value("userAction", self.user_action)
    

