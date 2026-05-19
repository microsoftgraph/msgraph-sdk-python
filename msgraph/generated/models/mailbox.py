from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .mailbox_folder import MailboxFolder

from .directory_object import DirectoryObject

@dataclass
class Mailbox(DirectoryObject, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.mailbox"
    # The collection of folders in the mailbox.
    folders: Optional[list[MailboxFolder]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Mailbox:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Mailbox
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Mailbox()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .mailbox_folder import MailboxFolder

        from .directory_object import DirectoryObject
        from .mailbox_folder import MailboxFolder

        fields: dict[str, Callable[[Any], None]] = {
            "folders": lambda n : setattr(self, 'folders', n.get_collection_of_object_values(MailboxFolder)),
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
        writer.write_collection_of_object_values("folders", self.folders)
    

