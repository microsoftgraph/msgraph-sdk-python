from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_restore_artifact import DriveRestoreArtifact
    from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
    from .restore_session_base import RestoreSessionBase

from .restore_session_base import RestoreSessionBase

@dataclass
class OneDriveForBusinessRestoreSession(RestoreSessionBase, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.oneDriveForBusinessRestoreSession"
    # A collection of restore points and destination details that can be used to restore a OneDrive for work or school drive.
    drive_restore_artifacts: Optional[list[DriveRestoreArtifact]] = None
    # A collection of user mailboxes and destination details that can be used to restore a OneDrive for work or school drive.
    drive_restore_artifacts_bulk_addition_requests: Optional[list[DriveRestoreArtifactsBulkAdditionRequest]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OneDriveForBusinessRestoreSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OneDriveForBusinessRestoreSession
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OneDriveForBusinessRestoreSession()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .drive_restore_artifact import DriveRestoreArtifact
        from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
        from .restore_session_base import RestoreSessionBase

        from .drive_restore_artifact import DriveRestoreArtifact
        from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
        from .restore_session_base import RestoreSessionBase

        fields: dict[str, Callable[[Any], None]] = {
            "driveRestoreArtifacts": lambda n : setattr(self, 'drive_restore_artifacts', n.get_collection_of_object_values(DriveRestoreArtifact)),
            "driveRestoreArtifactsBulkAdditionRequests": lambda n : setattr(self, 'drive_restore_artifacts_bulk_addition_requests', n.get_collection_of_object_values(DriveRestoreArtifactsBulkAdditionRequest)),
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
        writer.write_collection_of_object_values("driveRestoreArtifacts", self.drive_restore_artifacts)
        writer.write_collection_of_object_values("driveRestoreArtifactsBulkAdditionRequests", self.drive_restore_artifacts_bulk_addition_requests)
    

