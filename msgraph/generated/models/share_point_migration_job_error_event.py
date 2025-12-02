from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .public_error import PublicError
    from .share_point_migration_event import SharePointMigrationEvent
    from .share_point_migration_job_error_level import SharePointMigrationJobErrorLevel
    from .share_point_migration_object_type import SharePointMigrationObjectType

from .share_point_migration_event import SharePointMigrationEvent

@dataclass
class SharePointMigrationJobErrorEvent(SharePointMigrationEvent, Parsable):
    # The error property
    error: Optional[PublicError] = None
    # The errorLevel property
    error_level: Optional[SharePointMigrationJobErrorLevel] = None
    # The object ID. Read-only.
    object_id: Optional[str] = None
    # The objectType property
    object_type: Optional[SharePointMigrationObjectType] = None
    # The object URL. Read-only.
    object_url: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The current retry count of the job. Read-only.
    total_retry_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointMigrationJobErrorEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointMigrationJobErrorEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointMigrationJobErrorEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .public_error import PublicError
        from .share_point_migration_event import SharePointMigrationEvent
        from .share_point_migration_job_error_level import SharePointMigrationJobErrorLevel
        from .share_point_migration_object_type import SharePointMigrationObjectType

        from .public_error import PublicError
        from .share_point_migration_event import SharePointMigrationEvent
        from .share_point_migration_job_error_level import SharePointMigrationJobErrorLevel
        from .share_point_migration_object_type import SharePointMigrationObjectType

        fields: dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "errorLevel": lambda n : setattr(self, 'error_level', n.get_enum_value(SharePointMigrationJobErrorLevel)),
            "objectId": lambda n : setattr(self, 'object_id', n.get_str_value()),
            "objectType": lambda n : setattr(self, 'object_type', n.get_enum_value(SharePointMigrationObjectType)),
            "objectUrl": lambda n : setattr(self, 'object_url', n.get_str_value()),
            "totalRetryCount": lambda n : setattr(self, 'total_retry_count', n.get_int_value()),
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
        writer.write_object_value("error", self.error)
        writer.write_enum_value("errorLevel", self.error_level)
        writer.write_str_value("objectId", self.object_id)
        writer.write_enum_value("objectType", self.object_type)
        writer.write_str_value("objectUrl", self.object_url)
        writer.write_int_value("totalRetryCount", self.total_retry_count)
    

