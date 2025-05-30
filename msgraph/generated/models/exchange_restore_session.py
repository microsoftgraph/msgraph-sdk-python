from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
    from .mailbox_restore_artifact import MailboxRestoreArtifact
    from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
    from .restore_session_base import RestoreSessionBase

from .restore_session_base import RestoreSessionBase

@dataclass
class ExchangeRestoreSession(RestoreSessionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.exchangeRestoreSession"
    # The granularMailboxRestoreArtifacts property
    granular_mailbox_restore_artifacts: Optional[list[GranularMailboxRestoreArtifact]] = None
    # A collection of restore points and destination details that can be used to restore Exchange mailboxes.
    mailbox_restore_artifacts: Optional[list[MailboxRestoreArtifact]] = None
    # A collection of user mailboxes and destination details that can be used to restore Exchange mailboxes.
    mailbox_restore_artifacts_bulk_addition_requests: Optional[list[MailboxRestoreArtifactsBulkAdditionRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExchangeRestoreSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExchangeRestoreSession
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExchangeRestoreSession()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
        from .mailbox_restore_artifact import MailboxRestoreArtifact
        from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
        from .restore_session_base import RestoreSessionBase

        from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
        from .mailbox_restore_artifact import MailboxRestoreArtifact
        from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
        from .restore_session_base import RestoreSessionBase

        fields: dict[str, Callable[[Any], None]] = {
            "granularMailboxRestoreArtifacts": lambda n : setattr(self, 'granular_mailbox_restore_artifacts', n.get_collection_of_object_values(GranularMailboxRestoreArtifact)),
            "mailboxRestoreArtifacts": lambda n : setattr(self, 'mailbox_restore_artifacts', n.get_collection_of_object_values(MailboxRestoreArtifact)),
            "mailboxRestoreArtifactsBulkAdditionRequests": lambda n : setattr(self, 'mailbox_restore_artifacts_bulk_addition_requests', n.get_collection_of_object_values(MailboxRestoreArtifactsBulkAdditionRequest)),
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
        writer.write_collection_of_object_values("granularMailboxRestoreArtifacts", self.granular_mailbox_restore_artifacts)
        writer.write_collection_of_object_values("mailboxRestoreArtifacts", self.mailbox_restore_artifacts)
        writer.write_collection_of_object_values("mailboxRestoreArtifactsBulkAdditionRequests", self.mailbox_restore_artifacts_bulk_addition_requests)
    

