from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mailbox_details import MailboxDetails
    from .place import Place
    from .place_mode import PlaceMode

from .place import Place

@dataclass
class Desk(Place, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.desk"
    # The displayDeviceName property
    display_device_name: Optional[str] = None
    # The mailboxDetails property
    mailbox_details: Optional[MailboxDetails] = None
    # The mode property
    mode: Optional[PlaceMode] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Desk:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Desk
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Desk()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .mailbox_details import MailboxDetails
        from .place import Place
        from .place_mode import PlaceMode

        from .mailbox_details import MailboxDetails
        from .place import Place
        from .place_mode import PlaceMode

        fields: dict[str, Callable[[Any], None]] = {
            "displayDeviceName": lambda n : setattr(self, 'display_device_name', n.get_str_value()),
            "mailboxDetails": lambda n : setattr(self, 'mailbox_details', n.get_object_value(MailboxDetails)),
            "mode": lambda n : setattr(self, 'mode', n.get_object_value(PlaceMode)),
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
        writer.write_str_value("displayDeviceName", self.display_device_name)
        writer.write_object_value("mailboxDetails", self.mailbox_details)
        writer.write_object_value("mode", self.mode)
    

