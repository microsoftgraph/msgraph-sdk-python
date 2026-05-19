from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .browse_session_status import BrowseSessionStatus
    from .entity import Entity
    from .one_drive_for_business_browse_session import OneDriveForBusinessBrowseSession
    from .public_error import PublicError
    from .share_point_browse_session import SharePointBrowseSession

from .entity import Entity

@dataclass
class BrowseSessionBase(Entity, Parsable):
    # The size of the backup in bytes.
    backup_size_in_bytes: Optional[str] = None
    # The date and time when the browse session was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # Contains the error details if the browse session creation fails.
    error: Optional[PublicError] = None
    # The date and time after which the browse session is deleted automatically.
    expiration_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time of the restore point on which the browse session is created.
    restore_point_date_time: Optional[datetime.datetime] = None
    # The restorePointId property
    restore_point_id: Optional[str] = None
    # The status property
    status: Optional[BrowseSessionStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BrowseSessionBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BrowseSessionBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.oneDriveForBusinessBrowseSession".casefold():
            from .one_drive_for_business_browse_session import OneDriveForBusinessBrowseSession

            return OneDriveForBusinessBrowseSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointBrowseSession".casefold():
            from .share_point_browse_session import SharePointBrowseSession

            return SharePointBrowseSession()
        return BrowseSessionBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .browse_session_status import BrowseSessionStatus
        from .entity import Entity
        from .one_drive_for_business_browse_session import OneDriveForBusinessBrowseSession
        from .public_error import PublicError
        from .share_point_browse_session import SharePointBrowseSession

        from .browse_session_status import BrowseSessionStatus
        from .entity import Entity
        from .one_drive_for_business_browse_session import OneDriveForBusinessBrowseSession
        from .public_error import PublicError
        from .share_point_browse_session import SharePointBrowseSession

        fields: dict[str, Callable[[Any], None]] = {
            "backupSizeInBytes": lambda n : setattr(self, 'backup_size_in_bytes', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "restorePointDateTime": lambda n : setattr(self, 'restore_point_date_time', n.get_datetime_value()),
            "restorePointId": lambda n : setattr(self, 'restore_point_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(BrowseSessionStatus)),
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
        writer.write_str_value("backupSizeInBytes", self.backup_size_in_bytes)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("error", self.error)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_datetime_value("restorePointDateTime", self.restore_point_date_time)
        writer.write_str_value("restorePointId", self.restore_point_id)
        writer.write_enum_value("status", self.status)
    

