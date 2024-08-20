from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_restore_artifact import DriveRestoreArtifact
    from .restore_session_base import RestoreSessionBase

from .restore_session_base import RestoreSessionBase

@dataclass
class OneDriveForBusinessRestoreSession(RestoreSessionBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.oneDriveForBusinessRestoreSession"
    # A collection of restore points and destination details that can be used to restore a OneDrive for Business drive.
    drive_restore_artifacts: Optional[List[DriveRestoreArtifact]] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .drive_restore_artifact import DriveRestoreArtifact
        from .restore_session_base import RestoreSessionBase

        from .drive_restore_artifact import DriveRestoreArtifact
        from .restore_session_base import RestoreSessionBase

        fields: Dict[str, Callable[[Any], None]] = {
            "driveRestoreArtifacts": lambda n : setattr(self, 'drive_restore_artifacts', n.get_collection_of_object_values(DriveRestoreArtifact)),
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
    

