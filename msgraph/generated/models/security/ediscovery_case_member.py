from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .recipient_type import RecipientType

from ..entity import Entity

@dataclass
class EdiscoveryCaseMember(Entity, Parsable):
    # The display name of the eDiscovery case member. Allowed only for case members of type roleGroup.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies the recipient type of the eDiscovery case member. The possible values are: user, roleGroup, unknownFutureValue.
    recipient_type: Optional[RecipientType] = None
    # The smtp address of the eDiscovery case member. Allowed only for case members of type user.
    smtp_address: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdiscoveryCaseMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryCaseMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdiscoveryCaseMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .recipient_type import RecipientType

        from ..entity import Entity
        from .recipient_type import RecipientType

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "recipientType": lambda n : setattr(self, 'recipient_type', n.get_collection_of_enum_values(RecipientType)),
            "smtpAddress": lambda n : setattr(self, 'smtp_address', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("recipientType", self.recipient_type)
        writer.write_str_value("smtpAddress", self.smtp_address)
    

