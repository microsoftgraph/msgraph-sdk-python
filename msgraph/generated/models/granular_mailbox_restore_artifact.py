from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mailbox_restore_artifact import MailboxRestoreArtifact

from .mailbox_restore_artifact import MailboxRestoreArtifact

@dataclass
class GranularMailboxRestoreArtifact(MailboxRestoreArtifact):
    # .
    artifact_count: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # .
    search_response_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GranularMailboxRestoreArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GranularMailboxRestoreArtifact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GranularMailboxRestoreArtifact()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .mailbox_restore_artifact import MailboxRestoreArtifact

        from .mailbox_restore_artifact import MailboxRestoreArtifact

        fields: Dict[str, Callable[[Any], None]] = {
            "artifactCount": lambda n : setattr(self, 'artifact_count', n.get_int_value()),
            "searchResponseId": lambda n : setattr(self, 'search_response_id', n.get_str_value()),
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
        writer.write_int_value("artifactCount", self.artifact_count)
        writer.write_str_value("searchResponseId", self.search_response_id)
    

