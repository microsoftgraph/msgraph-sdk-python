from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .identity_type import IdentityType

from ..entity import Entity

@dataclass
class Identity(Entity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The type of identity. The possible values are: user or group for Microsoft Entra identities and externalgroup for groups in an external system.
    type: Optional[IdentityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Identity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Identity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Identity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .identity_type import IdentityType

        from ..entity import Entity
        from .identity_type import IdentityType

        fields: dict[str, Callable[[Any], None]] = {
            "type": lambda n : setattr(self, 'type', n.get_enum_value(IdentityType)),
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
        writer.write_enum_value("type", self.type)
    

