from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .exchange_restore_session import ExchangeRestoreSession
    from .identity_set import IdentitySet
    from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
    from .public_error import PublicError
    from .restore_job_type import RestoreJobType
    from .restore_session_artifact_count import RestoreSessionArtifactCount
    from .restore_session_status import RestoreSessionStatus
    from .share_point_restore_session import SharePointRestoreSession

from .entity import Entity

@dataclass
class RestoreSessionBase(Entity, Parsable):
    # The time of completion of the restore session.
    completed_date_time: Optional[datetime.datetime] = None
    # The identity of person who created the restore session.
    created_by: Optional[IdentitySet] = None
    # The time of creation of the restore session.
    created_date_time: Optional[datetime.datetime] = None
    # Contains error details if the restore session fails or completes with an error.
    error: Optional[PublicError] = None
    # Identity of the person who last modified the restore session.
    last_modified_by: Optional[IdentitySet] = None
    # Timestamp of the last modification of the restore session.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether the restore session was created normally or by a bulk job.
    restore_job_type: Optional[RestoreJobType] = None
    # The number of metadata artifacts that belong to this restore session.
    restore_session_artifact_count: Optional[RestoreSessionArtifactCount] = None
    # Status of the restore session. The value is an aggregated status of the restored artifacts. The possible values are: draft, activating, active, completedWithError, completed, unknownFutureValue, failed. Use the Prefer: include-unknown-enum-members request header to get the following members in this evolvable enum: failed.
    status: Optional[RestoreSessionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestoreSessionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestoreSessionBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exchangeRestoreSession".casefold():
            from .exchange_restore_session import ExchangeRestoreSession

            return ExchangeRestoreSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.oneDriveForBusinessRestoreSession".casefold():
            from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession

            return OneDriveForBusinessRestoreSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointRestoreSession".casefold():
            from .share_point_restore_session import SharePointRestoreSession

            return SharePointRestoreSession()
        return RestoreSessionBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .exchange_restore_session import ExchangeRestoreSession
        from .identity_set import IdentitySet
        from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
        from .public_error import PublicError
        from .restore_job_type import RestoreJobType
        from .restore_session_artifact_count import RestoreSessionArtifactCount
        from .restore_session_status import RestoreSessionStatus
        from .share_point_restore_session import SharePointRestoreSession

        from .entity import Entity
        from .exchange_restore_session import ExchangeRestoreSession
        from .identity_set import IdentitySet
        from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
        from .public_error import PublicError
        from .restore_job_type import RestoreJobType
        from .restore_session_artifact_count import RestoreSessionArtifactCount
        from .restore_session_status import RestoreSessionStatus
        from .share_point_restore_session import SharePointRestoreSession

        fields: dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "restoreJobType": lambda n : setattr(self, 'restore_job_type', n.get_enum_value(RestoreJobType)),
            "restoreSessionArtifactCount": lambda n : setattr(self, 'restore_session_artifact_count', n.get_object_value(RestoreSessionArtifactCount)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RestoreSessionStatus)),
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
        writer.write_datetime_value("completedDateTime", self.completed_date_time)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("restoreJobType", self.restore_job_type)
        writer.write_object_value("restoreSessionArtifactCount", self.restore_session_artifact_count)
        writer.write_enum_value("status", self.status)
    

