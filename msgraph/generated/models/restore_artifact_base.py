from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact_restore_status import ArtifactRestoreStatus
    from .destination_type import DestinationType
    from .drive_restore_artifact import DriveRestoreArtifact
    from .entity import Entity
    from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
    from .mailbox_restore_artifact import MailboxRestoreArtifact
    from .public_error import PublicError
    from .restore_point import RestorePoint
    from .site_restore_artifact import SiteRestoreArtifact

from .entity import Entity

@dataclass
class RestoreArtifactBase(Entity):
    # The time when restoration of restore artifact is completed.
    completion_date_time: Optional[datetime.datetime] = None
    # Indicates the restoration destination. The possible values are: new, inPlace, unknownFutureValue.
    destination_type: Optional[DestinationType] = None
    # Contains error details if the restore session fails or completes with an error.
    error: Optional[PublicError] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Represents the date and time when an artifact is protected by a protectionPolicy and can be restored.
    restore_point: Optional[RestorePoint] = None
    # The time when restoration of restore artifact is started.
    start_date_time: Optional[datetime.datetime] = None
    # The individual restoration status of the restore artifact. The possible values are: added, scheduling, scheduled, inProgress, succeeded, failed, unknownFutureValue.
    status: Optional[ArtifactRestoreStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestoreArtifactBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestoreArtifactBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveRestoreArtifact".casefold():
            from .drive_restore_artifact import DriveRestoreArtifact

            return DriveRestoreArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.granularMailboxRestoreArtifact".casefold():
            from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact

            return GranularMailboxRestoreArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxRestoreArtifact".casefold():
            from .mailbox_restore_artifact import MailboxRestoreArtifact

            return MailboxRestoreArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteRestoreArtifact".casefold():
            from .site_restore_artifact import SiteRestoreArtifact

            return SiteRestoreArtifact()
        return RestoreArtifactBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .artifact_restore_status import ArtifactRestoreStatus
        from .destination_type import DestinationType
        from .drive_restore_artifact import DriveRestoreArtifact
        from .entity import Entity
        from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
        from .mailbox_restore_artifact import MailboxRestoreArtifact
        from .public_error import PublicError
        from .restore_point import RestorePoint
        from .site_restore_artifact import SiteRestoreArtifact

        from .artifact_restore_status import ArtifactRestoreStatus
        from .destination_type import DestinationType
        from .drive_restore_artifact import DriveRestoreArtifact
        from .entity import Entity
        from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
        from .mailbox_restore_artifact import MailboxRestoreArtifact
        from .public_error import PublicError
        from .restore_point import RestorePoint
        from .site_restore_artifact import SiteRestoreArtifact

        fields: Dict[str, Callable[[Any], None]] = {
            "completionDateTime": lambda n : setattr(self, 'completion_date_time', n.get_datetime_value()),
            "destinationType": lambda n : setattr(self, 'destination_type', n.get_enum_value(DestinationType)),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "restorePoint": lambda n : setattr(self, 'restore_point', n.get_object_value(RestorePoint)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ArtifactRestoreStatus)),
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
        writer.write_datetime_value("completionDateTime", self.completion_date_time)
        writer.write_enum_value("destinationType", self.destination_type)
        writer.write_object_value("error", self.error)
        writer.write_object_value("restorePoint", self.restore_point)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("status", self.status)
    

