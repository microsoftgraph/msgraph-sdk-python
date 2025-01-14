from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OnPremisesDirectorySynchronizationFeature(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Used to block cloud object takeover via source anchor hard match if enabled.
    block_cloud_object_takeover_through_hard_match_enabled: Optional[bool] = None
    # Use to block soft match for all objects if enabled for the  tenant. Customers are encouraged to enable this feature and keep it enabled until soft matching is required again for their tenancy. This flag should be enabled again after any soft matching has been completed and is no longer needed.
    block_soft_match_enabled: Optional[bool] = None
    # When true, persists the values of Mobile and OtherMobile in on-premises AD during sync cycles instead of values of MobilePhone or AlternateMobilePhones in Microsoft Entra ID.
    bypass_dir_sync_overrides_enabled: Optional[bool] = None
    # Used to indicate that cloud password policy applies to users whose passwords are synchronized from on-premises.
    cloud_password_policy_for_password_synced_users_enabled: Optional[bool] = None
    # Used to enable concurrent user credentials update in OrgId.
    concurrent_credential_update_enabled: Optional[bool] = None
    # Used to enable concurrent user creation in OrgId.
    concurrent_org_id_provisioning_enabled: Optional[bool] = None
    # Used to indicate that device write-back is enabled.
    device_writeback_enabled: Optional[bool] = None
    # Used to indicate that directory extensions are being synced from on-premises AD to Microsoft Entra ID.
    directory_extensions_enabled: Optional[bool] = None
    # Used to indicate that for a Microsoft Forefront Online Protection for Exchange (FOPE) migrated tenant, the conflicting proxy address should be migrated over.
    fope_conflict_resolution_enabled: Optional[bool] = None
    # Used to enable object-level group writeback feature for additional group types.
    group_write_back_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Used to indicate on-premise password synchronization is enabled.
    password_sync_enabled: Optional[bool] = None
    # Used to indicate that writeback of password resets from Microsoft Entra ID to on-premises AD is enabled. This property isn't in use and updating it isn't supported.
    password_writeback_enabled: Optional[bool] = None
    # Used to indicate that we should quarantine objects with conflicting proxy address.
    quarantine_upon_proxy_addresses_conflict_enabled: Optional[bool] = None
    # Used to indicate that we should quarantine objects conflicting with duplicate userPrincipalName.
    quarantine_upon_upn_conflict_enabled: Optional[bool] = None
    # Used to indicate that we should soft match objects based on userPrincipalName.
    soft_match_on_upn_enabled: Optional[bool] = None
    # Used to indicate that we should synchronize userPrincipalName objects for managed users with licenses.
    synchronize_upn_for_managed_users_enabled: Optional[bool] = None
    # Used to indicate that Microsoft 365 Group write-back is enabled.
    unified_group_writeback_enabled: Optional[bool] = None
    # Used to indicate that feature to force password change for a user on logon is enabled while synchronizing on-premise credentials.
    user_force_password_change_on_logon_enabled: Optional[bool] = None
    # Used to indicate that user writeback is enabled.
    user_writeback_enabled: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPremisesDirectorySynchronizationFeature:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronizationFeature
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPremisesDirectorySynchronizationFeature()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "blockCloudObjectTakeoverThroughHardMatchEnabled": lambda n : setattr(self, 'block_cloud_object_takeover_through_hard_match_enabled', n.get_bool_value()),
            "blockSoftMatchEnabled": lambda n : setattr(self, 'block_soft_match_enabled', n.get_bool_value()),
            "bypassDirSyncOverridesEnabled": lambda n : setattr(self, 'bypass_dir_sync_overrides_enabled', n.get_bool_value()),
            "cloudPasswordPolicyForPasswordSyncedUsersEnabled": lambda n : setattr(self, 'cloud_password_policy_for_password_synced_users_enabled', n.get_bool_value()),
            "concurrentCredentialUpdateEnabled": lambda n : setattr(self, 'concurrent_credential_update_enabled', n.get_bool_value()),
            "concurrentOrgIdProvisioningEnabled": lambda n : setattr(self, 'concurrent_org_id_provisioning_enabled', n.get_bool_value()),
            "deviceWritebackEnabled": lambda n : setattr(self, 'device_writeback_enabled', n.get_bool_value()),
            "directoryExtensionsEnabled": lambda n : setattr(self, 'directory_extensions_enabled', n.get_bool_value()),
            "fopeConflictResolutionEnabled": lambda n : setattr(self, 'fope_conflict_resolution_enabled', n.get_bool_value()),
            "groupWriteBackEnabled": lambda n : setattr(self, 'group_write_back_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "passwordSyncEnabled": lambda n : setattr(self, 'password_sync_enabled', n.get_bool_value()),
            "passwordWritebackEnabled": lambda n : setattr(self, 'password_writeback_enabled', n.get_bool_value()),
            "quarantineUponProxyAddressesConflictEnabled": lambda n : setattr(self, 'quarantine_upon_proxy_addresses_conflict_enabled', n.get_bool_value()),
            "quarantineUponUpnConflictEnabled": lambda n : setattr(self, 'quarantine_upon_upn_conflict_enabled', n.get_bool_value()),
            "softMatchOnUpnEnabled": lambda n : setattr(self, 'soft_match_on_upn_enabled', n.get_bool_value()),
            "synchronizeUpnForManagedUsersEnabled": lambda n : setattr(self, 'synchronize_upn_for_managed_users_enabled', n.get_bool_value()),
            "unifiedGroupWritebackEnabled": lambda n : setattr(self, 'unified_group_writeback_enabled', n.get_bool_value()),
            "userForcePasswordChangeOnLogonEnabled": lambda n : setattr(self, 'user_force_password_change_on_logon_enabled', n.get_bool_value()),
            "userWritebackEnabled": lambda n : setattr(self, 'user_writeback_enabled', n.get_bool_value()),
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
        writer.write_bool_value("blockCloudObjectTakeoverThroughHardMatchEnabled", self.block_cloud_object_takeover_through_hard_match_enabled)
        writer.write_bool_value("blockSoftMatchEnabled", self.block_soft_match_enabled)
        writer.write_bool_value("bypassDirSyncOverridesEnabled", self.bypass_dir_sync_overrides_enabled)
        writer.write_bool_value("cloudPasswordPolicyForPasswordSyncedUsersEnabled", self.cloud_password_policy_for_password_synced_users_enabled)
        writer.write_bool_value("concurrentCredentialUpdateEnabled", self.concurrent_credential_update_enabled)
        writer.write_bool_value("concurrentOrgIdProvisioningEnabled", self.concurrent_org_id_provisioning_enabled)
        writer.write_bool_value("deviceWritebackEnabled", self.device_writeback_enabled)
        writer.write_bool_value("directoryExtensionsEnabled", self.directory_extensions_enabled)
        writer.write_bool_value("fopeConflictResolutionEnabled", self.fope_conflict_resolution_enabled)
        writer.write_bool_value("groupWriteBackEnabled", self.group_write_back_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("passwordSyncEnabled", self.password_sync_enabled)
        writer.write_bool_value("passwordWritebackEnabled", self.password_writeback_enabled)
        writer.write_bool_value("quarantineUponProxyAddressesConflictEnabled", self.quarantine_upon_proxy_addresses_conflict_enabled)
        writer.write_bool_value("quarantineUponUpnConflictEnabled", self.quarantine_upon_upn_conflict_enabled)
        writer.write_bool_value("softMatchOnUpnEnabled", self.soft_match_on_upn_enabled)
        writer.write_bool_value("synchronizeUpnForManagedUsersEnabled", self.synchronize_upn_for_managed_users_enabled)
        writer.write_bool_value("unifiedGroupWritebackEnabled", self.unified_group_writeback_enabled)
        writer.write_bool_value("userForcePasswordChangeOnLogonEnabled", self.user_force_password_change_on_logon_enabled)
        writer.write_bool_value("userWritebackEnabled", self.user_writeback_enabled)
        writer.write_additional_data_value(self.additional_data)
    

