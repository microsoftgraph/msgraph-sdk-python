from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
    from .restore_artifact_base import RestoreArtifactBase

from .restore_artifact_base import RestoreArtifactBase

@dataclass
class MailboxRestoreArtifact(RestoreArtifactBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = None
    # The new restored folder identifier for the user.
    restored_folder_id: Optional[str] = None
    # The new restored folder name.
    restored_folder_name: Optional[str] = None
    # The number of items that are being restored in the folder.
    restored_item_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailboxRestoreArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailboxRestoreArtifact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.granularMailboxRestoreArtifact".casefold():
            from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact

            return GranularMailboxRestoreArtifact()
        return MailboxRestoreArtifact()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
        from .restore_artifact_base import RestoreArtifactBase

        from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
        from .restore_artifact_base import RestoreArtifactBase

        fields: dict[str, Callable[[Any], None]] = {
            "restoredFolderId": lambda n : setattr(self, 'restored_folder_id', n.get_str_value()),
            "restoredFolderName": lambda n : setattr(self, 'restored_folder_name', n.get_str_value()),
            "restoredItemCount": lambda n : setattr(self, 'restored_item_count', n.get_int_value()),
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
        writer.write_str_value("restoredFolderId", self.restored_folder_id)
        writer.write_int_value("restoredItemCount", self.restored_item_count)
    

