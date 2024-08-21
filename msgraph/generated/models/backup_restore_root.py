from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_protection_rule import DriveProtectionRule
    from .drive_protection_unit import DriveProtectionUnit
    from .entity import Entity
    from .exchange_protection_policy import ExchangeProtectionPolicy
    from .exchange_restore_session import ExchangeRestoreSession
    from .mailbox_protection_rule import MailboxProtectionRule
    from .mailbox_protection_unit import MailboxProtectionUnit
    from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
    from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
    from .protection_policy_base import ProtectionPolicyBase
    from .protection_unit_base import ProtectionUnitBase
    from .restore_point import RestorePoint
    from .restore_session_base import RestoreSessionBase
    from .service_app import ServiceApp
    from .service_status import ServiceStatus
    from .share_point_protection_policy import SharePointProtectionPolicy
    from .share_point_restore_session import SharePointRestoreSession
    from .site_protection_rule import SiteProtectionRule
    from .site_protection_unit import SiteProtectionUnit

from .entity import Entity

@dataclass
class BackupRestoreRoot(Entity):
    # The list of drive inclusion rules applied to the tenant.
    drive_inclusion_rules: Optional[List[DriveProtectionRule]] = None
    # The list of drive protection units in the tenant.
    drive_protection_units: Optional[List[DriveProtectionUnit]] = None
    # The list of Exchange protection policies in the tenant.
    exchange_protection_policies: Optional[List[ExchangeProtectionPolicy]] = None
    # The list of Exchange restore sessions available in the tenant.
    exchange_restore_sessions: Optional[List[ExchangeRestoreSession]] = None
    # The list of mailbox inclusion rules applied to the tenant.
    mailbox_inclusion_rules: Optional[List[MailboxProtectionRule]] = None
    # The list of mailbox protection units in the tenant.
    mailbox_protection_units: Optional[List[MailboxProtectionUnit]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of OneDrive for Business protection policies in the tenant.
    one_drive_for_business_protection_policies: Optional[List[OneDriveForBusinessProtectionPolicy]] = None
    # The list of OneDrive for Business restore sessions available in the tenant.
    one_drive_for_business_restore_sessions: Optional[List[OneDriveForBusinessRestoreSession]] = None
    # List of protection policies in the tenant.
    protection_policies: Optional[List[ProtectionPolicyBase]] = None
    # List of protection units in the tenant.
    protection_units: Optional[List[ProtectionUnitBase]] = None
    # List of restore points in the tenant.
    restore_points: Optional[List[RestorePoint]] = None
    # List of restore sessions in the tenant.
    restore_sessions: Optional[List[RestoreSessionBase]] = None
    # List of Backup Storage apps in the tenant.
    service_apps: Optional[List[ServiceApp]] = None
    # Represents the tenant-level status of the Backup Storage service.
    service_status: Optional[ServiceStatus] = None
    # The list of SharePoint protection policies in the tenant.
    share_point_protection_policies: Optional[List[SharePointProtectionPolicy]] = None
    # The list of SharePoint restore sessions available in the tenant.
    share_point_restore_sessions: Optional[List[SharePointRestoreSession]] = None
    # The list of site inclusion rules applied to the tenant.
    site_inclusion_rules: Optional[List[SiteProtectionRule]] = None
    # The list of site protection units in the tenant.
    site_protection_units: Optional[List[SiteProtectionUnit]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupRestoreRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupRestoreRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupRestoreRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .drive_protection_rule import DriveProtectionRule
        from .drive_protection_unit import DriveProtectionUnit
        from .entity import Entity
        from .exchange_protection_policy import ExchangeProtectionPolicy
        from .exchange_restore_session import ExchangeRestoreSession
        from .mailbox_protection_rule import MailboxProtectionRule
        from .mailbox_protection_unit import MailboxProtectionUnit
        from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
        from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
        from .protection_policy_base import ProtectionPolicyBase
        from .protection_unit_base import ProtectionUnitBase
        from .restore_point import RestorePoint
        from .restore_session_base import RestoreSessionBase
        from .service_app import ServiceApp
        from .service_status import ServiceStatus
        from .share_point_protection_policy import SharePointProtectionPolicy
        from .share_point_restore_session import SharePointRestoreSession
        from .site_protection_rule import SiteProtectionRule
        from .site_protection_unit import SiteProtectionUnit

        from .drive_protection_rule import DriveProtectionRule
        from .drive_protection_unit import DriveProtectionUnit
        from .entity import Entity
        from .exchange_protection_policy import ExchangeProtectionPolicy
        from .exchange_restore_session import ExchangeRestoreSession
        from .mailbox_protection_rule import MailboxProtectionRule
        from .mailbox_protection_unit import MailboxProtectionUnit
        from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
        from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
        from .protection_policy_base import ProtectionPolicyBase
        from .protection_unit_base import ProtectionUnitBase
        from .restore_point import RestorePoint
        from .restore_session_base import RestoreSessionBase
        from .service_app import ServiceApp
        from .service_status import ServiceStatus
        from .share_point_protection_policy import SharePointProtectionPolicy
        from .share_point_restore_session import SharePointRestoreSession
        from .site_protection_rule import SiteProtectionRule
        from .site_protection_unit import SiteProtectionUnit

        fields: Dict[str, Callable[[Any], None]] = {
            "driveInclusionRules": lambda n : setattr(self, 'drive_inclusion_rules', n.get_collection_of_object_values(DriveProtectionRule)),
            "driveProtectionUnits": lambda n : setattr(self, 'drive_protection_units', n.get_collection_of_object_values(DriveProtectionUnit)),
            "exchangeProtectionPolicies": lambda n : setattr(self, 'exchange_protection_policies', n.get_collection_of_object_values(ExchangeProtectionPolicy)),
            "exchangeRestoreSessions": lambda n : setattr(self, 'exchange_restore_sessions', n.get_collection_of_object_values(ExchangeRestoreSession)),
            "mailboxInclusionRules": lambda n : setattr(self, 'mailbox_inclusion_rules', n.get_collection_of_object_values(MailboxProtectionRule)),
            "mailboxProtectionUnits": lambda n : setattr(self, 'mailbox_protection_units', n.get_collection_of_object_values(MailboxProtectionUnit)),
            "oneDriveForBusinessProtectionPolicies": lambda n : setattr(self, 'one_drive_for_business_protection_policies', n.get_collection_of_object_values(OneDriveForBusinessProtectionPolicy)),
            "oneDriveForBusinessRestoreSessions": lambda n : setattr(self, 'one_drive_for_business_restore_sessions', n.get_collection_of_object_values(OneDriveForBusinessRestoreSession)),
            "protectionPolicies": lambda n : setattr(self, 'protection_policies', n.get_collection_of_object_values(ProtectionPolicyBase)),
            "protectionUnits": lambda n : setattr(self, 'protection_units', n.get_collection_of_object_values(ProtectionUnitBase)),
            "restorePoints": lambda n : setattr(self, 'restore_points', n.get_collection_of_object_values(RestorePoint)),
            "restoreSessions": lambda n : setattr(self, 'restore_sessions', n.get_collection_of_object_values(RestoreSessionBase)),
            "serviceApps": lambda n : setattr(self, 'service_apps', n.get_collection_of_object_values(ServiceApp)),
            "serviceStatus": lambda n : setattr(self, 'service_status', n.get_object_value(ServiceStatus)),
            "sharePointProtectionPolicies": lambda n : setattr(self, 'share_point_protection_policies', n.get_collection_of_object_values(SharePointProtectionPolicy)),
            "sharePointRestoreSessions": lambda n : setattr(self, 'share_point_restore_sessions', n.get_collection_of_object_values(SharePointRestoreSession)),
            "siteInclusionRules": lambda n : setattr(self, 'site_inclusion_rules', n.get_collection_of_object_values(SiteProtectionRule)),
            "siteProtectionUnits": lambda n : setattr(self, 'site_protection_units', n.get_collection_of_object_values(SiteProtectionUnit)),
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
        writer.write_collection_of_object_values("driveInclusionRules", self.drive_inclusion_rules)
        writer.write_collection_of_object_values("driveProtectionUnits", self.drive_protection_units)
        writer.write_collection_of_object_values("exchangeProtectionPolicies", self.exchange_protection_policies)
        writer.write_collection_of_object_values("exchangeRestoreSessions", self.exchange_restore_sessions)
        writer.write_collection_of_object_values("mailboxInclusionRules", self.mailbox_inclusion_rules)
        writer.write_collection_of_object_values("mailboxProtectionUnits", self.mailbox_protection_units)
        writer.write_collection_of_object_values("oneDriveForBusinessProtectionPolicies", self.one_drive_for_business_protection_policies)
        writer.write_collection_of_object_values("oneDriveForBusinessRestoreSessions", self.one_drive_for_business_restore_sessions)
        writer.write_collection_of_object_values("protectionPolicies", self.protection_policies)
        writer.write_collection_of_object_values("protectionUnits", self.protection_units)
        writer.write_collection_of_object_values("restorePoints", self.restore_points)
        writer.write_collection_of_object_values("restoreSessions", self.restore_sessions)
        writer.write_collection_of_object_values("serviceApps", self.service_apps)
        writer.write_object_value("serviceStatus", self.service_status)
        writer.write_collection_of_object_values("sharePointProtectionPolicies", self.share_point_protection_policies)
        writer.write_collection_of_object_values("sharePointRestoreSessions", self.share_point_restore_sessions)
        writer.write_collection_of_object_values("siteInclusionRules", self.site_inclusion_rules)
        writer.write_collection_of_object_values("siteProtectionUnits", self.site_protection_units)
    

