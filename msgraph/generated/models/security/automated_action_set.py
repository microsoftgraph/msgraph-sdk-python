from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .account_object_id_action import AccountObjectIdAction
    from .account_sid_action import AccountSidAction
    from .device_action import DeviceAction
    from .email_action import EmailAction
    from .file_action import FileAction
    from .isolate_device_action import IsolateDeviceAction
    from .stop_and_quarantine_file_action import StopAndQuarantineFileAction

@dataclass
class AutomatedActionSet(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # File actions that allow files identified by file hash columns in the hunting-query results.
    allow_files: Optional[list[FileAction]] = None
    # File actions that block files identified by file hash columns in the hunting-query results.
    block_files: Optional[list[FileAction]] = None
    # Device actions that collect investigation packages from devices identified in the hunting-query results.
    collect_investigation_packages: Optional[list[DeviceAction]] = None
    # Account actions that disable users identified by account SID columns in the hunting-query results.
    disable_users: Optional[list[AccountSidAction]] = None
    # Account actions that force password resets for users identified by account SID columns in the hunting-query results.
    force_user_password_resets: Optional[list[AccountSidAction]] = None
    # Email actions that permanently delete messages identified in the hunting-query results.
    hard_delete_emails: Optional[list[EmailAction]] = None
    # Device actions that initiate investigations on devices identified in the hunting-query results.
    initiate_investigations: Optional[list[DeviceAction]] = None
    # Device actions that isolate devices identified in the hunting-query results.
    isolate_devices: Optional[list[IsolateDeviceAction]] = None
    # Account actions that mark users as compromised when they're identified by Microsoft Entra object ID columns in the hunting-query results.
    mark_users_as_compromised: Optional[list[AccountObjectIdAction]] = None
    # Email actions that move messages identified in the hunting-query results to Deleted Items.
    move_emails_to_deleted_items: Optional[list[EmailAction]] = None
    # Email actions that move messages identified in the hunting-query results to the Inbox.
    move_emails_to_inbox: Optional[list[EmailAction]] = None
    # Email actions that move messages identified in the hunting-query results to Junk Email.
    move_emails_to_junk: Optional[list[EmailAction]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Device actions that restrict app execution on devices identified in the hunting-query results.
    restrict_app_executions: Optional[list[DeviceAction]] = None
    # Device actions that run antivirus scans on devices identified in the hunting-query results.
    run_antivirus_scans: Optional[list[DeviceAction]] = None
    # Email actions that soft-delete messages identified in the hunting-query results.
    soft_delete_emails: Optional[list[EmailAction]] = None
    # File actions that stop running files and quarantine them on devices identified in the hunting-query results.
    stop_and_quarantine_files: Optional[list[StopAndQuarantineFileAction]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutomatedActionSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutomatedActionSet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutomatedActionSet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .account_object_id_action import AccountObjectIdAction
        from .account_sid_action import AccountSidAction
        from .device_action import DeviceAction
        from .email_action import EmailAction
        from .file_action import FileAction
        from .isolate_device_action import IsolateDeviceAction
        from .stop_and_quarantine_file_action import StopAndQuarantineFileAction

        from .account_object_id_action import AccountObjectIdAction
        from .account_sid_action import AccountSidAction
        from .device_action import DeviceAction
        from .email_action import EmailAction
        from .file_action import FileAction
        from .isolate_device_action import IsolateDeviceAction
        from .stop_and_quarantine_file_action import StopAndQuarantineFileAction

        fields: dict[str, Callable[[Any], None]] = {
            "allowFiles": lambda n : setattr(self, 'allow_files', n.get_collection_of_object_values(FileAction)),
            "blockFiles": lambda n : setattr(self, 'block_files', n.get_collection_of_object_values(FileAction)),
            "collectInvestigationPackages": lambda n : setattr(self, 'collect_investigation_packages', n.get_collection_of_object_values(DeviceAction)),
            "disableUsers": lambda n : setattr(self, 'disable_users', n.get_collection_of_object_values(AccountSidAction)),
            "forceUserPasswordResets": lambda n : setattr(self, 'force_user_password_resets', n.get_collection_of_object_values(AccountSidAction)),
            "hardDeleteEmails": lambda n : setattr(self, 'hard_delete_emails', n.get_collection_of_object_values(EmailAction)),
            "initiateInvestigations": lambda n : setattr(self, 'initiate_investigations', n.get_collection_of_object_values(DeviceAction)),
            "isolateDevices": lambda n : setattr(self, 'isolate_devices', n.get_collection_of_object_values(IsolateDeviceAction)),
            "markUsersAsCompromised": lambda n : setattr(self, 'mark_users_as_compromised', n.get_collection_of_object_values(AccountObjectIdAction)),
            "moveEmailsToDeletedItems": lambda n : setattr(self, 'move_emails_to_deleted_items', n.get_collection_of_object_values(EmailAction)),
            "moveEmailsToInbox": lambda n : setattr(self, 'move_emails_to_inbox', n.get_collection_of_object_values(EmailAction)),
            "moveEmailsToJunk": lambda n : setattr(self, 'move_emails_to_junk', n.get_collection_of_object_values(EmailAction)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "restrictAppExecutions": lambda n : setattr(self, 'restrict_app_executions', n.get_collection_of_object_values(DeviceAction)),
            "runAntivirusScans": lambda n : setattr(self, 'run_antivirus_scans', n.get_collection_of_object_values(DeviceAction)),
            "softDeleteEmails": lambda n : setattr(self, 'soft_delete_emails', n.get_collection_of_object_values(EmailAction)),
            "stopAndQuarantineFiles": lambda n : setattr(self, 'stop_and_quarantine_files', n.get_collection_of_object_values(StopAndQuarantineFileAction)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("allowFiles", self.allow_files)
        writer.write_collection_of_object_values("blockFiles", self.block_files)
        writer.write_collection_of_object_values("collectInvestigationPackages", self.collect_investigation_packages)
        writer.write_collection_of_object_values("disableUsers", self.disable_users)
        writer.write_collection_of_object_values("forceUserPasswordResets", self.force_user_password_resets)
        writer.write_collection_of_object_values("hardDeleteEmails", self.hard_delete_emails)
        writer.write_collection_of_object_values("initiateInvestigations", self.initiate_investigations)
        writer.write_collection_of_object_values("isolateDevices", self.isolate_devices)
        writer.write_collection_of_object_values("markUsersAsCompromised", self.mark_users_as_compromised)
        writer.write_collection_of_object_values("moveEmailsToDeletedItems", self.move_emails_to_deleted_items)
        writer.write_collection_of_object_values("moveEmailsToInbox", self.move_emails_to_inbox)
        writer.write_collection_of_object_values("moveEmailsToJunk", self.move_emails_to_junk)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("restrictAppExecutions", self.restrict_app_executions)
        writer.write_collection_of_object_values("runAntivirusScans", self.run_antivirus_scans)
        writer.write_collection_of_object_values("softDeleteEmails", self.soft_delete_emails)
        writer.write_collection_of_object_values("stopAndQuarantineFiles", self.stop_and_quarantine_files)
        writer.write_additional_data_value(self.additional_data)
    

