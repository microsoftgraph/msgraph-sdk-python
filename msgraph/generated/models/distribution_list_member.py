from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .contact import Contact
    from .entity import Entity
    from .recipient_type import RecipientType

from .entity import Entity

@dataclass
class DistributionListMember(Entity, Parsable):
    # The contact associated with the distribution list member. Read-only.
    contact: Optional[Contact] = None
    # The display name of the member. Read-only.
    display_name: Optional[str] = None
    # A system-generated unique identifier. Nonempty for contact, privateDL, and mailbox members. Read-only.
    member_id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The type property
    type: Optional[RecipientType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DistributionListMember:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DistributionListMember
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DistributionListMember()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .contact import Contact
        from .entity import Entity
        from .recipient_type import RecipientType

        from .contact import Contact
        from .entity import Entity
        from .recipient_type import RecipientType

        fields: dict[str, Callable[[Any], None]] = {
            "contact": lambda n : setattr(self, 'contact', n.get_object_value(Contact)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "memberId": lambda n : setattr(self, 'member_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(RecipientType)),
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
        writer.write_object_value("contact", self.contact)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("memberId", self.member_id)
        writer.write_enum_value("type", self.type)
    

