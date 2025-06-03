from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
    from .entity import Entity
    from .identity_set import IdentitySet
    from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
    from .protection_units_bulk_job_status import ProtectionUnitsBulkJobStatus
    from .public_error import PublicError
    from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

from .entity import Entity

@dataclass
class ProtectionUnitsBulkJobBase(Entity, Parsable):
    # The identity of person who created the job.
    created_by: Optional[IdentitySet] = None
    # The time of creation of the job.
    created_date_time: Optional[datetime.datetime] = None
    # The name of the protection units bulk addition job.
    display_name: Optional[str] = None
    # Error details containing resource resolution failures, if any.
    error: Optional[PublicError] = None
    # The identity of the person who last modified the job.
    last_modified_by: Optional[IdentitySet] = None
    # Timestamp of the last modification made to the job.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status property
    status: Optional[ProtectionUnitsBulkJobStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectionUnitsBulkJobBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectionUnitsBulkJobBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveProtectionUnitsBulkAdditionJob".casefold():
            from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob

            return DriveProtectionUnitsBulkAdditionJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxProtectionUnitsBulkAdditionJob".casefold():
            from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob

            return MailboxProtectionUnitsBulkAdditionJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteProtectionUnitsBulkAdditionJob".casefold():
            from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

            return SiteProtectionUnitsBulkAdditionJob()
        return ProtectionUnitsBulkJobBase()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
        from .entity import Entity
        from .identity_set import IdentitySet
        from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
        from .protection_units_bulk_job_status import ProtectionUnitsBulkJobStatus
        from .public_error import PublicError
        from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

        from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
        from .entity import Entity
        from .identity_set import IdentitySet
        from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
        from .protection_units_bulk_job_status import ProtectionUnitsBulkJobStatus
        from .public_error import PublicError
        from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ProtectionUnitsBulkJobStatus)),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("error", self.error)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
    

