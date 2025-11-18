from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..user import User
    from .activation_scope import ActivationScope

from .activation_scope import ActivationScope

@dataclass
class ActivateUserScope(ActivationScope, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.identityGovernance.activateUserScope"
    # The users property
    users: Optional[list[User]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActivateUserScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActivateUserScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActivateUserScope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..user import User
        from .activation_scope import ActivationScope

        from ..user import User
        from .activation_scope import ActivationScope

        fields: dict[str, Callable[[Any], None]] = {
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(User)),
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
        writer.write_collection_of_object_values("users", self.users)
    

