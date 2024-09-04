from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_protection_unit import DriveProtectionUnit
    from .entity import Entity
    from .identity_set import IdentitySet
    from .mailbox_protection_unit import MailboxProtectionUnit
    from .protection_unit_status import ProtectionUnitStatus
    from .public_error import PublicError
    from .site_protection_unit import SiteProtectionUnit

from .entity import Entity

@dataclass
class ProtectionUnitBase(Entity):
    # The identity of person who created the protection unit.
    created_by: Optional[IdentitySet] = None
    # The time of creation of the protection unit.
    created_date_time: Optional[datetime.datetime] = None
    # Contains error details if an error occurred while creating a protection unit.
    error: Optional[PublicError] = None
    # The identity of person who last modified the protection unit.
    last_modified_by: Optional[IdentitySet] = None
    # Timestamp of the last modification of this protection unit.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier of the protection policy based on which protection unit was created.
    policy_id: Optional[str] = None
    # The status of the protection unit. The possible values are: protectRequested, protected, unprotectRequested, unprotected, removeRequested, unknownFutureValue.
    status: Optional[ProtectionUnitStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectionUnitBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectionUnitBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveProtectionUnit".casefold():
            from .drive_protection_unit import DriveProtectionUnit

            return DriveProtectionUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxProtectionUnit".casefold():
            from .mailbox_protection_unit import MailboxProtectionUnit

            return MailboxProtectionUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteProtectionUnit".casefold():
            from .site_protection_unit import SiteProtectionUnit

            return SiteProtectionUnit()
        return ProtectionUnitBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .drive_protection_unit import DriveProtectionUnit
        from .entity import Entity
        from .identity_set import IdentitySet
        from .mailbox_protection_unit import MailboxProtectionUnit
        from .protection_unit_status import ProtectionUnitStatus
        from .public_error import PublicError
        from .site_protection_unit import SiteProtectionUnit

        from .drive_protection_unit import DriveProtectionUnit
        from .entity import Entity
        from .identity_set import IdentitySet
        from .mailbox_protection_unit import MailboxProtectionUnit
        from .protection_unit_status import ProtectionUnitStatus
        from .public_error import PublicError
        from .site_protection_unit import SiteProtectionUnit

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ProtectionUnitStatus)),
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
        writer.write_object_value("error", self.error)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_enum_value("status", self.status)
    

