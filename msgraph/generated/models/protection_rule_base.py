from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_protection_rule import DriveProtectionRule
    from .entity import Entity
    from .identity_set import IdentitySet
    from .mailbox_protection_rule import MailboxProtectionRule
    from .protection_rule_status import ProtectionRuleStatus
    from .public_error import PublicError
    from .site_protection_rule import SiteProtectionRule

from .entity import Entity

@dataclass
class ProtectionRuleBase(Entity):
    # The identity of person who created the rule.
    created_by: Optional[IdentitySet] = None
    # The time of creation of the rule.
    created_date_time: Optional[datetime.datetime] = None
    # Contains error details if an operation on a rule fails.
    error: Optional[PublicError] = None
    # true indicates that the protection rule is dynamic; false that it's static. Currently, only static rules are supported.
    is_auto_apply_enabled: Optional[bool] = None
    # The identity of the person who last modified the rule.
    last_modified_by: Optional[IdentitySet] = None
    # Timestamp of the last modification made to the rule.
    last_modified_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The status of the protection rule. The possible values are: draft, active, completed, completedWithErrors, unknownFutureValue.
    status: Optional[ProtectionRuleStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProtectionRuleBase:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProtectionRuleBase
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveProtectionRule".casefold():
            from .drive_protection_rule import DriveProtectionRule

            return DriveProtectionRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxProtectionRule".casefold():
            from .mailbox_protection_rule import MailboxProtectionRule

            return MailboxProtectionRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteProtectionRule".casefold():
            from .site_protection_rule import SiteProtectionRule

            return SiteProtectionRule()
        return ProtectionRuleBase()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .drive_protection_rule import DriveProtectionRule
        from .entity import Entity
        from .identity_set import IdentitySet
        from .mailbox_protection_rule import MailboxProtectionRule
        from .protection_rule_status import ProtectionRuleStatus
        from .public_error import PublicError
        from .site_protection_rule import SiteProtectionRule

        from .drive_protection_rule import DriveProtectionRule
        from .entity import Entity
        from .identity_set import IdentitySet
        from .mailbox_protection_rule import MailboxProtectionRule
        from .protection_rule_status import ProtectionRuleStatus
        from .public_error import PublicError
        from .site_protection_rule import SiteProtectionRule

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "error": lambda n : setattr(self, 'error', n.get_object_value(PublicError)),
            "isAutoApplyEnabled": lambda n : setattr(self, 'is_auto_apply_enabled', n.get_bool_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(ProtectionRuleStatus)),
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
        writer.write_bool_value("isAutoApplyEnabled", self.is_auto_apply_enabled)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_enum_value("status", self.status)
    

