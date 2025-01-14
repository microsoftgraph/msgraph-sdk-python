from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .on_user_create_start_handler import OnUserCreateStartHandler
    from .user_type import UserType

from .on_user_create_start_handler import OnUserCreateStartHandler

@dataclass
class OnUserCreateStartExternalUsersSelfServiceSignUp(OnUserCreateStartHandler, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onUserCreateStartExternalUsersSelfServiceSignUp"
    # The type of user to create. Maps to userType property of user object. The possible values are: member, guest, unknownFutureValue.
    user_type_to_create: Optional[UserType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnUserCreateStartExternalUsersSelfServiceSignUp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnUserCreateStartExternalUsersSelfServiceSignUp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnUserCreateStartExternalUsersSelfServiceSignUp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .on_user_create_start_handler import OnUserCreateStartHandler
        from .user_type import UserType

        from .on_user_create_start_handler import OnUserCreateStartHandler
        from .user_type import UserType

        fields: dict[str, Callable[[Any], None]] = {
            "userTypeToCreate": lambda n : setattr(self, 'user_type_to_create', n.get_enum_value(UserType)),
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
        writer.write_enum_value("userTypeToCreate", self.user_type_to_create)
    

