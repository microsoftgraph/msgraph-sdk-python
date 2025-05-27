from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .destination_type import DestinationType
    from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
    from .entity import Entity
    from .identity_set import IdentitySet
    from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
    from .public_error import PublicError
    from .restore_artifacts_bulk_request_status import RestoreArtifactsBulkRequestStatus
    from .restore_point_preference import RestorePointPreference
    from .restore_point_tags import RestorePointTags
    from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
    from .time_period import TimePeriod

from .entity import Entity

@dataclass
class RestoreArtifactsBulkRequestBase(Entity, Parsable):
    # The identity of the person who created the bulk request.
    created_by: Optional[IdentitySet] = None
    # The time when the bulk request was created.
    created_date_time: Optional[datetime.datetime] = None
    # Indicates the restoration destination. The possible values are: new, inPlace, unknownFutureValue.
    destination_type: Optional[DestinationType] = None
    # Name of the addition request.
    display_name: Optional[str] = None
    # Error details are populated for resource resolution failures.
    error: Optional[PublicError] = None
    # Identity of the person who last modified this entity.
    last_modified_by: Optional[IdentitySet] = None
    # Timestamp when this entity was last modified.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The start and end date and time of the protection period.
    protection_time_period: Optional[TimePeriod] = None
    # Indicates which protection units to restore. This property isn't implemented yet. Future value; don't use.
    protection_unit_ids: Optional[list[str]] = None
    # Indicates which restore point to return. The possible values are: oldest, latest, unknownFutureValue.
    restore_point_preference: Optional[RestorePointPreference] = None
    # The status property
    status: Optional[RestoreArtifactsBulkRequestStatus] = None
    # The type of the restore point. The possible values are: none, fastRestore, unknownFutureValue.
    tags: Optional[RestorePointTags] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestoreArtifactsBulkRequestBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestoreArtifactsBulkRequestBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveRestoreArtifactsBulkAdditionRequest".casefold():
            from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest

            return DriveRestoreArtifactsBulkAdditionRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxRestoreArtifactsBulkAdditionRequest".casefold():
            from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest

            return MailboxRestoreArtifactsBulkAdditionRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteRestoreArtifactsBulkAdditionRequest".casefold():
            from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

            return SiteRestoreArtifactsBulkAdditionRequest()
        return RestoreArtifactsBulkRequestBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .destination_type import DestinationType
        from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
        from .entity import Entity
        from .identity_set import IdentitySet
        from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
        from .public_error import PublicError
        from .restore_artifacts_bulk_request_status import RestoreArtifactsBulkRequestStatus
        from .restore_point_preference import RestorePointPreference
        from .restore_point_tags import RestorePointTags
        from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
        from .time_period import TimePeriod

        from .destination_type import DestinationType
        from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
        from .entity import Entity
        from .identity_set import IdentitySet
        from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
        from .public_error import PublicError
        from .restore_artifacts_bulk_request_status import RestoreArtifactsBulkRequestStatus
        from .restore_point_preference import RestorePointPreference
        from .restore_point_tags import RestorePointTags
        from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
        from .time_period import TimePeriod

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "destinationType": lambda n : setattr(self, 'destination_type', n.get_enum_value(DestinationType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "protectionTimePeriod": lambda n : setattr(self, 'protection_time_period', n.get_object_value(TimePeriod)),
            "protectionUnitIds": lambda n : setattr(self, 'protection_unit_ids', n.get_collection_of_primitive_values(str)),
            "restorePointPreference": lambda n : setattr(self, 'restore_point_preference', n.get_enum_value(RestorePointPreference)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(RestoreArtifactsBulkRequestStatus)),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_enum_values(RestorePointTags)),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("destinationType", self.destination_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("error", self.error)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_object_value("protectionTimePeriod", self.protection_time_period)
        writer.write_collection_of_primitive_values("protectionUnitIds", self.protection_unit_ids)
        writer.write_enum_value("restorePointPreference", self.restore_point_preference)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("tags", self.tags)
    

