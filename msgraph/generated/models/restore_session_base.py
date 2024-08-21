from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .exchange_restore_session import ExchangeRestoreSession
    from .identity_set import IdentitySet
    from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
    from .public_error import PublicError
    from .restore_session_status import RestoreSessionStatus
    from .share_point_restore_session import SharePointRestoreSession

from .entity import Entity

@dataclass
class RestoreSessionBase(Entity):
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
    # Status of the restore session. The value is an aggregated status of the restored artifacts. The possible values are: draft, activating, active, completedWithError, completed, unknownFutureValue, failed. You must use the Prefer: include-unknown-enum-members request header to get the following value in this evolvable enum: failed.
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
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .exchange_restore_session import ExchangeRestoreSession
        from .identity_set import IdentitySet
        from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
        from .public_error import PublicError
        from .restore_session_status import RestoreSessionStatus
        from .share_point_restore_session import SharePointRestoreSession

        from .entity import Entity
        from .exchange_restore_session import ExchangeRestoreSession
        from .identity_set import IdentitySet
        from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
        from .public_error import PublicError
        from .restore_session_status import RestoreSessionStatus
        from .share_point_restore_session import SharePointRestoreSession

        fields: Dict[str, Callable[[Any], None]] = {
            "completedDateTime": lambda n : setattr(self, 'completed_date_time', n.get_datetime_value()),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_enum_value("status", self.status)
    

